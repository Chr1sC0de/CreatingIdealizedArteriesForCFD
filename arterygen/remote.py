import paramiko as po
import scp
import pathlib as pt
import logging
from functools import wraps


class Copy_a_to_b_decorator:

    def __init__(self, path_a_type, path_b_type):
        self.path_a_type = path_a_type
        self.path_b_type = path_b_type

    def __call__(self, function):

        def decorator(obj: "Client", path_a: pt.Path, path_b: pt.Path, retries=0):
            retries += 1
            path_a = pt.Path(path_a)
            path_b = pt.Path(path_b)
            template = '%s %s To %s %s'%(self.path_a_type, path_a, self.path_b_type, path_b)
            if retries == 1:
                obj.logger.info('Copying %s'%template)
            try:
                function(obj, path_a, path_b, retries=retries)
                obj.logger.info('Completed Copy %s'%template)
                return True
            except ConnectionAbortedError:
                if not obj.ssh.get_transport().is_active():
                    obj.connect()
                obj.logger.info('Retrying Copy'%template)
                if retries > obj.retry_limit:
                    raise ConnectionError("Number of retries, %d, greater than retry limit %d"% (retries, obj.retry_limit) )
                obj.put(path_a, path_b, retries=retries)

        return decorator

class Client:

    def __init__(self, host, username, password, port=22, retry_limit=100):

        self.port        = port
        self.host        = host
        self.username    = username
        self.password    = password
        self.retry_limit = retry_limit
        self.logger      = logging.getLogger(f"{self.__class__.__name__}:{self.username}{self.host}")
        self.ssh         = po.SSHClient()
        self.ssh.load_system_host_keys()
        self.connect()

    def connect(self, *args, retries=0, **kwargs):
        retries+=1
        try:
            self.ssh.connect(self.host, username=self.username, password=self.password)
            self.transport = self.ssh.get_transport()
            self.scp       = scp.SCPClient(self.transport)
        except:
            if retries > self.retry_limit:
                raise ConnectionError(
                    "Number of retries, %d, greater than retry limit %d, \
                        cannot connect"%(retries, self.retry_limit)
                )
            self.logger.info('Retrying Connect')
            self.connect(retries=retries)

    def disconnect(self):
        self.ssh.close()
        self.scp.close()
        self.transport.close()

    @Copy_a_to_b_decorator("Local", "Remote")
    def copy_local_to_remote(self, local_folder, remote_folder, retries=100):
        self.scp.put(local_folder.as_posix(), remote_path=remote_folder.as_posix(),recursive=True)

    @Copy_a_to_b_decorator("Remote", "Local")
    def copy_remote_to_local(self, remote_folder, local_folder, retries=100):
        self.scp.get(remote_folder.as_posix(), local_path=local_folder.as_posix(), recursive=True)

    # utiltiy function for deleting a remote directory
    def delete_remote_directory(self, remote_folder):
        remote_folder = pt.Path(remote_folder)
        self.logger.info('Removing %s from %s'%(remote_folder,self.host))
        self.ssh.exec_command(
            "rm -rf %s"%(remote_folder.as_posix())
        )
        self.logger.info('Completed Removing %s from %s'%(remote_folder,self.host))
