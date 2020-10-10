import arterygen as ag
import pathlib as pt

cwd = pt.Path(__file__).parent

step_folder = cwd/"step_files"
foam_folder = cwd/"foam_cases"

if __name__ == "__main__":
    event_handler = ag.watchdog.handlers.STEPToFoamNewtonianSteadyFoam(foam_folder)
    observer      = ag.watchdog.observers.Step(step_folder, event_handler)
    observer.run()