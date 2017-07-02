import unittest
import pytest
from transformpy import trim

x = [1, 2, 3, 4, 5]

class TestArgs_x(unittest.TestCase):
    def test_trim_x_missing(self):
        with pytest.raises(TypeError):
            trim()

    def test_trim_x_nonnumeric(self):
        with pytest.raises(TypeError):
            trim('a')

class TestArgs_method(unittest.TestCase):
    def test_trim_method(self):
        with pytest.raises(ValueError):
            trim([1, 2], method = 'foo')

class TestArgs_lo_hi(unittest.TestCase):        
    def test_trim_hi_lo_one_provided(self):
        with pytest.raises(ValueError):
            trim([1, 2])

    def test_trim_lo_nonnumeric(self):
        with pytest.raises(ValueError):
            trim([1, 2], lo = 'foo')

    def test_trim_hi_nonnumeric(self):
        with pytest.raises(ValueError):
            trim([1, 2], hi = 'foo')

    def test_trim_hi_less_than_lo(self):
        with pytest.raises(ValueError):
            trim([1, 2], lo = 1, hi = 0)

class TestOutput(unittest.TestCase):
    def test_trim_lo_below_min(self):
        assert trim(x, lo = 0) == [1, 2, 3, 4, 5]

    def test_trim_lo_at_min(self):
        assert trim(x, lo = 1) == [1, 2, 3, 4, 5]

    def test_trim_lo_has_effect(self):
        assert trim(x, lo = 2) == [2, 2, 3, 4, 5]

    def test_trim_hi_above_max(self):
        assert trim(x, hi = 6) == [1, 2, 3, 4, 5]

    def test_trim_hi_at_max(self):
        assert trim(x, hi = 5) == [1, 2, 3, 4, 5]

    def test_trim_hi_has_effect(self):
        assert trim(x, hi = 4) == [1, 2, 3, 4, 4]
        
    def test_trim_lo_and_hi(self):
        assert trim(x, lo = 2, hi = 4) == [2, 2, 3, 4, 4]
        