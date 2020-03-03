"""
This script is for testing List.
"""
import pytest

LIST_FOR_TEST1 = [1, 2, 3]
LIST_FOR_TEST2 = ['a', 'b']


class TestList:
    """This class is for testing List."""

    @staticmethod
    def test_list_1_count():
        """
        Function to check count in list. If we add
        one more 1, we have 1 more 1.
        """
        list_for_test1_len = LIST_FOR_TEST1.count(1)
        list_for_test1_copy_t1 = LIST_FOR_TEST1.copy()
        list_for_test1_copy_t1.append(1)
        assert list_for_test1_copy_t1.count(1) == (list_for_test1_len + 1)

    @staticmethod
    def test_list_2_index():
        """Function to check index in list.
        We have an 'a' in 0 position, so we have it."""
        assert LIST_FOR_TEST2.index('a') == 0

    @staticmethod
    def test_list_3_copy():
        """function to check copy in list"""
        list_for_test_copy = LIST_FOR_TEST1.copy()
        assert list_for_test_copy == LIST_FOR_TEST1

    @staticmethod
    def test_list_4_insert():
        """function to check insert in list"""
        list_for_tests2_copy_t4 = LIST_FOR_TEST2.copy()
        list_for_tests2_copy_t4.insert(2, 'c')
        assert list_for_tests2_copy_t4[2] == 'c'

    @staticmethod
    @pytest.mark.parametrize('id_for_pop', [2, 1, 0])
    def test_list_5_pop(id_for_pop):
        """
        :param id_for_pop: index in list to delete value
        Parametrized test which checks pop in list.
        """
        list_for_test1_t5_copy = LIST_FOR_TEST1.copy()
        assert list_for_test1_t5_copy[
            id_for_pop] == list_for_test1_t5_copy.pop(id_for_pop)
