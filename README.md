# Get a fullpage screenshot of a file from Github Public/Private repository

## Clone the repository
```bash
$ git clone https://github.com/shahedex/github_repo_file_download_as_pdf.git
```
## Create and activate a Virtual Environment
```bash
$ cd github_file_fullpage_download
$ python3 -m venv venv
$ source venv/bin/activate
```

## Install the required dependencies
```bash
$ pip install -r requirements.txt
```
## Create a ENV file in the project directory
```bash
$ touch .env
$ nano .env
```
## Add the following to the .env file
```bash
GITHUB_TOKEN="your_github_personal_token"
GITHUB_REPOSITORY="the_repository_name"  # i.e, the-ionicus/tini
GITHUB_REPOSITORY_FILE="the_file_location"  # i.e, app/main/forms.py
```
## Run the program to get the screenshot
```bash
$ python screenshot.py
```

Open **downloaded_data** directory to get the **python raw** file, **generated_pdf** for the **PDF** version.
