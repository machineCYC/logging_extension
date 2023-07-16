import logging
from logging.config import dictConfig

import writer
from writer import MonitorLog

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "stdformatter": {
            "format": "%(module)s - %(levelname)s - %(funcName)s - %(lineno)s: %(message)s"
        },
    },
    "handlers": {
        "stdhandler": {
            "class": "logging.StreamHandler",
            "formatter": "stdformatter",
            'stream': 'ext://sys.stdout'
        },
        "specialhandler":{
            "class" : "writer.SpecialHandler",
            "formatter": "stdformatter",
        }
    },
    "loggers" : {
        "root": {
            "handlers": ["stdhandler", "specialhandler"],
            "level": "DEBUG",
            "propagate": True
            }
        }
}

dictConfig(LOGGING)
logger = logging.getLogger()
logger.debug("logger started")

mes_plaoload = {
    "job_name":"QQ",
    "job_start_time":"time_QQ"
}
msg_obj = MonitorLog(**mes_plaoload)

logging.log(level=100, msg=msg_obj)
