import requests
from decouple import config

hf_token = config('HUGGING_FACE_TOKEN')


embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text}
    )

    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()


if __name__ == "__main__":
    try:
        text = "testing decode!"
        embedding = generate_embedding(text)
        print("Generated Embedding:", embedding)
    except Exception as e:
        print("Error:", e)
