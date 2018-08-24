"""
Color-coding Slack log handler
"""

import logging
import requests


class SlackHandler(logging.Handler):
    """
    Color-coding Slack log handler
    """

    COLOR_DICT = {
        logging.NOTSET: "good",
        logging.DEBUG: "good",
        logging.INFO: "good",
        logging.WARNING: "warning",
        logging.ERROR: "danger",
        logging.CRITICAL: "danger"
    }

    def __init__(self, webhook_url):
        logging.Handler.__init__(self)
        self.webhook_url = webhook_url

    def emit(self, record):
        message = self.format(record)
        payload = {
            "attachments": [
                {
                    "text": message,
                    "color": self.COLOR_DICT[record.levelno]
                }
            ]
        }
        requests.post(self.webhook_url, json=payload)
