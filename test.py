import spotipy
import sys
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

if len(sys.argv) > 5:
	username = sys.argv[1]
	client_id = sys.argv[2]
	client_secret = sys.argv[3]
	redirect_uri = sys.argv[4]
	user = sys.argv[5]
else:
	print "wrong usage"
	sys.exit()
 
scope = 'user-modify-playback-state'
#client_credentials_manager = SpotifyClientCredentials()
token = util.prompt_for_user_token(username,scope)
token2 = util.prompt_for_user_token(username,"user-read-playback-state")
if token:
	deviceMap = {}
	sp = spotipy.Spotify(auth=token) 
	sp2 = spotipy.Spotify(auth=token2)
	devices = sp2.devices()
	for device in devices['devices']:
		print "available devices: "
		deviceMap[device["name"]] = device['id']
		print device["name"] + " "+device['id']
	
	deviceID = deviceMap.get(raw_input())
	while(deviceID == None):
		print "not a device listed"
		deviceID = deviceMap[raw_input()]
	
    	results = sp.start_playback(deviceID,"spotify:user:1287119165:playlist:357HDPhOK7dIR3T9d1ffQu",None,None)

	readIn = None
	print("exit, next, prev, pause, play, get playlist, play song  ")
	while(readIn != "exit"):
		readIn = raw_input()
		print(readIn)
		if readIn == "next":
			sp.next_track()
		if readIn == "prev":
			sp.previous_track()
		if readIn ==  "pause":
			sp.pause_playback()
		if readIn == "play":
			sp.start_playback()
  #  for item in results['items']:
  #     track = item['track']
  #    print track['name'] + ' - ' + track['artists'][0]['name']
else:
    print "Can't get token for", username 
