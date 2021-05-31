import os


class Configuration:
    def __init__(self):
        self.host = os.environ.get("QUERIDO_DIARIO_ELASTICSEARCH_HOST", "")
        self.index = os.environ.get("QUERIDO_DIARIO_ELASTICSEARCH_INDEX", "")
        self.root_path = os.environ.get("QUERIDO_DIARIO_API_ROOT_PATH", "")
        self.url_prefix = os.environ.get("QUERIDO_DIARIO_URL_PREFIX", "")

        self.suggestion_mailjet_rest_api_key = os.environ.get(
            "SUGGESTION_MAILJET_REST_API_KEY", ""
        )
        self.suggestion_mailjet_rest_api_secret = os.environ.get(
            "SUGGESTION_MAILJET_REST_API_SECRET", ""
        )
        self.suggestion_email_address = os.environ.get("SUGGESTION_EMAIL_ADDRESS", "")
        self.suggestion_name = os.environ.get("SUGGESTION_NAME", "")
        self.suggestion_mailjet_custom_id = os.environ.get(
            "SUGGESTION_MAILJET_CUSTOM_ID", ""
        )


def load_configuration():
    return Configuration()
