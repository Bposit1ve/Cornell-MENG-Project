## App Required Environment
* [Python 3.6+](https://www.python.org/downloads/)
* [Node.js](https://nodejs.org)
* [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

## Install required libraries

```
cd app
```

~~python3 -m venv venv (Skip this step)~~

```
pip install streamlit stmol rdkit py3Dmol
```


## From a separate terminal, run the app's Streamlit app:

```
cd app
cd molecule_visualization
```

~~pip install -e . # install template as editable package (Skip this optional step)~~

```
streamlit run app.py 
```
