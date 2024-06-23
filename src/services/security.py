from fastapi import Request, HTTPException, status

from data_classes import User

"""
A demo implementation of Security
In a real project we would:
1) Check if the token is valid using a key
2) Get the token value
3) Get the use from the token value
"""


class SecurityService(object):
    @classmethod
    def is_authenticated(cls, request: Request):
        token = request.headers.get("authorization")
        if not cls.token_is_valid(token):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Please provide valid bearer token",
            )
        request.state.token = token
        request.state.user = cls.get_user_from_token(token)

    @classmethod
    def get_user_from_token(cls, token: str) -> User:
        return User(id=0, username="RandomAdmin")

    @classmethod
    def token_is_valid(cls, token: str) -> bool:
        return token and token.startswith("Bearer ")
