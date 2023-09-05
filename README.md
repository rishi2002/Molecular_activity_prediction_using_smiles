# Molecular_activity_prediction_using_smiles
I use pytorch GRU for predicting molecular bioactivity on the Dopamine D2 receptor, which is affected by Parkinson's disease.
## Introduction
According to the WHO, 8.5 million individuals were suffering from the disease Parkinson’s disease
as of 2019. Hence, I have chosen Parkinson's disease, specifically the Dopamine D2 receptor, as
my target molecule, and predicted the bioactivity and solubility of various biomolecules to the
Dopamine D2 receptor. I have tested and compared two regression models, one deep-learning based
and another based on conventional machine learning, and trained them on data from the ChEMBL
database.
Prediction of bioactivity and solubility of biomolecules is a necessary and crucial step in the De
Novo Drug design problem. It is required to predict the efficacy of a drug, it is also necessary to
predict other properties like toxicity, stability, specificity, etc. While this does not solve the
problem, efficient prediction of toxicity and solubility of biomolecules can significantly streamline
the process of De Novo Drug design.
## Models
+ GRU
+ Linear Regression
## Data
I collected the data from the ChEMBL database. I one-hot encoded the SMILES strings to use them as features for the models.

