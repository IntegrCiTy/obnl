import pkg_resources  # part of setuptools
try:
    __version__ = pkg_resources.require("obnl")[0].version
except:
    pass
