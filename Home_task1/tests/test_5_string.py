"""
This script is for testing String.
"""
import pytest

STR_FOR_TEST = " Ququshka "
STR_FOR_TEST_T5 = STR_FOR_TEST


class TestString:
    """This script is for testing String."""

    @staticmethod
    def test_str_3_len():
        """function to check len in string"""
        assert len(STR_FOR_TEST) == 10

    @staticmethod
    def test_str_2_strip():
        """function to check strip in string"""
        str_for_test_copy_t2 = STR_FOR_TEST
        assert len(str_for_test_copy_t2.strip()) == 8
        assert str_for_test_copy_t2.strip()[0] != " "
        assert str_for_test_copy_t2.strip()[7] != " "
        with pytest.raises(IndexError):
            assert str_for_test_copy_t2.strip()[9] != " "

    @staticmethod
    def test_str_3_lower():
        """function to check lower in string"""
        str_for_test_copy_t3 = STR_FOR_TEST
        assert str_for_test_copy_t3.strip().lower()[0] == 'q'

    @staticmethod
    def test_str_4_sum():
        """function to check sum in string"""
        str_for_test_copy_t4 = STR_FOR_TEST
        assert len(str_for_test_copy_t4 + str_for_test_copy_t4) == len(
            str_for_test_copy_t4) * 2

    @staticmethod
    @pytest.mark.parametrize('i', list(range(len(STR_FOR_TEST_T5.strip()))))
    def test_str_5_upper(i):
        """
        :param i: iterator for string STR_FOR_TEST_T5
        Parametrized test which checks upper in string.
        """
        assert STR_FOR_TEST_T5.strip().upper()[i].isupper()
