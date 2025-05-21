import random


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length
        self.new_psw = ''

    def __call__(self):
        length_new_psw = random.randint(self.min_length, self.max_length)
        return self.new_psw.join(random.choice(self.psw_chars) for _ in range(length_new_psw))


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
psw = rnd()
lst_pass = [rnd() for _ in range(3)]
print(lst_pass)
