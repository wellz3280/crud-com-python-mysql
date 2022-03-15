# from abc import ABCMeta,abstractmethod
# (metaclass=ABCMeta)
class TakeBy:
    def __init__(self,table,data):
        self.table = table
        self.data = data

    def take_by_keys(self):
        data = self.data
        keys = []

        for key in data.keys():
            keys.append(key)

        return keys

    def take_by_values(self):
        data = self.data
        values = []

        for value in data.values():
            values.append(value)

        return values
