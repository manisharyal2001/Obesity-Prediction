import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the label encoder for the target variable
label_encoder = LabelEncoder()
label_encoder.classes_ = pd.read_pickle('label_encoder')

# Load the saved model
best_model = joblib.load('trained_model')


def predict_obesity():
    # Get user input
    gender = gender_var.get()
    age = float(age_entry.get())
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    family_history = family_history_var.get()
    favc = favc_var.get()
    fcvc = float(fcvc_entry.get())
    ncp = float(ncp_entry.get())
    caec = caec_var.get()
    smoke = smoke_var.get()
    ch2o = float(ch2o_entry.get())
    scc = scc_var.get()
    faf = float(faf_entry.get())
    tue = float(tue_entry.get())
    calc = calc_var.get()
    mtrans = mtrans_var.get()

    # Prepare input data
    data = pd.DataFrame({
        'Gender': [gender],
        'Age': [age],
        'Height': [height],
        'Weight': [weight],
        'family_history_with_overweight': [family_history],
        'FAVC': [favc],
        'FCVC': [fcvc],
        'NCP': [ncp],
        'CAEC': [caec],
        'SMOKE': [smoke],
        'CH2O': [ch2o],
        'SCC': [scc],
        'FAF': [faf],
        'TUE': [tue],
        'CALC': [calc],
        'MTRANS': [mtrans]
    })

    # Make prediction using the loaded model
    prediction = best_model.predict(data)
    result_label.config(text="Predicted obesity level: {}".format(
        label_encoder.inverse_transform(prediction)[0]))


# Create GUI
root = tk.Tk()
root.title("Obesity Prediction")

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Create input fields for numerical columns
ttk.Label(mainframe, text="Gender:").grid(column=1, row=1, sticky=tk.W)
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(
    mainframe, width=15, textvariable=gender_var, values=['Male', 'Female'])
gender_combobox.grid(column=2, row=1, sticky=tk.W)

ttk.Label(mainframe, text="Age:").grid(column=1, row=2, sticky=tk.W)
age_entry = ttk.Entry(mainframe, width=15)
age_entry.grid(column=2, row=2, sticky=tk.W)

ttk.Label(mainframe, text="Height in Meters:").grid(
    column=1, row=3, sticky=tk.W)
height_entry = ttk.Entry(mainframe, width=15)
height_entry.grid(column=2, row=3, sticky=tk.W)

ttk.Label(mainframe, text="Weight in KG:").grid(column=1, row=4, sticky=tk.W)
weight_entry = ttk.Entry(mainframe, width=15)
weight_entry.grid(column=2, row=4, sticky=tk.W)

ttk.Label(mainframe, text="family_history_with_overweight:").grid(
    column=1, row=5, sticky=tk.W)
family_history_var = tk.StringVar()
family_history_combobox = ttk.Combobox(
    mainframe, width=15, textvariable=family_history_var, values=['yes', 'no'])
family_history_combobox.grid(column=2, row=5, sticky=tk.W)

ttk.Label(mainframe, text="FAVC:").grid(column=1, row=6, sticky=tk.W)
favc_var = tk.StringVar()
favc_combobox = ttk.Combobox(
    mainframe, width=15, textvariable=favc_var, values=['yes', 'no'])
favc_combobox.grid(column=2, row=6, sticky=tk.W)

ttk.Label(mainframe, text="FCVC:").grid(column=1, row=7, sticky=tk.W)
fcvc_entry = ttk.Entry(mainframe, width=15)
fcvc_entry.grid(column=2, row=7, sticky=tk.W)

ttk.Label(mainframe, text="NCP:").grid(column=1, row=8, sticky=tk.W)
ncp_entry = ttk.Entry(mainframe, width=15)
ncp_entry.grid(column=2, row=8, sticky=tk.W)

ttk.Label(mainframe, text="CAEC:").grid(column=1, row=9, sticky=tk.W)
caec_var = tk.StringVar()
caec_combobox = ttk.Combobox(mainframe, width=15, textvariable=caec_var, values=[
                             'no', 'Sometimes', 'Frequently', 'Always'])
caec_combobox.grid(column=2, row=9, sticky=tk.W)

ttk.Label(mainframe, text="Smoke:").grid(column=1, row=10, sticky=tk.W)
smoke_var = tk.StringVar()
smoke_combobox = ttk.Combobox(
    mainframe, width=15, textvariable=smoke_var, values=['no', 'yes'])
smoke_combobox.grid(column=2, row=10, sticky=tk.W)

ttk.Label(mainframe, text="CH2O:").grid(column=1, row=11, sticky=tk.W)
ch2o_entry = ttk.Entry(mainframe, width=15)
ch2o_entry.grid(column=2, row=11, sticky=tk.W)

ttk.Label(mainframe, text="SCC:").grid(column=1, row=12, sticky=tk.W)
scc_var = tk.StringVar()
scc_combobox = ttk.Combobox(
    mainframe, width=15, textvariable=scc_var, values=['no', 'yes'])
scc_combobox.grid(column=2, row=12, sticky=tk.W)

ttk.Label(mainframe, text="FAF:").grid(column=1, row=13, sticky=tk.W)
faf_entry = ttk.Entry(mainframe, width=15)
faf_entry.grid(column=2, row=13, sticky=tk.W)

ttk.Label(mainframe, text="TUE:").grid(column=1, row=14, sticky=tk.W)
tue_entry = ttk.Entry(mainframe, width=15)
tue_entry.grid(column=2, row=14, sticky=tk.W)

ttk.Label(mainframe, text="CALC:").grid(column=1, row=15, sticky=tk.W)
calc_var = tk.StringVar()
calc_combobox = ttk.Combobox(mainframe, width=15, textvariable=calc_var, values=[
                             'no', 'Sometimes', 'Frequently', 'Always'])
calc_combobox.grid(column=2, row=15, sticky=tk.W)

ttk.Label(mainframe, text="MTRANS:").grid(column=1, row=16, sticky=tk.W)
mtrans_var = tk.StringVar()
mtrans_combobox = ttk.Combobox(mainframe, width=15, textvariable=mtrans_var, values=[
                               'Automobile', 'Bike', 'Motorbike', 'Public_Transportation', 'Walking'])
mtrans_combobox.grid(column=2, row=16, sticky=tk.W)

# Add a button to make prediction
ttk.Button(mainframe, text="Predict", command=predict_obesity).grid(
    column=2, row=17, sticky=tk.W)

# Add label to display result
result_label = ttk.Label(mainframe, text="")
result_label.grid(column=1, row=18, columnspan=2, sticky=tk.W)

root.mainloop()
