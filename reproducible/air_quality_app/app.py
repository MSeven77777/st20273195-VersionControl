import streamlit as st
from config import load_dataset, load_model_results

st.set_page_config(
    page_title="Beijing Air Quality Analysis",
    page_icon="☁️",
    layout="wide"
)

df, data_path = load_dataset()
results_df, results_path = load_model_results()


st.sidebar.title("CMP7005 PRAC1")
st.sidebar.write("**Project:** Beijing Air Quality Analysis")
st.sidebar.write("**Target:** PM2.5")
st.sidebar.write("**App Sections:** Dataset | Visualisation | Model Outputs")

if data_path:
    st.sidebar.success("Cleaned dataset loaded")
else:
    st.sidebar.error("Cleaned dataset not found")

if results_path:
    st.sidebar.success("Model results loaded")
else:
    st.sidebar.warning("Model results CSV not found")

st.title("☁️ Beijing Air Quality Analysis Application")

st.markdown(
    """
    This application presents the complete analytical workflow for PM2.5 prediction using the Beijing air-quality dataset.

    The analysis focuses on four representative monitoring stations:
    **Changping, Shunyi (suburban)** and **Tiantan, Wanshouxigong (urban)**, allowing comparison between different spatial environments.

    **Main sections:**

    1. **Dataset Section** – reviews the cleaned dataset, selected stations, date range, missing values, data types, and summary statistics.

    2. **Visualisation Section** – presents EDA results covering pollutant distributions, meteorological variables, correlation patterns, spatial differences between urban and suburban areas, and temporal PM2.5 variations.

    3. **Model Outputs Section** – displays regression and time-series modelling results, including RMSE comparison, prediction performance, Random Forest feature importance, and SARIMAX benchmark forecasts.
    """
)

st.divider()

col1, col2, col3, col4 = st.columns(4)

if df is not None:
    with col1:
        st.metric("Rows", f"{df.shape[0]:,}")
    with col2:
        st.metric("Columns", df.shape[1])
    with col3:
        st.metric("Stations", df["station"].nunique() if "station" in df.columns else "N/A")
    with col4:
        st.metric("Missing values", int(df.isnull().sum().sum()))
else:
    st.warning("Dataset could not be loaded. Please check the data path in config.py.")

st.divider()

st.subheader("Best Model Summary")

if results_df is not None and not results_df.empty:
    if "RMSE" in results_df.columns:
        results_df = results_df.sort_values("RMSE").reset_index(drop=True)
        best_model = results_df.iloc[0]
        st.success(
            f"Best model based on RMSE: **{best_model['Model']}** "
            f"| RMSE = {best_model['RMSE']:.3f} "
            f"| MAE = {best_model['MAE']:.3f} "
            f"| R² = {best_model['R2']:.3f}"
        )
    else:
        st.info("Model results were loaded, but the RMSE column was not found.")
else:
    st.info("Model results CSV was not found. The Model Outputs page can still show saved model figures if available.")

st.divider()

st.subheader("How to Use This Application")
st.write(
    "Use the page menu on the left to move between the dataset, EDA visualisations, and model outputs. "
    "The application is structured to match the assessment workflow and support clear navigation."
)
