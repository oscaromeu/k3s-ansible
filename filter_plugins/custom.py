__author__ = "oscar romeu"

from ansible import errors


class FilterModule(object):
    def filters(self):
        return {
            "is_list": self.is_list,
        }

    def is_list(self, value):
        return isinstance(value, list)
