from HttpTriggerRvStatus.vrm_site import VrmSite
import yaml
import pytest

from HttpTriggerRvStatus.victron_vrm import VrmSession


class TestVrm(object):

    @staticmethod
    def login():
        return VrmSession(username=None, password=None, demo=True)

    def test_login(self, vrm_session):
        assert vrm_session.initialized

    def test_userid(self, vrm_session: VrmSession):
        userid = vrm_session.userid
        assert int(userid) == 22

    def test_sites(self, vrm_session: VrmSession):
        sites = vrm_session.sites
        assert sites
        assert len(sites) == 3
        for site in sites:
            print(site.name, site.name in [
                "ResTS05 (PD)", "VIC JONES", "Victron GlobalLink 520 - AU Demo - BMV-712 & 150/70 MPPT"])


@pytest.fixture
def vrm_session() -> VrmSession:
    return TestVrm.login()
