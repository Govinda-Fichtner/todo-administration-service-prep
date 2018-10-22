import sys
from pytest import fixture

# ensure that the lib package can be found by tests
sys.path.append("../..")


@fixture
def context():
    return {}
