# Data Sources

## 1. Train Data

### Train Schedule and Station Information

Our system requires train numbers, train names, routes, stations,
station sequences, and scheduled timings.

Possible sources include:

- Indian Railways official information and railway data services
- IRCTC services
- Railway data APIs available for developers
- Public railway datasets

The data can be used to maintain train routes, station information,
and scheduled timings.

### Real-Time Train Location

For real-time train location, the system can potentially use:

- Railway APIs providing live train status
- Third-party railway data APIs
- GPS-based tracking data, if available

Real-time location data can provide the current station, current
position, and movement of a train.

### Train Delay Data

Delay information can be obtained from:

- Real-time railway status APIs
- Railway operational data
- Historical train delay datasets

The delay information can be used by the ETA prediction system
to calculate updated arrival times.

---

## 2. Weather Data

Weather conditions can affect train travel time and therefore can
be considered while calculating ETA.

### OpenWeather

OpenWeather provides weather information through APIs.

Possible data includes:

- Temperature
- Weather conditions
- Rain
- Wind
- Visibility

The weather information can be retrieved for locations near railway
stations.

---

## 3. Current Prototype

For the current prototype, the project uses simulated/sample data.

The file:

`train_data_live.csv`

contains sample train information such as:

- Train number
- Train name
- Current station
- Station index
- Delay
- Weather
- Speed multiplier

The sample data allows the team to develop and test the system
without depending on a live external API.

In the future, the sample data provider can be replaced with a
real-time API provider without changing the rest of the application.