import DataSet
import speech_recognition as sr
import keyboard, requests, json, geopy, time, sys, webbrowser, pyttsx3, random, subprocess, sys
from time import ctime
from geopy.geocoders import Nominatim

# moz_path = '/usr/bin/firefox %s'
# chrome_path = '/usr/bin/google-chrome-stable --no-sandbox %s'


# chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application" --no-sandbox %s'
# moz_path = 'C:\Program Files\Mozilla Firefox %s'

trained = {
			'greeting': ['Hello Sir', 'Hi', 'What\'s up'],
			'goodbye': ['Thank You Sir', 'See you soon', 'GoodBye', 'Sayonara', 'Tata'],
			'love': ['It is same for me', 'But I love you'],
			'food': ['Now you are making me hungry',
					 'I need food',
					 'Can you just give me some electric charge because I am hungry'
					]
		  }

trained_rand = ['I don\'t know what you are talking about Sir', 'I believe you are speaking about yourself Sir']

def speak(audioString) :
	print(audioString)
	engine = pyttsx3.init()
	engine.say(audioString)
	engine.runAndWait()

def recordAudio() :
	r = sr.Recognizer()
	r.pause_threshold = 1.6
	with sr.Microphone() as source :
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	data = ""
	try :
		data = r.recognize_google(audio)
		print(data)
	except LookupError:
		speak("Could not Understand")
	except sr.UnknownValueError :
		speak("Could not Understand")

	return data

# def openApp(AppName) :
# 	AppName = '-'.join(AppName).lower()
# 	path = subprocess.getoutput('which ' + AppName)
# 	subprocess.Popen(path)
#
# def getCoordinates(loc) :
# 	geolocator = Nominatim()
# 	location = geolocator.geocode(loc)
# 	id = []
# 	id.append(location.latitude)
# 	id.append(location.longitude)
# 	return id
#
# def getLoc():
# 	send_url = 'http://freegeoip.net/json'
# 	r = requests.get(send_url)
# 	j = json.loads(r.text)
# 	id = []
# 	id.append(j['latitude'])
# 	id.append(j['longitude'])
# 	return id
#
# def Location(data) :
# 	data = data.split(" ")
# 	loc = data[2:]
#
# 	if "where is" in data :
# 		speak("Hold on Sir, I will show you where " + loc + " is")
# 		webbrowser.get(moz_path).open('https://www.google.com/maps/place/' + loc + '/&amps')
#
# 	elif "coordinates" in data :
# 		if "current location" in loc :
# 			speak("Coordinates for " + " ".join(loc) + " are on terminal")
# 			print(getLoc())
# 		else :
# 			speak("Coordinates for " + " ".join(loc) + " are on terminal")
# 			print(getCoordinates(loc))

def bot(data) :
	if "how are you" in data :
		speak("I am Fine")

	elif "what" and "time" in data :
		speak("Current time is : " + ctime())

	elif "pause" in data :
		while True :
			data = recordAudio()
			if "start" in data :
				break

	elif "quit" in data :
		speak("Thank you sir, Hope you have a good time")
		sys.exit()

	elif ("thank you" or "thanks") in data :
		speak("You are welcome.")

	# elif "Google Search" in data :
	# 	try:
	# 		data = data.split(" ")
	# 		print(f'data: {data}')
	# 		loc = "+".join(data[2:])
	# 		print(f'loc: {loc}')
	# 		speak("Let me just google it for you sir")
	# 		webbrowser.get(moz_path).open('https://www.google.com/#safe=strict&q=' + loc)
	# 		# webbrowser.get().open('https://www.google.com/#safe=strict&q=' + loc)
	# 	except AttributeError as e:
	# 		print(e)
	# 		speak('I didn\'t get what I should search for' )

	elif "open application" in data :
		data = data.split(" ")
		speak("Opening Application " + ' '.join(data[2:]))
		openApp(data[2:])

	elif "press" in data :
		data = data.split(" ")
		key = data[1]
		speak("Pressing " + key)
		keyboard.press_and_release(key)

	# elif "play song" in data :
	# 	data = data.split(" ")
	# 	song = "+".join(data[2:])
	# 	webbrowser.get(moz_path).open('https://www.youtube.com/results?search_query=' + song)
	# 	time.sleep(7)
	# 	keyboard.press_and_release('enter')
	# 	time.sleep(5)
	# 	print("XYZ")
	# 	for i in range(0,8) :
	# 		keyboard.press_and_release('tab')
	# 		print(i)
	# 	keyboard.press_and_release('enter')

	else :
		cl = DataSet.classify(data)
		if len(cl) > 0 :
			if cl[0][0] == "location" :
				Location(data)
			else :
				t = random.choice(trained[cl[0][0]])
				# print(t)
				speak(t)
		else :
			t = random.choice(trained_rand)
			# print(t)
			speak(t)


def main() :
	time.sleep(2)
	speak("Hello Sir, What can I do for you?")
	data = " "
	while True :
		data = recordAudio()
		bot(data)
	# bot("hello")
	# bot("what's up")
	# bot("i love you")
	# bot("have a good day")
	# bot("play song NF - The Search")

if __name__ == '__main__':
	main()