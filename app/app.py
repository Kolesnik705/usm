from fastapi import FastAPI
from app.handlers import comments, followers, posts, strip, token, users

import logging
import logging.config

from app.settings import LOGGING
logging.config.dictConfig(LOGGING)


def create_app():
    """
    Creates fastAPI application"""
    app = FastAPI()

    app.include_router(token.router)
    app.include_router(users.router)
    app.include_router(followers.router)
    app.include_router(posts.router)
    app.include_router(comments.router)
    app.include_router(strip.router)

    return app
