import sys
import os

import unittest
import numpy as np

from numpy.testing import assert_almost_equal, assert_equal, assert_string_equal
from numpy.testing import assert_allclose, assert_raises, assert_raises_regex

targdir = os.path.dirname(os.path.abspath(__file__)) + '/../'
thisdir = os.path.dirname(os.path.abspath(__file__)) + '/'

sys.path.append(targdir)
libdir = targdir + "lib/"
sys.path.append(libdir)

# new files and functions to test
from lib.tools import example_function


# unit tests to call
def test_example_function():
    assert_equal(True, example_function())
