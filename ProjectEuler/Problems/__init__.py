from os.path import dirname, basename, isfile, join
import importlib
import glob


__globals = globals()
modules = glob.glob(join(dirname(__file__), "*.py"))
vals = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py') and not f.endswith('template.py')]
__all__ = vals

#for mod_name in vals :
   #s mod_name = file[:-3]   # strip .py at the end
    #__globals[mod_name] = importlib.import_module('.' + mod_name, package=__name__)