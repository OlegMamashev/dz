class ListMath:
    def __init__(self, lst: list = []):
        self.lst = lst

    @property
    def lst(self):
        return self._lst

    # @lst.setter
    # def lst(self, value):
    #     for i in value:
    #         if i