import nltk, os, json, datetime, numpy as np, time
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

training_data = []
training_data.append({"class":"greeting", "sentence":"how are you?"})
training_data.append({"class":"greeting", "sentence":"how is your day?"})
training_data.append({"class":"greeting", "sentence":"good day"})
training_data.append({"class":"greeting", "sentence":"how is it going today?"})
training_data.append({"class":"greeting", "sentence":"hello hi"})
training_data.append({"class":"greeting", "sentence":"hey there"})
training_data.append({"class":"greeting", "sentence":"what's up?"})

training_data.append({"class":"goodbye", "sentence":"have a nice day"})
training_data.append({"class":"goodbye", "sentence":"see you later"})
training_data.append({"class":"goodbye", "sentence":"have a nice day"})
training_data.append({"class":"goodbye", "sentence":"talk to you soon"})

training_data.append({"class":"location", "sentence":"where is"})
training_data.append({"class":"location", "sentence":"coordinates for"})
training_data.append({"class":"location", "sentence":"location of"})
training_data.append({"class":"location", "sentence":"how far is"})

training_data.append({"class":"food", "sentence":"make me a sandwich"})
training_data.append({"class":"food", "sentence":"can you make a sandwich?"})
training_data.append({"class":"food", "sentence":"having a sandwich today?"})
training_data.append({"class":"food", "sentence":"what's for lunch?"})
training_data.append({"class":"food", "sentence":"let's have dinner"})
training_data.append({"class":"food", "sentence":"what did you have for breakfast?"})
training_data.append({"class":"food", "sentence":"i am hungry"})

training_data.append({"class":"love", "sentence":"do you love someone?"})
training_data.append({"class":"love", "sentence":"i love you"})
training_data.append({"class":"love", "sentence":"i am in love"})
training_data.append({"class":"love", "sentence":"i love a girl"})
training_data.append({"class":"love", "sentence":"i love a boy"})

words = []
classes = []
documents = []
ignore_words = ['?']
for pattern in training_data :
	w = nltk.word_tokenize(pattern['sentence'])
	words.extend(w)
	documents.append((w, pattern['class']))
	if pattern['class'] not in classes :
		classes.append(pattern['class'])

words = [stemmer.stem(w.lower()) for w in words]

words = list(set(words))
classes = list(set(classes))

training = []
output = []
output_empty = [0] * len(classes)

for doc in documents :
	bag = []
	pattern_words = doc[0]
	pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
	for w in words :
		bag.append(1) if w in pattern_words else bag.append(0)

	training.append(bag)
	output_row = list(output_empty)
	output_row[classes.index(doc[1])] = 1
	output.append(output_row)

i = 0 
w = documents[i][0]

def sigmoid(x) :
	output = 1/(1 + np.exp(-x))
	return output

def sigmoid_output_to_derivative(x) :
	return x*(1-x)

def clean_up_sentence(s) :
	s_words = nltk.word_tokenize(s)
	s_words = [stemmer.stem(w.lower()) for w in s_words]
	return s_words

def bow(s, w, show_details = False) :
	s_words = clean_up_sentence(s)
	bag = [0] * len(w)
	for i in s_words :
		for j, k in enumerate(words) :
			if k == i :
				bag[j] = 1
				if show_details :
					print("Found in : " + k)
	return np.array(bag)

def think(sentence, show_details = False) :
	x = bow(sentence.lower(), words, show_details)
	if show_details :
		print("Sentence : " + sentence + "\nBow : " + str(x))
	l0 = x
	l1 = sigmoid(np.dot(l0, synapse_0))
	l2 = sigmoid(np.dot(l1, synapse_1))
	return l2

def train(X, y, hidden_neurons=10, alpha=1, epochs=50000, dropout=False, dropout_percent=0.5) :
	np.random.seed(1)
	last_mean_error = 1
	np.random.seed(1)

	last_mean_error = 1
	synapse_0 = 2*np.random.random((len(X[0]), hidden_neurons)) - 1
	synapse_1 = 2*np.random.random((hidden_neurons, len(classes))) - 1

	prev_synapse_0_weight_update = np.zeros_like(synapse_0)
	prev_synapse_1_weight_update = np.zeros_like(synapse_1)

	synapse_0_direction_count = np.zeros_like(synapse_0)
	synapse_1_direction_count = np.zeros_like(synapse_1)

	for j in iter(range(epochs+1)):

		layer_0 = X
		layer_1 = sigmoid(np.dot(layer_0, synapse_0))

		if(dropout):
			layer_1 *= np.random.binomial([np.ones((len(X),hidden_neurons))],1-dropout_percent)[0] * (1.0/(1-dropout_percent))

		layer_2 = sigmoid(np.dot(layer_1, synapse_1))

		layer_2_error = y - layer_2

		if (j% 10000) == 0 and j > 5000:
			if np.mean(np.abs(layer_2_error)) < last_mean_error:
				last_mean_error = np.mean(np.abs(layer_2_error))
			else:
				break

		layer_2_delta = layer_2_error * sigmoid_output_to_derivative(layer_2)

		layer_1_error = layer_2_delta.dot(synapse_1.T)

		layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)

		synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
		synapse_0_weight_update = (layer_0.T.dot(layer_1_delta))

		if(j > 0):
			synapse_0_direction_count += np.abs(((synapse_0_weight_update > 0)+0) - ((prev_synapse_0_weight_update > 0) + 0))
			synapse_1_direction_count += np.abs(((synapse_1_weight_update > 0)+0) - ((prev_synapse_1_weight_update > 0) + 0))        

		synapse_1 += alpha * synapse_1_weight_update
		synapse_0 += alpha * synapse_0_weight_update

		prev_synapse_0_weight_update = synapse_0_weight_update
		prev_synapse_1_weight_update = synapse_1_weight_update

	now = datetime.datetime.now()

	synapse = {'synapse0': synapse_0.tolist(), 'synapse1': synapse_1.tolist(),'datetime': now.strftime("%Y-%m-%d %H:%M"),'words': words,'classes': classes}

	synapse_file = "synapses.json"

	with open(synapse_file, 'w') as outfile:
		json.dump(synapse, outfile, indent=4, sort_keys=True)

X = np.array(training)
y = np.array(output)
ERROR_THRESHOLD = 0.2
train(X, y, hidden_neurons=20, alpha=0.1, epochs=100000, dropout=False, dropout_percent=0.2)


with open("synapses.json") as data_file : 
	synapse = json.load(data_file) 
	synapse_0 = np.asarray(synapse['synapse0']) 
	synapse_1 = np.asarray(synapse['synapse1'])

def classify(sentence, show_details = False) :
	results = think(sentence, show_details)
	results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD ] 
	results.sort(key=lambda x: x[1], reverse=True) 
	return_results =[[classes[r[0]],r[1]] for r in results]
	return return_results
