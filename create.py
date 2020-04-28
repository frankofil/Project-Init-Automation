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

    g = Github(token)
    user = g.get_user()
    login = user.login
    repository = user.create_repo(projectName, private=private)
    print(f'Succesfully created repository {projectName}')

    directory = path + str(projectName)
    os.mkdir(directory)
    os.chdir(directory)
    print("Succesfully created new directory")

    originalName = projectName
    projectName = projectName.replace('-', ' ')
    projectName = projectName.replace('_', ' ')

    commands = [f'echo # {projectName} >> README.md',
                'echo ## How to install? >> README.md',
                'echo Firstly clone repository to your computer >> README.md',
                'echo ```bash >> README.md',
                f'echo git clone https://github.com/{login}/{originalName}.git >> README.md',
                'echo ``` >> README.md',
                'echo Go to downloaded folder and install additional packages >> README.md',
                'echo ```bash >> README.md'
                'echo pip install -r requirements.txt >> README.md',
                'echo ``` >> README.md',
                'echo.> requirements.txt'
                'echo .vscode >> .gitignore',
                'echo __pycache__ >> .gitignore',
                'mkdir code'
                'git init',
                f'git remote add origin https://github.com/{login}/{originalName}.git',
                'git add .',
                'git commit -m "initial commit"',
                'git push -u origin master',
                'code .']

    for command in commands:
        os.system(command)
    print(f"Process completed. Git repository created in {directory}")


if __name__ == '__main__':
    create()
