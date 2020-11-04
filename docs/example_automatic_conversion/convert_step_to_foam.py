import arterygen as ag
import pathlib as pt
import click

# example simple python script which automatically converts a step file into an
# openfoam case

cwd = pt.Path(__file__).parent

step_folder = cwd/"step_files"
foam_folder = cwd/"foam_cases"

if __name__ == "__main__":
    # create an event handler for step files
    event_handler = ag.watchdog.handlers.STEPToFoamNewtonianSteadyFoam(foam_folder)
    # create our observer which will launch the event handler on any updates
    observer      = ag.watchdog.observers.Step(step_folder, event_handler)
    observer.run()