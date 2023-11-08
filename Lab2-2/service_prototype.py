import copy


class ServicePrototype:
    def clone(self):
        return copy.deepcopy(self)
