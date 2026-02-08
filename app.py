from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("random_forest_model.joblib")

# Get actual feature names from the model
X_columns = list(model.feature_name_)

# Dropdown options (extracted from feature names)
companies = ["Apple", "Asus", "Chuwi", "Dell", "Fujitsu", "Google", "HP", "Huawei", 
             "LG", "Lenovo", "MSI", "Mediacom", "Microsoft", "Razer", "Samsung", 
             "Toshiba", "Vero", "Xiaomi"]
types = ["Gaming", "Netbook", "Notebook", "Ultrabook", "Workstation"]
cpus = ["Intel Core i3", "Intel Core i5", "Intel Core i7", "Other Intel Processor"]
gpus = ["Intel", "Nvidia"]
os_options = ["Windows", "Others/No OS/Linux"]

@app.route("/", methods=["GET", "POST"])
def index():
    price = None

    if request.method == "POST":
        # Get dropdown values
        company = request.form["company"]
        cpu = request.form["cpu"]
        gpu = request.form["gpu"]
        typename = request.form["typename"]
        os_choice = request.form["os"]

        # Numeric inputs
        ram = int(request.form["ram"])
        weight = float(request.form["weight"])
        touchscreen = int(request.form["touchscreen"])
        ips = int(request.form["ips"])
        ppi = float(request.form["ppi"])
        hdd = int(request.form["hdd"])
        ssd = int(request.form["ssd"])

        # Create empty input dataframe with all features as 0
        input_df = pd.DataFrame(np.zeros((1, len(X_columns))), columns=X_columns)

        # Fill numerical features in the exact order expected by model
        input_df["Ram"] = ram
        input_df["Weight"] = weight
        input_df["Touchscreen"] = touchscreen
        input_df["IPS"] = ips
        input_df["PPI"] = ppi
        input_df["HDD"] = hdd
        input_df["SSD"] = ssd

        # One-hot encoding for categorical features
        input_df[f"Company_{company}"] = 1
        input_df[f"TypeName_{typename}"] = 1
        input_df[f"Cpu_brand_{cpu.replace(' ', '_')}"] = 1
        input_df[f"Gpu_brand_{gpu}"] = 1
        
        # Handle OS feature (special case due to slashes in feature name)
        if os_choice == "Windows":
            input_df["OS_Windows"] = 1
        else:
            input_df["OS_Others/No_OS/Linux"] = 1

        # Predict (model output is log(price), so apply exp to get actual price)
        log_prediction = model.predict(input_df)[0]
        price = int(np.exp(log_prediction))

    return render_template(
        "index.html",
        price=price,
        companies=companies,
        cpus=cpus,
        gpus=gpus,
        types=types,
        os_options=os_options
    )

if __name__ == "__main__":
    app.run(debug=True)
