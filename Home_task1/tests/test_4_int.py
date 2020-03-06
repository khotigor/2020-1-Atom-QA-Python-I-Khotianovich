"""
This script is for testing int.
"""
import random
import math
import pytest


class TestInt:
    """This class is for testing int."""

    @staticmethod
    def test_int_1_sum():
        """function to check sum in int"""
        assert 1 + 1 == 2

    @staticmethod
    def test_int_2_pow():
        """function to check pow with int"""
        assert pow(random.randint(2, 5), 0) == 1

    @staticmethod
    def test_int_3_sqrt():
        """function to check sqrt with int"""
        with pytest.raises(ValueError):
            assert math.sqrt(-1)

    @staticmethod
    def test_int_4_abs():
        """function to check abs in int"""
        assert abs(-1) == 1

    @staticmethod
    @pytest.mark.parametrize('i', [random.randint(3, 5),
                                   random.randint(6, 10)])
    def test_int_5_more(i):
        """
        :param i: random integer
        (randint(3,5) or randint(6,10))
        Parametrized test which checks that
        randint(3,5) and randint(6,10) more than 2.
        """
        assert i > 2
