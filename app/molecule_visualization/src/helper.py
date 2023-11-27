# Import necessary libraries
from stmol import showmol
import py3Dmol
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import streamlit as st

# Predefined list of SMILES strings (add more as needed)
smiles_options = [
    'CN1C=NC2=C1C(=O)N(C(=O)N2C)',  # Caffeine
    'CC(C)CC1=CC=C(C=C1)C(C)C(=O)O',  # Ibuprofen
    'C1=CC=C(C=C1)N',  # Aniline
    # Add more SMILES strings here
]

def check_SMILES(smi):
    mol = Chem.MolFromSmiles(smi)
    return mol is not None 

# Function to convert SMILES to 3D molecule block
def makeblock(smi):
    mol = Chem.MolFromSmiles(smi)           # Converts a SMILES string to an RDKit molecule object.
    mol = Chem.AddHs(mol)                   # Adds hydrogen atoms to the molecule object.
    AllChem.EmbedMolecule(mol)              # Generates 3D coordinates for the molecule.
    mblock = Chem.MolToMolBlock(mol)        # Converts the RDKit molecule to a MolBlock, a text representation used by many chemistry software.
    return mblock

# Function to render the 3D molecule
def render_mol_stick(xyz):
    threeDview = py3Dmol.view(height=600, width=700)   # Creates a new viewer object for rendering the 3D structure.
    threeDview.addModel(xyz, 'mol')                     # Adds the molecule in MolBlock format to the viewer.
    # Sets the style for rendering the molecule.
    threeDview.setStyle({'stick': {'radius':0.15}, 'sphere': {'scale': 0.25}})             
    threeDview.setBackgroundColor('white')              # Sets the background color of the viewer.
    threeDview.zoomTo()                                 # Adjusts the zoom so the entire molecule fits in the viewer.
    showmol(threeDview, height=600, width=700)         # Integrates the py3Dmol viewer into Streamlit's interface.
    threeDview.resize()


# Function to create the 2D molecule
def create_mol_2d(smi):
    mol = Chem.MolFromSmiles(smi)               # Converts the SMILES string to an RDKit molecule object
    mol = Chem.AddHs(mol)                       # Adds hydrogen atoms to the molecule object.
    AllChem.Compute2DCoords(mol)                # Computes the 2D coordinates for the molecule, which are needed for 2D rendering
    # Converts the molecule object to an image representing the 2D structure
    img = Draw.MolToImage(mol, size=(650, 600), kekulize=True, wedgeBonds=True, dpi=500)                 
    return img

# render 3D mol
def  render_3d(smi):
    st.markdown("### Molecule Structure")
    with st.expander("3D Structure", expanded=True):
        mol = makeblock(smi)
        render_mol_stick(mol)

# render 2D mol
def render_2d(smi):
    with st.expander("2D Structure", expanded=True):
        img = create_mol_2d(smi)
        st.image(img)