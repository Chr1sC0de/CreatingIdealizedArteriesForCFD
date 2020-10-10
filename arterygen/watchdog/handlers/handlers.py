import pathlib as pt
import subprocess
from collections import OrderedDict
import subprocess
import re
import pandas as pd
try:
    from ...glyph_template import generate_ideal_bifurcation_glyph_template_1
    from ...foam_templates import NewtonianSteadyBifurcationGenerator
except:
    from arterygen.glyph_template import generate_ideal_bifurcation_glyph_template_1
    from arterygen.foam_templates import NewtonianSteadyBifurcationGenerator


class STEPToFoam:
    '''
        Handler class,
        the name of the STEP file will be,
        base_*type*_inlet_*radius*_outlet1_*radius*_outlet2_*radius*,
        converts a step file to OpenFOAM case
    '''

    mesh_files = [
            "boundary", "cellZones", "faces",
            "faceZones", "neighbour", "owner", "points"
    ]

    def __init__(self, target_folder: pt.Path, openfoam_case_constructor):
        self.target_folder = target_folder
        self.openfoam_case_constructor = openfoam_case_constructor

    def __call__(self, case: pt.Path):

        # generate the openfoam case
        foam_folder = self.target_folder/case.stem
        if not all(
            [
                (foam_folder/"constant/polyMesh"/item).exists()
                    for item in self.mesh_files
            ]
        ):
            self.openfoam_case_constructor(foam_folder)
            # generate the glyph
            glyph_name = case.parent/"tmp.glyph"
            generate_ideal_bifurcation_glyph_template_1(
                case,
                glyph_name,
                foam_folder/"constant"/"polyMesh",
                connector_dimension_spacing = 0.2,
                inlet_domain_wall_spacing   = 0.025,
                TRexMaximumLayers           = 6,
                TRexGrowthRate              = 1.1
            )
            # now run the glyph to generate the openfoam mesh
            subprocess.run(f"tclsh.exe {glyph_name}")


def make_newtonian_steady_case(foam_folder):
    diameter   = float(foam_folder.name.split("_")[3])/1000
    NewtonianSteadyBifurcationGenerator(diameter, foam_folder).construct()


class STEPToFoamNewtonianSteadyFoam(STEPToFoam):
    def __init__(self, target_folder: pt.Path):
        super().__init__(target_folder, make_newtonian_steady_case)