Indonesia-COVID-19-Analytics-n-Explorations
============================

[![Visits Badge](https://badges.pufler.dev/visits/noczero/Indonesia-COVID-19-Analytics-n-Explorations)](https://github.com/noczero/Indonesia-COVID-19-Analytics-n-Explorations)
[![Updated Badge](https://badges.pufler.dev/created/noczero/Indonesia-COVID-19-Analytics-n-Explorations)](https://github.com/noczero/Indonesia-COVID-19-Analytics-n-Explorations)
[![Visits Badge](https://badges.pufler.dev/updated/noczero/Indonesia-COVID-19-Analytics-n-Explorations)](https://github.com/noczero/Indonesia-COVID-19-Analytics-n-Explorations)

This repository is for exploring covid-19 in Indonesia using data science approach. I can extract new active cases, still active cases, total confirmed cases, total cured cases, new cured cases, new dead cases, and total dead cases of all province in Indonesia. 

The data is from https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/edit#gid=2052139453 and managed by @kawalcovid19


### Project Structure

    .
    ├── data                    # Result of post processing in csv
    ├── image                   # Images files that contain generated plots   
    ├── notebooks               # Jupyter Notebooks file 
    ├── src                     # Python file for backend and apps, including utlilites
    └── README.md
    
### To Do
- [ ] Provide public API.   
  - [ ] Use fastAPI directly.
  - [ ] Use InfluxDB to store timeseries data, for backend using Laravel OAuth with token.
- [ ] Build front-end app using Dash.
- [ ] ... 

### Completed ✓
- [x] Load Data
- [x] Preprocessing
- [x] Generate timeline plot of every provinces in 7 cases
- [x] Prepare for backend
- [x] Run automation for updating plot started in 19:30 GMT+7
- [x] Generate aggregation plot so we get insight for monthly and for weekday on daily cases.
- [x] Generate CSV file for post processing result
- [x] Build k-Means model for clustering zone.

### How to Contribute
You can contribute to this repository, feel free to do pull request. I will review your PR.

### More Provinces API 
| Province      | API      |
| :---        |    :----             |
| Aceh      | https://apicovid.bravo.siat.web.id/api/v_update_covid19 |


### Visualization
> The images and data will be updated daily around 19:30 GMT +7

#### Provinces Timeline Data
- [Pulau Jawa](#Pulau-Jawa)
  * [Jakarta](#Jakarta)
  * [Banten](#Banten)
  * [Jawa Barat](#Jawa-Barat)
  * [Jawa Tengah](#Jawa-Tengah)
  * [Daerah Istimewa Yogyakarta](#Daerah-Istimewa-Yogyakarta)
  * [Jawa Timur](#Jawa-Timur)
- [Pulau Sumatera](#Pulau-Sumatera)
  * [Aceh](#Aceh)
  * [Sumatera Utara](#Sumatera-Utara)
  * [Riau](#Riau)
  * [Sumatera Barat](#Sumatera-Barat)
  * [Kepulauan Riau](#Kepulauan-Riau)
  * [Jambi](#Jambi)
  * [Sumatera Selatan](#Sumatera-Selatan)
  * [Bangka Belitung](#Bangka-Belitung)
  * [Bengkulu](#Bengkulu)
  * [Lampung](#Lampung)
- [Pulau Kalimantan](#Kalimantan)
  * [Kalimantan Barat](#Kalimantan-Barat)
  * [Kalimantan Tengah](#Kalimantan-Tengah)
  * [Kalimantan Utara](#Kalimantan-Utara)
  * [Kalimantan Timur](#Kalimantan-Timur)
  * [Kalimantan Selatan](#Kalimantan-Selatan)
- [Pulau Sulawesi](#Sulawesi)
  * [Sulawesi Selatan](#Sulawesi-Selatan)
  * [Sulawesi Barat](#Sulawesi-Barat)
  * [Sulawesi Tengah](#Sulawesi-Tengah)
  * [Gorontalo](#Gorontalo)
  * [Sulawesi Utara](#Sulawesi-Utara)
  * [Sulawesi Tenggara](#Sulawesi-Tenggara)
- [Bali](#Bali)
- [Nusa Tenggara Barat](#Nusa-Tenggara-Barat)
- [Nusa Tenggara Timur](#Nusa-Tenggara-Timur)
- [Maluku](#Maluku)
- [Maluku Utara](#Maluku-Utara)
- [Papua](#Papua)
- [Papua Barat](#Papua-Barat)

#### Cases on All Provinces
- [Still Active Cases](#Still-Active-Cases)    
- [New Active Cases](#New-Active-Cases)    
- [New Cured Cases](#New-Cured-Cases)        
- [New Dead Cases](#New-Dead-Cases)    
- [Total Confirmed Cases](#Total-Confirmed-Cases)    
- [Total Cured Cases](#Total-Cured-Cases)    
- [Total Dead Cases](#Total-Dead-Cases)  


#### Clustering Zone
![Culstering Zone](images/K-Means-Daily_Semua_Provinsi.png?raw=true "Clustering Zone")


![Culstering Zone 2](images/K-Means_Weekly_Semua_Provinsi.png?raw=true "Clustering Zone 2")

![Culstering Zone 3](images/K-Means_Weekly_no_norm_Semua_Provinsi.png?raw=true "Clustering Zone 3")
   
#### Pulau Jawa
##### Jakarta
###### Timeline Plot
![jkt active case](images/Kasus%20Aktif_Jakarta.png?raw=true "Active Case")
![jkt new case](images/Kasus%20Harian_Jakarta.png?raw=true "New Case")
![jkt dead case](images/Meninggal%20Dunia_Jakarta.png?raw=true "Dead Case")
![jkt new dead case](images/Meninggal%20Dunia%20Harian_Jakarta.png?raw=true "New Dead Case")
![jkt new cure case](images/Sembuh%20Harian_Jakarta.png?raw=true "New Cure Case")
![jkt cured case](images/Sembuh_Jakarta.png?raw=true "Cured Case")
![jkt total case](images/Total%20Case_Jakarta.png?raw=true "Total Confirmed Case")

###### Aggregation Plot
![Jakarta day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jakarta.png?raw=true "Average New Active Cases in Days")
![Jakarta day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jakarta.png?raw=true "Average Dead Cases in Days")
![Jakarta day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jakarta.png?raw=true "Average Cured Cases in Days")

![Jakarta month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Jakarta.png?raw=true "Average New Active Cases in Month")
![Jakarta month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Jakarta.png?raw=true "Average Dead Cases in Month")
![Jakarta month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Jakarta.png?raw=true "Average Cured Cases in Month")

##### Banten
![Banten active case](images/Kasus%20Aktif_Banten.png?raw=true "Active Case")
![Banten new case](images/Kasus%20Harian_Banten.png?raw=true "New Case")
![Banten dead case](images/Meninggal%20Dunia_Banten.png?raw=true "Dead Case")
![Banten new dead case](images/Meninggal%20Dunia%20Harian_Banten.png?raw=true "New Dead Case")
![Banten new cure case](images/Sembuh%20Harian_Banten.png?raw=true "New Cure Case")
![Banten cured case](images/Sembuh_Banten.png?raw=true "Cured Case")
![Banten total case](images/Total%20Case_Banten.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Banten day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Banten.png?raw=true "Average New Active Cases in Days")
![Banten day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Banten.png?raw=true "Average Dead Cases in Days")
![Banten day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Banten.png?raw=true "Average Cured Cases in Days")

![Banten month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Banten.png?raw=true "Average New Active Cases in Month")
![Banten month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Banten.png?raw=true "Average Dead Cases in Month")
![Banten month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Banten.png?raw=true "Average Cured Cases in Month")

##### Jawa Barat
###### Timeline Plot
![jabar active case](images/Kasus%20Aktif_Jabar.png?raw=true "Active Case")
![jabar new case](images/Kasus%20Harian_Jabar.png?raw=true "New Case")
![jabar dead case](images/Meninggal%20Dunia_Jabar.png?raw=true "Dead Case")
![jabar new dead case](images/Meninggal%20Dunia%20Harian_Jabar.png?raw=true "New Dead Case")
![jabar new cure case](images/Sembuh%20Harian_Jabar.png?raw=true "New Cure Case")
![jabar cured case](images/Sembuh_Jabar.png?raw=true "Cured Case")
![jabar total case](images/Total%20Case_Jabar.png?raw=true "Total Confirmed Case")

###### Aggregation Plot
![Jabar day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jabar.png?raw=true "Average New Active Cases in Days")
![Jabar day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jabar.png?raw=true "Average Dead Cases in Days")
![Jabar day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jabar.png?raw=true "Average Cured Cases in Days")

![Jabar month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Jabar.png?raw=true "Average New Active Cases in Month")
![Jabar month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Jabar.png?raw=true "Average Dead Cases in Month")
![Jabar month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Jabar.png?raw=true "Average Cured Cases in Month")


##### Jawa Tengah
###### Timeline Plot
![Jateng active case](images/Kasus%20Aktif_Jateng.png?raw=true "Active Case")
![Jateng new case](images/Kasus%20Harian_Jateng.png?raw=true "New Case")
![Jateng dead case](images/Meninggal%20Dunia_Jateng.png?raw=true "Dead Case")
![Jateng new dead case](images/Meninggal%20Dunia%20Harian_Jateng.png?raw=true "New Dead Case")
![Jateng new cure case](images/Sembuh%20Harian_Jateng.png?raw=true "New Cure Case")
![Jateng cured case](images/Sembuh_Jateng.png?raw=true "Cured Case")
![Jateng total case](images/Total%20Case_Jateng.png?raw=true "Total Confirmed Case")

###### Aggregation Plot
![Jateng day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jateng.png?raw=true "Average New Active Cases in Days")
![Jateng day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jateng.png?raw=true "Average Dead Cases in Days")
![Jateng day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jateng.png?raw=true "Average Cured Cases in Days")

![Jateng month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Jateng.png?raw=true "Average New Active Cases in Month")
![Jateng month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Jateng.png?raw=true "Average Dead Cases in Month")
![Jateng month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Jateng.png?raw=true "Average Cured Cases in Month")

##### Daerah Istimewa Yogyakarta
###### Timeline Plot
![DIY active case](images/Kasus%20Aktif_DIY.png?raw=true "Active Case")
![DIY new case](images/Kasus%20Harian_DIY.png?raw=true "New Case")
![DIY dead case](images/Meninggal%20Dunia_DIY.png?raw=true "Dead Case")
![DIY new dead case](images/Meninggal%20Dunia%20Harian_DIY.png?raw=true "New Dead Case")
![DIY new cure case](images/Sembuh%20Harian_DIY.png?raw=true "New Cure Case")
![DIY cured case](images/Sembuh_DIY.png?raw=true "Cured Case")
![DIY total case](images/Total%20Case_DIY.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![DIY day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20DIY.png?raw=true "Average New Active Cases in Days")
![DIY day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20DIY.png?raw=true "Average Dead Cases in Days")
![DIY day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20DIY.png?raw=true "Average Cured Cases in Days")

![DIY month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20DIY.png?raw=true "Average New Active Cases in Month")
![DIY month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20DIY.png?raw=true "Average Dead Cases in Month")
![DIY month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20DIY.png?raw=true "Average Cured Cases in Month")

##### Jawa Timur
###### Timeline Plot
![Jatim active case](images/Kasus%20Aktif_Jatim.png?raw=true "Active Case")
![Jatim new case](images/Kasus%20Harian_Jatim.png?raw=true "New Case")
![Jatim dead case](images/Meninggal%20Dunia_Jatim.png?raw=true "Dead Case")
![Jatim new dead case](images/Meninggal%20Dunia%20Harian_Jatim.png?raw=true "New Dead Case")
![Jatim new cure case](images/Sembuh%20Harian_Jatim.png?raw=true "New Cure Case")
![Jatim cured case](images/Sembuh_Jatim.png?raw=true "Cured Case")
![Jatim total case](images/Total%20Case_Jatim.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Jatim day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jatim.png?raw=true "Average New Active Cases in Days")
![Jatim day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jatim.png?raw=true "Average Dead Cases in Days")
![Jatim day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jatim.png?raw=true "Average Cured Cases in Days")

![Jatim month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Jatim.png?raw=true "Average New Active Cases in Month")
![Jatim month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Jatim.png?raw=true "Average Dead Cases in Month")
![Jatim month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Jatim.png?raw=true "Average Cured Cases in Month")

#### Pulau Sumatera
##### Aceh
###### Timeline Plot
![Aceh active case](images/Kasus%20Aktif_Aceh.png?raw=true "Active Case")
![Aceh new case](images/Kasus%20Harian_Aceh.png?raw=true "New Case")
![Aceh dead case](images/Meninggal%20Dunia_Aceh.png?raw=true "Dead Case")
![Aceh new dead case](images/Meninggal%20Dunia%20Harian_Aceh.png?raw=true "New Dead Case")
![Aceh new cure case](images/Sembuh%20Harian_Aceh.png?raw=true "New Cure Case")
![Aceh cured case](images/Sembuh_Aceh.png?raw=true "Cured Case")
![Aceh total case](images/Total%20Case_Aceh.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Aceh day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Aceh.png?raw=true "Average New Active Cases in Days")
![Aceh day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Aceh.png?raw=true "Average Dead Cases in Days")
![Aceh day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Aceh.png?raw=true "Average Cured Cases in Days")

![Aceh month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Aceh.png?raw=true "Average New Active Cases in Month")
![Aceh month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Aceh.png?raw=true "Average Dead Cases in Month")
![Aceh month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Aceh.png?raw=true "Average Cured Cases in Month")

##### Sumatera Utara
###### Timeline Plot
![Sumut active case](images/Kasus%20Aktif_Sumut.png?raw=true "Active Case")
![Sumut new case](images/Kasus%20Harian_Sumut.png?raw=true "New Case")
![Sumut dead case](images/Meninggal%20Dunia_Sumut.png?raw=true "Dead Case")
![Sumut new dead case](images/Meninggal%20Dunia%20Harian_Sumut.png?raw=true "New Dead Case")
![Sumut new cure case](images/Sembuh%20Harian_Sumut.png?raw=true "New Cure Case")
![Sumut cured case](images/Sembuh_Sumut.png?raw=true "Cured Case")
![Sumut total case](images/Total%20Case_Sumut.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Sumut day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sumut.png?raw=true "Average New Active Cases in Days")
![Sumut day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sumut.png?raw=true "Average Dead Cases in Days")
![Sumut day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sumut.png?raw=true "Average Cured Cases in Days")

![Sumut month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Sumut.png?raw=true "Average New Active Cases in Month")
![Sumut month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Sumut.png?raw=true "Average Dead Cases in Month")
![Sumut month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Sumut.png?raw=true "Average Cured Cases in Month")

##### Riau
###### Timeline Plot
![Riau active case](images/Kasus%20Aktif_Riau.png?raw=true "Active Case")
![Riau new case](images/Kasus%20Harian_Riau.png?raw=true "New Case")
![Riau dead case](images/Meninggal%20Dunia_Riau.png?raw=true "Dead Case")
![Riau new dead case](images/Meninggal%20Dunia%20Harian_Riau.png?raw=true "New Dead Case")
![Riau new cure case](images/Sembuh%20Harian_Riau.png?raw=true "New Cure Case")
![Riau cured case](images/Sembuh_Riau.png?raw=true "Cured Case")
![Riau total case](images/Total%20Case_Riau.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Riau day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Riau.png?raw=true "Average New Active Cases in Days")
![Riau day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Riau.png?raw=true "Average Dead Cases in Days")
![Riau day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Riau.png?raw=true "Average Cured Cases in Days")

![Riau month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Riau.png?raw=true "Average New Active Cases in Month")
![Riau month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Riau.png?raw=true "Average Dead Cases in Month")
![Riau month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Riau.png?raw=true "Average Cured Cases in Month")


##### Sumatera Barat
###### Timeline Plot
![Sumbar active case](images/Kasus%20Aktif_Sumbar.png?raw=true "Active Case")
![Sumbar new case](images/Kasus%20Harian_Sumbar.png?raw=true "New Case")
![Sumbar dead case](images/Meninggal%20Dunia_Sumbar.png?raw=true "Dead Case")
![Sumbar new dead case](images/Meninggal%20Dunia%20Harian_Sumbar.png?raw=true "New Dead Case")
![Sumbar new cure case](images/Sembuh%20Harian_Sumbar.png?raw=true "New Cure Case")
![Sumbar cured case](images/Sembuh_Sumbar.png?raw=true "Cured Case")
![Sumbar total case](images/Total%20Case_Sumbar.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Sumbar day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sumbar.png?raw=true "Average New Active Cases in Days")
![Sumbar day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sumbar.png?raw=true "Average Dead Cases in Days")
![Sumbar day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sumbar.png?raw=true "Average Cured Cases in Days")

![Sumbar month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Sumbar.png?raw=true "Average New Active Cases in Month")
![Sumbar month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Sumbar.png?raw=true "Average Dead Cases in Month")
![Sumbar month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Sumbar.png?raw=true "Average Cured Cases in Month")


##### Kepulauan Riau
###### Timeline Plot
![Kep Riau active case](images/Kasus%20Aktif_Kep%20Riau.png?raw=true "Active Case")
![Kep Riau new case](images/Kasus%20Harian_Kep%20Riau.png?raw=true "New Case")
![Kep Riau dead case](images/Meninggal%20Dunia_Kep%20Riau.png?raw=true "Dead Case")
![Kep Riau new dead case](images/Meninggal%20Dunia%20Harian_Kep%20Riau.png?raw=true "New Dead Case")
![Kep Riau new cure case](images/Sembuh%20Harian_Kep%20Riau.png?raw=true "New Cure Case")
![Kep Riau cured case](images/Sembuh_Kep%20Riau.png?raw=true "Cured Case")
![Kep Riau total case](images/Total%20Case_Kep%20Riau.png?raw=true "Total Confirmed Case")
![Kep Riau total case](images/Total%20Case_Kep%20Riau.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Kep%20Riau day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kep%20Riau.png?raw=true "Average New Active Cases in Days")
![Kep%20Riau day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kep%20Riau.png?raw=true "Average Dead Cases in Days")
![Kep%20Riau day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kep%20Riau.png?raw=true "Average Cured Cases in Days")

![Kep%20Riau month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Kep%20Riau.png?raw=true "Average New Active Cases in Month")
![Kep%20Riau month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Kep%20Riau.png?raw=true "Average Dead Cases in Month")
![Kep%20Riau month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Jakarta.png?raw=true "Average Cured Cases in Month")

##### Jambi
###### Timeline Plot
![Jambi active case](images/Kasus%20Aktif_Jambi.png?raw=true "Active Case")
![Jambi new case](images/Kasus%20Harian_Jambi.png?raw=true "New Case")
![Jambi dead case](images/Meninggal%20Dunia_Jambi.png?raw=true "Dead Case")
![Jambi new dead case](images/Meninggal%20Dunia%20Harian_Jambi.png?raw=true "New Dead Case")
![Jambi new cure case](images/Sembuh%20Harian_Jambi.png?raw=true "New Cure Case")
![Jambi cured case](images/Sembuh_Jambi.png?raw=true "Cured Case")
![Jambi total case](images/Total%20Case_Jambi.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Jambi day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jambi.png?raw=true "Average New Active Cases in Days")
![Jambi day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jambi.png?raw=true "Average Dead Cases in Days")
![Jambi day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Jambi.png?raw=true "Average Cured Cases in Days")

![Jambi month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Jambi.png?raw=true "Average New Active Cases in Month")
![Jambi month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Jambi.png?raw=true "Average Dead Cases in Month")
![Jambi month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Jambi.png?raw=true "Average Cured Cases in Month")

##### Sumatera Selatan
###### Timeline Plot
![Sumsel active case](images/Kasus%20Aktif_Sumsel.png?raw=true "Active Case")
![Sumsel new case](images/Kasus%20Harian_Sumsel.png?raw=true "New Case")
![Sumsel dead case](images/Meninggal%20Dunia_Sumsel.png?raw=true "Dead Case")
![Sumsel new dead case](images/Meninggal%20Dunia%20Harian_Sumsel.png?raw=true "New Dead Case")
![Sumsel new cure case](images/Sembuh%20Harian_Sumsel.png?raw=true "New Cure Case")
![Sumsel cured case](images/Sembuh_Sumsel.png?raw=true "Cured Case")
![Sumsel total case](images/Total%20Case_Sumsel.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Sumsel day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sumsel.png?raw=true "Average New Active Cases in Days")
![Sumsel day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sumsel.png?raw=true "Average Dead Cases in Days")
![Sumsel day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sumsel.png?raw=true "Average Cured Cases in Days")

![Sumsel month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Sumsel.png?raw=true "Average New Active Cases in Month")
![Sumsel month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Sumsel.png?raw=true "Average Dead Cases in Month")
![Sumsel month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Sumsel.png?raw=true "Average Cured Cases in Month")

##### Bangka Belitung
###### Timeline Plot
![Babel active case](images/Kasus%20Aktif_Babel.png?raw=true "Active Case")
![Babel new case](images/Kasus%20Harian_Babel.png?raw=true "New Case")
![Babel dead case](images/Meninggal%20Dunia_Babel.png?raw=true "Dead Case")
![Babel new dead case](images/Meninggal%20Dunia%20Harian_Babel.png?raw=true "New Dead Case")
![Babel new cure case](images/Sembuh%20Harian_Babel.png?raw=true "New Cure Case")
![Babel cured case](images/Sembuh_Babel.png?raw=true "Cured Case")
![Babel total case](images/Total%20Case_Babel.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Babel day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Babel.png?raw=true "Average New Active Cases in Days")
![Babel day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Babel.png?raw=true "Average Dead Cases in Days")
![Babel day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Babel.png?raw=true "Average Cured Cases in Days")

![Babel month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Babel.png?raw=true "Average New Active Cases in Month")
![Babel month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Babel.png?raw=true "Average Dead Cases in Month")
![Babel month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Babel.png?raw=true "Average Cured Cases in Month")

##### Bengkulu 
###### Timeline Plot
![Bengkulu active case](images/Kasus%20Aktif_Bengkulu.png?raw=true "Active Case")
![Bengkulu new case](images/Kasus%20Harian_Bengkulu.png?raw=true "New Case")
![Bengkulu dead case](images/Meninggal%20Dunia_Bengkulu.png?raw=true "Dead Case")
![Bengkulu new dead case](images/Meninggal%20Dunia%20Harian_Bengkulu.png?raw=true "New Dead Case")
![Bengkulu new cure case](images/Sembuh%20Harian_Bengkulu.png?raw=true "New Cure Case")
![Bengkulu cured case](images/Sembuh_Bengkulu.png?raw=true "Cured Case")
![Bengkulu total case](images/Total%20Case_Bengkulu.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Bengkulu day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Bengkulu.png?raw=true "Average New Active Cases in Days")
![Bengkulu day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Bengkulu.png?raw=true "Average Dead Cases in Days")
![Bengkulu day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Bengkulu.png?raw=true "Average Cured Cases in Days")

![Bengkulu month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Bengkulu.png?raw=true "Average New Active Cases in Month")
![Bengkulu month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Bengkulu.png?raw=true "Average Dead Cases in Month")
![Bengkulu month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Bengkulu.png?raw=true "Average Cured Cases in Month")

##### Lampung 
###### Timeline Plot
![Lampung active case](images/Kasus%20Aktif_Lampung.png?raw=true "Active Case")
![Lampung new case](images/Kasus%20Harian_Lampung.png?raw=true "New Case")
![Lampung dead case](images/Meninggal%20Dunia_Lampung.png?raw=true "Dead Case")
![Lampung new dead case](images/Meninggal%20Dunia%20Harian_Lampung.png?raw=true "New Dead Case")
![Lampung new cure case](images/Sembuh%20Harian_Lampung.png?raw=true "New Cure Case")
![Lampung cured case](images/Sembuh_Lampung.png?raw=true "Cured Case")
![Lampung total case](images/Total%20Case_Lampung.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Lampung day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Lampung.png?raw=true "Average New Active Cases in Days")
![Lampung day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Lampung.png?raw=true "Average Dead Cases in Days")
![Lampung day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Lampung.png?raw=true "Average Cured Cases in Days")

![Lampung month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Lampung.png?raw=true "Average New Active Cases in Month")
![Lampung month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Lampung.png?raw=true "Average Dead Cases in Month")
![Lampung month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Lampung.png?raw=true "Average Cured Cases in Month")


#### Kalimantan
##### Kalimantan Barat
###### Timeline Plot
![Kalbar active case](images/Kasus%20Aktif_Kalbar.png?raw=true "Active Case")
![Kalbar new case](images/Kasus%20Harian_Kalbar.png?raw=true "New Case")
![Kalbar dead case](images/Meninggal%20Dunia_Kalbar.png?raw=true "Dead Case")
![Kalbar new dead case](images/Meninggal%20Dunia%20Harian_Kalbar.png?raw=true "New Dead Case")
![Kalbar new cure case](images/Sembuh%20Harian_Kalbar.png?raw=true "New Cure Case")
![Kalbar cured case](images/Sembuh_Kalbar.png?raw=true "Cured Case")
![Kalbar total case](images/Total%20Case_Kalbar.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Kalbar day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kalbar.png?raw=true "Average New Active Cases in Days")
![Kalbar day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kalbar.png?raw=true "Average Dead Cases in Days")
![Kalbar day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kalbar.png?raw=true "Average Cured Cases in Days")

![Kalbar month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Kalbar.png?raw=true "Average New Active Cases in Month")
![Kalbar month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Kalbar.png?raw=true "Average Dead Cases in Month")
![Kalbar month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Kalbar.png?raw=true "Average Cured Cases in Month")

##### Kalimantan Tengah
###### Timeline Plot
![Kalteng active case](images/Kasus%20Aktif_Kalteng.png?raw=true "Active Case")
![Kalteng new case](images/Kasus%20Harian_Kalteng.png?raw=true "New Case")
![Kalteng dead case](images/Meninggal%20Dunia_Kalteng.png?raw=true "Dead Case")
![Kalteng new dead case](images/Meninggal%20Dunia%20Harian_Kalteng.png?raw=true "New Dead Case")
![Kalteng new cure case](images/Sembuh%20Harian_Kalteng.png?raw=true "New Cure Case")
![Kalteng cured case](images/Sembuh_Kalteng.png?raw=true "Cured Case")
![Kalteng total case](images/Total%20Case_Kalteng.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Kalteng day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kalteng.png?raw=true "Average New Active Cases in Days")
![Kalteng day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kalteng.png?raw=true "Average Dead Cases in Days")
![Kalteng day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kalteng.png?raw=true "Average Cured Cases in Days")

![Kalteng month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Kalteng.png?raw=true "Average New Active Cases in Month")
![Kalteng month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Kalteng.png?raw=true "Average Dead Cases in Month")
![Kalteng month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Kalteng.png?raw=true "Average Cured Cases in Month")

##### Kalimantan Utara
###### Timeline Plot
![Kaltara active case](images/Kasus%20Aktif_Kaltara.png?raw=true "Active Case")
![Kaltara new case](images/Kasus%20Harian_Kaltara.png?raw=true "New Case")
![Kaltara dead case](images/Meninggal%20Dunia_Kaltara.png?raw=true "Dead Case")
![Kaltara new dead case](images/Meninggal%20Dunia%20Harian_Kaltara.png?raw=true "New Dead Case")
![Kaltara new cure case](images/Sembuh%20Harian_Kaltara.png?raw=true "New Cure Case")
![Kaltara cured case](images/Sembuh_Kaltara.png?raw=true "Cured Case")
![Kaltara total case](images/Total%20Case_Kaltara.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Kaltara day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kaltara.png?raw=true "Average New Active Cases in Days")
![Kaltara day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kaltara.png?raw=true "Average Dead Cases in Days")
![Kaltara day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kaltara.png?raw=true "Average Cured Cases in Days")

![Kaltara month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Kaltara.png?raw=true "Average New Active Cases in Month")
![Kaltara month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Kaltara.png?raw=true "Average Dead Cases in Month")
![Kaltara month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Kaltara.png?raw=true "Average Cured Cases in Month")

##### Kalimantan Timur
###### Timeline Plot
![Kaltim active case](images/Kasus%20Aktif_Kaltim.png?raw=true "Active Case")
![Kaltim new case](images/Kasus%20Harian_Kaltim.png?raw=true "New Case")
![Kaltim dead case](images/Meninggal%20Dunia_Kaltim.png?raw=true "Dead Case")
![Kaltim new dead case](images/Meninggal%20Dunia%20Harian_Kaltim.png?raw=true "New Dead Case")
![Kaltim new cure case](images/Sembuh%20Harian_Kaltim.png?raw=true "New Cure Case")
![Kaltim cured case](images/Sembuh_Kaltim.png?raw=true "Cured Case")
![Kaltim total case](images/Total%20Case_Kaltim.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Kaltim day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kaltim.png?raw=true "Average New Active Cases in Days")
![Kaltim day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kaltim.png?raw=true "Average Dead Cases in Days")
![Kaltim day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kaltim.png?raw=true "Average Cured Cases in Days")

![Kaltim month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Kaltim.png?raw=true "Average New Active Cases in Month")
![Kaltim month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Kaltim.png?raw=true "Average Dead Cases in Month")
![Kaltim month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Kaltim.png?raw=true "Average Cured Cases in Month")


##### Kalimantan Selatan
###### Timeline Plot
![Kalsel active case](images/Kasus%20Aktif_Kalsel.png?raw=true "Active Case")
![Kalsel new case](images/Kasus%20Harian_Kalsel.png?raw=true "New Case")
![Kalsel dead case](images/Meninggal%20Dunia_Kalsel.png?raw=true "Dead Case")
![Kalsel new dead case](images/Meninggal%20Dunia%20Harian_Kalsel.png?raw=true "New Dead Case")
![Kalsel new cure case](images/Sembuh%20Harian_Kalsel.png?raw=true "New Cure Case")
![Kalsel cured case](images/Sembuh_Kalsel.png?raw=true "Cured Case")
![Kalsel total case](images/Total%20Case_Kalsel.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Kalsel day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kalsel.png?raw=true "Average New Active Cases in Days")
![Kalsel day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kalsel.png?raw=true "Average Dead Cases in Days")
![Kalsel day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Kalsel.png?raw=true "Average Cured Cases in Days")

![Kalsel month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Kalsel.png?raw=true "Average New Active Cases in Month")
![Kalsel month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Kalsel.png?raw=true "Average Dead Cases in Month")
![Kalsel month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Kalsel.png?raw=true "Average Cured Cases in Month")

#### Sulawesi
##### Sulawesi Selatan
###### Timeline Plot
![Sulsel active case](images/Kasus%20Aktif_Sulsel.png?raw=true "Active Case")
![Sulsel new case](images/Kasus%20Harian_Sulsel.png?raw=true "New Case")
![Sulsel dead case](images/Meninggal%20Dunia_Sulsel.png?raw=true "Dead Case")
![Sulsel new dead case](images/Meninggal%20Dunia%20Harian_Sulsel.png?raw=true "New Dead Case")
![Sulsel new cure case](images/Sembuh%20Harian_Sulsel.png?raw=true "New Cure Case")
![Sulsel cured case](images/Sembuh_Sulsel.png?raw=true "Cured Case")
![Sulsel total case](images/Total%20Case_Sulsel.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Sulsel day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sulsel.png?raw=true "Average New Active Cases in Days")
![Sulsel day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sulsel.png?raw=true "Average Dead Cases in Days")
![Sulsel day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sulsel.png?raw=true "Average Cured Cases in Days")

![Sulsel month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Sulsel.png?raw=true "Average New Active Cases in Month")
![Sulsel month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Sulsel.png?raw=true "Average Dead Cases in Month")
![Sulsel month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Sulsel.png?raw=true "Average Cured Cases in Month")

##### Sulawesi Barat
###### Timeline Plot
![Sulbar active case](images/Kasus%20Aktif_Sulbar.png?raw=true "Active Case")
![Sulbar new case](images/Kasus%20Harian_Sulbar.png?raw=true "New Case")
![Sulbar dead case](images/Meninggal%20Dunia_Sulbar.png?raw=true "Dead Case")
![Sulbar new dead case](images/Meninggal%20Dunia%20Harian_Sulbar.png?raw=true "New Dead Case")
![Sulbar new cure case](images/Sembuh%20Harian_Sulbar.png?raw=true "New Cure Case")
![Sulbar cured case](images/Sembuh_Sulbar.png?raw=true "Cured Case")
![Sulbar total case](images/Total%20Case_Sulbar.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Sulbar day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sulbar.png?raw=true "Average New Active Cases in Days")
![Sulbar day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sulbar.png?raw=true "Average Dead Cases in Days")
![Sulbar day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sulbar.png?raw=true "Average Cured Cases in Days")

![Sulbar month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Sulbar.png?raw=true "Average New Active Cases in Month")
![Sulbar month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Sulbar.png?raw=true "Average Dead Cases in Month")
![Sulbar month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Sulbar.png?raw=true "Average Cured Cases in Month")


##### Sulawesi Tengah
###### Timeline Plot
![Sulteng active case](images/Kasus%20Aktif_Sulteng.png?raw=true "Active Case")
![Sulteng new case](images/Kasus%20Harian_Sulteng.png?raw=true "New Case")
![Sulteng dead case](images/Meninggal%20Dunia_Sulteng.png?raw=true "Dead Case")
![Sulteng new dead case](images/Meninggal%20Dunia%20Harian_Sulteng.png?raw=true "New Dead Case")
![Sulteng new cure case](images/Sembuh%20Harian_Sulteng.png?raw=true "New Cure Case")
![Sulteng cured case](images/Sembuh_Sulteng.png?raw=true "Cured Case")
![Sulteng total case](images/Total%20Case_Sulteng.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Sulteng day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sulteng.png?raw=true "Average New Active Cases in Days")
![Sulteng day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sulteng.png?raw=true "Average Dead Cases in Days")
![Sulteng day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sulteng.png?raw=true "Average Cured Cases in Days")

![Sulteng month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Sulteng.png?raw=true "Average New Active Cases in Month")
![Sulteng month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Sulteng.png?raw=true "Average Dead Cases in Month")
![Sulteng month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Sulteng.png?raw=true "Average Cured Cases in Month")

##### Gorontalo
###### Timeline Plot
![Gorontalo active case](images/Kasus%20Aktif_Gorontalo.png?raw=true "Active Case")
![Gorontalo new case](images/Kasus%20Harian_Gorontalo.png?raw=true "New Case")
![Gorontalo dead case](images/Meninggal%20Dunia_Gorontalo.png?raw=true "Dead Case")
![Gorontalo new dead case](images/Meninggal%20Dunia%20Harian_Gorontalo.png?raw=true "New Dead Case")
![Gorontalo new cure case](images/Sembuh%20Harian_Gorontalo.png?raw=true "New Cure Case")
![Gorontalo cured case](images/Sembuh_Gorontalo.png?raw=true "Cured Case")
![Gorontalo total case](images/Total%20Case_Gorontalo.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Gorontalo day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Gorontalo.png?raw=true "Average New Active Cases in Days")
![Gorontalo day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Gorontalo.png?raw=true "Average Dead Cases in Days")
![Gorontalo day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Gorontalo.png?raw=true "Average Cured Cases in Days")

![Gorontalo month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Gorontalo.png?raw=true "Average New Active Cases in Month")
![Gorontalo month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Gorontalo.png?raw=true "Average Dead Cases in Month")
![Gorontalo month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Gorontalo.png?raw=true "Average Cured Cases in Month")

##### Sulawesi Utara
###### Timeline Plot
![Sulut active case](images/Kasus%20Aktif_Sulut.png?raw=true "Active Case")
![Sulut new case](images/Kasus%20Harian_Sulut.png?raw=true "New Case")
![Sulut dead case](images/Meninggal%20Dunia_Sulut.png?raw=true "Dead Case")
![Sulut new dead case](images/Meninggal%20Dunia%20Harian_Sulut.png?raw=true "New Dead Case")
![Sulut new cure case](images/Sembuh%20Harian_Sulut.png?raw=true "New Cure Case")
![Sulut cured case](images/Sembuh_Sulut.png?raw=true "Cured Case")
![Sulut total case](images/Total%20Case_Sulut.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Sulut day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sulut.png?raw=true "Average New Active Cases in Days")
![Sulut day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sulut.png?raw=true "Average Dead Cases in Days")
![Sulut day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sulut.png?raw=true "Average Cured Cases in Days")

![Sulut month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Sulut.png?raw=true "Average New Active Cases in Month")
![Sulut month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Sulut.png?raw=true "Average Dead Cases in Month")
![Sulut month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Sulut.png?raw=true "Average Cured Cases in Month")

##### Sulawesi Tenggara
###### Timeline Plot
![Sultra active case](images/Kasus%20Aktif_Sultra.png?raw=true "Active Case")
![Sultra new case](images/Kasus%20Harian_Sultra.png?raw=true "New Case")
![Sultra dead case](images/Meninggal%20Dunia_Sultra.png?raw=true "Dead Case")
![Sultra new dead case](images/Meninggal%20Dunia%20Harian_Sultra.png?raw=true "New Dead Case")
![Sultra new cure case](images/Sembuh%20Harian_Sultra.png?raw=true "New Cure Case")
![Sultra cured case](images/Sembuh_Sultra.png?raw=true "Cured Case")
![Sultra total case](images/Total%20Case_Sultra.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Sultra day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sultra.png?raw=true "Average New Active Cases in Days")
![Sultra day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sultra.png?raw=true "Average Dead Cases in Days")
![Sultra day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Sultra.png?raw=true "Average Cured Cases in Days")

![Sultra month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Sultra.png?raw=true "Average New Active Cases in Month")
![Sultra month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Sultra.png?raw=true "Average Dead Cases in Month")
![Sultra month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Sultra.png?raw=true "Average Cured Cases in Month")


#### Bali
###### Timeline Plot
![Bali active case](images/Kasus%20Aktif_Bali.png?raw=true "Active Case")
![Bali new case](images/Kasus%20Harian_Bali.png?raw=true "New Case")
![Bali dead case](images/Meninggal%20Dunia_Bali.png?raw=true "Dead Case")
![Bali new dead case](images/Meninggal%20Dunia%20Harian_Bali.png?raw=true "New Dead Case")
![Bali new cure case](images/Sembuh%20Harian_Bali.png?raw=true "New Cure Case")
![Bali cured case](images/Sembuh_Bali.png?raw=true "Cured Case")
![Bali total case](images/Total%20Case_Bali.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Bali day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Bali.png?raw=true "Average New Active Cases in Days")
![Bali day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Bali.png?raw=true "Average Dead Cases in Days")
![Bali day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Bali.png?raw=true "Average Cured Cases in Days")

![Bali month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Bali.png?raw=true "Average New Active Cases in Month")
![Bali month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Bali.png?raw=true "Average Dead Cases in Month")
![Bali month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Bali.png?raw=true "Average Cured Cases in Month")



#### Nusa Tenggara Barat
###### Timeline Plot
![NTB active case](images/Kasus%20Aktif_NTB.png?raw=true "Active Case")
![NTB new case](images/Kasus%20Harian_NTB.png?raw=true "New Case")
![NTB dead case](images/Meninggal%20Dunia_NTB.png?raw=true "Dead Case")
![NTB new dead case](images/Meninggal%20Dunia%20Harian_NTB.png?raw=true "New Dead Case")
![NTB new cure case](images/Sembuh%20Harian_NTB.png?raw=true "New Cure Case")
![NTB cured case](images/Sembuh_NTB.png?raw=true "Cured Case")
![NTB total case](images/Total%20Case_NTB.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![NTB day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20NTB.png?raw=true "Average New Active Cases in Days")
![NTB day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20NTB.png?raw=true "Average Dead Cases in Days")
![NTB day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20NTB.png?raw=true "Average Cured Cases in Days")

![NTB month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20NTB.png?raw=true "Average New Active Cases in Month")
![NTB month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20NTB.png?raw=true "Average Dead Cases in Month")
![NTB month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20NTB.png?raw=true "Average Cured Cases in Month")

#### Nusa Tenggara Timur
![NTT active case](images/Kasus%20Aktif_NTT.png?raw=true "Active Case")
![NTT new case](images/Kasus%20Harian_NTT.png?raw=true "New Case")
![NTT dead case](images/Meninggal%20Dunia_NTT.png?raw=true "Dead Case")
![NTT new dead case](images/Meninggal%20Dunia%20Harian_NTT.png?raw=true "New Dead Case")
![NTT new cure case](images/Sembuh%20Harian_NTT.png?raw=true "New Cure Case")
![NTT cured case](images/Sembuh_NTT.png?raw=true "Cured Case")
![NTT total case](images/Total%20Case_NTT.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![NTT day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20NTT.png?raw=true "Average New Active Cases in Days")
![NTT day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20NTT.png?raw=true "Average Dead Cases in Days")
![NTT day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20NTT.png?raw=true "Average Cured Cases in Days")

![NTT month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20NTT.png?raw=true "Average New Active Cases in Month")
![NTT month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20NTT.png?raw=true "Average Dead Cases in Month")
![NTT month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20NTT.png?raw=true "Average Cured Cases in Month")

#### Maluku 
###### Timeline Plot
![Maluku active case](images/Kasus%20Aktif_Maluku.png?raw=true "Active Case")
![Maluku new case](images/Kasus%20Harian_Maluku.png?raw=true "New Case")
![Maluku dead case](images/Meninggal%20Dunia_Maluku.png?raw=true "Dead Case")
![Maluku new dead case](images/Meninggal%20Dunia%20Harian_Maluku.png?raw=true "New Dead Case")
![Maluku new cure case](images/Sembuh%20Harian_Maluku.png?raw=true "New Cure Case")
![Maluku cured case](images/Sembuh_Maluku.png?raw=true "Cured Case")
![Maluku total case](images/Total%20Case_Maluku.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Maluku day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Maluku.png?raw=true "Average New Active Cases in Days")
![Maluku day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Maluku.png?raw=true "Average Dead Cases in Days")
![Maluku day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Maluku.png?raw=true "Average Cured Cases in Days")

![Maluku month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Maluku.png?raw=true "Average New Active Cases in Month")
![Maluku month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Maluku.png?raw=true "Average Dead Cases in Month")
![Maluku month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Maluku.png?raw=true "Average Cured Cases in Month")


#### Maluku Utara
###### Timeline Plot
![Malut active case](images/Kasus%20Aktif_Malut.png?raw=true "Active Case")
![Malut new case](images/Kasus%20Harian_Malut.png?raw=true "New Case")
![Malut dead case](images/Meninggal%20Dunia_Malut.png?raw=true "Dead Case")
![Malut new dead case](images/Meninggal%20Dunia%20Harian_Malut.png?raw=true "New Dead Case")
![Malut new cure case](images/Sembuh%20Harian_Malut.png?raw=true "New Cure Case")
![Malut cured case](images/Sembuh_Malut.png?raw=true "Cured Case")
![Malut total case](images/Total%20Case_Malut.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Malut day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Malut.png?raw=true "Average New Active Cases in Days")
![Malut day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Malut.png?raw=true "Average Dead Cases in Days")
![Malut day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Malut.png?raw=true "Average Cured Cases in Days")

![Malut month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Malut.png?raw=true "Average New Active Cases in Month")
![Malut month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Malut.png?raw=true "Average Dead Cases in Month")
![Malut month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Malut.png?raw=true "Average Cured Cases in Month")

#### Papua 
###### Timeline Plot
![Papua active case](images/Kasus%20Aktif_Papua.png?raw=true "Active Case")
![Papua new case](images/Kasus%20Harian_Papua.png?raw=true "New Case")
![Papua dead case](images/Meninggal%20Dunia_Papua.png?raw=true "Dead Case")
![Papua new dead case](images/Meninggal%20Dunia%20Harian_Papua.png?raw=true "New Dead Case")
![Papua new cure case](images/Sembuh%20Harian_Papua.png?raw=true "New Cure Case")
![Papua cured case](images/Sembuh_Papua.png?raw=true "Cured Case")
![Papua total case](images/Total%20Case_Papua.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Papua day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Papua.png?raw=true "Average New Active Cases in Days")
![Papua day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Papua.png?raw=true "Average Dead Cases in Days")
![Papua day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Papua.png?raw=true "Average Cured Cases in Days")

![Papua month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Papua.png?raw=true "Average New Active Cases in Month")
![Papua month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Papua.png?raw=true "Average Dead Cases in Month")
![Papua month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Papua.png?raw=true "Average Cured Cases in Month")

#### Papua Barat
###### Timeline Plot
![Papbar active case](images/Kasus%20Aktif_Papbar.png?raw=true "Active Case")
![Papbar new case](images/Kasus%20Harian_Papbar.png?raw=true "New Case")
![Papbar dead case](images/Meninggal%20Dunia_Papbar.png?raw=true "Dead Case")
![Papbar new dead case](images/Meninggal%20Dunia%20Harian_Papbar.png?raw=true "New Dead Case")
![Papbar new cure case](images/Sembuh%20Harian_Papbar.png?raw=true "New Cure Case")
![Papbar cured case](images/Sembuh_Papbar.png?raw=true "Cured Case")
![Papbar total case](images/Total%20Case_Papbar.png?raw=true "Total Confirmed Case")
###### Aggregation Plot
![Papbar day avg new case](images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Papbar.png?raw=true "Average New Active Cases in Days")
![Papbar day avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Papbar.png?raw=true "Average Dead Cases in Days")
![Papbar day avg cured case](images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20Papbar.png?raw=true "Average Cured Cases in Days")

![Papbar month avg new case](images/Kasus%20Harian%20Rata-Rata%20di%20Papbar.png?raw=true "Average New Active Cases in Month")
![Papbar month avg dead case](images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20Papbar.png?raw=true "Average Dead Cases in Month")
![Papbar month avg cured case](images/Sembuh%20Harian%20Rata-Rata%20di%20Papbar.png?raw=true "Average Cured Cases in Month")


## Stacked Plot
### Still Active Cases
![Still Active Cases](images/Kasus%20Aktif_Semua_Provinsi.png?raw=true "Still Active Cases on All Provinces")

### New Active Cases
![New Cases](images/Kasus%20Harian_Semua_Provinsi.png?raw=true "New Active Cases on All Provinces")

### New Cured Cases
![New Cured Cases](images/Sembuh%20Harian_Semua_Provinsi.png?raw=true "New Cured Cases on All Provinces")

### New Dead Cases
![New Dead Cases](images/Meninggal%20Dunia%20Harian_Semua_Provinsi.png?raw=true "New Dead Active Cases on All Provinces")

### Total Confirmed Cases
![Total Confirmed Cases](images/Total%20Case_Semua_Provinsi.png?raw=true "Total Confirmed Cases on All Provinces")

### Total Cured Cases
![Total Cured Cases](images/Sembuh_Semua_Provinsi.png?raw=true "Total Cured Cases on All Provinces")

### Total Dead Cases
![Total Dead Cases](images/Meninggal%20Dunia_Semua_Provinsi.png?raw=true "Total Dead Cases on All Provinces")

