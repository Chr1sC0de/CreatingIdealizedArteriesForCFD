import arterygen as ag
import pathlib as pt
import click
from functools import partial

# example simple python script which automatically converts a step file into an
# openfoam case

cwd = pt.Path(__file__).parent

step_folder = cwd/"step_files"
foam_folder = cwd/"foam_cases"

if __name__ == "__main__":
    # create an event handler for step files
    event_handler = ag.watchdog.handlers.STEPToFoamNewtonianSteadyFoam(foam_folder)
    # control the mesh density parameters
    event_handler.dimension_spacing = 0.2
    event_handler.wall_spacing = event_handler.dimension_spacing/6
    # create our observer which will launch the event handler on any updates
    observer      = ag.watchdog.observers.Step(step_folder, event_handler, max_wait=5)
    observer.run()