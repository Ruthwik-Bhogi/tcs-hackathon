import numpy as np
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

departments = ["ER", "ICU", "GENERAL_WARD"]

def generate_hospital_data(n_days=7, freq_per_hour=10):
    data = []

    base_time = datetime.now() - timedelta(days=n_days)

    for i in range(n_days * 24 * freq_per_hour):
        timestamp = base_time + timedelta(minutes=6*i)

        hour = timestamp.hour

        # realistic patterns:
        # ER spikes at night & weekends
        er_factor = 1.5 if hour >= 18 or hour <= 6 else 1.0

        # ICU depends on ER lag
        icu_factor = random.uniform(0.8, 1.2)

        # General ward steady
        gw_factor = 1.0

        er_patients = int(np.random.poisson(5 * er_factor))
        icu_patients = int(np.random.poisson(2 * icu_factor))
        gw_patients = int(np.random.poisson(8 * gw_factor))

        emergency_surge = er_patients > 10

        data.append([
            timestamp,
            er_patients,
            icu_patients,
            gw_patients,
            emergency_surge
        ])

    df = pd.DataFrame(data, columns=[
        "timestamp", "er", "icu", "general", "surge"
    ])

    return df


if __name__ == "__main__":
    df = generate_hospital_data()
    df.to_csv("data/hospital.csv", index=False)
    print("Synthetic hospital data generated.")
