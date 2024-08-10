# TargetBioactivityAnalysis! :shipit:
Welcome to the Bioactivity Data Pipeline repository! This collection of scripts is designed to help you obtain bioactivity data for multiple targets and compute molecular properties to understand the associations between these properties and compound activity.

# Requirements :+1:
> [!IMPORTANT]
> Start working with Google Colab or Jupyter Notebook
> You need to install the following packages:
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
You can install these packages using pip3 or pip:
> Get PaDEL-Descriptor file: wget https://github.com/dataprofessor/bioinformatics/raw/master/padel.zip to compute Descriptors

### The pipeline has been divided into multiple steps
*Step1* Use <code style="color: gold">Step1_Get_BioactivityData.ipynb</code> script to get the Bioactivity data IC50 (standard values) for each molecule of the respective target
*Step2* 
