import requests

# Replace 'YOUR_API_KEY' with your actual API key and set the correct endpoint URL
api_key = 'YOUR_API_KEY'
endpoint = 'https://api.anthropic.com/v1/messages'  # Example endpoint, verify with documentation

def get_claude_response(prompt):
    headers = {
        'x-api-key': '',  # Strip any extra spaces
        'Content-Type': 'application/json'
    }
    
    data = {
        'model': 'claude-v1',  # Specify the model name
        'prompt': prompt,
        'max_tokens': 150  # Adjust the number of tokens as needed
    }
    
    response = requests.post(endpoint, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['text']
    else:
        print(f"Error: {response.status_code}")
        print(response.json())  # Print full error message for debugging
        return None

# Example usage
prompt = "Tell me a joke."
response = get_claude_response(prompt)
if response:
    print("Claude's response:", response)
