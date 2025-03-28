import time

class Timer:
    def sleep_timer(self, seconds: int) -> bool:
        time.sleep(seconds)
        return True