import pytest
from HttpTriggerRvStatus.victron_vrm import VrmSession


class TestVrm(object):

    @staticmethod
    def login():
        return VrmSession(username=None, password=None, demo=True)

    def test_login(self, vrm_session):
        assert vrm_session.initialized


@pytest.fixture
def vrm_session() -> VrmSession:
    return TestVrm.login()
