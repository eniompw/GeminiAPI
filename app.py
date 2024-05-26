from flask import Flask
import requests
import os

app = Flask(__name__)
# Define the URL for the POST request
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key='
url += os.environ.get("GOOGLE_API_KEY")
# Create a dictionary for headers
headers = {
    "Content-Type": "application/json",  # Adjust content type as needed (e.g., application/xml)
}

@app.route('/')
def home():
    # Prepare the data to be sent (can be JSON, string, etc.)
    data = '{"contents":[{"parts":[{"text":"Explain how AI works"}]}]}'
    # Send the POST request with headers and data
    response = requests.post(url, headers=headers, data=data)
    # Check the response status code
    if response.status_code == 200:
    # Access the response data (if any)
        response_data = response.json() 
        return(response_data)
    else:
        return(response.json())