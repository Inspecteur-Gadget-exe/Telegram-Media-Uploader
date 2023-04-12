# Telegram-Uploader
Upload Images, Videos, Documents in any Telegram Channel or Group

<h2>Clone the repo: </h2>

```bash
git clone https://github.com/Inspecteur-Gadget-exe/Telegram-Uploader.git
```
```bash
cd Telegram-Uploader
```

<hr>

<h2>Concerning the CHAT_ID : </h2>

This is the method I use :  
  
  For a **group** :  

  - Open <code>https://web.telegram.org/k/</code>  
  - Go to the channel and you will see the URL as something like
       
  - <code>https://web.telegram.org/k/#-917282407</code> here <code>917282407</code> is the chat id.</code>
       
  For a **channel** :  
  
  - Open https://web.telegram.org/k/  
  - Go to the channel and you will see the URL as something like
 
  - <code>https://web.telegram.org/k/#@channeltest</code> here <code>@channeltest</code> is the chat id.</code>
   
<hr>

<h2>Concerning the TOKEN : </h2>

Go talk to <code>https://t.me/BotFather</code> on Telegram to create a bot.  

Follow these 3 steps :  

  1) <code>/start</code>
  2) <code>/newbot</code>
  - Choose his name
  - Choose his username
  3) Then, <code>https://t.me/BotFather</code> will send you a mesage with the link to your bot <code>t.me/MyBot</code> for example, and the token right below  

<hr>

<h2>Config.yaml : </h2>

Go to config.yaml and add the chat_id and token.

<hr>

<h2> Before running the script </h2>

```bash
pip install -r requirements.txt
```

To install 3 modules : 
  - requests
  - pyyaml
  - pillow

<hr>

<h2> Run the script </h2>

```bash
python main.py
```

You must specify the full PATH of the folder where the media are located.  

WARNING : Don't use backslash for the PATH, you must have something like Z:/Users/Desktop/This_Folder

I'm not going to explain the script because it's already commented but every 20 files uploaded, script stop for 40 secondes to avoid Time Out. Time Out stop the script... that's why we all want to avoid it.
