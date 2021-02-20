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
  - [ ] Use InfluxDB to store timeseries data, for backend using Laravel OAuth with token.
- [ ] Make more visualization plot in notebooks.
- [ ] Build front-end app using Dash.
- [ ] Build k-Means model for clustering zone.
- [ ] ... 

### Completed ✓
- [x] Load Data
- [x] Preprocessing
- [x] Plot All Province for 7 cases
- [x] Prepare for backend
- [x] Run automation for updating plot every 19:30 GMT+7


### Pull Request
You can contribute to this repository, feel free to do pull request. I will review your PR.

### Visualization
> The images will be updated daily at 19:30 GMT +7

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

   
#### Pulau Jawa
##### Jakarta
![jkt active case](notebooks/images/Kasus%20Aktif_Jakarta.png?raw=true "Active Case")
![jkt new case](notebooks/images/Kasus%20Harian_Jakarta.png?raw=true "New Case")
![jkt dead case](notebooks/images/Meninggal%20Dunia_Jakarta.png?raw=true "Dead Case")
![jkt new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Jakarta.png?raw=true "New Dead Case")
![jkt new cure case](notebooks/images/Sembuh%20Harian_Jakarta.png?raw=true "New Cure Case")
![jkt cured case](notebooks/images/Sembuh_Jakarta.png?raw=true "Cured Case")
![jkt total case](notebooks/images/Total%20Case_Jakarta.png?raw=true "Total Confirmed Case")

##### Banten
![Banten active case](notebooks/images/Kasus%20Aktif_Banten.png?raw=true "Active Case")
![Banten new case](notebooks/images/Kasus%20Harian_Banten.png?raw=true "New Case")
![Banten dead case](notebooks/images/Meninggal%20Dunia_Banten.png?raw=true "Dead Case")
![Banten new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Banten.png?raw=true "New Dead Case")
![Banten new cure case](notebooks/images/Sembuh%20Harian_Banten.png?raw=true "New Cure Case")
![Banten cured case](notebooks/images/Sembuh_Banten.png?raw=true "Cured Case")
![Banten total case](notebooks/images/Total%20Case_Banten.png?raw=true "Total Confirmed Case")


##### Jawa Barat
![jabar active case](notebooks/images/Kasus%20Aktif_Jabar.png?raw=true "Active Case")
![jabar new case](notebooks/images/Kasus%20Harian_Jabar.png?raw=true "New Case")
![jabar dead case](notebooks/images/Meninggal%20Dunia_Jabar.png?raw=true "Dead Case")
![jabar new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Jabar.png?raw=true "New Dead Case")
![jabar new cure case](notebooks/images/Sembuh%20Harian_Jabar.png?raw=true "New Cure Case")
![jabar cured case](notebooks/images/Sembuh_Jabar.png?raw=true "Cured Case")
![jabar total case](notebooks/images/Total%20Case_Jabar.png?raw=true "Total Confirmed Case")


##### Jawa Tengah
![Jateng active case](notebooks/images/Kasus%20Aktif_Jateng.png?raw=true "Active Case")
![Jateng new case](notebooks/images/Kasus%20Harian_Jateng.png?raw=true "New Case")
![Jateng dead case](notebooks/images/Meninggal%20Dunia_Jateng.png?raw=true "Dead Case")
![Jateng new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Jateng.png?raw=true "New Dead Case")
![Jateng new cure case](notebooks/images/Sembuh%20Harian_Jateng.png?raw=true "New Cure Case")
![Jateng cured case](notebooks/images/Sembuh_Jateng.png?raw=true "Cured Case")
![Jateng total case](notebooks/images/Total%20Case_Jateng.png?raw=true "Total Confirmed Case")

##### Daerah Istimewa Yogyakarta
![DIY active case](notebooks/images/Kasus%20Aktif_DIY.png?raw=true "Active Case")
![DIY new case](notebooks/images/Kasus%20Harian_DIY.png?raw=true "New Case")
![DIY dead case](notebooks/images/Meninggal%20Dunia_DIY.png?raw=true "Dead Case")
![DIY new dead case](notebooks/images/Meninggal%20Dunia%20Harian_DIY.png?raw=true "New Dead Case")
![DIY new cure case](notebooks/images/Sembuh%20Harian_DIY.png?raw=true "New Cure Case")
![DIY cured case](notebooks/images/Sembuh_DIY.png?raw=true "Cured Case")
![DIY total case](notebooks/images/Total%20Case_DIY.png?raw=true "Total Confirmed Case")

