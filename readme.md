# 📰 Daily News Reader

This Python project fetches the latest top news headlines using the **GNews API** and stores the results into both a formatted text file and a JSON backup file.  
It demonstrates **API integration, OOP concepts, JSON parsing, error handling, and file handling** — fully aligned with academic project requirements.

---

## 👩‍💻 Developer Information

| Field | Details |
|-------|---------|
| **Name** | Neha Yadav |
| **Roll No.** | 139 |
| **Course** | B.Tech CSE |
| **Project Type** | Python Mini Project |

---

## 📌 Features

✔ Fetches real-time news headlines  
✔ Uses environment variables to secure API key  
✔ Object-Oriented structure using an `Article` class  
✔ Error handling for internet/API failures  
✔ Saves news in two formats:  
   - `.txt` (human-readable format)  
   - `.json` (machine-readable backup format)  
✔ Clean and modular code with comments and docstrings

---

## 🛠️ Technologies Used

| Component | Purpose |
|----------|---------|
| Python 3 | Programming language |
| requests | API call handling |
| python-dotenv | Loading secret API key securely |
| JSON | Parsing API responses |
| File I/O | Saving news data |

---

## 📁 Project Structure

daily-news-reader/
│
├── main.py # Main application file
├── README.md # Project documentation
├── .env # Stores API Key (NOT uploaded)
├── .gitignore # Prevents sensitive files from uploading
└── news_YYYY-MM-DD.txt (auto generated)



---

## 🚀 How to Run This Project

### 1️⃣ Install Required Libraries

```sh
pip install requests python-dotenv
