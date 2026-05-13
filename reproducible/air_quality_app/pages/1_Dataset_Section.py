import pandas as pd
import streamlit as st
from config import load_dataset, safe_dataframe, STATION_ORDER

st.title("📖 Dataset Section")
st.write("This section allows users to inspect the cleaned dataset used for EDA and model building.")

df, data_path = load_dataset()

if df is None:
    st.error("Cleaned dataset not found. Please check the file path in config.py.")
    st.stop()

st.caption(f"Loaded file: {data_path}")

st.sidebar.header("Dataset Filters")

filtered_df = df.copy()

if "station" in filtered_df.columns:
    available_stations = [s for s in STATION_ORDER if s in filtered_df["station"].dropna().unique()]
    selected_stations = st.sidebar.multiselect(
        "Select station(s)",
        available_stations,
        default=available_stations
    )
    if selected_stations:
        filtered_df = filtered_df[filtered_df["station"].isin(selected_stations)]

if "datetime" in filtered_df.columns and pd.api.types.is_datetime64_any_dtype(filtered_df["datetime"]):
    min_date = filtered_df["datetime"].min().date()
    max_date = filtered_df["datetime"].max().date()
    date_range = st.sidebar.date_input(
        "Select date range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[
            (filtered_df["datetime"].dt.date >= start_date) &
            (filtered_df["datetime"].dt.date <= end_date)
        ]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Rows", f"{filtered_df.shape[0]:,}")
with col2:
    st.metric("Columns", filtered_df.shape[1])
with col3:
    st.metric("Missing values", int(filtered_df.isnull().sum().sum()))
with col4:
    if "station" in filtered_df.columns:
        st.metric("Selected stations", filtered_df["station"].nunique())
    else:
        st.metric("Selected stations", "N/A")

st.divider()

st.subheader("Dataset Preview")
preview_rows = st.slider("Rows to display", 5, 100, 10, step=5)
st.dataframe(safe_dataframe(filtered_df.head(preview_rows)), width="stretch")

st.subheader("Column Information")
column_info = pd.DataFrame({
    "Column": filtered_df.columns,
    "Data Type": filtered_df.dtypes.astype(str).values,
    "Missing Count": filtered_df.isnull().sum().values,
    "Missing %": (filtered_df.isnull().mean().values * 100).round(2)
})
st.dataframe(safe_dataframe(column_info), width="stretch")


st.subheader("Statistical Summary")
summary_df = filtered_df.describe(include="all").transpose().reset_index().rename(columns={"index": "Column"})
st.dataframe(safe_dataframe(summary_df), width="stretch")

if "station_type" in filtered_df.columns and "PM2.5" in filtered_df.columns:
    st.subheader("Mean PM2.5 by Station Type")
    type_summary = (
        filtered_df.groupby("station_type")["PM2.5"]
        .mean()
        .reset_index()
        .rename(columns={"PM2.5": "Mean PM2.5"})
    )
    st.dataframe(safe_dataframe(type_summary), width="stretch")
