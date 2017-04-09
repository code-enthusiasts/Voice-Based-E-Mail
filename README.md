# Voice-Based-E-Mail
This is a Python Application which allows its users to send, receive E-Mails through voice.


Complete the steps described in the rest of this page, and in about five minutes you'll have a simple Python command-line application that makes requests to the Gmail API.

Prerequisites:-



   1. Python 2.6 or greater.
   2. The pip package management tool.
   3. Access to the internet and a web browser.
   4. A Google account with Gmail enabled.
   
   Use the link given to create client_secret.json
   https://developers.google.com/gmail/api/quickstart/python
   

Step 1: Turn on the Gmail API

    a)Use this wizard to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to   credentials.
    b)On the Add credentials to your project page, click the Cancel button.
    c)At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the    Save button.
    d)Select the Credentials tab, click the Create credentials button and select OAuth client ID.
    e)Select the application type Other, enter the name "Gmail API Quickstart", and click the Create button.
    f)Click OK to dismiss the resulting dialog.
    g)Click the file_download (Download JSON) button to the right of the client ID.
    h)Move this file to your working directory and rename it client_secret.json.

Step 2: Install the Google Client Library

        Run the following command to install the library using pip:

        pip install --upgrade google-api-python-client

Step 3: Run the following commands on terminal-
        
        1) $ sudo apt-get install python-pip (check the version by running $ pip -V , must be version 9.0.1 or above).
        2) $ sudo python -m pip install html2text
        3) $ sudo pip install git
        4) $ sudo apt-get install libasound-dev
        5) $ git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
        6) $ cd pyaudio
        7) $ sudo python setup.py install
        8) $ sudo apt-get install libportaudio-dev
        9) $ sudo apt-get install python-dev
       10) $ sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
       11) $ sudo pip install SpeechRecognition        


Step 4: Save the files voice_project.py, send.py, text_speech.py, listmessages.py, authenticate.py, getmessage.py, client_secret.json in a folder named voice EMail

Step 5: Open Terminal and use the command 'cd voice EMail' to change the directory.

Step 6: Run 'python voice_project.py' to start the application
