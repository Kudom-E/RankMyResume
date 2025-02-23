import os
import openai
from dotenv import load_dotenv
import numpy as np

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)


def get_embedding(texts):
    response = client.embeddings.create(
        input=[str(text) for text in texts],
        model="text-embedding-ada-002"
    )
    return [np.array(embeddings.embedding) for embeddings in response.data]
