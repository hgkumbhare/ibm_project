import json
import os
import wave
import pyglet

def exit_callback(dt):
    pyglet.app.exit()

def playAudio(audioClip):
	sound = pyglet.media.load(audioClip, streaming=False)
	sound.play()

	pyglet.clock.schedule_once(exit_callback , sound.duration)
	pyglet.app.run()