from time import sleep


class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        hh = str(self._hour).rjust(2, '0')
        mm = str(self._minute).rjust(2, '0')
        ss = str(self._second).rjust(2, '0')
        return f'{hh}:{mm}:{ss}'


if __name__ == '__main__':
    clock = Clock(23, 59, 58)

    while True:
        print(clock.show())
        sleep(1)
        clock.run()
