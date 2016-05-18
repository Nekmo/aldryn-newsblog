"""Faked Meta module if Django-meta isn't installed and configured.
"""

class FakeMeta(object):
    pass


class FakeMetaModel(object):
    def as_meta(self):
        return FakeMeta()
