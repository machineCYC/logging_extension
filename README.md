# logging_extension

Develop the customer logging to support sending the log to the database through web API

    - api folder is the code base for the api service
    - cus_logging is the code base for the customer logging

Our target is doing the coustomer log when logging some information

In this case is show the log in the console and send the log to an api service at the same time

The python logging module has four main components

    - Loggers: log collector
    - Handlers: decide the distination of the log
    - Formatters: format the log
    - Filters: filter out some log

base on the definetion of the logging components, we can customize the handler, use the handler to send the request to api service

## setup the python env
    - poetry install

## run the code
    - run the api service
        - cd api/
        - uvicorn main:app --reload
    - run the logging example
        - python example.py

## Reference

- [Writing Custom Log Handlers In Python](https://dev.to/salemzii/writing-custom-log-handlers-in-python-58bi)

- [Python Logging Tutorial: How-To, Basic Examples & Best Practices](https://sematext.com/blog/python-logging/)