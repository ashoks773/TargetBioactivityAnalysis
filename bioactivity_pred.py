#!pip3 install flask
from flask import Flask, render_template, request
import pandas as pd
from rdkit import Chem
from rdkit.ML.Descriptors import MoleculeDescriptors
from rdkit.Chem import Descriptors
import joblib  # For loading your trained model
import numpy as np

app = Flask(__name__)

# Load your pre-trained QSAR model
model_path = "/Users/ashoksharma/Work/Python_bioinfo/Disease_target/models/TNFalpha_QSAR_model.pkl"  # Update with your model path
best_model = joblib.load(model_path)

# Select the molecular descriptors to compute
descriptor_names = [desc[0] for desc in Descriptors._descList]
calculator = MoleculeDescriptors.MolecularDescriptorCalculator(descriptor_names)

# Function to calculate descriptors for each molecule
def calculate_descriptors(mol):
    if mol is not None:
        return calculator.CalcDescriptors(mol)
    else:
        # Handle invalid SMILES
        return [None] * len(descriptor_names)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        smiles = request.form.get('smiles')
        
        # Handle CSV file upload and SMILES input
        if file:
            df = pd.read_csv(file)
            # Assuming 'canonical_smiles' column exists in the CSV
            df['mol'] = df['canonical_smiles'].apply(Chem.MolFromSmiles)
            df['descriptors'] = df['mol'].apply(calculate_descriptors)
            descriptors_df = pd.DataFrame(df['descriptors'].tolist(), columns=descriptor_names)
            predictions = best_model.predict(descriptors_df)
            df['predicted_pIC50'] = predictions
            prediction_results = df[['canonical_smiles', 'predicted_pIC50']].to_html(index=False)
        elif smiles:
            mol = Chem.MolFromSmiles(smiles)
            descriptors = calculate_descriptors(mol)
            prediction = best_model.predict([descriptors])
            prediction_results = f"<p>SMILES: {smiles}</p><p>Predicted pIC50: {prediction[0]}</p>"
        else:
            prediction_results = "No input provided"
        
        return render_template('prediction.html', prediction_results=prediction_results)

if __name__ == '__main__':
    app.run(debug=True)
