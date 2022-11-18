from dataclasses import dataclass
from enum import Enum, auto
from slack_sdk.webhook import WebhookClient

from src.config import Config


class MessageType(Enum):
    YAHOO = auto()
    PRTIMES = auto()
    TDNET = auto()
    SG_NEWS = auto()


class SlackClient():
    def __init__(self, message_type: MessageType) -> None:
        self._set_client(message_type)

    def _set_client(self, message_type: MessageType) -> None:
        self.config = Config()
        match message_type:
            case MessageType.YAHOO:
                url = self.config.slack_webhook_url_yahoo
            case MessageType.PRTIMES:
                url = self.config.slack_webhook_url_prtimes
            case MessageType.TDNET:
                url = self.config.slack_webhook_url_tdnet
            case MessageType.SG_NEWS:
                url = self.config.slack_webhook_url_singapore
            case _:
                print("INVALID WBEHOOK URL")

        if url != None:
            self.webhook = WebhookClient(url)
        else:
            pass

    def send_sample_message(self) -> None:
        self.webhook.send(
            text="sample message",
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "You have a new request:\n*<fakeLink.toEmployeeProfile.com|Fred Enriquez - New device request>*"
                    }
                }
            ]
        )
        
    def send_rss_feed(self, feed_name, url, title, summary=None) -> None:
        content = f"<{url}|{title}>\n{summary}" if summary is not None else f"<{url}|{title}>"
        self.webhook.send(
          text=f"{feed_name} RSS, {title}",
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": content
                    }
                }
            ]
        )