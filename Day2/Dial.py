class Dial:
    def __init__(self, start):
        self.position = start
        self.zero_counter = 0
        self.max_position = 99
        self.min_position = 0


    def turn_right(self, distance):
        new_abs_position = self.position + distance
        if new_abs_position > self.max_position:
            to_hit_zero = self.max_position + 1 - self.position
            rest = distance - to_hit_zero
            number_of_zeros = int(rest / (self.max_position + 1)) + 1

            self.position = rest % (self.max_position + 1)

            self._increase_zero_counter(number_of_zeros)
            print("Number of zeros hit while turning right: {}".format(number_of_zeros))
        else:
            self.position = new_abs_position

        self._check_for_zero()


    def turn_left(self, distance):
        new_abs_position = self.position - distance
        if new_abs_position < self.min_position:
            to_hit_zero = self.position + 1
            rest = distance - to_hit_zero
            number_of_zeros = int(rest / (self.max_position + 1)) + 1
            
            self.position = self.max_position - (rest % (self.max_position + 1))

            print("Number of zeros hit while turning left: {}".format(number_of_zeros))
            self._increase_zero_counter(number_of_zeros)
        else:
            self.position = self.position - distance

        self._check_for_zero()


    def get_zero_count(self):
        return self.zero_counter

    def _check_for_zero(self):
        if(self.position == 0):
            self._increase_zero_counter(1)

    def _increase_zero_counter(self, number_of_hits):
        self.zero_counter += number_of_hits