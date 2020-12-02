try:
    from .test_gnuprolog import all_gnu_tests
except Exception:
    pass

try:
    from .test_swipy import all_swipl_tests
except Exception:
    pass

try:
    from .test_xsb import all_xsb_tests
except Exception:
    pass

from .test_kanren import test_kanren
from .test_datalog import test_datalog
from .test_language import test_language

