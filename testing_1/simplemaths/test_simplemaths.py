import pytest
from simplemaths.simplemaths import SimpleMaths as sm

class TestSimpleMaths():
    pass

def test_FloatInput():
    '''Negative test: Attempts to input a float '''
    with pytest.raises(TypeError):
        sm(1.0)

def test_ListInput():
    '''Negative test: Attempts to input a list of numbers'''
    with pytest.raises(TypeError):
        sm([2,4])

def test_square():
    '''Positive test: checks basic number squaring'''
    obj = sm(2)
    assert obj.square() == 4

def test_factorial():
    '''Positive test: checks basic factorial'''
    obj = sm(3)
    assert obj.factorial() == 6

def test_factorial_zero():
    '''Positive test: checks 0 factorial is equal to 1'''
    obj = sm(0)
    assert obj.factorial() == 1

def test_power():
    '''Positive test: checks default invoke of power'''
    obj = sm(3)
    assert obj.power() == 27

def test_powertozero():
    '''Positive test: checks that number to the power of zero is one'''
    obj = sm(3)
    assert obj.power(0) == 1

def test_oddeveneven():
    '''Positive test: checks even number returns even result'''
    obj = sm(2)
    assert obj.odd_or_even() == 'Even'

def test_oddevenodd():
    '''Positive test: checks odd number returns odd result'''
    obj = sm(3)
    assert obj.odd_or_even() == 'Odd'

def test_oddevenzero():
    '''Positive test: checks zero returns even result, as expected by this method'''
    obj = sm(0)
    assert obj.odd_or_even() == 'Even'

def test_squareroot():
    '''Positive test: checks basic invoke of square root'''
    obj = sm(4)
    assert obj.square_root() == 2

def test_squareroot_imag():
    '''Positive test: checks square root of negative number returns expected imaginary number, ignoring real component due to memory precision'''
    obj = sm(-4)
    assert obj.square_root() == pytest.approx(2j)

