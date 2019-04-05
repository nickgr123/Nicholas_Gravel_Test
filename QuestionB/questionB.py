import re


class Version:

    def __init__(self, version):
        if version is None:
            raise Exception("Version can not be None")
        if not isinstance(version, str):
            raise Exception("Version must be string")
        pattern = re.compile('^(?:(\d+\.(?:\d+\.)*\d+))$')
        if not pattern.match(version):
            raise Exception("Invalid Format")
        self.version = version

    def __eq__(self, other):
        if isinstance(other, Version):
            return self._createVersionTuple(self.version) == self._createVersionTuple(other.version)
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, Version):
            return self._createVersionTuple(self.version) > self._createVersionTuple(other.version)
        return False

    def __lt__(self, other):
        if isinstance(other, Version):
            return self._createVersionTuple(self.version) < self._createVersionTuple(other.version)
        return False

    def _createVersionTuple(self, version):
        return tuple(map(int, (version.split("."))))
