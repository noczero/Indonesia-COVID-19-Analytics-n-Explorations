Indonesia-COVID-19-Analytics-n-Explorations
============================

> This repository is for exploring covid-19 in Indonesia using data science approach. I can extract new active cases, still active cases, total confirmed cases, total cured cases, new cured cases, new dead cases, and total dead cases of all province in Indonesia. 

> The data is from https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/edit#gid=2052139453 and managed by @kawalcovid19

### Project Structure

    .
    ├── image                   # Images files that generated from notebooks
    ├── notebooks               # Jupyter Notebooks file    
    ├── src                     # Python file for backend and apps, including utlilites
    └── README.md
    
### To Do
- [ ] Public API   
  - [ ] Use fastAPI directly.
  - [ ] Use InfluxDB to store timeseries and forward to Laravel with OAuth.
- [ ] More visualization plot
- [ ] Front-end App using Dash

### Completed ✓
- [x] Load Data
- [x] Preprocessing
- [x] Plot All Province for 7 cases
- [x] Prepare for backend