##### Jawa Timur
![Jatim active case](notebooks/images/Kasus%20Aktif_Jatim.png?raw=true "Active Case")
![Jatim new case](notebooks/images/Kasus%20Harian_Jatim.png?raw=true "New Case")
![Jatim dead case](notebooks/images/Meninggal%20Dunia_Jatim.png?raw=true "Dead Case")
![Jatim new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Jatim.png?raw=true "New Dead Case")
![Jatim new cure case](notebooks/images/Sembuh%20Harian_Jatim.png?raw=true "New Cure Case")
![Jatim cured case](notebooks/images/Sembuh_Jatim.png?raw=true "Cured Case")
![Jatim total case](notebooks/images/Total%20Case_Jatim.png?raw=true "Total Confirmed Case")

#### Pulau Sumatera
##### Aceh
![Aceh active case](notebooks/images/Kasus%20Aktif_Aceh.png?raw=true "Active Case")
![Aceh new case](notebooks/images/Kasus%20Harian_Aceh.png?raw=true "New Case")
![Aceh dead case](notebooks/images/Meninggal%20Dunia_Aceh.png?raw=true "Dead Case")
![Aceh new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Aceh.png?raw=true "New Dead Case")
![Aceh new cure case](notebooks/images/Sembuh%20Harian_Aceh.png?raw=true "New Cure Case")
![Aceh cured case](notebooks/images/Sembuh_Aceh.png?raw=true "Cured Case")
![Aceh total case](notebooks/images/Total%20Case_Aceh.png?raw=true "Total Confirmed Case")

##### Sumatera Utara
![Sumut active case](notebooks/images/Kasus%20Aktif_Sumut.png?raw=true "Active Case")
![Sumut new case](notebooks/images/Kasus%20Harian_Sumut.png?raw=true "New Case")
![Sumut dead case](notebooks/images/Meninggal%20Dunia_Sumut.png?raw=true "Dead Case")
![Sumut new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Sumut.png?raw=true "New Dead Case")
![Sumut new cure case](notebooks/images/Sembuh%20Harian_Sumut.png?raw=true "New Cure Case")
![Sumut cured case](notebooks/images/Sembuh_Sumut.png?raw=true "Cured Case")
![Sumut total case](notebooks/images/Total%20Case_Sumut.png?raw=true "Total Confirmed Case")

##### Riau
![Riau active case](notebooks/images/Kasus%20Aktif_Riau.png?raw=true "Active Case")
![Riau new case](notebooks/images/Kasus%20Harian_Riau.png?raw=true "New Case")
![Riau dead case](notebooks/images/Meninggal%20Dunia_Riau.png?raw=true "Dead Case")
![Riau new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Riau.png?raw=true "New Dead Case")
![Riau new cure case](notebooks/images/Sembuh%20Harian_Riau.png?raw=true "New Cure Case")
![Riau cured case](notebooks/images/Sembuh_Riau.png?raw=true "Cured Case")
![Riau total case](notebooks/images/Total%20Case_Riau.png?raw=true "Total Confirmed Case")


##### Sumatera Barat
![Sumbar active case](notebooks/images/Kasus%20Aktif_Sumbar.png?raw=true "Active Case")
![Sumbar new case](notebooks/images/Kasus%20Harian_Sumbar.png?raw=true "New Case")
![Sumbar dead case](notebooks/images/Meninggal%20Dunia_Sumbar.png?raw=true "Dead Case")
![Sumbar new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Sumbar.png?raw=true "New Dead Case")
![Sumbar new cure case](notebooks/images/Sembuh%20Harian_Sumbar.png?raw=true "New Cure Case")
![Sumbar cured case](notebooks/images/Sembuh_Sumbar.png?raw=true "Cured Case")
![Sumbar total case](notebooks/images/Total%20Case_Sumbar.png?raw=true "Total Confirmed Case")


