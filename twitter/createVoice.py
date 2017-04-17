import json
import os
import wave
import pyglet
from watson_developer_cloud import TextToSpeechV1

def exit_callback(dt):
    pyglet.app.exit()


def textToSpeech(s):
	text_to_speech = TextToSpeechV1(
	  username= "cd6d0299-40d7-4d77-b131-05beb7de172b",
	  password= "0b6iVnKvtuuy",
	    x_watson_learning_opt_out=True)  # Optional flag

	audio_file= open('sayTweet.wav','wb')#('/mnt/c/Users/dell/Desktop/Watson/test1.wav','wb')
	audio_file.write(text_to_speech.synthesize( s, accept='audio/wav',voice="en-US_AllisonVoice"))
	sound = pyglet.media.load('sayTweet.wav', streaming=False)
	sound.play()

	pyglet.clock.schedule_once(exit_callback , sound.duration)
	pyglet.app.run()


textToSpeech('Say your tweet out loud')