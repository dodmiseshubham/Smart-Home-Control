import TopNavigation from "../TopNavigation/TopNavigation";
import axios from 'axios';
import "./control.css";

import { Button } from 'carbon-components-react'

import { useState, useEffect } from 'react';

function Control() {   

    let [cntMsg, setCntMsg] = useState("")
    let [isLoaded, setIsLoaded] = useState(false)
    let [isTrain, setIsTrain] = useState(true)

    useEffect(() => {
        axios.get(`http://0.0.0.0:8001/automatestatus`)
        .then(res => {
          const status = res.data;
          let msg = ""
          if (status["status"]) {
            msg = "AC is running in Automated mode"
          } else {
            msg = "AC is running in Training mode"
          }
             
          setCntMsg(msg)
          setIsLoaded(true)
          setIsTrain(status["status"])
        })
    }, []);

    function changeControl() {
        axios.get(`http://0.0.0.0:8001/automate`)
        .then(res => {
          const weather = res.data;
          alert("Control Changed")
          window.location.reload(false);
        })
    }

    return (
      <div>
        <TopNavigation/>
        <div className="control">
        <h3> Control your Climate</h3>
        { !isLoaded ? (
              <div>
                  <h3>Control Loading...</h3>
              </div>
          ):(
              <div>
                 Current Status: {cntMsg}
                 <br></br>
                 <br></br>
                 <br></br>
                 <button className="button-cnt1" onClick={() => changeControl()} disabled={!isTrain}>Start Training Mode</button>
                 <br></br>
                 <br></br>
                 <br></br>
                 <button className="button-cnt2" onClick={() => changeControl()} disabled={isTrain}>Start Automatic mode</button>
              </div>
          )}
        </div>
      </div>
    );
  }

  export default Control;