##### Kepulauan Riau
![Kep Riau active case](notebooks/images/Kasus%20Aktif_Kep%20Riau.png?raw=true "Active Case")
![Kep Riau new case](notebooks/images/Kasus%20Harian_Kep%20Riau.png?raw=true "New Case")
![Kep Riau dead case](notebooks/images/Meninggal%20Dunia_Kep%20Riau.png?raw=true "Dead Case")
![Kep Riau new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Kep%20Riau.png?raw=true "New Dead Case")
![Kep Riau new cure case](notebooks/images/Sembuh%20Harian_Kep%20Riau.png?raw=true "New Cure Case")
![Kep Riau cured case](notebooks/images/Sembuh_Kep%20Riau.png?raw=true "Cured Case")
![Kep Riau total case](notebooks/images/Total%20Case_Kep%20Riau.png?raw=true "Total Confirmed Case")
![Kep Riau total case](notebooks/images/Total%20Case_Kep%20Riau.png?raw=true "Total Confirmed Case")

##### Jambi
![Jambi active case](notebooks/images/Kasus%20Aktif_Jambi.png?raw=true "Active Case")
![Jambi new case](notebooks/images/Kasus%20Harian_Jambi.png?raw=true "New Case")
![Jambi dead case](notebooks/images/Meninggal%20Dunia_Jambi.png?raw=true "Dead Case")
![Jambi new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Jambi.png?raw=true "New Dead Case")
![Jambi new cure case](notebooks/images/Sembuh%20Harian_Jambi.png?raw=true "New Cure Case")
![Jambi cured case](notebooks/images/Sembuh_Jambi.png?raw=true "Cured Case")
![Jambi total case](notebooks/images/Total%20Case_Jambi.png?raw=true "Total Confirmed Case")

##### Sumatera Selatan
![Sumsel active case](notebooks/images/Kasus%20Aktif_Sumsel.png?raw=true "Active Case")
![Sumsel new case](notebooks/images/Kasus%20Harian_Sumsel.png?raw=true "New Case")
![Sumsel dead case](notebooks/images/Meninggal%20Dunia_Sumsel.png?raw=true "Dead Case")
![Sumsel new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Sumsel.png?raw=true "New Dead Case")
![Sumsel new cure case](notebooks/images/Sembuh%20Harian_Sumsel.png?raw=true "New Cure Case")
![Sumsel cured case](notebooks/images/Sembuh_Sumsel.png?raw=true "Cured Case")
![Sumsel total case](notebooks/images/Total%20Case_Sumsel.png?raw=true "Total Confirmed Case")

##### Bangka Belitung
![Babel active case](notebooks/images/Kasus%20Aktif_Babel.png?raw=true "Active Case")
![Babel new case](notebooks/images/Kasus%20Harian_Babel.png?raw=true "New Case")
![Babel dead case](notebooks/images/Meninggal%20Dunia_Babel.png?raw=true "Dead Case")
![Babel new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Babel.png?raw=true "New Dead Case")
![Babel new cure case](notebooks/images/Sembuh%20Harian_Babel.png?raw=true "New Cure Case")
![Babel cured case](notebooks/images/Sembuh_Babel.png?raw=true "Cured Case")
![Babel total case](notebooks/images/Total%20Case_Babel.png?raw=true "Total Confirmed Case")

##### Bengkulu 
![Bengkulu active case](notebooks/images/Kasus%20Aktif_Bengkulu.png?raw=true "Active Case")
![Bengkulu new case](notebooks/images/Kasus%20Harian_Bengkulu.png?raw=true "New Case")
![Bengkulu dead case](notebooks/images/Meninggal%20Dunia_Bengkulu.png?raw=true "Dead Case")
![Bengkulu new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Bengkulu.png?raw=true "New Dead Case")
![Bengkulu new cure case](notebooks/images/Sembuh%20Harian_Bengkulu.png?raw=true "New Cure Case")
![Bengkulu cured case](notebooks/images/Sembuh_Bengkulu.png?raw=true "Cured Case")
![Bengkulu total case](notebooks/images/Total%20Case_Bengkulu.png?raw=true "Total Confirmed Case")

