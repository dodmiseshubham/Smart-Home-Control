import TopNavigation from "../TopNavigation/TopNavigation";
import axios from 'axios';
import "./mlmodel.css";

// import { Button } from 'carbon-components-react';
import { Button } from '@material-ui/core';

import { useState, useEffect } from 'react';

function MLModel() {   
    
    function trainModel() {
        axios.get(`http://0.0.0.0:8001/trainmodel`)
        .then(res => {
          const weather = res.data;
          alert("Model Trained")
        })
    }

    return (
      <div>
        <TopNavigation/>
        <div className="mlmodel">
            <h3>Train the Machine Learning model</h3>
            <button className="button-ml" onClick={() => trainModel()}>Train</button>
        </div>
      </div>
    );
  }

  export default MLModel;