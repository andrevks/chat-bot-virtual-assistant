import time
from flask_cors import CORS
from flask import Flask, request


app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "Welcome"

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/record', methods = ['POST'])
def recordings():
  if request.method == 'POST':
    data = request.get_json()
    voice_clip = data['voice_clip']
    print(f">>>>>>>>>>>>>>>{data}")
    return {'data': voice_clip} 
    # return {'data':'asflkjalfjlasdkjf'}
  # else:
  #   data = 'Testing...' if not voice_clip else voice_clip
  #   return {'voice': data }
  
  # data = voice_clip
  # if data:
  #   return f"Voice clip received {data}"
  # else :
  #   return f"Where is the voice clip?"