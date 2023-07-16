from dataclasses import dataclass
from cus_logging.data_models.MonitorEnpointBase import MonitorEnpointBase


@dataclass
class MonitorLog(MonitorEnpointBase):
    job_name: str
    job_start_time: str

    def __post_init__(self):
        self.endpoint = "monitor/job"
        # self._check_nested_field("task", Task)