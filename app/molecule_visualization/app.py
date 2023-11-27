import streamlit as st
from src import helper as mol_helper

st.set_page_config(layout="wide")

st.title('Molecule Visualization (SMILES)')

# Create two columns for the two molecule visualizations
col1, col2 = st.columns(2)

# Column 1 for the first molecule
with col1:
    st.subheader("Molecule 1")
    smiles_options_1 = mol_helper.smiles_options + ['customize']
    compound_smiles_1 = st.selectbox('Select a SMILES string for Molecule 1', smiles_options_1, help="Select a predefined molecule or customize your own.")

    custom_smiles_1 = ""
    if compound_smiles_1 == 'customize':
        custom_smiles_1 = st.text_input('Enter custom SMILES for Molecule 1', help="Use uppercase letters")

    active_smiles_1 = custom_smiles_1 if custom_smiles_1 else compound_smiles_1

    if compound_smiles_1 == 'customize' and custom_smiles_1:
        if not mol_helper.check_SMILES(custom_smiles_1):
            st.error("Invalid SMILES string for Molecule 1. (If you believe the string is correct, try uppercases)")
        else:
            mol_helper.render_3d(active_smiles_1)
            mol_helper.render_2d(active_smiles_1)

    elif compound_smiles_1 != 'customize':
        mol_helper.render_3d(active_smiles_1)
        mol_helper.render_2d(active_smiles_1)

# Column 2 for the second molecule
with col2:
    st.subheader("Molecule 2")
    smiles_options_2 = mol_helper.smiles_options + ['customize']
    compound_smiles_2 = st.selectbox('Select a SMILES string for Molecule 2', smiles_options_2, help="Select a predefined molecule or customize your own.", key='molecule_2')

    custom_smiles_2 = ""
    if compound_smiles_2 == 'customize':
        custom_smiles_2 = st.text_input('Enter custom SMILES for Molecule 2', help="Use uppercase letters", key='smiles_2')

    active_smiles_2 = custom_smiles_2 if custom_smiles_2 else compound_smiles_2

    if compound_smiles_2 == 'customize' and custom_smiles_2:
        if not mol_helper.check_SMILES(custom_smiles_2):
            st.error("Invalid SMILES string for Molecule 2. (If you believe the string is correct, try uppercases)")
        else:
            mol_helper.render_3d(active_smiles_2)
            mol_helper.render_2d(active_smiles_2)

    elif compound_smiles_2 != 'customize':
        mol_helper.render_3d(active_smiles_2)
        mol_helper.render_2d(active_smiles_2)
