import sys
sys.path.append(".")
import pytest
import platform
import os

from bin.perceptron import Perceptron

# Test expected to pass
def test_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
        ], [1, 1, 1, 0])

    assert the_perceptron.predict([1, 1]) == 1, "Error in [1,1], result should be 1"
    assert the_perceptron.predict([1, 0]) == 1, "Error in [1,0], result should be 1"
    assert the_perceptron.predict([0, 1]) == 1, "Error in [0,1], result should be 1"
    assert the_perceptron.predict([0, 0]) == 0, "Error in [0,0], result should be 0"


# Fail Test
@pytest.mark.xfail(reason="XFAIL", strict=True)

# Test expected to pass
def test_perceptron_fail():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
        ], [1, 1, 1, 0])

    assert the_perceptron.predict([1, 1]) == 0 , "Error in [1,1], result should be 1 - Failing Test"


@pytest.mark.skipif(platform.system()!="Linux", reason="Not linux ubuntu OS")

def test_memory():
    # GIVEN getting all memory using os.popen()
    total_memory, used_memory, free_memory = map(
        int, os.popen('free -t -m').readlines()[-1].split()[1:])

    assert total_memory > 0, "total memory is not less than 0"
    assert used_memory > 0, "used memory is not less than 0"
    assert free_memory > 0, "free memory is not less than 0"


@pytest.mark.skip(reason="This test is not yet ready for prime test")
def test_bogus():
    # GIVEN initial value of x
    x = 1234

    # THEN check value of data
    assert x == 4321, "X should be 'hey'"
