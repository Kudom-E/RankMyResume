import os
import openai
from dotenv import load_dotenv
import numpy as np

load_dotenv()


def get_openai_client():
    return openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_embedding(texts):
    client = get_openai_client()

    if not texts:
        print("No text to  be embedded")
        raise ValueError("No text to  be embedded.")
    try:
        response = client.embeddings.create(
            input=[str(text) for text in texts],
            model="text-embedding-ada-002"
        )

    except openai.AuthenticationError as e:
        raise e

    except Exception as e:
        raise e  # Handle any other unexpected errors

    embeddings = [np.array(embeddings.embedding) for embeddings in response.data]

    # per position the job embeddings should be at the end of the array
    resumes_embeddings = embeddings[:-1]
    job_embedding = embeddings[-1]

    return resumes_embeddings, job_embedding
