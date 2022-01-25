import re
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if not re.match("^[a-z]{3,}$", username):
            raise UserInputError("Malformatted username, min. 3 characters, a-z")

        if not re.match("^(?=.*[a-z])(?=.*[^a-z]).{8,}$", password):
            raise UserInputError("Malformatted password (min. 8 characters, at least 1 other character than a-z)")

        if password != password_confirmation:
            raise UserInputError("Passwords do not match")


user_service = UserService()
