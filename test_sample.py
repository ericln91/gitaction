import garbage
import numpy as np

def test_foo():
    data = garbage.foo()
    assert len(data) == 10

def test_bar():
    xx = garbage.bar()
    assert type(xx) == np.ndarray

def test_foo2():
    data = garbage.bar()
    assert type(data) == str