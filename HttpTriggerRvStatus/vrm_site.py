
from .util import camel_to_snake
import typing


class VrmSiteFailure(Exception):
    pass


class VrmSite(object):
    pass


class VrmSites(object):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        success: bool = kwargs.pop("success")
        records: typing.Sequence(typing.Collection) = kwargs.pop("records")
        if not success:
            raise VrmSiteFailure

        self.sites = []
        for record in records:
            site = VrmSite()
            self.sites.append(site)
            for k, v in record.items():
                setattr(site, camel_to_snake(k), v)
