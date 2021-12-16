
import React, { useEffect, useState } from "react";
import SpeechRecognition, {
  useSpeechRecognition
} from "react-speech-recognition";
import mic from './dark.png';
// import "./speech-to-text.css";

const SpeechToText = () => {
  const { transcript, resetTranscript } = useSpeechRecognition();
  const printOnSubmit = (e) =>{
    e.preventDefault();
    // alert(e.target.text.value);
    const voiceText = e.target.text.value?e.target.text.value: " " ;
    let voiceClip = {'voice_clip': voiceText}
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
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // alert(e.target.text.value);
    console.log("MIC pressed");
    
  };

  useEffect(() => {
    SpeechRecognition.startListening({ continuous: true });
    console.log("Now listening...");
    return () => {
      SpeechRecognition.stopListening();
      console.log("Stopped Listening");
    };
  }, []);
  if (!SpeechRecognition.browserSupportsSpeechRecognition()) {
    alert("Browser does not support speech recognition");
  }
  return (
    <div>
    <img src={mic} className="mic" alt="microphone" onClick={handleSubmit}/>
      <form onSubmit={printOnSubmit}>
        <textarea name="text" rows={3} cols={20} value={transcript}></textarea>
        <div className="btn-container">
          <span onClick={resetTranscript} className="btn">
            Clear Text 
          </span>
          <button type="submit" className="btn">
            Send Text
          </button>
        </div>
      </form>
    </div>
  );
};

export default SpeechToText;