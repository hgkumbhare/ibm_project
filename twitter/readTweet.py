import json
import os
import wave
import pyglet
from watson_developer_cloud import TextToSpeechV1
import recordVoiceModule
import speechToTextModule

def exit_callback(dt):
    pyglet.app.exit()


def textToSpeech(s):
	text_to_speech = TextToSpeechV1(
	  username= "cd6d0299-40d7-4d77-b131-05beb7de172b",
	  password= "0b6iVnKvtuuy",
	    x_watson_learning_opt_out=True)  # Optional flag

	audio_file= open('t1.wav','wb')#('/mnt/c/Users/dell/Desktop/Watson/test1.wav','wb') 
	audio_file.write(text_to_speech.synthesize( s, accept='audio/wav',voice="en-US_AllisonVoice"))

	sound = pyglet.media.load('t1.wav', streaming=False)
	sound.play()

	pyglet.clock.schedule_once(exit_callback , sound.duration)
	pyglet.app.run()

	#ans=input()
	recordVoiceModule.record('response.wav')
	response=speechToTextModule.speechToText('response.wav')

	if "yes" in response:
		return 1
	else:
		return 0	
textToSpeech('It was an honor to welcome President Al Sisi of Egypt to the @WhiteHouse as we renew the historic partnership betwe\xe2\x80\xa6 https://t.co/mc7zVfg6Gz' )