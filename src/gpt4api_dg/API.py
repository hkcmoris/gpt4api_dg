"""
This module contains the API for the gpt4api_dg package.

...

Functions
---------
set_api_key(api_key: str)
    Set the api key for openai
create_user(id: str, username: str)
    Create a new user
create_conversation(user: User, instruction: Message)
    Create a new conversation
get_response(user: User, message: Message)
    Get response from the api
"""
import logging
from datetime import datetime
from typing import Literal

import openai
from gpt4api_dg.models import User, Conversation, Message


users = {}
conversations = {}


def set_api_key(api_key: str):
    """
    Set the api key for openai

    ...

    Parameters
    ----------
    api_key : str
        The api key for openai
    """
    openai.api_key = api_key


def create_user(id: str, username: str) -> User | Literal[False]:
    """
    Create a new user

    ...

    Parameters
    ----------
    id : str
        id of a user, has to be a string due to openai's api
    username : str
        username of the user

    Returns
    -------
    User
        User object or False if user already exists
    """
    if id in users:
        return False
    user = User(id, username)
    users[user.id] = user
    return user


def create_conversation(user: User, instruction: Message) -> Conversation | Literal[False]:
    """
    Create a new conversation

    ...

    Parameters
    ----------
    user : User
        User object
    instruction : Message
        Message object containing the instructions for bot behavior

    Returns
    -------
    Conversation
        Conversation object or False if conversation already exists

    Notes
    -----
    Typically, a conversation is formatted with a system message first,
    followed by alternating user and assistant messages.
    The system message helps set the behavior of the assistant.
    """
    if user.id in conversations:
        return False
    conversation = Conversation(user, instruction)
    conversations[user.id] = conversation
    return conversation


def get_response(user: User, message: Message) -> Message | None:
    """
    Get response from the api

    ...

    Parameters
    ----------
    user : User
        User object
    message : Message
        Message object

    Returns
    -------
    Message
        Message object or None if conversation not found
    """
    if user.id in conversations:
        conversation = conversations[user.id]
        return conversation.get_response(message)
    return None


# def log_conversation(user: User):
#     """Log conversation

#     Args:
#         user (User): User object

#     Returns:
#         bool: True if conversation logged or False if conversation not found
#     """
#     if user.id in conversations:
#         conversation = conversations[user.id]

#         log_name = f"{user.id}_conversation_{}.log"
#         return True
#     return False


if __name__ == "__main__":
    msg = "This is a python module, not a standalone program. It is intended to be imported by other python programs."
    print(msg)
    logging.info(msg)
