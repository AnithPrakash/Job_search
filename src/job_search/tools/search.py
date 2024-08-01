import requests
import json
import os
from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
load_dotenv()


class searchtool:

    @tool("search_internet")
    def search_internet(query:str):
        """search the job requirment skill needed for the job on internet.This tool return 5 result from
           google search engine"""
        return searchtool.search(query)
    
    @tool("search_lindedin")
    def search_linkedin(query:str):
        """Search for the job listing in linkedin """
        return searchtool.search(f" site:linkedin.com {query}",limit=1)

    @tool("project")
    def project(query:str):
        """Search for futuristic project in internet for the job type"""
        return searchtool.search(query,limit=1)

    @tool("open page")
    def open_page(url:str)-> str:
        """
        use the tool to open a webpage and get the content """

        loader=WebBaseLoader(url)
        return loader.load()

    def search(query,limit=1):

        url = "https://google.serper.dev/search"

        payload = json.dumps({
        "q": query,
        "num":limit,
        })
        headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        result=response.json().get('organic',[])
        string=[]
        for item in result:
            string.append(f"{item['title']}\n{item['snippet']}\n{item['link']}\n\n")

        return f"searcch results for '{query}':\n\n" + "\n".join(string)



