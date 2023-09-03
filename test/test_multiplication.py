from SRC.calculator import multiply, add
import logging
import pytest

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def test_multiplication():
    logger.info("positive test case")
    result = multiply(3, 4)
    assert result == 12

def test_negative_multiplication():
    logger.info("negative test case")
    result = multiply(3, -4)
    assert result == -12

def test_add_string():
    logger.warning("high chances of exception")
    with pytest.raises(TypeError):
        add("string", 4)

def testCalculation():
    logger.debug("Check the sum")
    assert 2+2 == 4