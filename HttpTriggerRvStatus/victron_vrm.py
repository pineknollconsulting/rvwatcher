from typing import Union, Sequence
from . import vrmapi
from . import vrm_site


class VrmNotLoggedIn(Exception):
    pass


class VrmSession(object):
    def __init__(self, username: str, password: str, demo: bool = False) -> None:
        super().__init__()
        self._api: vrmapi.VRM_API = vrmapi.VRM_API(username, password, demo)
        self._sites: Union[Sequence[vrm_site.VrmSite], None] = None
        self._userid: int = int(self._api.user_id)

    def initialized(self) -> bool:
        return self._api.is_initialized

    @property
    def userid(self) -> int:
        return self._api.user_id

    @property
    def sites(self) -> vrm_site.VrmSite:
        sites = self._api.get_user_sites(
            self._api.user_id, extended=False)
        vrm_sites = vrm_site.VrmSites(**sites)
        self._sites = vrm_sites.sites
        return self._sites
