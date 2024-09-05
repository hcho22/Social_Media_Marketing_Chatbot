import requests
import json
import os

from langchain_community.tools import tool
from langchain_community.document_loaders import WebBaseLoader


class SearchTools:
    
    @tool('search_internet')
    def search_internet(query: str) -> str:
        """
        Use this tool to search the internet for information. This tools returns 5 results from Google Search Engine. 
        """
        return SearchTools.search(query)
    
    @tool('search_instagram')
    def search_instagram(query: str) -> str:
        """
        Use this tool to serach instagram for information. This tool returns 5 results from Instagram. 
        """
        return SearchTools.search(f"site:instagram.com {query}", limit=5)

    @tool('open page')
    def open_page(url: str) -> str:
        """
        Use this tool to open a webpage and get the content.
        """
        loader = WebBaseLoader(url)
        return loader.load()


    def search(query, limit=5):
        url = "https://google.serper.dev/search"
        payload = json.dumps({
           "q": query,
           "num": limit,
        })
        headers = {
            'X-API-KEY': os.getenv("SERPER_API_KEY"),
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json()['organic']

        string = []
        for result in results:
            string.append(f"{result['title']}\n{result['snippet']}\n{result['link']}\n\n")

        return f"Search results for '{query}':\n\n" + "\n".join(string)
    

if __name__ == "__main__":
    print(SearchTools.open_page("https://www.python.org/"))