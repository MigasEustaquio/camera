from gtts import gTTS
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

def recognized(nome): #Comando com o rosto reconhecido
	frase = "Welcome_" + nome
	sai_som(frase)


def sai_som(audio):
	
	nome = audio.replace("_", " ")
	audio = audio.replace(" ", "_")
	print("\nPi: " + nome)

	if os.path.isfile("audios/{}.mp3".format(audio)):
		os.system('mpg321 audios/{}.mp3 >/dev/null 2>&1'.format(audio))

	else:
		tts = gTTS(nome,lang='en-us')
		#Salva o arquivo de audio
		tts.save("audios/{}.mp3".format(audio))
		#Da play ao audio
		os.system('mpg321 audios/{}.mp3 >/dev/null 2>&1'.format(audio))



def initialize():
	
	sai_som("Welcome to my face recognition software.")
	sai_som("The software consists in 3 parts.")
	sai_som("Face Detection, AI Train and Face Recognition.")
	sai_som("Which one do you wanna run?")


def led(liga):
	if liga == 1:
		GPIO.output(4, 1)
	else:
		GPIO.output(4, 0)
	
	
