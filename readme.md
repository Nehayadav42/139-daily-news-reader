# 📰 Daily News Reader

A simple Python project that fetches the latest top news headlines using the **GNews API** and saves them into a formatted text file.  
This project demonstrates **REST API usage, JSON handling, OOP concepts, environment variables, and file handling** in Python.

---

## 📌 Features

- Fetches live news using the GNews API
- Stores title, description, and URL
- Saves output into a text file named with the current date
- Uses a class (`Article`) to structure news data
- Stores API key securely using `.env` file

---

## 🛠️ Technologies Used

| Component | Purpose |
|----------|---------|
| Python   | Programming language |
| requests | To make API calls |
| python-dotenv | To load API key securely |
| JSON     | To parse API response |
| File Handling | To save results locally |

---

## 📁 Project Structure

daily-news-reader/
│
├── main.py # Main Python script
├── README.md # Project documentation
├── .env # Stores API key (Not uploaded to GitHub)
└── .gitignore # Prevents .env from being pushed to repo


---

## 🚀 Setup & Installation

### 1️⃣ Install Dependencies

Run:

```sh
pip install requests python-dotenv

