
import cups

class CUPSWatch(object):
    def __init__(self, configItems = None):
        self.configItems = configItems or []

    def watch(self):
        cupsConnection = cups.Connection(self.configItems['server'])
        activeJobs = cupsConnection.getJobs(which_jobs="not-completed")
