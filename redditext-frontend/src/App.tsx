import { useEffect, useState } from 'react';
import './App.css'
import Controls from './components/Controls'
import RedditPostContainer from './components/RedditPost'

interface RedditPost {
  sub: string,
  title: string,
  permalink: string,
  url: string,
}

const App = () => {

  const [title, setTitle] = useState('');
  const [sub, setSub] = useState('');
  const [url, setUrl] = useState('');

  const fetchRedditPost = async () => {
    fetch('http://127.0.0.1:5000/reddit_post').then(async (res) => {
      const redditPost: RedditPost = await res.json();
      setTitle(redditPost.title);
      setSub(redditPost.sub);
      setUrl(redditPost.url);
    })
    
  }

  const handleShuffleClick = () => {
    fetchRedditPost()
  }

  useEffect(() => {
    fetchRedditPost();
  }, []);
  

  return (
    <div className="App" >
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <a className="navbar-brand" href="#">Redditext</a>
        <div id="navbarSupportedContent"></div>
      </nav>
      <div className="row text-center" style={{paddingTop: '10px'}}>
        <div className="col-12">
            <h5 style={{color: 'white'}}>Click the button and get a random Reddit post!</h5>
        </div>
      </div>
      <Controls onShuffleClick={handleShuffleClick}/>
      <RedditPostContainer title={title} sub={sub} url={url}/>
      <footer className="footer text-center text-lg-start bg-light text-muted">
        <section
          className="d-flex justify-content-center justify-content-lg-between p-4 border-bottom"
        >
          <div className="me-5 d-none d-lg-block">
            <span></span>
          </div>
        </section>
      </footer>
    </div>
  )
}

export default App
