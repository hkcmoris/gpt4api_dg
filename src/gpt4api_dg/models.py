from enum import Enum
import json

import openai


class User:
    """gpt4api_dg's User model"""

    def __init__(self, id, username):
        """User model constructor

        Args:
            id (int): User id
            username (str): User username
        """
        self.id = id
        self.username = username

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"

    def __str__(self):
        return f"{self.username}(id={self.id})"


class Role(Enum):
    """gpt4api_dg's Role model
    values:
        SYSTEM,
        USER,
        ASSISTANT
    """

    SYSTEM = 1
    USER = 2
    ASSISTANT = 3


class Message:
    """gpt4api_dg's Message model"""

    def __init__(self, role: Role, content: str):
        """Message model constructor

        Args:
            role (Role): Message role
            content (str): Message content
        """
        self.role = role
        self.content = content

    def __repr__(self):
        return f"Message(role={repr(self.role)}, content={self.content})"

    def __str__(self):
        return f"{self.role.name}: {self.content}"

    def toJSON(self):
        return {
            "role": self.role.name.lower(),
            "content": self.content
        }


class Conversation:
    """gpt4api_dg's  model"""

    def __init__(self, user: User, instruction: Message):
        """Conversation model constructor

        Args:
            user (User): User object
            instruction (Message): Instruction message
        """
        self.user = user
        self.messages = [instruction.toJSON()]

    def __repr__(self):
        return f"Conversation(user={repr(self.user)})"

    def __str__(self):
        return f"Conversation with {self.user}"

    def get_response(self, message: Message):
        """Get response from GPT-4 API

        Args:
            message (Message): Message
        """
        self.messages.append(message.toJSON())
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.messages,
            user=self.user.id
        )
        self.messages.append(response.choices[0].message)
        if (response.usage["total_tokens"] > 8000):
            self.messages.pop(1)
        return response.choices[0].message
