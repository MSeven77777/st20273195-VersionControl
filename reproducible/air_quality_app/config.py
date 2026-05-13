from pathlib import Path
import pandas as pd
import streamlit as st

# This config works both in the Google Drive / Colab reproducible folder
# and after the same project structure is uploaded to GitHub.
APP_DIR = Path(__file__).resolve().parent
BASE_DIR = APP_DIR.parent
PROJECT_DIR = BASE_DIR.parent

DATA_DIR = PROJECT_DIR / "data"
FIG_DIR = BASE_DIR / "figures"
RESULT_DIR = BASE_DIR / "results"

CLEANED_DATA_CANDIDATES = [
    RESULT_DIR / "combined_cleaned_air_quality.csv",
    DATA_DIR / "combined_cleaned_air_quality.csv",
    DATA_DIR / "combined_data.csv"
]

MODEL_RESULT_CANDIDATES = [
    RESULT_DIR / "final_model_results.csv",
    DATA_DIR / "final_model_results.csv",
    RESULT_DIR / "task3_model_results.csv",
    DATA_DIR / "task3_model_results.csv",
    RESULT_DIR / "model_results.csv",
    DATA_DIR / "model_results.csv"
]

STATION_ORDER = ["Changping", "Shunyi", "Tiantan", "Wanshouxigong"]


def first_existing_path(paths):
    for path in paths:
        path = Path(path)
        if path.exists():
            return path
    return None


def safe_dataframe(data):
    """
    Make a dataframe safe for Streamlit/Arrow display.
    This prevents errors caused by mixed object columns, such as strings mixed with bool values.
    """
    if data is None:
        return None

    df_safe = data.copy()

    for col in df_safe.columns:
        if pd.api.types.is_datetime64_any_dtype(df_safe[col]):
            df_safe[col] = df_safe[col].astype(str)

    object_cols = df_safe.select_dtypes(include=["object"]).columns
    for col in object_cols:
        df_safe[col] = df_safe[col].astype(str)

    return df_safe


@st.cache_data
def load_dataset():
    path = first_existing_path(CLEANED_DATA_CANDIDATES)
    if path is None:
        return None, None

    df = pd.read_csv(path)

    if "datetime" in df.columns:
        df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")

    return df, str(path)


@st.cache_data
def load_model_results():
    path = first_existing_path(MODEL_RESULT_CANDIDATES)
    if path is None:
        return None, None

    df = pd.read_csv(path)
    return df, str(path)


def figure_path(filename: str) -> Path:
    return FIG_DIR / filename


def figure_exists(filename: str) -> bool:
    return figure_path(filename).exists()


def show_figure(filename: str, caption: str = None):
    path = figure_path(filename)
    if path.exists():
        st.image(str(path), caption=caption, width="stretch")
    else:
        st.warning(f"Figure not found: {filename}")


def format_number(value, decimals=2):
    try:
        return f"{float(value):,.{decimals}f}"
    except Exception:
        return str(value)
