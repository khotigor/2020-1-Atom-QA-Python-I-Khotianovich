"""
This script is for testing Dictionary.
"""
import pytest

DIC_FOR_TEST = {1: 'a', 2: 'b', 3: 'c'}


class TestDictionary:
    """This class is for testing Dictionary."""

    @staticmethod
    def test_dic_1_copy():
        """function to check copy in dictionary"""
        assert DIC_FOR_TEST == DIC_FOR_TEST.copy()

    @staticmethod
    def test_dic_2_get():
        """function to check get in dictionary"""
        assert DIC_FOR_TEST.get(1) == 'a'

    @staticmethod
    def test_dic_3_update():
        """function to check update in dictionary"""
        DIC_FOR_TEST.update({4: 'd'})
        assert DIC_FOR_TEST.get(4) == 'd'

    @staticmethod
    def test_dic_3_pop():
        """function to check pop in dictionary"""
        DIC_FOR_TEST.pop(4)
        assert DIC_FOR_TEST.get(4) is None

    @staticmethod
    @pytest.mark.parametrize('id_for_pop', [3, 2, 1])
    def test_dic_5_pop_all(id_for_pop):
        """
        :param id_for_pop: list of ints
        parametrized test which checks pop in dictionary.
        """
        DIC_FOR_TEST.pop(id_for_pop)
        assert DIC_FOR_TEST.get(id_for_pop) is None
