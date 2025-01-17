# EPA Categories

The files in this repository can be used to identify membership in the EPA New Chemical Categories (NCC) for chemicals of interest using the NCC profiler as implemented in the OECD QSAR Toolbox v4.6. This README outlines how to use the functions provided herein, including how to set up a repository for use, format inputs, and apply functions. 

## Repository Setup

The package ncc_categories can be used as a standalone module or installed in a Python instance or virtual environment. 

### Stand-alone Module

In order to use this code as a standalone module, the file and folder structure must be preserved for  [data/raw/epa_categories.xml](data/raw/epa_categories.xml) and [categories.py](categories.py). Thus, there should be a folder with the following contents:

        ├── categories.py
        ├──data
        │   └── raw
        │       └── epa_categories.xml

Running the following in any script or notebook located in the same folder as categories.py will give direct access to the main user functions for categorizing chemicals:

``` python
from categories import queryAll, listCategories, singleQuery, printTree
```
For files in folders other than that containing categories.py, the user need only adjust the file path in front of 'categories' in the above code. 

### Local Installation

To install the package in a Python instance or virtual environment, you will need to save the folder [package_builder/](package_builder/) and its contents on your machine. Then, you will run the following code with the desired instance or virtual environment activated:

``` 
pip install <path/to/package_builder>/package_builder/.
```

## Input Format

The classification methods used in this set use DSSTOX_SID, Log Kow, Molecular Weight, SMILES, Water Solubility,and RDkit.Mol to determine category membership. Classification functions will require all of this information for each chemical of interest. The key/column names for each of these categories are as follows:

- DSSTOX_SID: 'dsstox_sid'
- Log Kow: 'logp'
- Molecular Weight: 'mol_weight'
- RDKit.Mol: 'mol'
- SMILES: 'smiles'
- Water Solubility: 'ws', *If using predictions from OPERA, these are provided in units as mol/L but the category definitions as implemented in the Toolbox rely on units of mg/L (unlike the original category definitions which used units of ug/L). Current code will assign categories based on mg/L inputs.

Chemicals can be provided as a DataFrame containing these columns, a dictionary containing each of these keys, or a list of dictionaries, each with all of the required keys. In addition, there are built-in error and input checks to warn users if the input type is incompatible with the desired function. 

### Input examples:

```python
from rdkit import Chem
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
Note: catgeories.py and ncc_categories.py include code that parses the original QSAR Toolbox XML in order to create many of the tests for the EPA categories. To this end, there are many functions defined in the script that are not particularly meant for general use, and instead allow for parsing of XML and organisation of tests and queries. This section will focus on the functions that allow users to match chemicals to categories and to obtain information about those categories.

### Code Structure Information
categories.py defines a Query class. Instances of the Query class correspond to the different available categories. These instances are stored by category key in the dictionary all_tests. Each instance has a .query attribute, which can be applied to an individual chemical in order to obtain a boolean value for whether the given chemical belongs in the specified category. Most queries were built directly from the parsed XML, but some categories required hard-coding of the query tests due to corrupted SMARTS in the XML. These hard-coded categories are italicised in the category list below. 

### Function Definitions
- [**singleQuery**](https://github.com/laxleary/EPA_Categories/blob/e98e68724a4955ba5571faa06a1c806f8ae0aa34/categories.py#L1037): A quick method for determining whether a chemical belongs in a specific category.

    - Inputs: 
      - *one_chem*, individual Chemical, provided as a dictionary or DataFrame slice with the keys/columns speficied above. 
      - *category_title*, String representing a category title. Possibilities listed below.
    - Output: *boolean*, value specifies whether x is in Category Title or not

- [**printTree**](https://github.com/laxleary/EPA_Categories/blob/e98e68724a4955ba5571faa06a1c806f8ae0aa34/categories.py#L1059): Allows the user to view the testing process for determining whether a chemical belongs in a specific category. Can be run with or without a chemical input.

    - Inputs: 
      - *one_chem*, Default value of x is None but an individual chemical can also be supplied with the same
    constraints as in singleQuery 
      - *category_title*, String representing a category title. Possibilities listed below.
      - *printer*, Boolean with default value True. If True, then this result will be output to the console as
      a print statement. If False, nothing will be printed and the result will instead be a string variable.
    - Output: *printed logic tree*, Each line of the logic tree will contain the query type and all necessary parameters. If data is provided for x, the last value of each line will contain the boolean value for whether x fulfills that piece of the query. 
        - For the XML-originating queries, the first value will be the query ID identifying the query in the XML document. 
        - For hard-coded queries, the first value will instead say CustomQuery and all lines after the first will terminate with "does not process", since the functions for all subqueries are contained within the top branch of the tree only.

If you wish to store the entire set of logical trees for all chemical categories, add categories.all_tests to your imports and run the following code:

```python
the_test_dictionary = {}
for key in all_tests.keys():
    the_test_dictionary[key] = printTree(key,None, printer = False)
