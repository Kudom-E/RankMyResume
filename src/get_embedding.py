import os
import openai
from dotenv import load_dotenv
import numpy as np

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key="Some_key")


def get_embedding(texts):
    if not texts:
        print("No text to  be embedded")
        return None
    try:
        response = client.embeddings.create(
            input=[str(text) for text in texts],
            model="text-embedding-ada-002"
        )

    except openai.AuthenticationError as e:
        print(f"OpenAI API returned an API Error: {e}")
        print(type(e))
        raise e

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None  # Handle any other unexpected errors

    return [np.array(embeddings.embedding) for embeddings in response.data]
