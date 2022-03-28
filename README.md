# HEPData_YAML
The purpose of the project is to provide some macros to convert a .txt file to a .yaml file, 
as well as to show how to create the submission.yaml file needed for the HEPData repository to read the files and organize them.

# Prerequisites

These examples and macros work with Python 3, the macros use the next libraries (os and yaml).


# How to run the project

This project consist of 2 Macros in python, and I only tested it on Linux 

### txt_yaml.py

For the first Macro is just run a Python code, but this code is going to ask you for the file name

```

user@user: python txt_yaml.py
file name: 

```
### sublistyaml.py

To run the second Macro is necesary to create two txt list:
- texlist.txt (list of the names of the yaml files with the data) 
- plotlist.txt (list of the name of the plots, the macro recognize png files)

To create that kind of list in Linux is just the next command

```
user@user: ls *.txt > texlist.txt
user@user: ls *.png > plotlist.txt

```

After obtaining the lists you can run the macro like any other python code.

```

user@user: python sublistyaml.py

```

