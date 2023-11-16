"""
Speed-up your code by automatically identifying functions that should use caching in your code!
:param module: the module to wrap
:param autocache_path: the path to store the files required by CacheGenius
"""
from sys import modules
from types import ModuleType
from .cachegenius import autocache_func, autocache_module, report, empty

__all__ = ["autocache_func", "autocache_module", "report", "empty"]


class CallableModule(ModuleType):
    """Inspired from https://stackoverflow.com/a/74604283"""

    def __init__(self):
        ModuleType.__init__(self, __name__)
        self.__dict__.update(modules[__name__].__dict__)

    def __call__(self, *args, **kwargs):
        autocache_module(*args, **kwargs)

    mod_call = __call__
    __all__ = list(set(vars().keys()) - {"__qualname__"})


modules[__name__] = CallableModule()
