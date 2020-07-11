# BLM Twitter

This application was built to analyze how different parts of the country were tweeting about the Black Lives Matter movement.

![Build](https://img.shields.io/github/workflow/status/jgarabedian/blm-twitter/Build?style=for-the-badge)
![Version](https://img.shields.io/github/v/release/jgarabedian/blm-twitter?style=for-the-badge)
![Deployment](https://img.shields.io/github/deployments/jgarabedian/blm-twitter/blm-twitter?label=Heroku&style=for-the-badge)
![License](https://img.shields.io/github/license/jgarabedian/blm-twitter?style=for-the-badge)

## The Strategy
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

<a href="https://www.buymeacoffee.com/jgarabedian" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/lato-black.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>
