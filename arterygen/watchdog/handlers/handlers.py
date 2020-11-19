import pathlib as pt
import subprocess
from collections import OrderedDict
import subprocess
import re
import pandas as pd
import shutil
try:
    from ...glyph_template import generate_ideal_bifurcation_glyph_template_1
    from ...foam_templates import NewtonianSteadyBifurcationGenerator
except:
    from arterygen.glyph_template import generate_ideal_bifurcation_glyph_template_1
    from arterygen.foam_templates import NewtonianSteadyBifurcationGenerator

import logging
import time

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

    dimension_spacing        = 0.25,
    wall_spacing             = 0.25/8,
    trex_maximum_layers      = 6,
    trex_growth_rate         = 1.1,

    def __init__(self, target_folder: pt.Path, openfoam_case_constructor):
        self.target_folder = target_folder
        # case constructor has the form function(filename, polymesh_folder_target)
        self.openfoam_case_constructor = openfoam_case_constructor

    def __call__(self, case: pt.Path, rename=None):

        # generate the openfoam case
        self.foam_folder = self.target_folder/case.stem
        self.openfoam_case_constructor(self.foam_folder)
        # give the case constructor tome time to create the folder
        time.sleep(5)
        if not all(
            [
                (self.foam_folder/"constant/polyMesh"/item).exists()
                    for item in self.mesh_files
            ]
        ):
            # generate the case
            generate_ideal_bifurcation_glyph_template_1(
                case,
                self.foam_folder/"constant"/"polyMesh",
                dimension_spacing        = self.dimension_spacing,
                wall_spacing             = self.wall_spacing,
                trex_maximum_layers      = self.trex_maximum_layers,
                trex_growth_rate         = self.trex_growth_rate,
                inlet_connector_names     = ("con-1", "con-7"),
                outlet_1_connector_names  = ("con-28", "con-31"),
                outlet_2_connector_names = ("con-35", "con-37")
            )
        return self.foam_folder

    def clean(self):
        if self.foam_folder.exists():
            shutil.rmtree(self.foam_folder)

def make_newtonian_steady_case(foam_folder):
    diameter   = float(foam_folder.name.split("_")[3])/1000
    NewtonianSteadyBifurcationGenerator(diameter, foam_folder).construct()

class STEPToFoamNewtonianSteadyFoam(STEPToFoam):
    def __init__(self, target_folder: pt.Path):
        super().__init__(target_folder, make_newtonian_steady_case)