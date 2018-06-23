import spotipy
from database import *
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import os 

class Modify: 
	shuffle = False
	play = False
	scope = 'user-modify-playback-state'
	token = None 
	def __init__():
		token = util.prompt_for_user_token('1287119165',scope,cache_path='~/Documents/MediaCenter/server/modifyToken')
	client = spotipy.Spotify(token)
	def pause():
		play = False
		client.pause_playback()
	def play():
		client.start_playback()
		play = True
	def seek(ms):
		client.seek_track(ms)
	def volume(percent):
		client.volume(percent)
	def next():
		client.next_track()
	def prev():
		client.prev_track()
	def shuffle():
		if shuffle:
			shuffle = false
			client.shuffle(false)
		else: 
			shuffle = true
			client.shuffle(true)



