import time
from flask_cors import CORS
from flask import Flask, request
# import time, random, sys
# from util import VirtualAssistant
from util import DataSet
from util.virtualAssistant import VirtualAssistant
app = Flask(__name__)
cors = CORS(app)
assistant = VirtualAssistant(dataset=DataSet)

@app.route('/')
def home():
    return "Welcome to the chatbot API"


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/record', methods=['POST'])
def recordings():
    if request.method == 'POST':
        data = request.get_json()
        voice_clip = data['voice_clip']
        print(f">>>>>>>>>>>>>>>{data}")
        answer = assistant.bot(str(voice_clip))
        # answer = voice_clip
        print(f'answer: {answer}')
        return {"answer": answer}
        # return {"data":data}
    # else:
    #   data = 'Testing...' if not voice_clip else voice_clip
    #   return {'voice': data }

    # data = voice_clip
    # if data:
    #   return f"Voice clip received {data}"
    # else :
    #   return f"Where is the voice clip?"


if __name__ == '__main__':
    app.run(debug=False)
