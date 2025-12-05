🔐 Enigma / XOR Cipher Web Tool

A secure, web-based encryption tool capable of encrypting and decrypting messages using bitwise XOR logic. This project demonstrates full-stack Python development, separating business logic from the presentation layer, and includes containerization for easy deployment.

(Note: Upload your screenshot as 'https://www.google.com/search?q=demo.png' to your repository to see it here)

🚀 Features

XOR Encryption Engine: Custom-built logic class to handle bitwise operations.

Web Interface: Clean, responsive UI built with Flask and Bootstrap 5.

Dual Mode: Can encrypt text into ciphertext and decrypt it back using a numeric key.

Containerized: Fully Dockerized for "write once, run anywhere" capability.

Error Handling: Robust input validation (ensures keys are numeric).

🛠️ Tech Stack

Backend: Python 3, Flask

Frontend: HTML5, Jinja2 Templates, Bootstrap 5 (CSS)

DevOps: Docker, Dockerfile

Architecture: Separation of Concerns (Logic vs. UI)

📂 Project Structure

/Enigma
├── app.py              # The Web Server (Flask Controller)
├── logic.py            # The "Brain" (Pure Python Logic)
├── Dockerfile          # Container configuration
├── requirements.txt    # Dependencies list
└── templates/
    └── index.html      # The Frontend Interface


🔧 Installation & Usage

Option 1: Run with Docker (Recommended)

You don't need to install Python or dependencies if you have Docker.

Build the Image:

docker build -t enigma-web .


Run the Container:

docker run -p 5000:5000 enigma-web


Access the App:
Open your browser and go to http://localhost:5000

Option 2: Run Locally (Python)

Clone the repository:

git clone [https://github.com/Arshimo0/Enigma.git](https://github.com/Arshimo0/Enigma.git)
cd Enigma


Install dependencies:

pip install -r requirements.txt


Start the server:

python3 app.py


🧠 Logic Overview

The core logic resides in logic.py. It uses a symmetric XOR cipher algorithm:

# Simplified Logic
result = ''.join(chr(ord(char) ^ key) for char in text)


This ensures that applying the same key twice returns the original message (A ^ B ^ B = A).

👨‍💻 Author

Arshia (Arshimo0)

Built as a demonstration of Python Web Development and DevOps practices.
