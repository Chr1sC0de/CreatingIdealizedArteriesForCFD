from pointwise import GlyphClient
import pathlib as pt

def load_file(glyph, filepath):

    filepath = pt.Path(filepath)
    assert filepath.exists(), f"the file {filepath} does not exist"
    filepath = filepath.as_posix().replace("\\", "/")

    command = [
        "set _TMP(mode_1) [pw::Application begin DatabaseImport]",
        f" $_TMP(mode_1) initialize -strict -type Automatic {filepath}",
        " $_TMP(mode_1) read",
        " $_TMP(mode_1) convert",
        "$_TMP(mode_1) end",
    ]
    return glyph.eval("\n".join(command))

def get_quilts(pw):
    all_entities = pw.Database.getAll()
    return [quilt for quilt in all_entities if "Quilt" in quilt.glyphType]

def get_models(pw):
    all_entities = pw.Database.getAll()
    return [quilt for quilt in all_entities if "Model" in quilt.glyphType]

def get_connectors_by_name(pw, *connector_names):
    return [pw.GridEntity.getByName(name) for name in connector_names]


if __name__ == "__main__":

    import pathlib as pt

    folder     = pt.Path(r"D:\Github\IdealBifurcations\solidworksMeshes\inlet_1.86_bif_1.13_outlet_1.405")
    input_file = folder/"0.step"

    glf = GlyphClient(port=2807)
    pw  = glf.get_glyphapi()

    # initialize the data
    pw.Application.setUndoMaximumLevels(10)
    pw.Application.reset()
    # set connector to spacing
    pw.Connector.setCalculateDimensionMethod("Spacing")
    pw.Connector.setCalculateDimensionSpacing(.5)
    # make the mode unstructured
    pw.Application.setGridPreference("Unstructured")

    load_file(glf, input_file)
    # get all the model entit
    model = get_models(pw)
    # create the unstructured grid
    pw.DomainUnstructured.createOnDatabase(model)
    # get the inlet connectors by name
    inlet_outlet_connectors_names = [
        ["con-31", "con-32"],
        ["con-3", "con-15"],
        ["con-24", "con-34"]
    ]
    inlet_outlet_connectors = [
        get_connectors_by_name(pw, *con_set) for con_set in
            inlet_outlet_connectors_names
    ]
    # now create unstructured domains
    pass

