from SRC.calculator import subtract, add
import logging
import pytest

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def test_positive_subtract():
    logger.info("positive test case")
    result = subtract(4,3)
    assert result == 1

def test_subtract():
    logger.info("negative test case")
    result = subtract(3, -4)
    assert result == 7

def test_add_string():
    logger.warning("high chances of exception")
    with pytest.raises(TypeError):
        add("string", 4)

def testCalculation():
    logger.debug("Check the sum")
    assert 2+2 == 4