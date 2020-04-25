import sys
import os
from dotenv import load_dotenv
from github import Github


load_dotenv()
token = os.getenv("TOKEN")
path = os.getenv("FILEPATH")


def create():
    private = True
    projectName = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "-public":
        private = False

    os.makedirs(path + str(projectName))

    g = Github(token)
    user = g.get_user()
    repository = user.create_repo(projectName, private=private)
    print(f'Succesfully created repository {projectName}')


if __name__ == '__main__':
    create()
