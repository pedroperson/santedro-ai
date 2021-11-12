# santedro-ai

When first running this project, you will need some packages. Run these commands inside the project


# First time ever
1. Get visual Studio
2. In Visual Studio:
  1. open the folder where you want to install the project
  2. Open the terminal with Ctrl + \` (key to the left of 1)
  3. In the terminal, run:
  ```
  git clone https://github.com/pedroperson/santedro-ai
  ```
  4. Open the folder that just got downloaded with visual studio code


3. Visual Studio Extensions:
  1. In visual studio, there is an icon in the left-most bar that takes you to extensions.
  2. Search python in it and download the Python file

## ON MAC

```
pip3 install --upgrade pip
pip3 install --upgrade tensorflow

pip install gym
brew install swig
pip install box2d-py
pip install box2d
```

## ON WINDOWS

```
idk lol, try the above and paste what works here
```

To open this in colab, you can click here
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)

# Testing

Ideally, every file should have at least one test file

Python weirdness : You must have an empty (or otherwise) **init**.py file in your test directory (must be named test/). Also need to add the init.py file to each subfolder for it to work

## Creating new test

Your test files inside "test/" match the pattern test\_\*.py. They can be inside a subdirectory under test/, and those subdirs can be named as anything.

## Running tests

Run all tests :

```
python -m unittest
```

Run a single test: (can use a '-v' flag for more verbose output)

```
python -m unittest test/test_something.py
```
