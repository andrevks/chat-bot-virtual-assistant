import React, {useState, useEffect } from 'react';
import mainPhoto from './mainphoto.png';
import mic from './dark.png';
import './App.css';
import SpeechToText from './SpeechRecognition';
import TextToSpeech from "./TextToSpeech";

function App() {
  const [ currentTime, setCurrentTime ] = useState(0);

  // useEffect(()=>{
  //   fetch('http://localhost:5000/time',{
  //     mode: 'cors'
  //   }).then(res => res.json()).then(data =>{
  //     setCurrentTime(data.time);
  //   });
  // }, []);

  // const handleSubmit = e => {
  //   e.preventDefault();
  //   let voiceClip = {'voice_clip':'No PAIN no GAIN!'};
  //   voiceClip = JSON.stringify(voiceClip);
  //   fetch('http://localhost:5000/record', {
  //     method: 'POST',
  //     headers: {
  //       'Content-Type': 'application/json'
  //     },
  //     mode: 'cors',
  //     body: voiceClip
  //   }).then(res => res.json()).then(data =>{
  //     console.log(data);
  //   });
    
  // };


  return (
    <div className="App">
      <div className=''> </div>
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <div 
        style={{
          position: 'relative',
          width: '100%',
          height: '100%',
          minHeight: '100vh',
          background: '#375CEF'}}
        >
        <img src={mainPhoto} className="mainPhoto" alt="Main Photo"/>

          {/* <p>
            The current time is {currentTime}.
          </p> */}
          <TextToSpeech/>
        <SpeechToText/>

        </div>

      </header>
    </div>
  );
}

export default App;