##### Lampung 
![Lampung active case](notebooks/images/Kasus%20Aktif_Lampung.png?raw=true "Active Case")
![Lampung new case](notebooks/images/Kasus%20Harian_Lampung.png?raw=true "New Case")
![Lampung dead case](notebooks/images/Meninggal%20Dunia_Lampung.png?raw=true "Dead Case")
![Lampung new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Lampung.png?raw=true "New Dead Case")
![Lampung new cure case](notebooks/images/Sembuh%20Harian_Lampung.png?raw=true "New Cure Case")
![Lampung cured case](notebooks/images/Sembuh_Lampung.png?raw=true "Cured Case")
![Lampung total case](notebooks/images/Total%20Case_Lampung.png?raw=true "Total Confirmed Case")


#### Kalimantan
##### Kalimantan Barat
![Kalbar active case](notebooks/images/Kasus%20Aktif_Kalbar.png?raw=true "Active Case")
![Kalbar new case](notebooks/images/Kasus%20Harian_Kalbar.png?raw=true "New Case")
![Kalbar dead case](notebooks/images/Meninggal%20Dunia_Kalbar.png?raw=true "Dead Case")
![Kalbar new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Kalbar.png?raw=true "New Dead Case")
![Kalbar new cure case](notebooks/images/Sembuh%20Harian_Kalbar.png?raw=true "New Cure Case")
![Kalbar cured case](notebooks/images/Sembuh_Kalbar.png?raw=true "Cured Case")
![Kalbar total case](notebooks/images/Total%20Case_Kalbar.png?raw=true "Total Confirmed Case")

##### Kalimantan Tengah
![Kalteng active case](notebooks/images/Kasus%20Aktif_Kalteng.png?raw=true "Active Case")
![Kalteng new case](notebooks/images/Kasus%20Harian_Kalteng.png?raw=true "New Case")
![Kalteng dead case](notebooks/images/Meninggal%20Dunia_Kalteng.png?raw=true "Dead Case")
![Kalteng new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Kalteng.png?raw=true "New Dead Case")
![Kalteng new cure case](notebooks/images/Sembuh%20Harian_Kalteng.png?raw=true "New Cure Case")
![Kalteng cured case](notebooks/images/Sembuh_Kalteng.png?raw=true "Cured Case")
![Kalteng total case](notebooks/images/Total%20Case_Kalteng.png?raw=true "Total Confirmed Case")

##### Kalimantan Utara
![Kaltara active case](notebooks/images/Kasus%20Aktif_Kaltara.png?raw=true "Active Case")
![Kaltara new case](notebooks/images/Kasus%20Harian_Kaltara.png?raw=true "New Case")
![Kaltara dead case](notebooks/images/Meninggal%20Dunia_Kaltara.png?raw=true "Dead Case")
![Kaltara new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Kaltara.png?raw=true "New Dead Case")
![Kaltara new cure case](notebooks/images/Sembuh%20Harian_Kaltara.png?raw=true "New Cure Case")
![Kaltara cured case](notebooks/images/Sembuh_Kaltara.png?raw=true "Cured Case")
![Kaltara total case](notebooks/images/Total%20Case_Kaltara.png?raw=true "Total Confirmed Case")

##### Kalimantan Timur
![Kaltim active case](notebooks/images/Kasus%20Aktif_Kaltim.png?raw=true "Active Case")
![Kaltim new case](notebooks/images/Kasus%20Harian_Kaltim.png?raw=true "New Case")
![Kaltim dead case](notebooks/images/Meninggal%20Dunia_Kaltim.png?raw=true "Dead Case")
![Kaltim new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Kaltim.png?raw=true "New Dead Case")
![Kaltim new cure case](notebooks/images/Sembuh%20Harian_Kaltim.png?raw=true "New Cure Case")
![Kaltim cured case](notebooks/images/Sembuh_Kaltim.png?raw=true "Cured Case")
![Kaltim total case](notebooks/images/Total%20Case_Kaltim.png?raw=true "Total Confirmed Case")


