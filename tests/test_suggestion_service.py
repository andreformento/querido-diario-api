from unittest import TestCase
from unittest.mock import MagicMock

from suggestions import (
    Suggestion,
    MailjetSuggestionService,
)


class MailjetSuggestionServiceTest(TestCase):
    def setUp(self):
        self.mailjet_client = MagicMock()

        self.subject = MailjetSuggestionService(
            mailjet_client=self.mailjet_client,
            # mailjet_client=self.sender_mock,
            suggestion_email_address="from-email@address",
            suggestion_name="from name",
            suggestion_mailjet_custom_id="custom_id",
        )

    def test_send_email(self):
        self.mailjet_client.send.create().configure_mock(status_code=200)

        suggestion_result = self.subject.add_suggestion(
            Suggestion(
                title="Title of suggestion",
                email_address="email@address.com",
                name="My Name",
                content="Content of suggestion",
            )
        )

        self.assertTrue(suggestion_result)

    def test_not_send_email(self):
        self.mailjet_client.send.create().configure_mock(status_code=401)

        suggestion_result = self.subject.add_suggestion(
            Suggestion(
                title="Oops",
                email_address="wrong@address.com",
                name="A girl has no name",
                content="Argument Clinic",
            )
        )

        self.assertFalse(suggestion_result)
