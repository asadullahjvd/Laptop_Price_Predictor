import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load("random_forest_model.joblib")
X_columns = list(model.feature_names_in_)

st.title("💻 Laptop Price Predictor")

companies = ["Apple", "Asus", "Chuwi", "Dell", "Fujitsu", "Google", "HP", "Huawei",
             "LG", "Lenovo", "MSI", "Mediacom", "Microsoft", "Razer", "Samsung",
             "Toshiba", "Vero", "Xiaomi"]
types = ["Gaming", "Netbook", "Notebook", "Ultrabook", "Workstation"]
cpus = ["Intel Core i3", "Intel Core i5", "Intel Core i7", "Other Intel Processor"]
gpus = ["Intel", "Nvidia"]
os_options = ["Windows", "Others/No OS/Linux"]

company   = st.selectbox("Company", companies)
typename  = st.selectbox("Type", types)
cpu       = st.selectbox("CPU", cpus)
gpu       = st.selectbox("GPU", gpus)
os_choice = st.selectbox("OS", os_options)

ram         = st.selectbox("RAM (GB)", [4, 8, 16, 32, 64])
weight      = st.number_input("Weight (kg)", 0.5, 5.0, 2.0)
touchscreen = st.selectbox("Touchscreen", [0, 1])
ips         = st.selectbox("IPS Display", [0, 1])
ppi         = st.number_input("PPI", 100.0, 400.0, 150.0)
hdd         = st.selectbox("HDD (GB)", [0, 256, 512, 1000, 2000])
ssd         = st.selectbox("SSD (GB)", [0, 128, 256, 512, 1000])

if st.button("Predict Price"):
    input_df = pd.DataFrame(np.zeros((1, len(X_columns))), columns=X_columns)

    input_df["Ram"]         = ram
    input_df["Weight"]      = weight
    input_df["Touchscreen"] = touchscreen
    input_df["IPS"]         = ips
    input_df["PPI"]         = ppi
    input_df["HDD"]         = hdd
    input_df["SSD"]         = ssd

    input_df[f"Company_{company}"]                        = 1
    input_df[f"TypeName_{typename}"]                      = 1
    input_df[f"Cpu_brand_{cpu.replace(' ', '_')}"]        = 1
    input_df[f"Gpu_brand_{gpu}"]                          = 1

    if os_choice == "Windows":
        input_df["OS_Windows"] = 1
    else:
        input_df["OS_Others/No_OS/Linux"] = 1

    log_prediction = model.predict(input_df)[0]
    price = int(np.exp(log_prediction))
    st.success(f"💰 Estimated Laptop Price: **Rs. {price:,}**")
