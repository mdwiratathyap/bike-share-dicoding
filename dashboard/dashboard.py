import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

def create_seasonal(df):
    seasonal = df.groupby(by="season").agg({
    "cnt": "mean",
    "casual": "mean",
    "registered": "mean"
    }).reset_index()

    return seasonal

def create_dday(df):
    dday = df.groupby(by=["weekday"]).agg({
        "casual": "mean",
        "registered": "mean"
    }).reset_index()

    dday_melt = dday.melt('weekday', var_name='rent', value_name='mean')

    return dday_melt


def create_hour(df):
    hour_fall = df.loc[df["season"]=="Fall"].groupby(by="hr").agg({
        "cnt":"mean",
    })

    hour_spring = df.loc[df["season"]=="Spring"].groupby(by="hr").agg({
        "cnt":"mean",
    })

    hour_winter = df.loc[df["season"]=="Winter"].groupby(by="hr").agg({
        "cnt":"mean",
    })

    hour_summer = df.loc[df["season"]=="Summer"].groupby(by="hr").agg({
        "cnt":"mean",
    })

    return hour_fall, hour_spring, hour_winter, hour_summer

day_df = pd.read_csv("https://raw.githubusercontent.com/mdwiratathyap/bike-share-dicoding/main/dashboard/day_clean_data.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/mdwiratathyap/bike-share-dicoding/main/dashboard/hour_clean_data.csv")

datetime_columns = ["dteday"]
day_df.sort_values(by="instant", inplace=True)
day_df.reset_index(inplace=True)

for column in datetime_columns:
    day_df[column] = pd.to_datetime(day_df[column])

min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

with st.sidebar:
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df1 = day_df[(day_df["dteday"] >= str(start_date)) & 
                (day_df["dteday"] <= str(end_date))]
main_df2 = hour_df[(hour_df["dteday"] >= str(start_date)) & 
                (hour_df["dteday"] <= str(end_date))]


seasonal = create_seasonal(main_df1)
dday_melt = create_dday(main_df1)
hour_fall, hour_spring, hour_winter, hour_summer = create_hour(main_df2)


st.header('Bike Share Dashboard')


st.subheader("Penyewaan Sepeda untuk Tiap Musim")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    y="cnt", 
    x="season",
    data=seasonal
)
ax.set_xlabel(None)
ax.set_ylabel(None)
ax.set_title('Rata-rata penyewaan sepeda berdasarkan musim')
st.pyplot(fig)


st.subheader("Penyewaan Sepeda dalam Sehari")
fig, ax = plt.subplots(figsize=(10, 6)) 
ax.plot(hour_fall["cnt"], label = "fall", marker = "o")
ax.plot(hour_spring["cnt"], label = "spring", marker = "x")
ax.plot(hour_winter["cnt"], label = "winter", marker = "*")
ax.plot(hour_summer["cnt"], label = "summer", marker = "v")
ax.set_title("Tren penyewaan sepeda setiap musim dalam sehari")
ax.set_xlabel("Jam")
ax.set_ylabel("jumlah rata-rata")
ax.legend(loc="upper left")
st.pyplot(fig)



st.subheader("Penyewaan Casual dan Registered dalam Seminggu")
fig, ax = plt.subplots(figsize=(10, 6))
# Create an array with the colors you want to use
colors = ["#69b3a2", "#4374B3"]
sns.set_palette(sns.color_palette(colors))
# grouped barplot
sns.barplot(
    x="weekday", 
    y="mean", 
    hue="rent", 
    data=dday_melt, 
    ci=None
    )
# Customize the axes and title
ax.set_title("Rata-rata penyewaan sepeda berdasarkan hari")
ax.set_ylabel("mean")
# Remove top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
st.pyplot(fig)

st.caption('Copyright (c) Dera Bike Rental')
