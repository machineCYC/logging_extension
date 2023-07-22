import logging
from logging.config import dictConfig

import yaml

from cus_logging.data_models import MonitorLog

with open("./cus_logging/configs/base_config.yaml", "r") as f:
    logging_config = yaml.load(f, Loader=yaml.FullLoader)

print(logging_config)
dictConfig(logging_config)
logger = logging.getLogger("cus-logger")
logger.debug("logger started")

mes_plaoload = {
    "job_name":"QQ",
    "job_start_time":"time_QQ"
}
msg_obj = MonitorLog(**mes_plaoload)

logging.log(level=100, msg=msg_obj)
