import pytest
from main import add,sub,mul,div

def test_add():
    s= add(2,3)
    assert s ==5

def test_mul():
    s= mul(2,3)
    assert s == 6