##### Kalimantan Selatan
![Kalsel active case](notebooks/images/Kasus%20Aktif_Kalsel.png?raw=true "Active Case")
![Kalsel new case](notebooks/images/Kasus%20Harian_Kalsel.png?raw=true "New Case")
![Kalsel dead case](notebooks/images/Meninggal%20Dunia_Kalsel.png?raw=true "Dead Case")
![Kalsel new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Kalsel.png?raw=true "New Dead Case")
![Kalsel new cure case](notebooks/images/Sembuh%20Harian_Kalsel.png?raw=true "New Cure Case")
![Kalsel cured case](notebooks/images/Sembuh_Kalsel.png?raw=true "Cured Case")
![Kalsel total case](notebooks/images/Total%20Case_Kalsel.png?raw=true "Total Confirmed Case")

#### Sulawesi
##### Sulawesi Selatan
![Sulsel active case](notebooks/images/Kasus%20Aktif_Sulsel.png?raw=true "Active Case")
![Sulsel new case](notebooks/images/Kasus%20Harian_Sulsel.png?raw=true "New Case")
![Sulsel dead case](notebooks/images/Meninggal%20Dunia_Sulsel.png?raw=true "Dead Case")
![Sulsel new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Sulsel.png?raw=true "New Dead Case")
![Sulsel new cure case](notebooks/images/Sembuh%20Harian_Sulsel.png?raw=true "New Cure Case")
![Sulsel cured case](notebooks/images/Sembuh_Sulsel.png?raw=true "Cured Case")
![Sulsel total case](notebooks/images/Total%20Case_Sulsel.png?raw=true "Total Confirmed Case")

##### Sulawesi Barat
![Sulbar active case](notebooks/images/Kasus%20Aktif_Sulbar.png?raw=true "Active Case")
![Sulbar new case](notebooks/images/Kasus%20Harian_Sulbar.png?raw=true "New Case")
![Sulbar dead case](notebooks/images/Meninggal%20Dunia_Sulbar.png?raw=true "Dead Case")
![Sulbar new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Sulbar.png?raw=true "New Dead Case")
![Sulbar new cure case](notebooks/images/Sembuh%20Harian_Sulbar.png?raw=true "New Cure Case")
![Sulbar cured case](notebooks/images/Sembuh_Sulbar.png?raw=true "Cured Case")
![Sulbar total case](notebooks/images/Total%20Case_Sulbar.png?raw=true "Total Confirmed Case")


##### Sulawesi Tengah
![Sulteng active case](notebooks/images/Kasus%20Aktif_Sulteng.png?raw=true "Active Case")
![Sulteng new case](notebooks/images/Kasus%20Harian_Sulteng.png?raw=true "New Case")
![Sulteng dead case](notebooks/images/Meninggal%20Dunia_Sulteng.png?raw=true "Dead Case")
![Sulteng new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Sulteng.png?raw=true "New Dead Case")
![Sulteng new cure case](notebooks/images/Sembuh%20Harian_Sulteng.png?raw=true "New Cure Case")
![Sulteng cured case](notebooks/images/Sembuh_Sulteng.png?raw=true "Cured Case")
![Sulteng total case](notebooks/images/Total%20Case_Sulteng.png?raw=true "Total Confirmed Case")

##### Gorontalo
![Gorontalo active case](notebooks/images/Kasus%20Aktif_Gorontalo.png?raw=true "Active Case")
![Gorontalo new case](notebooks/images/Kasus%20Harian_Gorontalo.png?raw=true "New Case")
![Gorontalo dead case](notebooks/images/Meninggal%20Dunia_Gorontalo.png?raw=true "Dead Case")
![Gorontalo new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Gorontalo.png?raw=true "New Dead Case")
![Gorontalo new cure case](notebooks/images/Sembuh%20Harian_Gorontalo.png?raw=true "New Cure Case")
![Gorontalo cured case](notebooks/images/Sembuh_Gorontalo.png?raw=true "Cured Case")
![Gorontalo total case](notebooks/images/Total%20Case_Gorontalo.png?raw=true "Total Confirmed Case")

