import { useEffect, useState } from "react";
import io from 'socket.io-client';
import Spinner from 'react-bootstrap/Spinner';

type ControlsProps = {
  onShuffleClick: () => void;
}

const Controls = (props: ControlsProps) => {
  const [audioUrl, setAudioUrl] = useState('');
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    const socket = io('http://localhost:5000');

    socket.on('open', () => {
      console.log('WebSocket connection established');
    });

    socket.on('message', (event) => {
      console.log(event)
    });

    socket.on('audio', (event) => {
      setAudioUrl(`${event.file_path}`);
      setIsLoading(false);
    });

    socket.on('close', () => {
      console.log('WebSocket connection closed');
    });

    return () => {
      socket.close();
    };
  }, []);

  const handleShuffle = () => {
    props.onShuffleClick()
    setAudioUrl('');
    setIsLoading(true)
  }

  return (
    <div className="row text-center" style={{paddingTop: '10px'}}>
      <div className="col-12">
        <button className="btn btn-success" onClick={handleShuffle}>Shuffle!</button>
      </div>
      <div className="col-12">
        <br/>
        {isLoading
          ? (
              <Spinner animation="grow" variant="light" role="status">
                <span className="visually-hidden">Loading...</span>
              </Spinner>
            )
          : (
              <audio controls>
                <source src={audioUrl} type="audio/wav"/>
                Your browser does not support the audio element.
              </audio>
            )
        }
      </div>
    </div>
  )
}

export default Controls;