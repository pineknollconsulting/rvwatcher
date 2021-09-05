from . import vrmapi


class VrmSession(object):
    def __init__(self, username: str, password: str, demo: bool = False) -> None:
        super().__init__()
        self.api: vrmapi.VRM_API = vrmapi.VRM_API(username, password, demo)

    def initialized(self):
        return self.api.is_initialized
