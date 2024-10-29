import openai
import os

# Set your OpenAI API key as an environment variable or directly
openai.api_key = os.getenv('OPENAI_API_KEY')  # Recommended
#openai.api_key = "your_openai_api_key_here"  # Or set directly

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
