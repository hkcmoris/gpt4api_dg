import os
import dotenv
from src.gpt4api_dg import API
from src.gpt4api_dg.models import User, Conversation, Message, Role

dotenv.load_dotenv()

# Now you can access the environment variables
API.set_api_key(os.getenv("OPENAI_API_KEY"))
user = API.create_user("1", "test")  # Create a new user
instruction = API.Message(
    role=Role.SYSTEM,
    content='You are a helpful assistant for a music streaming service. You are listening to a user\'s music and they ask you a question. You can respond to them with a message.'
)
API.create_conversation(user, instruction)  # Create a new conversation

content = input(f"{user.username}: ")  # Get user input
response = API.get_response(user, Message(
    role=Role.USER, content=content))  # Get response

print(f"bot: {response.content}")  # Print response

content = input(f"{user.username}: ")  # Get user input
response = API.get_response(user, Message(
    role=Role.USER, content=content))  # Get response

print(f"bot: {response.content}")  # Print response

content = input(f"{user.username}: ")  # Get user input
response = API.get_response(user, Message(
    role=Role.USER, content=content))  # Get response

print(f"bot: {response.content}")  # Print response

# example of a conversation on a discord server with a user who is listening to Spotify
response = API.get_response(user, Message(
    role=Role.SYSTEM,
    content=f"User `{user.username}` stopped listening to Spotify. Ask them how they liked it."
))  # Get response

print(f"bot: {response.content}")  # Print response
