# Web-Scraped Chatbot
![Image](https://github.com/user-attachments/assets/96921c22-70c6-4e22-bdde-88dd117e3a2c)
## Overview
WebWise is an intelligent web-scraping chatbot that allows users to interact with websites and fetch content in real-time. The chatbot can answer user queries based on the content retrieved from specified URLs, providing a seamless and interactive experience.

## Watch the Demo Video

[![Watch the video](https://github.com/user-attachments/assets/96921c22-70c6-4e22-bdde-88dd117e3a2c)](https://www.youtube.com/watch?v=UIZjb3ZBW4w&t=18s)

## Features
- Fetch website content using a URL input.
- Ask questions about the fetched content.
- User-friendly interface with modern design.
- Loading and error messages for better user feedback.
- Responsive design for mobile devices.

## Technologies Used
- **Flask**: A lightweight WSGI web application framework for Python.
- **Requests**: A simple HTTP library for Python to make requests to web pages.
- **BeautifulSoup**: A library for parsing HTML and XML documents.
- **JavaScript**: For handling user interactions and asynchronous requests.
- **HTML/CSS**: For structuring and styling the web application.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/akhileshpandey0180/chatbot
    cd chatbot
    ``` 

2. Install the required packages:
    ```bash
    pip install Flask
    pip install requests
    pip install beautifulsoup4
    ``` 
3. Set your Hugging Face API token:

4. Run the Flask application:
    ```bash
    python app.py
    ```

5. Open your browser and go to http://127.0.0.1:5000.

## Usage

    - Enter a valid website URL in the "Enter website URL..." input field and click "Fetch Website" to retrieve the content.
    - Type your question in the "Type your message..." input field and click "Send" to get a response based on the fetched content.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
