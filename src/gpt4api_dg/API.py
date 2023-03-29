import logging
from datetime import datetime

import openai
from src.gpt4api_dg.models import User, Conversation, Message


users = {}
conversations = {}


def set_api_key(api_key: str):
    """Set OpenAI API key

    Args:
        api_key (str): OpenAI API key
    """
    openai.api_key = api_key


def create_user(id: str, username: str):
    """Create a new user

    Args:
        id (str): User id
        username (str): User username

    Returns:
        User: User object or False if user already exists
    """
    if id in users:
        return False
    user = User(id, username)
    users[user.id] = user
    return user


# @users.get
# def get(id: str):
#     """Get user by id

#     Args:
#         id (str): User id

#     Returns:
#         User: User object or False if user not found
#     """
#     if id in users:
#         return users[id]
#     return False


def create_conversation(user: User, instruction: Message):
    """Create a new conversation

    Args:
        user (User): User object
        instruction (Message): Instruction message

    Returns:
        Conversation: Conversation object or False if conversation already exists
    """
    if user.id in conversations:
        return False
    conversation = Conversation(user, instruction)
    conversations[user.id] = conversation
    return conversation


def get_response(user: User, message: Message):
    """Get response from conversation

    Args:
        user (User): User object
        message (Message): Message object

    Returns:
        Message: Response message or None if conversation not found
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
