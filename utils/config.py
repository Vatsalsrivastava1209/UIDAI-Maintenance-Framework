# config.py - Central place for all tunable parameters
CONFIG = {
    "risk_weights": {
        "enrol": 0.25,          # High enrolment = higher impact risk
        "update_rate": 0.40,    # Low update = higher risk (inverted)
        "balance": 0.35         # Low balance = higher risk (inverted)
    },
    "clustering": {
        "n_clusters": 4,
        "features": ["enrol_norm", "update_rate_norm", "balance_norm"]
    },
    "thresholds": {
        "min_enrol_for_analysis": 1000,
        "high_enrol_quantile": 0.7,
        "low_update_quantile": 0.3
    },
    "files": {
        "pincode_mapping": "pincode_directory.csv",
        "district_geojson": "india_districts.json"
    }
}