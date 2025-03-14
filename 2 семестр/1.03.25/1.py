class Factory:
    @staticmethod
    def build_sequence():
        seq = list()
        return seq

    @staticmethod
    def build_number(string):
        string = int(string)
        return string


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(','):
            item = factory.build_number(sub)
            seq.append(item)
        return seq


loader = Loader
print(loader.parse_format('4, 5, -6', Factory))
