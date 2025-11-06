import pandas as pd
from nba.simple_clean import simple_clean

# Data manipulation and visualisations for the games.csv.
query_gameinfo = """
    SELECT *
    FROM game_info
"""


def data_view_info() -> pd.DataFrame:
    """
    This is a simple function to view the data before making any manipulations
    """
    data_new = simple_clean(query_gameinfo)
    return data_new


def game_info_clean(data_new: pd.DataFrame) -> pd.DataFrame:
    """
    Parameters:
    data: pd.DataFrame
    This is the output from the data_view() function which
    connects to sql and read the data into a pandas dataframe

    Returns:
    pd.DataFrame
    Cleaned DataFrame
    """
    # convert to date_time
    data_new["game_date"] = pd.to_datetime(
        data_new["game_date"], errors="coerce"
    )

    # extract the day and time for analysis
    data_new["Day"] = data_new["game_date"].dt.day_name()
    data_new["Month"] = data_new["game_date"].dt.month_name()
    data_new["Year"] = data_new["game_date"].dt.year

    data_new = data_new.dropna(subset=["game_time", "game_date", "attendance"])
    data_new = data_new.drop(columns=["game_time"])

    data_new.columns = [
        "Game Id",
        "Game Date",
        "Attendance",
        "Day",
        "Month",
        "Year",
    ]

    return data_new


def day_pd(data_new: pd.DataFrame) -> pd.DataFrame:
    attendance_by_day = data_new.groupby("Day")["Attendance"].mean()
    attendance_by_day = attendance_by_day.reindex(
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
    )
    return attendance_by_day.reset_index()


def month_pd(data_new: pd.DataFrame) -> pd.DataFrame:
    attendance_by_m = data_new.groupby("Month")["Attendance"].mean()
    attendance_by_m = attendance_by_m.reindex(
        [
            "January",
            "February",
            "March",
            "April",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
    )
    return attendance_by_m.reset_index()


def year_pd(data_new: pd.DataFrame) -> pd.DataFrame:
    attendance_by_yr = data_new.groupby("Year")["Attendance"].sum()
    return attendance_by_yr.reset_index()
