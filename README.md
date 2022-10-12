# BankayaChallenge
A coding challenge to Python SWE Positon

# Answer to questions about Python
You can find the answer of the questions in technical_answers.txt file.

# Clone the Project

In the folder where you want to work, open a terminal and write the following command:
```
git clone https://github.com/CesarLuV/BankayaChallenge.git
```

# Create a virtual Environment (Unix Based Systems)

Run the following commands:

1. `cd BankayaChallenge`
2. `python3 -m venv .env`
3. `source .env/bin/activate`

Note: To deactivate the virtual environment, in the terminal run the command `deactivate`

# Using a specific Python version (3.10.5)
For Python in macOS, use *pyenv*:

```brew install pyenv```

To install a specific Python version, move to the *BankayaChallenge* folder and run:

```pyenv install 3.10.5```

To select a version for every command run with the current folder:

```pyenv local 3.10.5```

To list available versions:

```pyenv versions```

To set Python 3.10.5 version, run:

```
export PATH="/shims:$PATH"
eval "$(pyenv init -)"
```

# Update your pip version
Once you have activated the virtual environment, to verify you are up to date with python installer package, you should run the following command:
```
python3 -m pip install --upgrade pip
```

# Install the requirements
Once you have activated the virtual environment, run the following command:
```
pip3 install -r requirements.txt
```

# Running the project
Execute the following command:

```uvicorn main:app --reload```

As is the default port, you should be able to see the running project on: 
```http://127.0.0.1:8000```


# Running the tests
In the terminal, move to the directory where *BankayaChallenge* is, at the same level of `main.py`.

## Testing the client
Run the following command:
```
python3 -m pytest ./test/*.py
```

# Verify the PEP8 Standar for Python files
Located where *BankayaChallenge* project folder is, you can run the following comands:
```
pycodestyle --first common/utils.py
pycodestyle --show-source --show-pep8 main.py
```

The above commands will indicate wich possible PEP8 coding standard metrics should be modified for the maximum readability of the souece code.

**NOTE**: That lines of the code are just examples and should be aplied for all files.