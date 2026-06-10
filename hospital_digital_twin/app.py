import streamlit as st
import time
import pandas as pd
from simulator.digital_twin import HospitalTwin
from ml.predict import predict_surge

st.set_page_config(page_title="Hospital AI Digital Twin")

st.title("🏥 Hospital AI Digital Twin")

twin = HospitalTwin()

placeholder = st.empty()

for i in range(50):

    state = twin.step()

    features = [
        state["er"],
        state["icu"],
        state["general"],
        time.localtime().tm_hour,
        time.localtime().tm_wday,
        state["er"],
        state["total"]
    ]

    risk = predict_surge(features)

    with placeholder.container():

        st.metric("ER Patients", state["er"])
        st.metric("ICU Patients", state["icu"])
        st.metric("General Ward", state["general"])
        st.metric("Total Load", state["total"])

        st.metric("🚨 Surge Risk", f"{risk*100:.2f}%")

        if risk > 0.7:
            st.error("⚠ Emergency admissions likely to increase significantly!")
        elif risk > 0.4:
            st.warning("Moderate load expected")
        else:
            st.success("Stable hospital conditions")

    time.sleep(1)
