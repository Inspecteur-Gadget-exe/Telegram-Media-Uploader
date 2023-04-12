import os
import requests
import time
import yaml
from PIL import Image

# Check if YAML file exists and load it if it does
if os.path.exists('config.yaml'):
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
else:
    config = {}

# Ask for token if not present in YAML file
if 'TOKEN' not in config:
    config['TOKEN'] = input("Enter the Telegram access token : ")

# Ask for chat ID if not present in YAML file
if 'CHAT_ID' not in config:
    config['CHAT_ID'] = input("Enter the chat ID (channel or group) where you want to send the files : ")

# Write YAML file with new data
with open('config.yaml', 'w') as f:
    yaml.dump(config, f)

# Load token and chat ID from YAML file
TOKEN = config['TOKEN']
CHAT_ID = config['CHAT_ID']

# Ask for full folder path each time the script is run
folder_path = input("\n\tChoose the full PATH of the folder where the media are located.\nShould be something like Z:/Users/Desktop/This_Folder\n\n\t -> : ")

# Get list of files in folder
files = os.listdir(folder_path)

# Loop to send each file
for i, file in enumerate(files):
    file_path = folder_path + '/' + file
    # Prepare data for sending
    data = {'chat_id': CHAT_ID}
    files = {'document': open(file_path, 'rb')}
    # Send request
    response = requests.post('https://api.telegram.org/bot' + TOKEN + '/sendDocument', data=data, files=files)
    # Display response
    print(response.content)
    os.system('cls')
    
    # If 10 images have been sent, stop for 40 seconds
    if i % 19 == 0 and i > 0:
        os.system('cls')
        for j in range(0, 40, 1):
            print("Avoiding Time Out, waiting 40 seconds and the script will continue to send medias.")
            print("\nWaiting : {} seconds / 40".format(j))
            time.sleep(1)
            os.system('cls')
        print("Waiting : Done.")
        time.sleep(1)