import pytest
import src.funcions as f

def test_primo_1():
    assert f.es_primo(7) == True
    
def test_no_es_primo():
    assert f.es_primo(8) == False
    
    