```
Now, the variable the_test_dictionary stores strings representing the tests required for classifying chemicals into each category, stored by category title.

- [**queryAll**](https://github.com/laxleary/EPA_Categories/blob/689642cd346f8ae27deaa3df7723742bb4083f3d/categories.py#L988): Given a set of chemical(s), returns a DataFrame containing one column for chemical DSSTOXSIDs and individual columns for every category included in all_tests. These columns will contain boolean values, thus describing category membership for the chemical set in a fingerprint-like way. 

    - Inputs: 
      - *chemicals*, A DataFrame, Dictionary, or list of Dictionaries of Chemicals and their attributes, including dsstox_sid, smiles, logp, ws, mol_weight, and RDKIT MolfromSmiles (labelled as 'mol'). There must be keys or column names to match each of these attribute titles.
      - *boolean_outputs*, Default value is False. This function will, by default, output category_df with binary values descripbing category membership. If desired, this matrix can instead be output with boolean values by setting boolean_outputs to True. 
    
    - Output: *category_df*, A DataFrame of chemicals and their category memberships, with an example depicted below:

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>chemicals</th>
      <th>Acid Chlorides</th>
      <th>Acrylamides</th>
      <th>Acrylates/Methacrylates (Acute toxicity)</th>
      <th>Aldehydes (Acute toxicity)</th>
      <th>Aliphatic Amines</th>
      <th>Aluminum Compounds</th>
      <th>Anilines (Acute toxicity)</th>
      <th>Azides (Acute toxicity)</th>
      <th>Benzotriazoles (Acute toxicity)</th>
      <th>...</th>
      <th>Organotins (Chronic toxicity)</th>
      <th>Phenols (Chronic toxicity)</th>
      <th>Phosphinate Esters (Chronic toxicity)</th>
      <th>Polynitroaromatics (Chronic toxicity)</th>
      <th>Substituted Triazines (Chronic toxicity)</th>
      <th>Thiols (Chronic toxicity)</th>
      <th>Vinyl Esters (Chronic toxicity)</th>
      <th>Diazoniums (Chronic toxicity)</th>
      <th>Ethylene Glycol Ethers</th>
      <th>Benzotriazoles</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>DTXSID90480751</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DTXSID50939730</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>DTXSID2036405</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>DTXSID1024835</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>DTXSID30878870</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 67 columns</p>
</div>

- [**listCategories**](https://github.com/laxleary/EPA_Categories/blob/689642cd346f8ae27deaa3df7723742bb4083f3d/categories.py#L1018): Given an individual chemical, this function outputs a list of all categories to which the chemical belongs. 

    - Input: *one_chem*, A DataFrame or Dictionary representing a single chemical and its attributes, including dsstox_sid, smiles, logp, ws, mol_weight, and RDKIT MolfromSmiles (labelled as 'mol'). There must be keys or column names to match each of these attribute titles. 
    - Output: *all_cats*, A list of all categories to which the chemical belongs according to the included tests. 


### Included Categories
- Acid Chlorides
- *Acrylamides*
- *Acrylates/Methacrylates (Acute toxicity)*
- *Acrylates/Methacrylates (Chronic toxicity)*
- *Aldehydes (Acute toxicity)*
- *Aldehydes (Chronic toxicity)*
- *Aliphatic Amines*
- *Alkoxysilanes*
- Aluminum Compounds
- *Aminobenzothiazole Azo Dyes*
- Anhydrides, Carboxylic acid
- Anilines (Acute toxicity)
- Anilines (Chronic toxicity)
- *Anionic Surfactants*
- Azides (Acute toxicity)
- Azides (Chronic toxicity)
- Benzotriazole-hindered phenols
- Benzotriazoles (Acute toxicity)
- Benzotriazoles (Chronic toxicity)
- Boron Compounds
- Cationic (quaternary ammonium) surfactants
- Cobalt
- *Dianilines*
- Diazoniums (Acute toxicity)
- Diazoniums (Chronic toxicity)
- Dichlorobenzidine-based Pigments
- Diisocyanates
- *Dithiocarbamates (Acute toxicity)*
- *Dithiocarbamates (Chronic toxicity)*
- *Epoxides*
- Esters (Acute toxicity)
- Esters (Chronic toxicity)
- *Ethylene Glycol Ethers*
- Hindered Amines
- *Hydrazines and Related Compounds*
- *Imides (Acute toxicity)*
- *Imides (Chronic toxicity)*
- Lanthanides or Rare Earth Metals
- *Neutral Organics*
- Nickel Compounds
- *Nonionic Surfactants*
- *Organotins (Acute toxicity)*
- *Organotins (Chronic toxicity)*
- Peroxides
- Phenolphthaleins
- Phenols (Acute toxicity)
- Phenols (Chronic toxicity)
- Phosphates, Inorganic
- Phosphinate Esters (Acute toxicity)
- Phosphinate Esters (Chronic toxicity)
- *Polynitroaromatics (Acute toxicity)*
- *Polynitroaromatics (Chronic toxicity)*
- Rosin
- Soluble complexes of Zinc
- Stilbene, derivatives of 4,4-bis(triazin-2-ylamino)-
- *Substituted Triazines (Acute toxicity)*
- *Substituted Triazines (Chronic toxicity)*
- *Thiols (Acute toxicity)*
- *Thiols (Chronic toxicity)*
- *Triarylmethane Pigments/Dyes with Non-solubilizing Groups*
- Vinyl Esters (Acute toxicity)
- Vinyl Esters (Chronic toxicity)
- Vinyl Sulfones
- Zirconium Compounds
- *beta-Naphthylamines, Sulfonated*


