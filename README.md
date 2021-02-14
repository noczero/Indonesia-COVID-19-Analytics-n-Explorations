Indonesia-COVID-19-Analytics-n-Explorations
============================

> This repository is for exploring covid-19 in Indonesia using data science approach. I can extract new active cases, still active cases, total confirmed cases, total cured cases, new cured cases, new dead cases, and total dead cases of all province in Indonesia. 

> The data is from https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/edit#gid=2052139453 and managed by @kawalcovid19


### Project Structure

    .
    ├── notebooks               # Jupyter Notebooks file 
       ├── image                # Images files that generated from notebooks   
    ├── src                     # Python file for backend and apps, including utlilites
    └── README.md
    
### To Do
- [ ] Provide public API.   
  - [ ] Use fastAPI directly.
  - [ ] Use InfluxDB to store timeseries and forward to Laravel with OAuth.
- [ ] Make more visualization plot in notebooks.
- [ ] Build front-end app using Dash.
- [ ] Build k-Means model for clustering zone.
- [ ] ... 

### Completed ✓
- [x] Load Data
- [x] Preprocessing
- [x] Plot All Province for 7 cases
- [x] Prepare for backend


### Pull Request
You can contribute to this repository, feel free to do pull request. I will review your PR.

### Visualization
#### Updated at 13 February
##### Jakarta
![jkt active case](notebooks/images/Kasus%20Aktif_Jakarta.png?raw=true "Active Case")
![jkt new case](notebooks/images/Kasus%20Harian_Jakarta.png?raw=true "New Case")
![jkt dead case](notebooks/images/Meninggal%20Dunia_Jakarta.png?raw=true "Dead Case")
![jkt new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Jakarta.png?raw=true "New Dead Case")
![jkt new cure case](notebooks/images/Sembuh%20Harian_Jakarta.png?raw=true "New Cure Case")
![jkt cured case](notebooks/images/Sembuh_Jakarta.png?raw=true "Cured Case")
![jkt total case](notebooks/images/Total%20Case_Jakarta.png?raw=true "Total Confirmed Case")



