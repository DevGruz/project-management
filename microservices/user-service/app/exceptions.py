class EmailAlreadyInUseError(Exception):
    def __init__(self, email):
        super().__init__(f"User with email '{email}' already exists.")
        self.email = email
