# TargetBioactivityAnalysis! :shipit:
Welcome to the Bioactivity Data Pipeline repository! This collection of scripts is designed to help you obtain bioactivity data for multiple targets and compute molecular properties to understand the associations between these properties and compound activity.

## Requirements :crossed_fingers:
> [!TIP]
> Start working with Google Colab or Jupyter Notebook! 
> * First, install the following packages using pip3 or pip:
`chembl_webresource_client`
`pandas`
`rdkit`
`numpy`
`matplotlib`
`seaborn`
`scipy`
`scikit-learn`
`lazypredict`
`keras`
`tensorflow`
`flask'
> * Get PaDEL-Descriptor file: wget https://github.com/dataprofessor/bioinformatics/raw/master/padel.zip to compute Descriptors

## Steps :writing_hand:
> [!NOTE]
> ## The pipeline has been divided into multiple steps
> * **Step1:** Use **<span style="color:blue">Step1_Get_BioactivityData.ipynb</span>** script to get the Bioactivity data IC50 (standard values) for each molecule of the respective target.
> * **Step2:** Use **<span style="color:blue">Step2_TargetSpecificExploratory_Analysis.ipynb</span>** script
> ** to compute molecular properties of the compounds for the target of interest (ex: TNF-alpha).
> ** to check the distribution of these properties across compound activities
> ** to convert IC50 standard values to pIC50 and then association of pIC50 with different properties
> * **Step3:** Use **<span style="color:blue">Step3_Descriptors_Bioactivity_Association.ipynb</span>** script
> ** to compute Descriptors and Fingerprints of each compound.
> ** Exploratory analysis including **PCA** and **tSNE** to check how well the top features separate the classes.
> ** Feature Importance Analysis; Classification for performance assessment and SHAP Analysis to interpret model predictions and understand feature contributions using SHAP values.
> * **Step4:** use **<span style="color:blue">Step4_TNF-alpha_QSARmodel.ipynb</span>** script to generate QSAR model. Check the model's performance on the external dataset and then save the final model to be used by the **bioactivity_pred.py**!!

# Run Bioactivity App
Before running the Bioactivity app. Make sure you have all packages installed. The final model **TNFalpha_QSAR_model.pkl**  is saved in the model's folder. Make sure to change the location of the model in the bioactivity_pred.py file. To run the bioactivity code, download and organize the folders as provided below
### To run the local bioactivity prediction web server.
``` r
python3.12 bioactivity_pred.py

/your_project_directory
├── bioactivity_pred.py
├── templates
│ ├── index.html
│ └── prediction.html
├── models
│ ├── TNFalpha_QSAR_model.pkl
```

## Contact: :raised_back_of_hand:
> [!IMPORTANT]
> For any questions please contact: :point_right: Ashok K. Sharma; ashoks773@gmail.com 
