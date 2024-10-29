import openai
import os

# Set your OpenAI API key as an environment variable or directly
openai.api_key = os.getenv('OPENAI_API_KEY')  # Recommended
#openai.api_key = "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"  # Or set directly

def get_response(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can also use "gpt-4" if you have access
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"
