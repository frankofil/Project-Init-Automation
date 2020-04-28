# Project Init Automation

## Before you download
This program uses your __GitHub token__ to communicate via API, so if you don't remember your token
and don't want to generate a new one, you won't be able to run this program.

## How to install and setup?
Firstly clone repository to your computer
```bash
git clone https://github.com/frankofil/Project-Init-Automation.git
```
Go to downloaded folder and install additional packages
```bash
pip install -r requirements.txt
```
Create .env file in downloaded folder and store there your GitHub token as well as path to folder
where you want all of you future projects to be stored. Your .env file must follow exact same layout
as example below
```
TOKEN = "Here_Paste_Your_GitHub_Token"
FILEPATH="/path/to/your/project"
```
Finally add downloaded folder to the PATH to enable usage of 'create' command anywhere in Command Prompt

## How to use this program?
To run the script type in
```bash
create name-of-your-repository
```
This command will create private repository (by default), if you want it to be public use a flag
```bash
create name-of-your-repository -public
```

Project inspired by Kalle Hallden

