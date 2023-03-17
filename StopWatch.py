import time


class StopWatch():


    def __init__(self):
        self.start = time.time()
        self.countdown = 0


    def get_seconds(self):
        return int(self.countdown)


    def update(self, dt):
        now = time.time()

        self.countdown = now - self.start


    def reset(self):
        self.__init__()
