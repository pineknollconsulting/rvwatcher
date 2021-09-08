
class VrmException(Exception):
    def __init__(self, message: str, status_code=None) -> None:
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class VrmLoginFailure(VrmException):
    def __init__(self, message: str = "Login failed", status_code=None) -> None:
        super().__init__(message=message, status_code=status_code)


class VrmRequestFailure(VrmException):
    def __init__(self, message: str = "Request failed", status_code=None) -> None:
        super().__init__(message=message, status_code=status_code)
