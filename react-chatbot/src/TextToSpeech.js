import React, { useEffect, useState } from "react";
import { useSpeechSynthesis } from 'react-speech-kit';
import SpeechRecognition from "react-speech-recognition";

const TextToSpeech = ({answer}) => {
    const [value, setValue] = React.useState('');
    const { speak } = useSpeechSynthesis();

    useEffect(async ()  => { // const voices = window.speechSynthesis.getVoices();
        const voice = await window.speechSynthesis.getVoices()[7];
        // console.log("voices: ", voice);
        speak({text: answer, voice: voice});
    }, [answer]);

    // const handleSubmit = (e) => {
    //     e.preventDefault();
    //     const voice = window.speechSynthesis.getVoices()[7];
    //     speak({text: value, voice: voice});
    // };

    return (
        <div className='speech'>
            {/*<div className='group'>*/}
            {/*    <h2>Text to Speech Converter</h2>*/}
            {/*</div>*/}
            {/*<div className='group'>*/}
            {/*    <textarea rows='10' value={value} onChange={(event => setValue(event.target.value))}*/}
            {/*    ></textarea>*/}
            {/*</div>*/}
            {/*<div className='group'>*/}
            {/*    <button onClick={handleSubmit}>*/}
            {/*        Speech*/}
            {/*    </button>*/}
            {/*</div>*/}
        </div>
    );
};
export default TextToSpeech;