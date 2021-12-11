#!/usr/local/bin/python
# coding: utf-8
import tweepy

 
access_token = '1461845283940282370-Z9xKelCs6uZY8oYN8pqiFWMb7dvMz9'
access_token_secret ='eQN42Qgm3HelRJM83UJProgqS3eZy2gxOLHJeEQ5agbLW'
API_key='VsD3tZb92XJDKFeVP0emknbyk'
API_secret_key = 'AePTmd7TjAXdjHTApNzFOMekYHcvEzgHCpkORTUmLFxRH9i5xL'

def OAuth():
    try:
        auth = tweepy.OAuthHandler(API_key,API_secret_key)
        auth.set_access_token(access_token,access_token_secret)

        return auth

    except Exception as e:
        return None

def publicationt_tweet(msg):
    oauth = OAuth()
    api = tweepy.API(oauth)
    api.update_status(msg)

    print('tweet publié')

