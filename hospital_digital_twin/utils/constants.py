# utils/constants.py

"""
Centralized constants for the Hospital AI Digital Twin
"""

# --------------------------------------------------
# Departments
# --------------------------------------------------

ER = "ER"
ICU = "ICU"
GENERAL_WARD = "GENERAL_WARD"

DEPARTMENTS = [
    ER,
    ICU,
    GENERAL_WARD
]

# --------------------------------------------------
# Capacity Limits
# --------------------------------------------------

MAX_ER_BEDS = 100
MAX_ICU_BEDS = 40
MAX_GENERAL_BEDS = 150

TOTAL_HOSPITAL_CAPACITY = (
    MAX_ER_BEDS +
    MAX_ICU_BEDS +
    MAX_GENERAL_BEDS
)

# --------------------------------------------------
# Staff Limits
# --------------------------------------------------

MAX_ER_STAFF = 25
MAX_ICU_STAFF = 20
MAX_GENERAL_STAFF = 40

# --------------------------------------------------
# Prediction Thresholds
# --------------------------------------------------

LOW_RISK_THRESHOLD = 0.30
MEDIUM_RISK_THRESHOLD = 0.50
HIGH_RISK_THRESHOLD = 0.70

# --------------------------------------------------
# Alert Messages
# --------------------------------------------------

ALERT_STABLE = (
    "Stable hospital conditions."
)

ALERT_WARNING = (
    "Moderate increase in patient load expected."
)

ALERT_SURGE = (
    "Emergency admissions likely to increase significantly."
)

# --------------------------------------------------
# Synthetic Data Generation
# --------------------------------------------------

DEFAULT_DAYS = 30

HOURS_PER_DAY = 24

PATIENT_GENERATION_INTERVAL_MINUTES = 15

# --------------------------------------------------
# Stream Simulator
# --------------------------------------------------

STREAM_INTERVAL_SECONDS = 2

MAX_EVENT_HISTORY = 500

# --------------------------------------------------
# XGBoost Model
# --------------------------------------------------

MODEL_PATH = "models/xgb_model.pkl"

TARGET_COLUMN = "surge"

FEATURE_COLUMNS = [
    "er",
    "icu",
    "general",
    "hour",
    "dayofweek",
    "rolling_er",
    "rolling_total"
]

# --------------------------------------------------
# Dashboard
# --------------------------------------------------

DASHBOARD_TITLE = (
    "🏥 Hospital AI Digital Twin"
)

PAGE_ICON = "🏥"

REFRESH_RATE_SECONDS = 2

# --------------------------------------------------
# Optional vLLM
# --------------------------------------------------

VLLM_MODEL = (
    "mistralai/Mistral-7B-Instruct-v0.2"
)

MAX_LLM_TOKENS = 100

# --------------------------------------------------
# Emergency Surge Simulation
# --------------------------------------------------

SURGE_MULTIPLIER = 1.3

WEEKEND_MULTIPLIER = 1.2

NIGHT_SHIFT_MULTIPLIER = 1.5

# --------------------------------------------------
# Logging
# --------------------------------------------------

LOG_LEVEL = "INFO"

LOG_FILE = "hospital_twin.log"
