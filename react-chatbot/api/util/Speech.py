import DataSet
# import speech_recognition as sr
import time, random, sys
from time import ctime


trained = {
			# 'greeting': ['Hello Sir', 'Hi', 'What\'s up'],
			# 'goodbye': ['Thank You Sir', 'See you soon', 'GoodBye', 'Sayonara', 'Tata'],
			# 'love': ['It is same for me', 'But I love you'],
			# 'food': ['Now you are making me hungry',
			# 		 'I need food',
			# 		 'Can you just give me some electric charge because I am hungry'
			# 		],e
			# 'questions': [
			# 			'Wait, do you use a computer daily?',
			# 			'are you tired of having to use a slow computer?',
			# 			'would you be interested in a new computer?'
			# 		],
			# 'prospect': [
			# 			  'I\'m calling because I think this product is for you...',
			# 			  'I\'m seeling Latops. The inicial price is $1000.'
			# 			],
			'intro': [
						'I\'m a Susan Halper from PreTech.',
						' We sell the best tech in the world, mostly laptops.'
					],
			'cta': [
					'So you wanna buy, then ?'
					'i could take the laptop with me and meet you tomorrow at the mall',

					'If you have interest in buying the laptop I will make a discount for you!'
					],

}

trained_rand = ['I don\'t know what you are talking about Sir', 'I believe you are speaking about yourself Sir']

def speak(audioString) :
	print(audioString)
	return audioString
	# engine = pyttsx3.init()
	# engine.say(audioString)
	# engine.runAndWait()

# def recordAudio() :
# 	r = sr.Recognizer()
# 	r.pause_threshold = 1.6
# 	with sr.Microphone() as source :
# 		r.adjust_for_ambient_noise(source)
# 		audio = r.listen(source)

# 	data = ""
# 	try :
# 		data = r.recognize_google(audio)
# 		print(data)
# 	except LookupError:
# 		speak("Could not Understand")
# 	except sr.UnknownValueError :
# 		speak("Could not Understand")

# 	return data

def bot(data) :
	if "how are you" in data:
		speak("I am Fine")

	elif "what" and "time" in data:
		speak("Current time is : " + ctime())

	# elif "that's fine" and "Totally, I can't speak right now" in data :
	# 	speak("I'm a Susan Halper from PreTech. We sell the best tech in the world, mostly laptops.")

	# elif "pause" in data :
	# 	while True :
	# 		data = recordAudio()
	# 		if "start" in data :
	# 			break

	# elif "quit" in data :
	# 	speak("Thank you sir, Hope you have a good time")
	# 	sys.exit()

	elif "close" and "deal" in data:
		speak("That's great, the price is a thousand dollars, I will contact you tomorrow for further information")
		# sys.exit()

	elif ("thank you" or "thanks") in data:
		speak("You are welcome.")

	else :
		cl = DataSet.classify(data)
		if len(cl) > 0 :
			if cl[0][0] == "location":
				pass
				# Location(data)
			else:
				# Choose the response randomly
				t = random.choice(trained[cl[0][0]])
				# print(t)
				speak(t)
		else:
			t = random.choice(trained_rand)
			# print(t)
			speak(t)


def main() :
	time.sleep(2)
	# speak("Hello Sir, What can I do for you?")
	speak('Did I catch you at a bad time?')
	time.sleep(0.2)
	speak("I'm a Susan Halper from PreTech. We sell the best tech in the world, mostly laptops.")
	time.sleep(0.2)
	speak("I have the lastest ultrabook laptop model that is just for you...")
	time.sleep(0.2)
	# data = " "
	# speak("who are you?")
	# bot("who are you?")
	# speak("I want to see it")
	# bot("I want to see it")
	# speak("Ok, let's close the deal then")
	# bot("Ok, let's close the deal then")


# 	data = " "
# 	data = recordAudio()
# 	bot(data)
# 	while True :
# 		data = recordAudio()
# 		bot(data)

# if __name__ == '__main__':
# 	main()