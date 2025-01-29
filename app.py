from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Replace with your Hugging Face API details
HF_API_URL = "https://api-inference.huggingface.co/models/gpt2"
HF_API_TOKEN = 'Hugging Face API'

# Global variable to store website content
website_content = ""

def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError:
        return "Error: Unable to connect to the URL. Please check your internet connection."
    except requests.exceptions.Timeout:
        return "Error: The request timed out. Please try again later."
    except requests.exceptions.RequestException as e:
        return f"Error fetching website content: {e}"

def query_hugging_face_api(text_input):
    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}"
    }
    data = {
        "inputs": text_input
    }
    response = requests.post(HF_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return f"Error: {response.status_code}, {response.text}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fetch_content', methods=['POST'])
def fetch_content():
    global website_content
    url = request.form['url']
    website_content = fetch_website_content(url)
    if "Error" in website_content:
        return jsonify({'error': website_content}), 400  # Return error with 400 status code
    return jsonify({'message': 'Website content fetched. You can now ask questions about it.'})


@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    query = f"Given the following content: {website_content[:1000]}, answer this question: {user_input}"
    response = query_hugging_face_api(query)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
