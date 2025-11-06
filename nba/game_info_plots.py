import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np


def day_chart(data_new: pd.DataFrame) -> Figure:
    """
    Average attendance by day, plotted as a bar chart
        Parameters
    df : pd.DataFrame
        DataFrame with columns 'Day' and 'Attendance'.

    Returns
    Figure
        The matplotlib Figure object containing the plot.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(
        data_new["Day"],
        data_new["Attendance"],
        color="CadetBlue",
        edgecolor="black",
        linewidth=1.2,
    )
    plt.xticks(rotation=45)
    ax.set_title("Average Attendance by Day")
    ax.set_xlabel("Day")
    ax.set_ylabel("Attendance")
    return fig


def month_chart(data_new: pd.DataFrame) -> Figure:
    """
    Average attendance by month, plotted as a bar chart
        Parameters
    df : pd.DataFrame
        DataFrame with columns 'Month' and 'Attendance'.

    Returns
    Figure
        The matplotlib Figure object containing the plot.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(
        data_new["Month"],
        data_new["Attendance"],
        color="CadetBlue",
        edgecolor="black",
        linewidth=1.2,
    )
    plt.xticks(rotation=45)
    ax.set_title("Average Attendance by Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Attendance")
    return fig


def line_year(data_new: pd.DataFrame) -> Figure:
    """
    Total attendance by year, plotted
    as a line chart with linear trend line fitted
        Parameters
    df : pd.DataFrame
        DataFrame with columns 'Month' and 'Attendance'.

    Returns
    Figure
        The matplotlib Figure object containing the plot.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(data_new["Year"], data_new["Attendance"], color="Salmon")

    # trend line
    slope, intercept = np.polyfit(data_new["Year"], data_new["Attendance"], 1)
    y_trend = slope * data_new["Year"] + intercept
    ax.plot(data_new["Year"], y_trend, label="Trend Line")

    ax.set_xlabel("Year")
    ax.set_ylabel("Total Attendance")
    ax.set_title("Total Attendance by Year")
    return fig
