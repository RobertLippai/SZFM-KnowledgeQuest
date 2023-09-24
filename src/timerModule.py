class TimerManger:
    def __init__(self, count_from):
        self.count_from = count_from
        self.time_left = count_from

    def decrement(self):
        if self.time_left > 0:
            self.time_left = self.time_left - 1
        return self.time_left

    def get_time_left(self):
        return self.time_left

    def reset(self):
        self.time_left = self.count_from
