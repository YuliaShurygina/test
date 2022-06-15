class Training:
    def __init__(self, action, duration, weight ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        pass
    def get_distance(self):
    def get_mean_speed(self):
    def get_spent_calories(self):


class Running(Training):
    coeff_calorie_1 = 18
    coeff_calorie_2 = 20 
    def get_spent_calories(self):

class SportsWalking(Training):
    def __init__(self, height,  action, duration, weight):
    super().__init__(action, duration, weight)
    self.height = height
    def get_spent_calories(self):


class Swimming(Training):
    def __init__(self, length_pool, count_pool) -> None:
        super().__init__()
        self.length_pool = length_pool
        self.count_pool = count_pool
        def get_spent_calories(self):
        def get_mean_speed(self):


class InfoMessage:
    def get_message()