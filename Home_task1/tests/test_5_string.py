"""
This script is for testing String.
"""
import pytest

STR_FOR_TEST = " Ququshka "


class TestString:
    """This script is for testing String."""

    @staticmethod
    def test_str_3_len():
        """function to check len in string"""
        assert len(STR_FOR_TEST) == 10

    @staticmethod
    def test_str_2_strip():
        """function to check strip in string"""
        assert len(STR_FOR_TEST.strip()) == 8
        assert STR_FOR_TEST.strip()[0] != " "
        with pytest.raises(IndexError):
            assert STR_FOR_TEST.strip()[9] != " "

    @staticmethod
    def test_str_lower():
        """function to check lower in string"""
        assert STR_FOR_TEST.strip().lower()[0] == 'q'

    @staticmethod
    def test_str_sum():
        """function to check sum in string"""
        assert len(STR_FOR_TEST + STR_FOR_TEST) == len(STR_FOR_TEST) * 2

    @staticmethod
    @pytest.mark.parametrize('i', list(range(len(STR_FOR_TEST.strip()))))
    def test_str_5_upper(i):
        """
        :param i: iterator for string STR_FOR_TEST
        Parametrized test which checks upper in string.
        """
        assert STR_FOR_TEST.strip().upper()[i].isupper()
