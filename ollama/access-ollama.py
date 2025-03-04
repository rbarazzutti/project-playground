from ollama import Client

client = Client(
  host='https://ollama-01.fever.ch',
  headers={'X-API-Key': 'key1'}
)
response = client.chat(model='deepseek-r1:1.5b', messages=[
  {
    'role': 'user',
    'content': 'how many paws have a cat?',
  },
])

print(response)
