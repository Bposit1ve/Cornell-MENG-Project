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
    custom_smiles = st.text_input('Enter your custom SMILES string', help="Press Enter to Render Molecule")

# update smiles string
active_smiles = custom_smiles if custom_smiles else compound_smiles


if active_smiles:
    # Text illustration and rendering for 3D molecule
    st.markdown("### Molecule Structure")
    st.markdown("Below is the 3D structure of the molecule:")
    mol = mol_helper.makeblock(active_smiles)
    mol_helper.render_mol_stick(mol)

    # Text illustration and rendering for 2D molecule
    st.markdown("Below is the 2D structure of the molecule:")
    img = mol_helper.render_mol_2d(active_smiles)
    st.image(img)
