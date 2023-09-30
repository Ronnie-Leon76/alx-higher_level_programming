#!/usr/bin/python3
"""
Script takes 2 arguments in order to solve this challenge. 
The first argument will be the repository name.
The second argument will be the owner name.
"""
import requests
import sys
if __name__ == "__main__":
    response = requests.get('https://api.github.com/repos/{}/{}/commits'
                            .format(sys.argv[2], sys.argv[1]))
    commits = response.json()
    for commit in commits[:10]:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
