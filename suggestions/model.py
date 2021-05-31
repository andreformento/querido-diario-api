class Suggestion:
    """
    Object containing the data to suggest
    """

    def __init__(
        self, title, email_address, name, content,
    ):
        self.title = title
        self.email_address = email_address
        self.name = name
        self.content = content

    def __hash__(self):
        return hash((self.title, self.email_address, self.name, self.content,))

    def __eq__(self, other):
        return (
            self.title == other.title
            and self.email_address == other.email_address
            and self.name == other.name
            and self.content == other.content
        )

    def __repr__(self):
        return f"Suggestion({self.title}, {self.email_address}, {self.name}, {self.content})"
