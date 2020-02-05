class LogStream(object):
    def __init__(self):
        self.logs = ''

    def write(self, str):
        self.logs += str

    def flush(self):
        pass

    def __str__(self):
        return self.logs
