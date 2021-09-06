from dataclasses import dataclass
from .util import camel_to_snake
import typing
import logging


class VrmSiteFailure(Exception):
    pass


@dataclass
class VrmSite:
    id_side: int
    access_level: int
    owner: bool
    is_admin: bool
    name: str
    id_user: int
    pv_max: int
    timezone: str
    geofence_enabled: bool
    realtime_updates: bool
    has_mains: int
    has_generator: int
    alarm_monitoring: int
    invalid_v_r_m_auth_token_used_in_log_request: int
    syscreated: int
    grafana_enabled: int
    shared: bool
    device_icon: str
    identifier:  typing.Any = None
    phonenumber:  typing.Any = None
    notes:  typing.Any = None
    geofence:  typing.Any = None
    no_data_alarm_timeout:  typing.Any = None


class VrmSites(object):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        success: bool = kwargs.pop("success")
        records: typing.Sequence(typing.Collection) = kwargs.pop("records")
        if not success:
            raise VrmSiteFailure

        self.sites: typing.Sequence[typing.Collection] = []
        for record in records:
            reformatted_site = {camel_to_snake(
                k): v for (k, v) in record.items()}
            site = VrmSite(reformatted_site)
            self.sites.append(site)
