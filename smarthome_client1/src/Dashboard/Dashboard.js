import './Dashboard.css';
import TopNavigation from "../TopNavigation/TopNavigation";
import axios from 'axios';

import { useState, useEffect } from 'react';

function Dashboard() {

    let [weatherDetails, setWeatherDetails] = useState({})
    let [isLoaded, setIsLoaded] = useState(false)

    useEffect(() => {
        axios.get(`http://0.0.0.0:8001/getweather`)
        .then(res => {
          const weather = res.data;
          // this.setState({ persons });
          setWeatherDetails(weather)
          setIsLoaded(true)
          console.log("Weather ",weather)
        })
    }, []);

    

    return (
      <div>
        <TopNavigation/>
        <div className='dashboard'>
          <h2>Dashboard</h2>
          { !isLoaded ? (
              <div>
                  <h3>Weather Loading...</h3>
              </div>
          ):(
              <div>
                  <p>Location: {weatherDetails["location"]["name"]}</p>
                  <p>Time: {weatherDetails["location"]["localtime"]}</p>
                  <p>Current Temprature: {weatherDetails["current"]["temp_f"]} F</p>
                  <p>Feels like Temprature: {weatherDetails["current"]["feelslike_f"]} F</p>
                  <p>Humidity: {weatherDetails["current"]["humidity"]} %</p>
                  <p>Precipitattion: {weatherDetails["current"]["precip_mm"]} mm</p>
                  <p>Cloud coverage: {weatherDetails["current"]["cloud"]} %</p>
                  <p>Pressure: {weatherDetails["current"]["pressure_in"]} inch</p>

                  <p>Room Temprature {weatherDetails["roomTemprature"]} F</p>
              </div>
          )}
        </div>
      </div>
    );
  }

  export default Dashboard;