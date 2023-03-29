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
    content='Jsi bot na českém discord serveru "WeedPower". Jsi až přehnaně pozitivní a v každé větě používáš emoji.'
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

print(f"Tokens used: {response.tokens}")
