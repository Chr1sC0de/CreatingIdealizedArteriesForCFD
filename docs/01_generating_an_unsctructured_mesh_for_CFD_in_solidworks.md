# Generating an Unstructured Mesh for CFD with Pointwise

The simplest way to mesh the our artery for CFD is via an unstructured mesh. However,
we must note that an unstructured mesh can lead unrealistic results. Nonetheless
it is far easier to script the generation of arteries using unstructured grids.

As we will be interested in the

## Step 1: Import the Domain and Assign the Average Spacing

Import the surface into pointwise and assign an average spacing for any generated
connectors.

<img src=./images/unstructured_dimension_connector.PNG height="500">

## Step 2: Create Unstructured Surface Domain

Select the unstructured option from the taskbar and create a domain on the database

<img src=./images/unstructured_domains_on_database_entities.PNG width="500">

## Step 3: Create Inlet and Outlet Patches

Highlight the connectors on the inlet and outlet patches and then assemble the
domains.

<img src=./images/unstructured_inlet_outlet_patches.PNG width="500">

Select the patches and select Grid > Solve

<img src=./images/unstructured_select_solve_inlet_outlet_patches.PNG width="500">

We are more interested in what occurs at the wall of the artery so we will apply a
T-rex boundary condition to the mesh at the edges