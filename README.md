# CMP7005-PRAC1 – PM2.5 Air Quality Analysis

## ☁️ Project Overview
This project analyses Beijing air quality data to explore PM2.5 patterns and build predictive models using machine learning and time-series approaches.

## 📖 Dataset
This study uses data from four monitoring stations:
- Changping (Suburban)
- Shunyi (Suburban)
- Tiantan (Urban)
- Wanshouxigong (Urban)

⚠️ The dataset is not included due to file size limitations.  
Please download it from:
https://drive.google.com/drive/folders/1W-vp82yeAjVvEJfaExwUfbzQTTyDe77F?usp=sharing

Place the data in a `data/` folder before running.

## 📂 Project Structure
- notebooks/ → analysis and modelling and GUI
- figures/ → visualisations
- results/ → model outputs

## 🌲 Models
- Baseline Mean
- Linear Regression
- Random Forest (Tuned)
- SARIMAX (Time Series)

## ▶️ How to Run

1. Download the dataset from the Google Drive link above and place it in a `data/` folder.

2. Open the notebooks in the `notebooks/` folder and run them in order:
   - Exploratory data analysis
   - Model building
   - Streamlit GUI preparation

3. The generated figures and model outputs are saved in:
   - `figures/`
   - `results/`

4. To run the Streamlit application, open the GUI notebook and follow the instructions inside to launch the app using Streamlit.
