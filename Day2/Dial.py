class Dial:
    def __init__(self, start):
        self.position = start
        self.zero_counter = 0
        self.max_position = 100
        self.min_position = 0

    # Simulate each rotation stop - turning right
    def turn_right(self, distance):
        for _ in range(distance):
            self.position = (self.position + 1) % 100
            self._check_for_zero()

    # # Simulate each rotation stop - turning left
    def turn_left(self, distance):
        for _ in range(distance):
            self.position = (self.position - 1) % 100
            self._check_for_zero()

    def get_zero_count(self):
        return self.zero_counter

    def _check_for_zero(self):
        if(self.position == 0):
            self._increase_zero_counter(1)

    def _increase_zero_counter(self, number_of_hits):
        self.zero_counter += number_of_hits