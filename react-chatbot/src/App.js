import React, {useState, useEffect } from 'react';
import mainPhoto from './mainphoto.png';
import mic from './dark.png';
import './App.css';

function App() {
  const [ currentTime, setCurrentTime ] = useState(0);

  useEffect(()=>{
    fetch('/time',{
      mode: 'cors'
    }).then(res => res.json()).then(data =>{
      setCurrentTime(data.time);
    });
  }, []);

  const handleSubmit = e => {
    e.preventDefault();
    let voiceClip = {'voice_clip':'No PAIN no GAIN!'};
    voiceClip = JSON.stringify(voiceClip);
    fetch('http://localhost:5000/record', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      mode: 'cors',
      body: voiceClip
    }).then(res => res.json()).then(data =>{
      console.log(data);
    });
    
    // alert("You clicked ");
    // or you can send to backend
  };


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

        <img src={mic} className="mic" alt="microphone" onClick={handleSubmit}/>
          <p>
            The current time is {currentTime}.
          </p>
        </div>

      </header>
    </div>
  );
}

export default App;
