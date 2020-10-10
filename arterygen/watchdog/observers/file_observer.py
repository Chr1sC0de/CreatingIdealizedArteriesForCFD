import pathlib as pt
from collections import OrderedDict
import abc


class FileObserver(abc.ABC):

    @abc.abstractproperty
    def target_extension(self):
        NotImplemented


    def __init__(
        self, target_folder: pt.Path, event_handler
    ):
        # event handler takes in the path to the new step fie
        self.target_folder = target_folder
        self.cases         = OrderedDict()
        self.event_handler = event_handler

    def update_case_files(self):
        files = list(self.target_folder.glob("*" + self.target_extension))
        for item in files:
            if item not in self.cases.keys():
                self.cases[item.absolute()] = False

    def run(self):
        while True:
            self.update_case_files()
            for key, value in self.cases.items():
                if not value:
                    self.event_handler(key)
                    self.cases[key] = True


class Step(FileObserver):
    target_extension = "STEP"