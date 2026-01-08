class Timer:
    def __init__(self, duration_ms: int = 0):
        self.elasped = 0
        self.duration = duration_ms

    def update_timer(self, delta_time: int):
        self.elasped += delta_time
    
    def has_elasped(self) -> bool:
        if self.elasped > self.duration:
            self.elasped = 0
            return True
        else:
            return False