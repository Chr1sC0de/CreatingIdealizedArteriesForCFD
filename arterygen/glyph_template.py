from pointwise import GlyphClient
import pathlib as pt
from typing import List

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

def echo(text):
    print(text)

def generate_ideal_bifurcation_glyph_template_1(
    input_filename          : pt.Path,
    output_directory        : pt.Path,
    dimension_spacing       : float= 0.2,
    wall_spacing            : float= 0.025,
    trex_maximum_layers     : float= 6,
    trex_growth_rate        : float= 1.1,
    inlet_connector_names    : List[str] = ("con-1", "con-7"),
    outlet_1_connector_names : List[str] = ("con-28", "con-31"),
    outlet_2_connector_names: List[str] = ("con-35", "con-37"),
    port                    : int       = 0,
    echo_callback = "default"
):
    # note when port is 0 the client is connected to tclsh directly

    input_filename   = pt.Path(input_filename)
    output_directory = pt.Path(output_directory)

    assert input_filename.exists(), "The input file does not exist"
    assert output_directory.exists(), "The output directory does not exist "
    if echo_callback is None:
        glf = GlyphClient(port=0)
    elif echo_callback is "default":
        print("Info: processing", input_filename)
        glf = GlyphClient(port=0, callback=echo)
    else:
        print("Info: processing", input_filename)
        glf = GlyphClient(port=0, callback=echo_callback)

    pw  = glf.get_glyphapi()

    # reset the servers workspace
    pw.Application.reset()

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

    with pw.Application.begin("DatabaseImport") as databaseimport:
        databaseimport.initialize(
            "-strict", "-type", "Automatic", input_filename.absolute().as_posix()
        )
        databaseimport.read()
        databaseimport.convert()

    all_database_entities = pw.Database.getAll()
    for entity in all_database_entities:
        if entity._type == "pw::Model":
            model_database = entity
    wall_domains        = pw.DomainUnstructured.createOnDatabase(
            "-parametricConnectors", "Aligned", "-merge", 0, [model_database,]
        )

    # isolate the inlet and outlet connectors
    inlet_outlet_connector_names = [
        inlet_connector_names, outlet_1_connector_names, outlet_2_connector_names
    ]
    # get the inlet and outlet connectort objects
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
    block = pw.BlockUnstructured.createFromDomains(all_domains)[0]

    # set the boundary conditions of the block and then solve
    with pw.Application.begin("UnstructuredSolver", block) as block_solver:
        # get the necessary boundary conditions
        wall_trex_condition = pw.TRexCondition.getByName("WALL")
        match_trex_condition     = pw.TRexCondition.create()
        match_trex_condition.setName("MATCH")

        # create the list required to be placed into the WALL bc
        block_wall_list = [ [block, dom, "Opposite"]  for dom in wall_domains ]
        # create the list required to be placed into the MATCH bc
        block_match_list = [ [block, dom, "Same"]  for dom in inlet_outlet_domains ]

        # finally apply the correct t-rex condition to domains
        wall_trex_condition.apply(block_wall_list)
        match_trex_condition.apply(block_match_list)
        # set the solver attributes
        block.setUnstructuredSolverAttribute("TRexMaximumLayers", trex_maximum_layers)
        block.setUnstructuredSolverAttribute("TRexGrowthRate", trex_growth_rate)
        # set complete when incomplete
        block_solver.setStopWhenFullLayersNotMet("true")
        block_solver.setAllowIncomplete("true")
        block_solver.run("Initialize")
        block_solver.run("Refine")

    # set the CAE solver
    pw.Application.setCAESolver("OpenFOAM")

    # Create Boundary Conditions
    wall_bc = pw.BoundaryCondition.create()
    wall_bc.setName("WALL")
    wall_bc.setPhysicalType("-usage", "CAE", "wall")

    inlet_bc = pw.BoundaryCondition.create()
    inlet_bc.setName("INLET")
    inlet_bc.setPhysicalType("-usage", "CAE", "patch")

    outlet_1_bc = pw.BoundaryCondition.create()
    outlet_1_bc.setName("OUTLET-1")
    outlet_1_bc.setPhysicalType("-usage", "CAE", "patch")

    outlet_2_bc = pw.BoundaryCondition.create()
    outlet_2_bc.setName("OUTLET-2")
    outlet_2_bc.setPhysicalType("-usage", "CAE", "patch")

    # assign the correct domains to the boundary conditions

    wall_bc.apply([[block, dom] for dom in wall_domains])

    inlet_bc.apply([block, inlet_outlet_domains[0]])
    outlet_1_bc.apply([block, inlet_outlet_domains[1]])
    outlet_2_bc.apply([block, inlet_outlet_domains[2]])

    with pw.Application.begin("CaeExport") as cae_exporter:
        cae_exporter.addAllEntities()
        cae_exporter.initialize(
            "-strict", "-type", "CAE", output_directory.absolute().as_posix()
        )
        cae_exporter.verify()
        cae_exporter.write()

    if echo_callback is None:
        pass
    elif echo_callback is "default":
        print("Info: completed processing", input_filename)
    else:
        print("Info: completed processing", input_filename)