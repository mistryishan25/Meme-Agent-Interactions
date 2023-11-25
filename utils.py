class Logger:

    def __init__(self, verbose=True):
        self.verbose = verbose

    def __call__(self, msg, *args):
        if self.verbose:
            print(msg, *args)
