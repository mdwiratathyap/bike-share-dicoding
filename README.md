# Bike Rentals - Final Project Data Analytics
## 0. Overview Project
This project was created as the final project of one of the coding courses. In this project, in-depth data analysis is carried out to answer predetermined business questions. This project can be run via notebook and has a dashboard that can be accessed at https://bike-share-dicoding-dera.streamlit.app/

## 1. File Structures
```
.
├── dashboard
│   ├── dashboard.py
│   └── day_clean_data.csv
│   └── hour_clean_data.csv
├── Bike-sharing-dataset
│   ├── Readme.txt
│   ├── day.csv
|   └── hour.csv
├── README.md
├── bike_sharing.ipynb
└── requirements.txt
```

## 2. Overview Dataset
Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions,
precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to  
the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA which is 
publicly available in http://capitalbikeshare.com/system-data. We aggregated the data on two hourly and daily basis and then 
extracted and added the corresponding weather and seasonal information. Weather information are extracted from http://www.freemeteo.com. 

## 3. Project Workflow
 - Defined business questions for data exploration
1. Data Wrangling: 
 - Gathering data
 - Assessing data
 - Cleaning data
2. Exploratory Data Analysis:
 - Create Data exploration
3. Data Visualization:
 - Create Data Visualization that answer business questions
4. Dashboard:
 - Set up the DataFrame which will be used
 - Complete the dashboard with various data visualizations
   
## 4. Cuplikan Dashboard
![image](https://github.com/mdwiratathyap/bike-share-dicoding/assets/159518724/10ae925d-7469-419b-ad49-65e11fd9d815)

## 5. How to Access Project
Setup the environment:
```
pip install -r requirements.txt
```
To run the dashboard locally, run this in the terminal:
```
streamlit run dashboard.py
```
