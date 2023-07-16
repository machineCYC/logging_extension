import logging
from dataclasses import asdict
from dataclasses import dataclass
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class MonitorBase:
    """
    do some validate
    """
    def _check_nested_field(self, attr_name:str, _cls:Any) -> None:
        pass


class MonitorEnpointBase(MonitorBase):
    endpoint: str


@dataclass
class MonitorLog(MonitorEnpointBase):
    job_name: str
    job_start_time: str

    def __post_init__(self):
        self.endpoint = "monitor/job"
        # self._check_nested_field("task", Task)

class SpecialHandler(logging.Handler):

    def __init__(self)-> None:
        logging.Handler.__init__(self=self)
        self.url = "http://127.0.0.1:8000"
        self.session = session = requests.Session()
        self.adapter = HTTPAdapter(
            max_retries=Retry(
                total=5,
                backoff_factor=0.5,
                # status_forcelist=[403, 500]
                allowed_methods=Retry.DEFAULT_ALLOWED_METHODS.union(["POST"])
            ),
        )
        self.session.mount('https://', self.adapter)
        self.session.mount('http://', self.adapter)


    def emit(self, record) -> None:
        if isinstance(record.msg, MonitorEnpointBase):
            response = self.session.post(f"{self.url}/{record.msg.endpoint}", json=asdict(record.msg))
