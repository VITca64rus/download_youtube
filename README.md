<h1 align="center">Download video from YouTube</h1>
<h2>Description</h2>
  <p>
<img align="left" src="https://raw.githubusercontent.com/VITca64rus/download_youtube/master/description.gif">
You can download videos from YouTube using my telegram bot. You should only send a link to the video. </br> This is my second telegram bot. I learned how to create them on the <a href="https://www.coursera.org/learn/python-for-web/">Coursera course</a>
</p>

<p></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></p>

<h2>How to use</h2>
<p>
1. command /start - displays a welcome message </br>
2. command /help - displays information on all available commands</br>
3. If you send a text message, the bot will think that you have sent a link and will try to download the video, but will not be able to do so. What it will tell you in a reply message</br>
4. The same will happen with links not on YouTube videos</br>
5. If you send a link to a YouTube video, the bot will offer you options for downloading formats.
Once you select the format the bot will start downloading the video and then sending it to you
</p>

<h2>About the project</h2>
<p>
  - The bot is written in Python 3.9.4</br>
  - To interact with the Telegram API, I use the pyTelegramBotAPI library</br>
  - To download videos from YouTube, I use the pytube library</br>
</p>

<h2>Project setup</h2>
<code>git clone https://github.com/VITca64rus/download_youtube</code></br>
<code>pip install -r requirements.txt</code></br>
<code>python telegram_bot.py</code></br>

