import React, { useEffect, useState } from "react";
import SpeechRecognition, {
  useSpeechRecognition
} from "react-speech-recognition";
import mic from './dark.png';
import TextToSpeech from "./TextToSpeech";
// import "./speech-to-text.css";

const SpeechToText = () => {
  const {
    transcript,
    listening,
    resetTranscript,
    browserSupportsSpeechRecognition
  } = useSpeechRecognition();

  const [answer, setAnswer] = React.useState(" ");

  // const printOnSubmit = (e) =>{
  //   e.preventDefault();
  //   // alert(e.target.text.value);
  //   const voiceText = e.target.text.value? e.target.text.value: " " ;
  //   let voiceClip = {'voice_clip': voiceText}
  //   voiceClip = JSON.stringify(voiceClip);
  //   fetch('http://localhost:5000/record', {
  //     method: 'POST',
  //     headers: {
  //       'Content-Type': 'application/json'
  //     },
  //     mode: 'cors',
  //     body: voiceClip
  //   }).then(res => res.json()).then(data =>{
  //     console.log(data['answer']);
  //     data = data['answer'];
  //     setAnswer(data);
  //   });
  // };

  const sendVoice =  (voiceText) =>{
    // alert(e.target.text.value);
    let voiceClip = {'voice_clip': voiceText};
    voiceClip = JSON.stringify(voiceClip);
    fetch('http://localhost:5000/record', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      mode: 'cors',
      body: voiceClip
    }).then(res => res.json()).then(data =>{
      console.log(data['answer']);
      data = data['answer'];
      setAnswer(data);
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // alert(e.target.text.value);
    console.log("transcript:", transcript);
    await sendVoice(transcript);
    resetTranscript();
    console.log("transcript reseted");
  };

  useEffect(() => {
    SpeechRecognition.startListening({ continuous: true });
    // SpeechRecognition.startListening();
    console.log("Now listening...");
    return () => {
      SpeechRecognition.stopListening();
      console.log("Stopped Listening");
    };
  }, [resetTranscript]);

  // useEffect(async () => {
  //   console.log("transcript:", transcript);
  //   await sendVoice(transcript);
  //   resetTranscript();
  //   console.log("transcript reseted");
  // }, [transcript]);

  if (!browserSupportsSpeechRecognition) {
    return <span> Browser does not support speech recognition.</span>;
  }

  return (
    <div>
      <TextToSpeech answer={answer}/>

      <img src={mic} className="mic" alt="microphone" onClick={handleSubmit}/>
      <br/>
      <span>{transcript}</span>
      <br/>
      <br/>
      <button onClick={resetTranscript}>Clear</button>

      {/*<form onSubmit={printOnSubmit}>*/}
      {/*  <textarea name="text" rows={3} cols={20} value={transcript}></textarea>*/}
      {/*  <div className="btn-container">*/}
      {/*    <span onClick={resetTranscript} className="btn">*/}
      {/*      Clear Text */}
      {/*    </span>*/}
      {/*    <button type="submit" className="btn">*/}
      {/*      Send Text*/}
      {/*    </button>*/}
      {/*  </div>*/}
      {/*</form>*/}
    </div>
  );
};

export default SpeechToText;