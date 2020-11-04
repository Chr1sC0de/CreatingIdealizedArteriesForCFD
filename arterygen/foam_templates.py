import pathlib as pt
import abc
import distutils.dir_util
import numpy as np

_newtonian_steady_case = pt.Path(__file__).parent/"OpenFOAM_templates"/"newtonian_steady"

class FoamTemplateGenerator(abc.ABC):

    case_path = None

    def __init__(self, target_path: pt.Path):
        self.target_path = pt.Path(target_path)

    @abc.abstractmethod
    def modify(self):
        NotImplemented

    def construct(self):
        distutils.dir_util.copy_tree(
            self.case_path.absolute().as_posix(),
            self.target_path.absolute().as_posix()
        )
        self.modify()

class NewtonianSteadyBifurcationGenerator(FoamTemplateGenerator):

    case_path = _newtonian_steady_case

    def __init__(self, diameter, *args):
        area = np.pi * (diameter/2)**2
        self.inlet_velocity = 1.43*(diameter**2.55)/area
        super().__init__(*args)

    def modify(self):
        U_file = self.target_path/"0"/"U"
        file_text = [
            "/*--------------------------------*- C++ -*----------------------------------*\\",
            "| =========                 |                                                 |",
            "| \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |",
            "|  \\\\    /   O peration     | Version:  2.1.1                                 |",
            "|   \\\\  /    A nd           | Web:      www.OpenFOAM.org                      |",
            "|    \\\\/     M anipulation  |                                                 |",
            "\\*---------------------------------------------------------------------------*/",
            "FoamFile",
            "{",
            "    version     2.0;",
            "    format      ascii;",
            "    class       volVectorField;",
            "    object      U;",
            "}",
            "// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //",
            "",
            "dimensions      [0 1 -1 0 0 0 0];",
            "",
            "internalField   uniform (0 0 0);",
            "",
            "boundaryField",
            "{",
            "    WALL",
            "    {",
            "        type            fixedValue;",
            "        value           uniform (0 0 0);",
            "    }",
            "",
            "",
            "	INLET",
            "	{",
            "		type     surfaceNormalFixedValue;",
            f"		refValue -{self.inlet_velocity};",
            "	}",
            "",
            "    OUTLET_1",
            "    {",
            "        type            zeroGradient;",
            "    }",
            "",
            "    OUTLET_2",
            "    {",
            "        type            zeroGradient;",
            "    }",
            "}",
            "",
            "// ************************************************************************* //",
        ]
        with open(U_file, "w", newline="\n") as f:
            f.write("\n".join(file_text))