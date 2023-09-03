from SRC.calculator import add
import logging
import pytest

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def test_positive_add():
    logger.info("positive test case")
    result = add(3, 4)
    assert result == 7

def test_add():
    logger.info("negative test case")
    result = add(3, -4)
    assert result == -1

def test_add_string():
    logger.warning("high chances of exception")
    with pytest.raises(TypeError):
        add("string", 4)

def testCalculation():
    logger.debug("Check the sum")
    assert 2+2 == 4