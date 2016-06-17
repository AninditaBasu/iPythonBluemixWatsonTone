# iPythonBluemixWatsonTone

A starter app to analyse the tone of tweets through Watson services on Bluemix. 

## Installation

1.    Deploy this app to Bluemix by clicking here: [![Deploy to Bluemix](https://bluemix.net/deploy/button.png)](https://bluemix.net/deploy?repository=https://github.com/AninditaBasu/iPythonBluemixWatsonTone)
2.    Follow the onscreen directions. After the app is deployed and running, click the app's URL. You are taken to the iPython Jupyter login page. 
3.    Click __Log in__ without typing any password. The iPython framework opens. Open a new notebook, import the `hello_world.py` script, and run it. You should be asked your name and shown some lines of text.

## Files and folders

-    `static`
    - `hello.txt`: A file that is used by the HelloWorld script (further down this list).
    -  `tweets_sample.json`: A file that contains some tweets to work with.
-    `License.txt`: Contains placeholder text that you replace with the license that you distribute your app with.
-    `Procfile`: Contains the command that tells Bluemix which file to launch when the app is opened. In this file, the iPython framework is specified as the app launchpoint.
-    `README.md`: The file that you are reading at this moment.
-    `manifest.yml`: A file that tells Bluemix a bit more about the app.
-    `requirements.txt`: A file for listing the Python libraries that you need for your app code, with each library on a new line.
-    `hello_world.py`: A simple HelloWorld script to test the deployment of this app with.
-    `watson_get_tweets.py`: A file with the code that was used in Part 1 of the tutorial series: Ask Watson what Twitter is telling you.
