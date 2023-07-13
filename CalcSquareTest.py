import pytest


def MainSquare():
    main_square = MainSquare()
    pass


class test_main_square:
    def test_side_square(self):
        main_square = MainSquare()
        a = 5
        b = 5
        c = 5
        d = 5
        expected_result = 5
        result = self.main_square.side_square(a, b, c, d)
        assert result == expected_result


    def test_diagonal(self):
        main_square = MainSquare()
        a = 5
        expected_result = 7.071
        result = self.main_square.test_diagonal(a)
        assert result == expected_result


    def test_perimeter_square(self):
        main_square = MainSquare()
        a = 5
        expected_result = 20
        result = self.main_square.test_perimeter_square(a)
        assert result == expected_result


    def test_perimeter_square_by_zero(self):
        main_square = MainSquare()
        a = 5
        with pytest.raises(ZeroDivisionError):
            result = main_square.perimeter_square(a)



