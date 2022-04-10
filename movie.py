import re
from readline import set_completer
from unicodedata import name
import requests

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token_key = "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"
    
    def GetUser(self,username):
        responce = requests.get(self.api_url+"/users/"+username)
        return responce.json()
    
    def GetRepository(self,username):
        responce = requests.get(self.api_url+"/users/"+username+"/repos")
        return responce.json()
    
    def createRepository(self, repositoryName):
        response =requests.post(self.api_url+"/user/repos?access_token="+self.token_key, json={
            "name":name,
            "description":"This is my first python repo",
            "homepage":"https://Karakter99.com",
            "private": False,
            "has_issues":True, 
            "has_project": True, 
            'has_wiki':True,
        }) 
        return response.json()
 
github = Github()

while True:
    secim = input("1-Find User\n2-Get Repository\n3-Create repository\n4-Exit\nChoice:")
    if secim == "4":
        break
    else:
        if secim=="1":
            username = input("Username: ")
            result=github.GetUser(username=username)
            print(f"Username:{result['name']} , public repos: {result['public_repos']} , followers: {result['followers']}")
        elif secim =="2":
            username = input("Username: ")
            result=github.GetRepository(username=username)
            i=1
            for repo in result:
                print(f"{i}: {repo['name']}")
                i+=1
        elif secim =="3":
            name = input("Enter repo name: ")
            result = github.createRepository(name)
            print(result)
        else:
            print("Wrong Choice")

         
