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
> * **Step1** Use <code style="color : gold">Step1_Get_BioactivityData.ipynb</code> script to get the Bioactivity data IC50 (standard values) for each molecule of the respective target
> * **Step2**
