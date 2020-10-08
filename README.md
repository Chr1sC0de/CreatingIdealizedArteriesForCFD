# Generating Idealized Arteries with SolidWorks, PointWise and Python for CFD in OpenFOAM

Examples outlining how to generate ideal arteries for Computational Fluid
Dynamics Studies using [SolidWorks](https://www.solidworks.com/) and
[PointWise](https://www.pointwise.com/) as well as semi-automation of the model
generation process.

## Contents

### [Generating a Simple Template Artery in SolidWorks](./docs/00_generating_a_ideal_artery_in_solidworks.md)

### [Creating an unstructured mesh with pointwise](./docs/01_generating_an_unsctructured_mesh_for_CFD_in_solidworks.md)

### TBD: Semi-Automation of Reconstruction

    1. Via pointwise journalling create an automated script for CFD mesh generation
    2. Using python we can design watchdog program for a folder which contains our solidworks STEP files
    3. Generate the artery templates
    4. Automatically call the pointwise journalled glyphs
    5. Calculate case boundary conditions and construct OpenFoam case
    6. Send case to cloud and run the CFD with Python