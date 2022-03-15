class TakeBy:
    def take_by_keys(self,data):
        dado = data
        keys = []

        for key in dado.keys():
            keys.append(key)

        return keys

    def take_by_values(self,data):
        dado = data
        values = []

        for value in dado.values():
            values.append(value)

        return values