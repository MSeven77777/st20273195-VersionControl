import streamlit as st
from config import load_model_results, show_figure, safe_dataframe

st.title("🌳 Model Outputs Section")
st.write("This section presents model performance metrics, prediction results, and model interpretation outputs.")

results_df, results_path = load_model_results()

st.subheader("Model Performance Table")

if results_df is not None and not results_df.empty:
    st.caption(f"Loaded file: {results_path}")

    if "RMSE" in results_df.columns:
        results_df = results_df.sort_values("RMSE").reset_index(drop=True)

    st.dataframe(safe_dataframe(results_df), width="stretch")

    if all(col in results_df.columns for col in ["Model", "RMSE", "MAE", "R2"]):
        best_model = results_df.iloc[0]
        st.success(
            f"Best model: **{best_model['Model']}** | "
            f"RMSE = {best_model['RMSE']:.3f} | "
            f"MAE = {best_model['MAE']:.3f} | "
            f"R² = {best_model['R2']:.3f}"
        )
else:
    st.warning(
        "Model results CSV was not found. Please save the final model results table from the Model Building notebook."
    )

st.divider()

st.subheader("Metric Explanation")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**MAE**")
    st.write("Average absolute prediction error. Lower is better.")
with col2:
    st.markdown("**RMSE**")
    st.write("Penalises larger prediction errors more strongly. Lower is better.")
with col3:
    st.markdown("**R²**")
    st.write("Proportion of PM2.5 variation explained by the model. Higher is better.")

st.divider()


st.subheader("Model Visualisations")

model_figures = {
    "Prediction Comparison": {
        "file": "model_prediction_comparison.png",
        "text": "Compares actual PM2.5 values with predictions from the baseline and machine-learning models."
    },
    "RMSE Model Comparison": {
        "file": "model_comparison_rmse.png",
        "text": "Compares model error using RMSE. The model with the lowest RMSE performs best."
    },
    "Random Forest Feature Importance": {
        "file": "random_forest_feature_importance.png",
        "text": "Shows which input features were most important for the tuned Random Forest model."
    },
    "SARIMAX Benchmark Forecast": {
        "file": "sarimax_weather_forecast_all_stations.png",
        "text": "Shows the SARIMAX time-series benchmark. This compares traditional time-series modelling with machine learning."
    }
}

selected_model_figure = st.selectbox(
    "Select model figure",
    list(model_figures.keys())
)

fig_info = model_figures[selected_model_figure]
st.info(fig_info["text"])
show_figure(fig_info["file"], caption=selected_model_figure)

st.divider()

st.subheader("Modelling Conclusion")
st.write(
    "The machine-learning models, especially Random Forest and Tuned Random Forest, are expected to perform better "
    "because they can use pollutant variables, meteorological variables, time features, lag features, and rolling averages. "
    "SARIMAX is retained as a traditional time-series benchmark, but PM2.5 spikes are difficult for linear time-series models to predict accurately."
)