##### Sulawesi Utara
![Sulut active case](notebooks/images/Kasus%20Aktif_Sulut.png?raw=true "Active Case")
![Sulut new case](notebooks/images/Kasus%20Harian_Sulut.png?raw=true "New Case")
![Sulut dead case](notebooks/images/Meninggal%20Dunia_Sulut.png?raw=true "Dead Case")
![Sulut new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Sulut.png?raw=true "New Dead Case")
![Sulut new cure case](notebooks/images/Sembuh%20Harian_Sulut.png?raw=true "New Cure Case")
![Sulut cured case](notebooks/images/Sembuh_Sulut.png?raw=true "Cured Case")
![Sulut total case](notebooks/images/Total%20Case_Sulut.png?raw=true "Total Confirmed Case")

##### Sulawesi Tenggara
![Sultra active case](notebooks/images/Kasus%20Aktif_Sultra.png?raw=true "Active Case")
![Sultra new case](notebooks/images/Kasus%20Harian_Sultra.png?raw=true "New Case")
![Sultra dead case](notebooks/images/Meninggal%20Dunia_Sultra.png?raw=true "Dead Case")
![Sultra new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Sultra.png?raw=true "New Dead Case")
![Sultra new cure case](notebooks/images/Sembuh%20Harian_Sultra.png?raw=true "New Cure Case")
![Sultra cured case](notebooks/images/Sembuh_Sultra.png?raw=true "Cured Case")
![Sultra total case](notebooks/images/Total%20Case_Sultra.png?raw=true "Total Confirmed Case")


#### Bali
![Bali active case](notebooks/images/Kasus%20Aktif_Bali.png?raw=true "Active Case")
![Bali new case](notebooks/images/Kasus%20Harian_Bali.png?raw=true "New Case")
![Bali dead case](notebooks/images/Meninggal%20Dunia_Bali.png?raw=true "Dead Case")
![Bali new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Bali.png?raw=true "New Dead Case")
![Bali new cure case](notebooks/images/Sembuh%20Harian_Bali.png?raw=true "New Cure Case")
![Bali cured case](notebooks/images/Sembuh_Bali.png?raw=true "Cured Case")
![Bali total case](notebooks/images/Total%20Case_Bali.png?raw=true "Total Confirmed Case")



#### Nusa Tenggara Barat
![NTB active case](notebooks/images/Kasus%20Aktif_NTB.png?raw=true "Active Case")
![NTB new case](notebooks/images/Kasus%20Harian_NTB.png?raw=true "New Case")
![NTB dead case](notebooks/images/Meninggal%20Dunia_NTB.png?raw=true "Dead Case")
![NTB new dead case](notebooks/images/Meninggal%20Dunia%20Harian_NTB.png?raw=true "New Dead Case")
![NTB new cure case](notebooks/images/Sembuh%20Harian_NTB.png?raw=true "New Cure Case")
![NTB cured case](notebooks/images/Sembuh_NTB.png?raw=true "Cured Case")
![NTB total case](notebooks/images/Total%20Case_NTB.png?raw=true "Total Confirmed Case")

#### Nusa Tenggara Timur
![NTT active case](notebooks/images/Kasus%20Aktif_NTT.png?raw=true "Active Case")
![NTT new case](notebooks/images/Kasus%20Harian_NTT.png?raw=true "New Case")
![NTT dead case](notebooks/images/Meninggal%20Dunia_NTT.png?raw=true "Dead Case")
![NTT new dead case](notebooks/images/Meninggal%20Dunia%20Harian_NTT.png?raw=true "New Dead Case")
![NTT new cure case](notebooks/images/Sembuh%20Harian_NTT.png?raw=true "New Cure Case")
![NTT cured case](notebooks/images/Sembuh_NTT.png?raw=true "Cured Case")
![NTT total case](notebooks/images/Total%20Case_NTT.png?raw=true "Total Confirmed Case")
#### Maluku 
![Maluku active case](notebooks/images/Kasus%20Aktif_Maluku.png?raw=true "Active Case")
![Maluku new case](notebooks/images/Kasus%20Harian_Maluku.png?raw=true "New Case")
![Maluku dead case](notebooks/images/Meninggal%20Dunia_Maluku.png?raw=true "Dead Case")
![Maluku new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Maluku.png?raw=true "New Dead Case")
![Maluku new cure case](notebooks/images/Sembuh%20Harian_Maluku.png?raw=true "New Cure Case")
![Maluku cured case](notebooks/images/Sembuh_Maluku.png?raw=true "Cured Case")
![Maluku total case](notebooks/images/Total%20Case_Maluku.png?raw=true "Total Confirmed Case")


