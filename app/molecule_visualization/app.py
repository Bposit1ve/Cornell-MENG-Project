# Import necessary libraries
import streamlit as st
from src import helper as mol_helper

# Streamlit app title
st.title('Molecule Visualization (SMILES)')

# Update the list to include 'customize' option
smiles_options = mol_helper.smiles_options + ['customize']
compound_smiles = st.selectbox('Select a SMILES string', smiles_options, help="Select a predefined molecule or customize your own.")

# text_input bar for customize situation
custom_smiles = ""
if compound_smiles == 'customize':
    custom_smiles = st.text_input('Enter your custom SMILES string', help="Use uppercase letters")

# update smiles string
active_smiles = custom_smiles if custom_smiles else compound_smiles


if active_smiles:
    # Render the molecule
    mol_helper.render_3d(active_smiles)
    mol_helper.render_2d(active_smiles)