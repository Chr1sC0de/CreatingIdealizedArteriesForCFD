# Generating Idealized Arteries with SolidWorks, PointWise and Python for CFD in OpenFOAM

The current repository contains examples and tools for creating a pipeline
for semi-automatically generating idealised arteries (with bifurcations) from [SolidWorks](https://www.solidworks.com/) models for CFD application with [PointWise](https://www.pointwise.com/). It also contains strategies for automating CFD on the super computer using python.

![](./docs/bifurcation/images/open_foam_case.PNG)

## Contents

The following contents show how to generate your own pipeline from scratch

### Generating Arteries Without a Bifurcation

#### [Creating a Statistical Shape Model](./docs/no_bifurcation/00_creating_a_statistical_shape_model.ipynb)

#### [Creating a Structured Mesh using Pointwise and Python](./docs/bifurcation/../no_bifurcation/01_creating_structured_meshes_in_pointwise.ipynb)

![](./docs/no_bifurcation/images/final_mesh.PNG)

### Generating Arteries with a Bifurcation

#### [Generating a Simple Template Artery with a Bifurcation in SolidWorks](./docs/bifurcation/00_generating_a_ideal_artery_in_solidworks.md)

![](./docs/bifurcation/images/solidworks_template_artery.PNG)

#### [Creating an Unstructured Mesh with Pointwise](./docs/bifurcation/01_generating_an_unsctructured_mesh_for_CFD_in_solidworks.md)

![](./docs/bifurcation/images/unstructured_grid_generation/inlet_outlet_patched.PNG)

#### [Connecting to an Active Pointwise Port and Programmatically Constructing an Unstructured Mesh](./docs/bifurcation/02_convert_step_to_openfoam_with_pointwise_python_api.ipynb)

#### [Programmatically Creating OpenFoam Cases From a Template](./docs/bifurcation/03_programatically_creating_openfoam_cases_from_a_template.ipynb)

#### [Automatic Conversion of STEP Files to OpenFoam](./docs/bifurcation/04_automatically_convert_step_files_to_openfoam_with_an_observer.ipynb)

#### [Using Solidworks Configurations and VBA To Programmatically Generate Cases](./docs/bifurcation/05_using_solidworks_configurations_and_vba_to_programatically_generate_examples.md)

### Running Jobs

#### [Automatic Handling of OpenFoam Jobs on the Gadi Super Computer with Python](./docs/automatic_handling_of_super_computer_jobs_with_python.ipynb)

### Post-Processing

#### [Unwrapping Models]

## Examples

The examples folder contains scripts for automating the process for many cases.
