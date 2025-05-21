class WordString:
    def __init__(self):
        self.string = ''

    def __len__(self):
        return len(self._string.split())

    def __call__(self, indx):
        words_list = self._string.split()
        return words_list[indx]

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self._string = value


words = WordString()
words.string = "Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
