This project is for the creation and then prediction of the stock prices of the SONATA stock via the use of a LSTM model.

The finstreet_model_script.ipynb is a jupyter notebook contating the script used for loading, and training the model.
The scaler and model created are stored as a .joblib and a .keras file respectively and can be loaded in directly into the program

In order to run the scripts successfully change the path files given in the code with the actual path files.

make sure that the following requirements are installed: tensorflow, scikit-learn

```python
# Loading the scaler
from joblib import load
load("path_to_joblib")
```

```python
# Loading the model
from tensorflow import keras
keras.models.load_model("path_to_model")
```

In case the data is to be loaded directly from the fyers api the three files\n
getAccessToken.py, getHistoryData.py, and getToken.py may be used

just replace the APP_ID, PIN and SECRET_ID variables in the files.
