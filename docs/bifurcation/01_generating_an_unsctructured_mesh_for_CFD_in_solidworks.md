# Generating an Unstructured Mesh for CFD with Pointwise

The simplest way to mesh the our artery for CFD is via an unstructured mesh. However,
we must note that an unstructured mesh can lead unrealistic results. Nonetheless
it is far easier to script the generation of arteries using unstructured grids.

As we will be interested in the

## Step 1: Import the Domain and Assign the Average Spacing

Import the surface into pointwise and assign an average spacing for any generated
connectors.

<img src=./images/unstructured_grid_generation/imported_database.PNG height="500">
<img src=./images/unstructured_grid_generation/average_connector_length.PNG height="500">

## Step 2: Create Unstructured Surface Domain

Select the unstructured option from the taskbar and create a domain on the database

<img src=./images/unstructured_grid_generation/unstructured_domains_on_database_entities.PNG height="500">

## Step 3: Create Inlet and Outlet Patches

Highlight the connectors on the inlet and outlet patches and then assemble the
domains.

<img src=./images/unstructured_grid_generation/inlet_outlet_patched.PNG height="500">

Select the patches and select Grid > Solve

<img src=./images/unstructured_grid_generation/inlet_outlet_patch_solve.PNG height="500">

We are more interested in what occurs at the wall of the artery so we will apply a
T-rex boundary condition to the mesh at the edges, making the cells at the wall
smaller than the cells at the centre of the mesh.

<img
src=./images/unstructured_grid_generation/inlet_outlet_patch_boundary_conditions.PNG
height="500">

Now we can assign the growth rate of the t-rex cells at the boundary and the kind
of cells grown at the boundary.

<img src=./images/unstructured_grid_generation/t_rex_inlet_outlet_patches.PNG
height="500">

Then we can select the "initialize" and "refine" buttons to generate the t-rex
meshes at the inlet and outlet patches.

<img
src=./images/unstructured_grid_generation/initialize_and_refine_inlet_outlet_patches.PNG
height="500">

## Step 3: Generating the Internal Mesh

Given we have constructed the boundaries of our mesh we can construct the internal
field. We can initialize a block by the selecting the "Assemble Block" button from
the toolbar. After the block has been generated, select the block and select Grid >
Solve. Going into the boundary conditions, create a Wall and Match boundary condition
assigning the artery walls to Wall and the inlet and outlet patches to Match.

<img
src=./images/unstructured_grid_generation/unstructured_block_solve.PNG
height="500">

Ensure that the block t-rex settings match our inlet and outlet domain settings,

<img
src=./images/unstructured_grid_generation/block_t_rex_settings.PNG
height="500">

Finally initialize and refine the mesh.

## Exporting the CAE

Under CAE > Select Solver select OpenFOAM as the solver. Then, under CAE > Set
Boundary Conditions generate 1 wall and three patch boundary conditions and assign
the appropriate boundaries.

<img
src=./images/unstructured_grid_generation/wall_inlet_outlet_boudnary_conditions.PNG
height="500">

Finally we can go to File > Export CAE to save the OpenFOAM mesh.