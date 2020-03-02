"""
This script is for testing Set.
"""
import random
import pytest

SET_FOR_TEST1 = {1, 2, 3}
SET_FOR_TEST2 = {4, 5}


class TestSet:
    """This class is for testing Set."""

    @staticmethod
    def test_set_1_len():
        """function to check len in set"""
        assert len(SET_FOR_TEST1) == 3

    @staticmethod
    def test_set_2_repeat_an_element():
        """function to check isdisjoint in set"""
        assert SET_FOR_TEST1.isdisjoint(SET_FOR_TEST2)

    @staticmethod
    def test_set_3_copy():
        """function to check copy in set"""
        set_for_test1_copy = SET_FOR_TEST1.copy()
        assert set_for_test1_copy == SET_FOR_TEST1

    @staticmethod
    def test_set_4_add():
        """function to check add in set"""
        set_for_test1_copy = SET_FOR_TEST1.copy()
        set_for_test1_copy.add(random.randint(10, 11))
        assert (len(set_for_test1_copy)) == (len(SET_FOR_TEST1) + 1)

    @staticmethod
    @pytest.mark.parametrize('set_for_test', [{1, 2, 3, 4, 5},
                                              {1, 2, 3, 4, 5, 6}])
    def test_set_5_subset(set_for_test):
        """
        :param set_for_test: set to check set to subset
        parametrized test which checks on subset.
        """
        assert set_for_test >= SET_FOR_TEST1
