# - read a file from a repository, 
# - replace all the instances of the text "Andrew" with your name. 
# - commit those changes and push the file back to the repository (needs authorisation)

from github import Github
from config import config as cfg
import requests


# Get the key from the config file
apikey = cfg["githubkey"]

# Use the key
g = Github(apikey)

# Get the clone URL
repo = g.get_repo("holmstead/PFDA")
print(repo.clone_url)

# Get the download URL
fileInfo = repo.get_contents("requirements.txt")
urlOfFile = fileInfo.download_url
print (urlOfFile)

# Output contents of file
response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)