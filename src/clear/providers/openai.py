from openai import OpenAI
from clear.config import read_config
from clear.tools.schema import tooling

def chat(messages):
    config_data = read_config()
    client = OpenAI(
        api_key = config_data['apiKey'],
        base_url = config_data['baseURL']
        )
    completion = client.chat.completions.create(
        model = config_data['model'],
        messages = messages,
        tools = tooling()
    )

    return completion.choices[0].message