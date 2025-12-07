from dotenv import load_dotenv
import os
import requests
from datetime import datetime


load_dotenv()

class Article:
    def __init__(self, title, url, description):
        self.title = title
        self.url = url
        self.description = description

    def format(self):
        return f"Title: {self.title}\nURL: {self.url}\nDescription: {self.description}\n"

 #Function to fetch news from API
def fetch_news():
    API_KEY = os.getenv("API_KEY")
    url = f"https://gnews.io/api/v4/top-headlines?token={API_KEY}&lang=en"

    response = requests.get(url)

   
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        print("Failed to fetch news. Check your API key or internet connection.")
        return []

# Function to save news to file
def save_news(news_articles):
    file_name = f"news_{datetime.now().strftime('%Y-%m-%d')}.txt"

    with open(file_name, "w", encoding="utf-8") as file:
        for article in news_articles:
            file.write(article.format())
            file.write("-" * 80 + "\n")

    print(f"News saved successfully in file: {file_name}")


def main():
    print("Fetching today's top news...\n")
    data = fetch_news()

    if not data:
        print("No news found.")
        return

   
    articles = [
        Article(item["title"], item["url"], item.get("description", "No description available"))
        for item in data
    ]

    save_news(articles)

    print("\nDone! ✔")



if __name__ == "__main__":
    main()
