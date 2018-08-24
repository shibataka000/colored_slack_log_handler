import logging

import mock

from colored_slack_log_handler import SlackHandler


def test_emit():
    url = "https://hooks.slack.com/services/AAA/BBB/CCC"

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    slack_handler = SlackHandler(url)
    slack_handler.setLevel(logging.DEBUG)
    logger.addHandler(slack_handler)

    with mock.patch("requests.post") as m:
        logger.debug("DEBUG")
        m.assert_called_with(
            url,
            json={"attachments": [{"text": "DEBUG", "color": "good"}]}
        )
        logger.info("INFO")
        m.assert_called_with(
            url,
            json={"attachments": [{"text": "INFO", "color": "good"}]}
        )
        logger.warn("WARNING")
        m.assert_called_with(
            url,
            json={"attachments": [{"text": "WARNING", "color": "warning"}]}
        )
        logger.error("ERROR")
        m.assert_called_with(
            url,
            json={"attachments": [{"text": "ERROR", "color": "danger"}]}
        )
        logger.critical("CRITICAL")
        m.assert_called_with(
            url,
            json={"attachments": [{"text": "CRITICAL", "color": "danger"}]}
        )
