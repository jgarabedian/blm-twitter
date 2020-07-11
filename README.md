#BLM Twitter

This application was built to analyze how different parts of the country were tweeting about the Black Lives Matter movement.

![Build](https://img.shields.io/github/workflow/status/jgarabedian/blm-twitter/Build?style=for-the-badge)
![Version](https://img.shields.io/github/v/release/jgarabedian/blm-twitter?style=for-the-badge)
![Deployment](https://img.shields.io/github/deployments/jgarabedian/blm-twitter/blm-twitter?label=Heroku&style=for-the-badge)
![License](https://img.shields.io/github/license/jgarabedian/blm-twitter?style=for-the-badge)

##The Strategy
The goal is to continue learning python and use it to gain 
insight into a subject I'm very interested in. By taking a sample of tweets from 
different cities, my hypothesis is that different areas of the country feel different 
about BLM at different times. So once we take the random sample of tweets, run a sentiment 
analysis on the content of the tweet to determine the differences between the cities.

## Getting Started
We take advantage of the virtual env (I use venv myself) and highly recommend PyCharm for this application. 
Install the packages from [requirements.txt](/requirements.txt) and run through [app,py](/app.py).

### Twitter API
We utilize [Tweepy](http://docs.tweepy.org/en/latest/api.html) to pull in the latest tweets that we analyze for this application. Was super helpful/easy and I highly recommend!

### Natural Language Processing
For the Natural Language Processing, we utilize [TextBlob](https://textblob.readthedocs.io/en/dev/) to make things nice and simple. 
Once again, highly recommend this for beginners, but always looking for improvement on this.

### Visualizations
We've been a fan of plotly recently because of the vast documentation and (which is a theme) 
how simple it is to get up and running. 

## Contributions
I welcome anyone who wants to contribute!! I also encourage any suggestions 
or improvements, as I'm young in my journey and looking to learn.

## Support my hosting costs :smirk:
<style>.bmc-button img{height: 34px !important;width: 35px !important;margin-bottom: 1px !important;box-shadow: none !important;border: none !important;vertical-align: middle !important;}.bmc-button{padding: 7px 15px 7px 10px !important;line-height: 35px !important;height:51px !important;text-decoration: none !important;display:inline-flex !important;color:#ffffff !important;background-color:#000000 !important;border-radius: 5px !important;border: 1px solid transparent !important;padding: 7px 15px 7px 10px !important;font-size: 20px !important;letter-spacing:-0.08px !important;box-shadow: 0px 1px 2px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;margin: 0 auto !important;font-family:'Lato', sans-serif !important;-webkit-box-sizing: border-box !important;box-sizing: border-box !important;}.bmc-button:hover, .bmc-button:active, .bmc-button:focus {-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;text-decoration: none !important;box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;opacity: 0.85 !important;color:#ffffff !important;}</style><link href="https://fonts.googleapis.com/css?family=Lato&subset=latin,latin-ext" rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/jgarabedian"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px;font-size:19px !important;">Buy me a coffee</span></a>