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
> * Get PaDEL-Descriptor file: wget https://github.com/dataprofessor/bioinformatics/raw/master/padel.zip to compute Descriptors

## Steps :writing_hand:
> [!NOTE]
> ## The pipeline has been divided into multiple steps
> * **Step1:** Use **<span style="color:blue">Step1_Get_BioactivityData.ipynb</span>** script to get the Bioactivity data IC50 (standard values) for each molecule of the respective target.
> * **Step2:** Use **<span style="color:blue">Step2_TargetSpecificExploratory_Analysis.ipynb</span>** script
> ** to compute molecular properties of the compounds for the target of interest (ex: TNF-alpha).
> ** to check the distribution of these properties across compound activities
> ** to convert IC50 standard values to pIC50 and then association of pIC50 with different properties

## Contact: :raised_back_of_hand:
> [!IMPORTANT]
> For any questions please contact: :point_right: Ashok K. Sharma; ashoks773@gmail.com 
