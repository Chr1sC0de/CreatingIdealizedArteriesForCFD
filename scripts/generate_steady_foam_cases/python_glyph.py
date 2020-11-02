from pointwise import GlyphClient
import pathlib as pt

filename          = pt.Path("D:/Github/IdealBifurcations/scripts/generate_steady_foam_cases/step_files/base_01_inlet_3_bif_1.4_outlet_1.6_angle_0.STEP")
assert filename.exists()
dimension_spacing   = 0.2
wall_spacing        = 0.025
trex_maximum_layers = 6
trex_growth_rate    = 1.1

def get_all_entities(api_object, prefix, counter=1):
    entities = []
    while True:
        try:
            entities.append(
                api_object.GridEntity.getByName("%s-%d"%(prefix, counter))
            )
            counter += 1
        except:
            break
    return entities


if __name__ == "__main__":

    glf = GlyphClient(port=2807)
    pw = glf.get_glyphapi()

    # set the connector calculation method and spacing
    pw.Connector.setCalculateDimensionMethod("Spacing")
    pw.Connector.setCalculateDimensionSpacing(dimension_spacing)
    # no set the grid preference to unstructured grids
    pw.Application.setGridPreference("Unstructured")

    '''
    We convert the following code segment to python:
        set _TMP(mode_1) [pw::Application begin DatabaseImport]
            $_TMP(mode_1) initialize -strict -type Automatic {input_file}
            $_TMP(mode_1) read
            $_TMP(mode_1) convert
            $_TMP(mode_1) end
        unset _TMP(mode_1)
    '''

    if False:
        with pw.Application.begin("DatabaseImport") as databaseimport:
            databaseimport.initialize(
                "-strict", "-type", "Automatic", filename.absolute().as_posix()
            )
            databaseimport.read()
            databaseimport.convert()

        surfaceDatabase = pw.DatabaseEntity.getByName("NONE-56")
        database = pw.DomainUnstructured.createOnDatabase(
                "-parametricConnectors", "Aligned", "-merge", 0, [surfaceDatabase,]
            )
    # first isolate the wall domains
    wall_domains = get_all_entities(pw, "dom")
    # isolate the inlet and outlet connectors
    inlet_outlet_connector_names = [
        ("con-1", "con-7"), ("con-28", "con-31"), ("con-35", "con-37")
    ]
    inlet_outlet_connectors = [
        [pw.GridEntity.getByName(con_name) for con_name in con_pair] for con_pair in
        inlet_outlet_connector_names
    ]
    # create the domains using the inlet and outlet connectors
    inlet_outlet_domains = [
        pw.DomainUnstructured.createFromConnectors(connector_pair)[0] for
        connector_pair in inlet_outlet_connectors
    ]

    # generate t-rex mesh for the inlet and outlet domains
    with pw.Application.begin("UnstructuredSolver", inlet_outlet_domains) as unstruc_solver:
        # use the create factory method to generate a trex condition and apply the
        # condition to the necessary domains and connectors
        trex_condition = pw.TRexCondition.create()
        trex_condition.setName("WALL")
        trex_condition.setConditionType("Wall")
        trex_condition.setValue(wall_spacing)
        domain_connector_pairs = []
        for domain, connector_pair in zip(inlet_outlet_domains, inlet_outlet_connectors):
            for connector in connector_pair:
                domain_connector_pairs.append(
                    [domain, connector, "Same"]
                )
        trex_condition.apply(domain_connector_pairs)
        # create a collection of domains and set the unstructured solver attributes
        for domain in inlet_outlet_domains:
            domain.setUnstructuredSolverAttribute("TrexMaximumLayers", trex_maximum_layers)
            domain.setUnstructuredSolverAttribute("TrexGrowthRate", trex_growth_rate)
            domain.setUnstructuredSolverAttribute("TRexCellType", "TriangleQuad")
        unstruc_solver.run("Initialize")
        unstruc_solver.run("Refine")

    # create a list of all domains and create a block for meshing
    all_domains = []
    all_domains.extend(wall_domains)
    all_domains.extend(inlet_outlet_domains)
    block = pw.BlockUnstructured.createFromDomains(all_domains)

    # set the boundary conditions of the block and then solve

