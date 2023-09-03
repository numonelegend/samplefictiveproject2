from SRC.calculator import add, divide
import logging
import pytest

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def test_division():
    logger.info("positive test case")
    result = divide(4, 4)
    assert result == 1

def test_negative_division():
    logger.critical("Not to divide by zero")
    logger.info("negative test case")
    result = divide(4, -4)
    assert result == -1

def test_add_string():
    logger.warning("high chances of exception")
    with pytest.raises(TypeError):
        add("string", 4)

def testCalculation():
    logger.debug("Check the sum")
    assert 2+2 == 4