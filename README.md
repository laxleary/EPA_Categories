# EPA Categories

The files in this repository can be used to identify membership in the EPA Categories provided from the OECD 2010 QSAR Toolbox 2.0 for chemicals of interest. This README outlines how to use the functions provided herein, including how to set up a repository for use, format inputs, and apply functions.

## Repository Setup

In order to use this code in an independent repository, the file and folder structure must be preserved for  [data/raw/epa_categories.xml](data/raw/epa_categories.xml) and [categories.py](categories.py). Thus, there should be a folder with the following contents:

        ├── categories.py
        ├──data
        │   └── raw
        │       └── epa_categories.xml


## Input Format

The classification methods used in this set use DSSTOX_SID, , Log Kow, Molecular Weight, SMILES, Water Solubility,and RDkit.Mol to determine category membership. Classification functions will require all of this information for each chemical of interest. The key/column names for each of these categories are as follows:

- DSSTOX_SID: 'dsstox_sid'
- Log Kow: 'logp'
- Molecular Weight: 'mol_weight'
- RDKit.Mol: 'mol'
- SMILES: 'smiles'
- Water Solubility: 'ws'

Chemicals can be provided as a DataFrame containing these columns, a dictionary containing each of these keys, or a list of dictionaries, each with all of the required keys. In addition, there are built-in error and input checks to warn users if the input type is incompatible with the desired function. 

### Input examples:

```python
import rdkit as Chem
import pandas as pd

# Single-chemical Dictionary
test_chem = {'dsstox_sid': 'DTXSID7020009',
                'smiles': 'CC#N',
                'logp': -0.33971,
                'ws': 12.6417,
                'mol_weight': 41.053,
                'mol': Chem.MolFromSmiles('CC#N')}

# Multi-chemical list of Dictionaries
new_test_chems = [{'dsstox_sid': 'DTXSID3060164',
  'smiles': 'C1=CC=CC=C1C(C1C=CC=CC=1)C1C=CC=CC=1',
  'logp': 5.76,
  'ws': 4.07380277804113e-07,
  'mol_weight': 244.125200512,
  'mol': Chem.MolFromSmiles('C1=CC=CC=C1C(C1C=CC=CC=1)C1C=CC=CC=1')},
 {'dsstox_sid': 'DTXSID7060837',
  'smiles': 'ICCCI',
  'logp': 3.02,
  'ws': 0.0007413102413009177,
  'mol_weight': 295.855896192,
  'mol': Chem.MolFromSmiles('ICCCI')},
 {'dsstox_sid': 'DTXSID9025879',
  'smiles': 'OC(=O)C=CC1C=CC(C=CC(O)=O)=CC=1',
  'logp': 1.99,
  'ws': 0.009120108393559097,
  'mol_weight': 218.0579088,
  'mol': Chem.MolFromSmiles('OC(=O)C=CC1C=CC(C=CC(O)=O)=CC=1')}]

# Multi-chemical Dictionary
test_chems_together = {'dsstox_sid': ['DTXSID3060164','DTXSID7060837'],
  'smiles': ['C1=CC=CC=C1C(C1C=CC=CC=1)C1C=CC=CC=1','ICCCI'],
  'logp': [5.76,3.02],
  'ws': [4.07380277804113e-07,0.0007413102413009177],
  'mol_weight': [244.125200512,295.855896192],
  'mol': [Chem.MolFromSmiles('C1=CC=CC=C1C(C1C=CC=CC=1)C1C=CC=CC=1'),Chem.MolFromSmiles('ICCCI')]}

#Note that the 'mol' attribute can be easily calculated using RDKit with the 'smiles' attribute, so initial data imports likely will not have the 'mol' attribute and instead should be modified as necessary to prep for function use. This process is shown in the final input example below.

# DataFrame
test_chems_df = pd.read_csv('data/raw/readme_examples.csv').set_index('Unnamed: 0', drop = True)
test_chems_df['mols'] = [Chem.MolFromSmiles(smile) for smile in test_chems_df['smiles']]

 
```

## User-Focused Functions
Note: catgeories.py includes code that parses the original QSAR Toolbox XML in order to create many of the tests for the EPA categories. To this end, there are many functions defined in the script that are not particularly meant for general use, and instead allow for parsing of XML and organization of tests and queries. This section will focus on the functions that allow users to match chemicals to categories and to obtain information about those categories. 