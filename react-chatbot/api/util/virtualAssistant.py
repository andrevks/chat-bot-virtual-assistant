import random

# import DataSet

class VirtualAssistant:

    def __init__(self, dataset):
        self.dataset = dataset
        self.trained = {
            'intro': [
                'I\'m a Susan Halper from PreTech.' ,
                ' We sell the best tech in the world, mostly laptops.'
            ] ,
            'cta': [
                'So you wanna buy, then ?'
                'i could take the laptop with me and meet you tomorrow at the mall' ,

                'If you have interest in buying the laptop I will make a discount for you!'
            ] ,
            'confirmation':[
                'That\'s amazing, see you',
                'I\'m looking forward to this',
                'You won\'t regret! this is a unique opportunity'
            ]
        }
        self.trained_rand = ['I don\'t know what you are talking about Sir' ,
                             'I believe you are speaking about yourself Sir']

    def speak(self, audioString):
        print(audioString)
        return audioString

    def bot(self, data):
        if "how are you" in data:
            data = "I am Fine"
            self.speak(data)
            return data

        elif "close" and "deal" in data:
            data = "That's great, the price is a thousand dollars, I will contact you tomorrow for further information"
            self.speak(data)
            return data

        elif ("thank you" or "thanks") in data:
            data = "You are welcome."
            self.speak(data)
            return data

        else:
            cl = self.dataset.classify(data)
            if len(cl) > 0:
                if cl[0][0] == "location":
                    pass
                # Location(data)
                else:
                    # Choose the response randomly
                    try:
                        t = random.choice(self.trained[cl[0][0]])
                        # print(t)
                        self.speak(t)
                        return t
                    except KeyError as keyE:
                        print(f"There's no response to it, classfication: {keyE}")
                        return "No response"
                    except Exception as e:
                        print(f"Error on the response: {e}")

            else:
                t = random.choice(self.trained_rand)
                # print(t)
                self.speak(t)
                return t