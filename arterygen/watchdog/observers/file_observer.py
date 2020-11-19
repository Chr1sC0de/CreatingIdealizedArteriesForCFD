import pathlib as pt
from collections import OrderedDict
import abc
import logging
import time

logger = logging.getLogger()


class FileObserver(abc.ABC):

    @abc.abstractproperty
    def target_extension(self):
        NotImplemented


    def __init__(
        self, target_folder: pt.Path, event_handler, max_wait=None
    ):
        # event handler takes in the path to the new step fie
        self.target_folder = target_folder
        self.cases         = OrderedDict()
        self.event_handler = event_handler
        self.max_wait      = max_wait
        self._last_len_files = 0
        self._current_wait   = 0


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

            if len(self.cases) != self._last_len_files:
                self._last_len_files = len(self.cases)
                self._current_wait = 0
            else:
                self._current_wait += 1

            if self.max_wait is not None:
                # sleep for 1 second to simulate waiting for next
                time.sleep(1)
                if self._current_wait > self.max_wait:
                    break

class Step(FileObserver):
    target_extension = "STEP"