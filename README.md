# Chatbot Web Application

A full-stack chatbot web application built with Flask, integrated with OpenAI's ChatGPT model. The app features a responsive UI, runs in a Dockerized environment, and is served using Nginx.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Docker Commands](#docker-commands)
- [License](#license)

## Features

- Interactive chatbot powered by OpenAI's ChatGPT
- Responsive user interface
- Dockerized for easy deployment
- Nginx for serving the application

## Technologies

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: (optional) MongoDB/MySQL (not currently used in this example)
- **Containerization**: Docker
- **Web Server**: Nginx
- **Chatbot Model**: OpenAI's GPT-3.5-turbo or GPT-4

## Setup Instructions

1. **Clone the Repository**

```bash
git clone [https://github.com/yourusername/ChatbotApp.git](https://github.com/Samnoyal/ChatBot.git)
cd ChatBot
```
2. **Create a .env File**
   
In the project root, create a .env file and add your environment variables:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

3. **Build and Run the Application**
   
Ensure you have Docker and Docker Compose installed. Then, run the following command:
```bash
docker-compose up --build
```

## Usage
   - Open your web browser and navigate to http://localhost.
   - Type your message in the input field and press "Send" to interact with the chatbot.
### Environment Variables
   - Make sure to set the following environment variables in your .env file:
   - OPENAI_API_KEY: Your OpenAI API key for using the ChatGPT model.
### Docker Commands
**Build the Docker image:**
```bash
docker-compose build
```
**Run the application:**
```bash
docker-compose up
```
**Stop the application:**
```bash
docker-compose down
```

## Contact
- For any questions or suggestions, please feel free to reach out to [samnoyal33@gmail.com].

## License
- This project is licensed under the MIT License. See the LICENSE file for details.
