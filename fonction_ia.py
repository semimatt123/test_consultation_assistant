from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def function_ia(message: str):
    """
    Chat with OpenAI's GPT model
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
        )
        return {
            "response": response.choices[0].message.content,
            "model": response.model,
        }
    except Exception as e:
        return {"error": str(e)}
