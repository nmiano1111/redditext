import { useEffect, useState } from "react";

type RedditPostContainerProps = {
  title: string,
  sub: string,
  url: string,
}

const RedditPostContainer = (props: RedditPostContainerProps) => {
  
  const [loading, setLoading] = useState(true);
  
  return (
    <div className="row" style={{paddingTop: '15px'}}>
      <div id="side-banner-0" className="col-sm-0 col-md-2 col-lg-2"></div>
      <div id="main-content" className="col-sm-12 col-md-10 col-lg-8">
        <div id="content-card" className="card border-light mb-3" style={{backgroundColor: '#222222'}}>
          <div className="card-header border-light mb-3">
            <h4 style={{color: 'white'}}>{props.title}</h4>
            <h6 style={{color: 'white'}}>/r/{props.sub}</h6>
          </div>
          <div className="card-body">
            <div className="img-fluid" style={{position: 'relative', paddingBottom: 'calc(107.50% + 44px)'}}><iframe src={props.url} frameBorder='0' scrolling='no' width='100%' height='100%' style={{position: 'absolute', top: '0', left: '0'}} allowFullScreen></iframe></div>
          </div>
        </div>
      </div>
      <div id="side-banner-1" className="col-sm-0 col-md-2 col-lg-2"></div>
    </div>
  )
}

export default RedditPostContainer;