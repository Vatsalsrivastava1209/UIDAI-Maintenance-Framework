import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from .config import CONFIG


def calculate_risk_index(df):
    """Calculate the Identity Maintenance Risk Index (district or state level)."""
    scaler = MinMaxScaler()

    df["enrol_norm"] = scaler.fit_transform(df[["total_enrolments"]])
    df["update_rate_norm"] = scaler.fit_transform(df[["update_rate"]])
    df["balance_norm"] = scaler.fit_transform(df[["balance_score"]])

    w = CONFIG["risk_weights"]
    df["identity_maintenance_risk"] = (
            w["enrol"] * df["enrol_norm"] +
            w["update_rate"] * (1 - df["update_rate_norm"]) +
            w["balance"] * (1 - df["balance_norm"])
    )

    df["risk_level"] = pd.qcut(df["identity_maintenance_risk"], q=3,
                               labels=["Low Risk", "Medium Risk", "High Risk"])
    return df


def calculate_balance_score(df_updates):
    """Variance-based balance across age groups."""
    long = df_updates.melt(id_vars=['group'], value_vars=['demo_age_5_17', 'demo_age_17_'],
                           var_name='age_group', value_name='count')
    variance = long.groupby('group')['count'].var().fillna(0)
    return (1 / (1 + variance)).to_frame("balance_score")