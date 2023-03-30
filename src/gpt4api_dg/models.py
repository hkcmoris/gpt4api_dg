"""
A module to represent the models used in the project.

...

Classes
-------
User
    A class to represent a user.
Role
    A class to represent a role.
Message
    A class to represent a message.
Conversation
    A class to represent a conversation.

Functions
---------
None

Exceptions
----------
None

Notes
-----
None

Examples
--------
None
"""

from enum import Enum
import json

import openai


class User:
    """
    A class to represent a user.

    ...

    Attributes
    ----------
    id : str
        id of a self.messages, has to be a string due to openai's api
    username : str
        username of the self.messages
    """

    id = "None"
    username = "None"

    def __init__(self, id: str, username: str):
        """
        Parameters
        ----------
        id : str
            id of a user, has to be a string due to openai's api
        username : str
            username of the user
        """
        self.id = id
        self.username = username

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"

    def __str__(self):
        return f"{self.username}(id={self.id})"


class Role(Enum):
    """
    A class to represent a role.

    ...

    Attributes
    ----------
    SYSTEM : int
        system role, used for sending system prompts to the api
    USER : int
        user role, used for sending user prompts to the api
    ASSISTANT : int
        assistant role, this role represents the api's response
    """

    SYSTEM = 1
    USER = 2
    ASSISTANT = 3


class Message:
    """
    A class to represent a message.

    ...

    Attributes
    ----------
    role : Role
        message role
    content : str
        message content

    Methods
    -------
    toJSON():
        Returns a json representation of the message
    """

    role = Role.USER
    content = ""

    def __init__(self, role: Role, content: str):
        """
        Parameters
        ----------
        role : Role
            message role
        content : str
            message content
        """
        self.role = role
        self.content = content

    def __repr__(self):
        return f"Message(role={repr(self.role)}, content={self.content})"

    def __str__(self):
        return f"{self.role.name.lower()}: {self.content}"

    def toJSON(self):
        """
        Returns
        -------
        json
            json representation of the message
        """
        return {
            "role": self.role.name.lower(),
            "content": self.content
        }


class Conversation:
    """
    A class to represent a conversation.

    ...

    Attributes
    ----------
    user : User
        user object
    messages : list
        list of messages

    Methods
    -------
    get_response(message: Message):
        Sends a message to the api and returns the response
    """

    user = None
    messages = []

    def __init__(self, user: User, instruction: Message):
        """
        Parameters
        ----------
        user : User
            user object
        instruction : Message
            instruction message

        Notes
        -----
        Typically, a conversation is formatted with a system message first,
        followed by alternating user and assistant messages.
        The system message helps set the behavior of the assistant.
        """
        self.user = user
        self.messages = [instruction.toJSON()]

    def __repr__(self):
        return f"Conversation(user={repr(self.user)})"

    def __str__(self):
        return f"Conversation with {self.user}"

    def get_response(self, message: Message) -> Message:
        """
        Sends a message to the api and returns the response

        ...

        Parameters
        ----------
        message : Message
            message object

        Returns
        -------
        Message
            message object
        """
        self.messages.append(message.toJSON())
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.messages,
            user=self.user.id
        )
        self.messages.append(response.choices[0].message)
        # FIXME: This doesn't works
        if (response.usage["total_tokens"] > 8000):
            self.messages.pop(1)

        return Message(Role.ASSISTANT, response.choices[0].text)
