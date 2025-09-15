# CSCI310-Template-2025
Template for assignments in CSCI310 Fall 2025

## Prerequisites
These instructions assume the following:
1. [VS Code](https://code.visualstudio.com/download) is installed
1. [uv](https://docs.astral.sh/uv/) is installed

## Required setups
1. Create a new repository selecting this one as a Template
1. Open VS Code
1. Clone your new repository
1. Open a terminal window
1. Create a virtual environment (`uv venv .venv --python 3.12`)
1. Activate the virtual environment as the output from creating it says to
1. Install [Sphinx](https://www.sphinx-doc.org/en/master/) (`uv pip install sphinx`)
1. Change directory in terminal to the docs folder (`cd docs`)
1. Run `sphinx-quickstart -t ../templates`
1. Run `make html` on a Mac or `.\make.bat html` on Windows
1. This should finish with `build succeeded`
1. Add `conf.py` (should just show as modified) and `index.rst` (should show as new file) to your repository
1. Change the name of `hello.py` to something related to your project
1. Change the name `hello` in `index.rst` to the name of your file
1. Modify both `conf.py` and `index.rst` to have the correct project name, author, and date
1. Modify your .py file to have your name in the top docstring and to describe your project
1. Make the documentation again by running `make html` on a Mac or `.\make.bat html` on Windows
1. If it runs successfully, you are ready to modify the code to implement your project
1. Lastly, modify this `README.md` file to match your project
