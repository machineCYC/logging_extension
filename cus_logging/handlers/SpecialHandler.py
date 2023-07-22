import logging
from dataclasses import asdict

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from cus_logging.data_models import MonitorEnpointBase


class SpecialHandler(logging.Handler):

    def __init__(self) -> None:
        super().__init__(100)
        # logging.Handler.__init__(self=self)
        self.url = "http://127.0.0.1:8000"
        self.session = session = requests.Session()
        self.adapter = HTTPAdapter(
            max_retries=Retry(
                total=2,
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
