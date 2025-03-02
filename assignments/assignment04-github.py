# - read a file from a repository
# - replace all the instances of the text "Andrew" with your name 
# - commit those changes and push the file back to the repository (needs authorisation)


from github import Github           # https://pypi.org/project/PyGithub/
from config import config as cfg    # Load config.py, it has the key inside  
import requests
import regex as re


# Get the key from the config file
apikey = cfg["githubkey"]

# Use the key
g = Github(apikey)

# Get the clone URL
repo = g.get_repo("holmstead/WSAA_coursework")
#print(repo.clone_url)

# Get the download URL
file_info = repo.get_contents("my_work/test.txt")
url_of_file = file_info.download_url
#print (url_of_file)

# Output contents of file
response = requests.get(url_of_file)
content_of_file = response.text
#print(content_of_file)

# Create new content to upload to github (replace name)
old_word = 'Andrew'
new_word = 'Matt'

# Use regex to replace the word case-insensitively
updated_content = re.sub(rf'\b{re.escape(old_word)}\b', new_word, content_of_file, flags=re.IGNORECASE)

# Print the updated contents
#print(updated_content)

# Push to github the new content
github_response = repo.update_file(file_info.path, "updated by prog, replaced name", updated_content, file_info.sha)
print(github_response)