#### Maluku Utara
![Malut active case](notebooks/images/Kasus%20Aktif_Malut.png?raw=true "Active Case")
![Malut new case](notebooks/images/Kasus%20Harian_Malut.png?raw=true "New Case")
![Malut dead case](notebooks/images/Meninggal%20Dunia_Malut.png?raw=true "Dead Case")
![Malut new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Malut.png?raw=true "New Dead Case")
![Malut new cure case](notebooks/images/Sembuh%20Harian_Malut.png?raw=true "New Cure Case")
![Malut cured case](notebooks/images/Sembuh_Malut.png?raw=true "Cured Case")
![Malut total case](notebooks/images/Total%20Case_Malut.png?raw=true "Total Confirmed Case")

#### Papua 
![Papua active case](notebooks/images/Kasus%20Aktif_Papua.png?raw=true "Active Case")
![Papua new case](notebooks/images/Kasus%20Harian_Papua.png?raw=true "New Case")
![Papua dead case](notebooks/images/Meninggal%20Dunia_Papua.png?raw=true "Dead Case")
![Papua new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Papua.png?raw=true "New Dead Case")
![Papua new cure case](notebooks/images/Sembuh%20Harian_Papua.png?raw=true "New Cure Case")
![Papua cured case](notebooks/images/Sembuh_Papua.png?raw=true "Cured Case")
![Papua total case](notebooks/images/Total%20Case_Papua.png?raw=true "Total Confirmed Case")

#### Papua Barat
![Papbar active case](notebooks/images/Kasus%20Aktif_Papbar.png?raw=true "Active Case")
![Papbar new case](notebooks/images/Kasus%20Harian_Papbar.png?raw=true "New Case")
![Papbar dead case](notebooks/images/Meninggal%20Dunia_Papbar.png?raw=true "Dead Case")
![Papbar new dead case](notebooks/images/Meninggal%20Dunia%20Harian_Papbar.png?raw=true "New Dead Case")
![Papbar new cure case](notebooks/images/Sembuh%20Harian_Papbar.png?raw=true "New Cure Case")
![Papbar cured case](notebooks/images/Sembuh_Papbar.png?raw=true "Cured Case")
![Papbar total case](notebooks/images/Total%20Case_Papbar.png?raw=true "Total Confirmed Case")

### Still Active Cases
![Still Active Cases](notebooks/images/Kasus%20Aktif_Semua_Provinsi.png?raw=true "Still Active Cases on All Provinces")

### New Active Cases
![New Cases](notebooks/images/Kasus%20Harian_Semua_Provinsi.png?raw=true "New Active Cases on All Provinces")

### New Cured Cases
![New Cured Cases](notebooks/images/Sembuh%20Harian_Semua_Provinsi.png?raw=true "New Cured Cases on All Provinces")

### New Dead Cases
![New Dead Cases](notebooks/images/Meninggal%20Dunia%20Harian_Semua_Provinsi.png?raw=true "New Dead Active Cases on All Provinces")

### Total Confirmed Cases
![Total Confirmed Cases](notebooks/images/Total%20Case_Semua_Provinsi.png?raw=true "Total Confirmed Cases on All Provinces")

### Total Cured Cases
![Total Cured Cases](notebooks/images/Sembuh_Semua_Provinsi.png?raw=true "Total Cured Cases on All Provinces")

### Total Dead Cases
![Total Dead Cases](notebooks/images/Meninggal%20Dunia_Semua_Provinsi.png?raw=true "Total Dead Cases on All Provinces")

## Provinces API 
| Province      | API      |
| :---        |    :----             |
| Aceh      | https://apicovid.bravo.siat.web.id/api/v_update_covid19 |
