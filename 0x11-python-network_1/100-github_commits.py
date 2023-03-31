#!/usr/bin/python3
"""List 10 commits of a repository by a user using github API"""
import sys
import requests


def main():
    user = sys.argv[2]
    repo = sys.argv[1]
    query = {'per_page': 10}
    url = f'https://api.github.com/repos/{user}/{repo}/commits'
    res = requests.get(url, data=query)
    objs = res.json()

    for obj in objs[:10]:
        commit = obj['commit']
        author = commit['author']
        print(f"{obj.get('sha')}:", author.get('name'))


if __name__ == '__main__':
    main()
