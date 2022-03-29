# HEPData_YAML
The purpose of the project is to provide some macros to convert a .txt file into a .yaml file, 
as well as to show how to create the submission.yaml file needed for the HEPData repository to read the files and organize them.

# Prerequisites

These examples and macros work with Python 3, the macros use the next libraries (os and yaml).


# How to run the project

This project consists of 2 Macros in python, and I only tested it on Linux 

### txt_yaml.py

For the first Macro is just run a Python code, however this code is going to ask you for the name of the file

```

user@user: python txt_yaml.py
file name: 

```
### sublistyaml.py

To run the second Macro is necessary to create two txt lists:
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

# How to use the project and explanation of the macros

The project was designed for cases when you have data tables in a .txt file and you want to convert them to the format required 
by the HEPData repository, where for each table a file is made, for more information about this please read 
the HEPData documentation (https://hepdata-submission.readthedocs.io/en/latest/submission_yaml.html).

To begin with, we use the macro txt_yaml.py, where it takes the txt file and splits the values of the table in python lists, 
in order to arrange the values starting with the dependent variable and its different errors. 
Each error is labeled if it is a sys or stat error, it is necessary to take into account if the error is symmetrical or asymmetrical, 
depending on this you have to change a label and modify the macro (the example uses symmetrical errors).  

Then organize the values of the independent variable. The macro creates a .txt file at the beginning with the same name as the input, 
but at the end it changes the file format to a .yaml file.
The variable names have to be placed inside the code.


Once you have all the .yaml files you have to create a list with the names of all these files, you also need a list with the name of all 
the plots. With these two lists, you can run the macro sublistyaml.py, which creates a submission.txt file, where it goes through 
the names of the list of .yaml files and associates them with the respective plot, for this the code in a loop where it takes the 
names of the .yaml files and compares them with the names of the plots. Then it organizes it and writes it in the form requested 
by HEPData. 

Finally, you have the .yaml files, the plots, and the submission.yaml file, now it is simply compress and upload to the HEPData 
repository (which you must have permission to upload).

You can find a complete example in the folder "example".

# Credits

This project was developed for the high energy physics group at Purdue University.



