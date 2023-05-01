import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from './Dashboard/Dashboard';
import TopNavigation from "../src/TopNavigation/TopNavigation";
import PersonalData from "../src/PersonalData/PersonalData";
import MLModel from './MLModel/MLModel';
import Control from './Control/Control';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
  <Routes>
    <Route path="/app" element={<App />}></Route>
    <Route path="/" element={<Dashboard />} />
    <Route path="/personaldata" element={<PersonalData />} />
    <Route path="/mlmodel" element={<MLModel />} />
    <Route path="/control" element={<Control />} />
  </Routes>
</BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
