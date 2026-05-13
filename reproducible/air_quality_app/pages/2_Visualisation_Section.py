import streamlit as st
from config import show_figure

st.title("🧐 Visualisation Section")
st.write("This section presents the main EDA figures generated from the cleaned dataset.")

figure_catalogue = {
    "Univariate analysis": {
        "Pollutant Distributions": {
            "file": "01_pollutant_distributions.png",
            "text": "Shows the distribution of major pollutant variables using histograms."
        },
        "Meteorological Variable Distributions": {
            "file": "02_meteorological_variable_distributions.png",
            "text": "Shows the distribution of meteorological variables such as temperature, pressure, rainfall, and wind speed."
        },
        "PM2.5 by Station: Median and IQR": {
            "file": "03_pm25_station_median_iqr.png",
            "text": "Compares the typical PM2.5 level and variability across the four selected stations."
        },
        "PM2.5 Distribution by Station": {
            "file": "04_pm25_distribution_by_station_kde.png",
            "text": "Uses KDE curves to compare PM2.5 distribution patterns across stations."
        },
        "Mean PM2.5: Urban vs Suburban": {
            "file": "05_mean_pm25_urban_suburban.png",
            "text": "Compares the average PM2.5 level between urban and suburban station groups."
        },
        "PM2.5 Air-Quality Level Distribution": {
            "file": "14_pm25_air_quality_levels_pie.png",
            "text": "Shows the proportion of PM2.5 observations in different air-quality categories."
        },
        "Wind Direction Frequency": {
            "file": "16_wind_direction_frequency_polar_with_regions_spacious.png",
            "text": "Uses a polar chart to show which wind directions appear most frequently."
        }
    },
    "Bivariate analysis": {
        "PM2.5 vs Temperature": {
            "file": "06_pm25_vs_temp_density_trend.png",
            "text": "Combines a density background with a trend line to show how PM2.5 changes across temperature ranges."
        },
        "NO2 vs O3": {
            "file": "07_no2_vs_o3_density_trend.png",
            "text": "Shows the relationship between NO2 and O3, which is useful for understanding pollutant interactions."
        },
        "Weekday vs Weekend PM2.5": {
            "file": "15_average_pm25_weekday_weekend_pie.png",
            "text": "Compares PM2.5 levels between weekdays and weekends."
        }
    },
    "Multivariate analysis": {
        "Correlation Heatmap": {
            "file": "08_correlation_heatmap.png",
            "text": "Summarises relationships between pollutants and meteorological variables."
        },
        "Correlation with PM2.5": {
            "file": "09_corr_with_pm25.png",
            "text": "Ranks variables by their correlation with PM2.5."
        },
        "Mean Pollutant Levels by Station": {
            "file": "18_eda_mean_pollutant_levels_by_station_heatmap.png",
            "text": "Compares pollutant levels across stations using a heatmap."
        },
        "Pollutant Composition by Station": {
            "file": "19_eda_pollutant_composition_by_station_combined.png",
            "text": "Shows how the selected pollutants contribute proportionally within each station."
        }
    },
    "Temporal analysis": {
        "Seasonal Pattern by Month": {
            "file": "10_pm25_seasonal_pattern_by_month.png",
            "text": "Shows monthly seasonal PM2.5 patterns and highlights higher winter pollution."
        },
        "Urban vs Suburban Monthly Trend": {
            "file": "11_monthly_pm25_urban_suburban_improved.png",
            "text": "Compares PM2.5 trends between urban and suburban station groups."
        },
        "Seasonal PM2.5: Urban vs Suburban": {
            "file": "12_seasonal_pm25_urban_suburban_simple.png",
            "text": "Summarises seasonal PM2.5 differences between urban and suburban groups."
        },
        "Diurnal PM2.5 Pattern": {
            "file": "13_diurnal_pm25_pattern_day_night_simplified.png",
            "text": "Shows how PM2.5 changes across hours of the day with day-night background periods."
        },
        "PM2.5 Decomposition: Trend and Seasonality": {
            "file": "17_pm25_decomposition_trend_monthly_seasonal.png",
            "text": "Separates PM2.5 into long-term trend and monthly seasonal effects."
        },
        "Yearly Average Pollutant Trends": {
            "file": "20_eda_yearly_average_pollutants_combined.png",
            "text": "Compares yearly average trends for multiple pollutants across stations."
        }
    }
}

selected_category = st.sidebar.radio(
    "Select visualisation category",
    list(figure_catalogue.keys())
)

selected_title = st.sidebar.selectbox(
    "Select figure",
    list(figure_catalogue[selected_category].keys())
)

figure_info = figure_catalogue[selected_category][selected_title]

st.subheader(selected_title)
st.info(figure_info["text"])
show_figure(figure_info["file"], caption=selected_title)
