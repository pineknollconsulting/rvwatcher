from . import vrmapi
from . import vrm_site


class VrmNotLoggedIn(Exception):
    pass


class VrmSession(object):
    def __init__(self, username: str, password: str, demo: bool = False) -> None:
        super().__init__()
        self._api: vrmapi.VRM_API = vrmapi.VRM_API(username, password, demo)
        self._sites = None
        self._userid = None

    def initialized(self):
        return self._api.is_initialized

    @property
    def userid(self):
        return self._api.user_id

    @property
    def sites(self):
        sites = self._api.get_user_sites(
            self._api.user_id, extended=False)
        self._sites = vrm_site.VrmSites(**sites)
        return self._sites
