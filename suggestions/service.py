import abc
import logging

from mailjet_rest import Client

from .model import Suggestion


class SuggestionService(abc.ABC):
    """
    Service to send a suggestion
    """

    @abc.abstractmethod
    def add_suggestion(self, suggestion: Suggestion):
        """
        Method to send a suggestion
        """


class MailjetSuggestionService(SuggestionService):
    def __init__(
        self,
        mailjet_client: Client,
        suggestion_email_address: str,
        suggestion_name: str,
        suggestion_mailjet_custom_id: str,
    ):
        self.mailjet_client = mailjet_client
        self.suggestion_email_address = suggestion_email_address
        self.suggestion_name = suggestion_name
        self.suggestion_mailjet_custom_id = suggestion_mailjet_custom_id
        self.logger = logging.getLogger(__name__)

    def add_suggestion(self, suggestion: Suggestion):
        data = {
            "Messages": [
                {
                    "From": {
                        "Email": suggestion.email_address,
                        "Name": suggestion.name,
                    },
                    "To": [
                        {
                            "Email": self.suggestion_email_address,
                            "Name": self.suggestion_name,
                        }
                    ],
                    "Subject": suggestion.title,
                    "TextPart": suggestion.content,
                    "CustomID": self.suggestion_mailjet_custom_id,
                }
            ]
        }
        result = self.mailjet_client.send.create(data=data)

        self.logger.debug(f"Suggestion body response {result.json()}")
        if 200 <= result.status_code <= 299:
            self.logger.info(f"Suggestion created for {suggestion.email_address}")
            return True
        else:
            self.logger.error(
                f"Error on send email {suggestion.email_address}. Status code response: {result.status_code}"
            )
            return False


def create_suggestion_service(
    suggestion_mailjet_rest_api_key: str,
    suggestion_mailjet_rest_api_secret: str,
    suggestion_email_address: str,
    suggestion_name: str,
    suggestion_mailjet_custom_id: str,
) -> SuggestionService:
    return MailjetSuggestionService(
        mailjet_client=Client(
            auth=(suggestion_mailjet_rest_api_key, suggestion_mailjet_rest_api_secret),
            version="v3.1",
        ),
        suggestion_email_address=suggestion_email_address,
        suggestion_name=suggestion_name,
        suggestion_mailjet_custom_id=suggestion_mailjet_custom_id,
    )
