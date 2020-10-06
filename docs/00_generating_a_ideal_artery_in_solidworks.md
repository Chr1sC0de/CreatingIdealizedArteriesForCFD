# Generating A Simple Ideal Template Artery Using SolidWorks

In this document we will be showing students how to generate an idealized template
artery for computational fluid dynamics simulations. The resulting artery is shown
bellow.

<img src=./images/solidworks_template_artery.PNG width="500">

## Step 1: Importing the Main and Bifurcation Centerlines

We shall start by importing the centerlines which describe the path of the main and
bifurcation portion of our artery. The centerlines can either be text or sldcrv
files.

<img src=./images/centelines.PNG width="500">

We can now import the files using SolidWorks insert > Curve > curve through xyz
points

<img src=./images/curve_through_xyz_plane.PNG width="500">

<img src=./images/imported_centerlines.PNG width="500">

## Step 2: Creating Cylindrical Segments

The idealized artery is essentially created by joining three cylindrical segments
with a T-junction. In this section we will outline how generate the three segments
and make them easily modifiable.

<img src=./images/three_cylindrical_segments.PNG width="500">

To generate a segment we can define a region along a centreline bounded by two
planes. To generate the two planes we must define points coincident to our curve.
This can be done by using Surfaces > Reference Geometry > Point.

<img src=./images/point.PNG width="500">

We can then modify the distance of the point along the centreline. This allows us to
easily control the length of our artery segment.

<img src=./images/point_distance.PNG width="500">

Finally, by selecting our point and the coincident curve, we can generate a plane
perpendicular to our centreline.

<img src=./images/perpendicular_plane.PNG width="500">

Now we can generate the 6 planes which describe the bounds of our three cylindrical
segments.

<img src=./images/bounding_planes.PNG width="501">

Now that we have our bounding planes we can create our surfaces using Toolbar >
Surfaces > Swept Surface. But before we do that we must first draw our inlet circle
on one of our inlet planes using Toolbar > Sketch > Sketch > circle function.

<img src=./images/inlet_circle.PNG width="501">

Once the circle is created we can now use Toolbar > Surfaces > Swept Surface to
generate the cylindrical section. Select "Keep Orientation Normal" for the profile
orientation to ensure a smooth sweep

<img src=./images/swept_surface.PNG width="501">

Now to divide our segment we can use Toolbar > Surfaces > Trim Surface

<img src=./images/trim_surface.PNG width="501">

Perform the same procedure using the remaining boundary planes to generate the
desired segments.

## Step 3: Trimming the connecting sections

To generate the T-junction we will need to align the connecting patches of our
created cylindrical sections as well as divide the outlet edges into multiple
sections using a Trim Surface. To do so modify the end points of our T-junction such
that the cylindrical segments overlap slightly.

<img src=./images/overlapping.PNG width="501">

now we can generate a plane using this set of points to create a sketch which can act
as our trimming lines.

<img src=./images/trimming_plane.PNG width="501">

We can now draw a partial rectangle which act as the trimming lines for our
T-junction.

<img src=./images/trimming_lines.PNG width="501">

Notice how the segments of our partial edges are divided into 3 segments. Each
segment acts to halve the trimmed edge.

<img src=./images/trim_with_sketch.PNG width="501">

These segments will create edges which can be lofted to generate our T-Junction

<img src=./images/loftable_edges.PNG width="501">

## Step 4: Generating the T-Junction

To generate the T-Junction use Toolbar > Surfaces > Lofted Surface on adjacent edges

<img src=./images/lofted_surfaces.PNG width="501">

Now this doesn't look too realistic so we can apply a tangency to face boundary
condition

<img src=./images/all_lofted_surfaces.PNG width="501">


Finally we can fill the holes using Toolbar > Surfaces > Surface Fill

<img src=./images/surface_fill.PNG width="501">

Note: we can modify the T-Junction by modifying the surface time sketch

<img src=./images/modifiable_sketch.PNG width="501">

Now we can export the file as step file to generate a CFD Mesh with pointwise