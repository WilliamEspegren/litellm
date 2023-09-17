from litellm import completion
import litellm
import os

user_message = "Write a short poem about the sky"
messages = [{"content": user_message, "role": "user"}]

def test_stream_chunk_builder():
    litellm.api_key = os.environ["OPENAI_API_KEY"]
    response = completion(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True
    )

    for chunk in response:
        print(chunk)
test_stream_chunk_builder()