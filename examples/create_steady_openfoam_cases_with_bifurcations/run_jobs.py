import pathlib as pt
import arterygen as ag
import config
import logging
import numpy as np
import multiprocessing as mp
import click

logging.basicConfig(level=logging.INFO)

def submit_job(folder: pt.Path, remote_destination: pt.Path, manager_dict: dict):

    log_path = folder/"job_log.npz"

    client   = ag.remote.Client(config.host, config.username, config.password, retry_limit=100)

    client.copy_local_to_remote(folder, remote_destination)

    # if on windows ensure that the shell script is dos
    client.ssh.exec_command(
        f"cd {(remote_destination/folder.name).as_posix()}; dos2unix openfoam_job.sh"
    )
    # submit the job

    _, stdout, _ = client.ssh.exec_command(
        f"cd {(remote_destination/folder.name).as_posix()}; qsub openfoam_job.sh"
    )

    # keep track job id
    output = stdout.read().decode("utf-8")
    job_id = output.split(".")[0]
    np.savez(log_path, job_id=job_id)
    client.logger.info(f"{folder.name} is running with JobID: {job_id}")
    manager_dict[job_id] = remote_destination/folder.name

    client.disconnect()


def download_job(remote_folder: pt.Path, local_destination: pt.Path):

    client = ag.remote.Client(config.host, config.username, config.password)
    client.logger.info(f"{remote_folder.name} has finished running")
    client.copy_remote_to_local(remote_folder, local_destination)
    client.delete_remote_directory(remote_folder)
    client.disconnect()

@click.command()
@click.option("--local_main_folder", default=".", type=pt.Path)
@click.option("--remote_main_folder", type=pt.Path)
@click.option("--max_cases", default=4, type=int)
def main(local_main_folder, remote_main_folder, max_cases):

    client = ag.remote.Client(config.host, config.username, config.password)

    all_cases     = list(local_main_folder.glob("*"))
    running_cases = mp.Manager().dict()

    while True:

        # copy over the desired number of cases to the super computer
        if len(running_cases) < max_cases:
            try:
                folder = all_cases.pop()

                p = mp.Process(target=submit_job, args=(folder, remote_main_folder, running_cases))
                p.start()
                p.join()
            except:
                pass

        # check whether some jobs are complete and copy them back to the local system
        for job_id in list(running_cases.keys()):
            remote_folder = running_cases[job_id]
            # the file which submits the job should create a dummy file called completed.tmp
            _, stdout, _  = client.ssh.exec_command("cd %s; FILE=completed.tmp; [ -e \"./$FILE\" ] && echo 1 || echo 0"%remote_folder.as_posix())
            parsed_stdout = bool(int(stdout.read().decode("utf-8")))
            if parsed_stdout:
                p             = mp.Process(
                    target=download_job, args=(remote_folder, local_main_folder))
                p.start()
                p.join()
                running_cases.pop(job_id)
        if all([not len(all_cases), not len(running_cases)]):
            break

    client.disconnect()

if __name__ == "__main__":
    main()