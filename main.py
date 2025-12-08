"""
Daily News Reader  
Author: Neha Yadav (Roll No. 139)

Description:
This Python script fetches the latest top news headlines from the GNews API
using the requests library. It uses OOP concepts such as encapsulation with an
`Article` class, handles errors using try-except, works with JSON data from APIs,
and saves the formatted news output into a text file named with the current date.
"""

import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")


# --------------------------------------------------------
# CLASS: Article -> Demonstrates Encapsulation in OOP
# --------------------------------------------------------
class Article:
    def __init__(self, title, url, description):
        # Private attributes for encapsulation
        self.__title = title
        self.__url = url
        self.__description = description

    # Getter Methods
    def get_title(self):
        return self.__title

    def get_url(self):
        return self.__url

    def get_description(self):
        return self.__description

    # Format output text
    def format(self):
        return (
            f"Title: {self.__title}\n"
            f"URL: {self.__url}\n"
            f"Description: {self.__description}\n"
        )


# --------------------------------------------------------
# FUNCTION: Fetch Latest News from API with Error Handling
# --------------------------------------------------------
def fetch_news():
    try:
        url = f"https://gnews.io/api/v4/top-headlines?token={API_KEY}&lang=en"
        response = requests.get(url)
        response.raise_for_status()  # raises an HTTPError if API response is invalid

        return response.json().get("articles", [])

    except requests.exceptions.HTTPError:
        print("❌ Error: Invalid API Key or Unauthorized request.")

    except requests.exceptions.ConnectionError:
        print("❌ Error: Internet connection issue.")

    except Exception as error:
        print(f"❌ Unexpected Error: {error}")

    return []


# --------------------------------------------------------
# FUNCTION: Save formatted news to a text file
# --------------------------------------------------------
def save_to_text(articles):
    file_name = f"news_{datetime.now().strftime('%Y-%m-%d')}.txt"

    with open(file_name, "w", encoding="utf-8") as file:
        for article in articles:
            file.write(article.format())
            file.write("-" * 80 + "\n")

    print(f"✔ News saved successfully in: {file_name}")


# --------------------------------------------------------
# OPTIONAL FEATURE: Save news as JSON
# --------------------------------------------------------
def save_to_json(articles):
    json_data = [
        {
            "title": article.get_title(),
            "url": article.get_url(),
            "description": article.get_description(),
        }
        for article in articles
    ]

    with open("news.json", "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, indent=4)

    print("✔ JSON backup created: news.json")


# --------------------------------------------------------
# MAIN PROGRAM EXECUTION
# --------------------------------------------------------
def main():
    print("\n📢 Fetching today's top news...\n")

    data = fetch_news()

    if not data:
        print("⚠ No news found. Program ended.")
        return

    # Create Article objects
    articles = [
        Article(item["title"], item["url"], item.get("description", "No description available"))
        for item in data
    ]

    # Save output
    save_to_text(articles)
    save_to_json(articles)

    print("\n🎉 Done! Your news file has been generated.\n")


# Run the program
if __name__ == "__main__":
    main()


