
# Code created by Manuel Sebastián Torres Hernández

#----------------------------------------------------------------------------------------------
#This code transform a txt file to a YAMl file with the necesary order to HEPData 
#--------------------------------------------------------------------------------------------

import os
from pathlib import Path

print("file name:   ")
file1 = input()

in_file = open(file1, 'r')

lines = in_file.readlines()
valor1 = lines[9].strip().split()  #This line is for the start of the data in the txt table, the number is the row number in the txt file  
print(len(valor1))
print(valor1)  # just to check if the value is correct


archivo = open(file1 + 'yaml', "w")

#---------------------------------------------------------------------------------------------------------------------------
# This part is for the dependent Variable 
# If your file have more columns you can add more "if" to create the yaml file
#---------------------------------------------------------------------------------------------------------------------------

archivo.write("dependent_variables: \n")
archivo.write("- header: {name: ' $ Y $', units: 'm' }  \n")
archivo.write("  values: \n")

for i in range(8, len(lines)):
    valor = lines[i].strip().split()
    archivo.write(f"  - value: {valor[1]} \n")
    if len(valor)==3:
        archivo.write("    errors: \n")
        archivo.write(f"    - symerror: {valor[2]} \n")
        archivo.write( "      label: stat \n")
    if len(valor)==4:
        archivo.write("    errors: \n")
        archivo.write(f"    - symerror: {valor[2]} \n")
        archivo.write( "      label: stat \n")
        archivo.write(f"    - symerror: {valor[3]} \n")
        archivo.write( "      label: syst \n")

    else:
        pass

#-----------------------------------------------------------------------------------------------
# This part is for the independent Variable
#-----------------------------------------------------------------------------------------------


archivo.write("independent_variables: \n")
archivo.write("- header: {name: ' $X$ ', units: 's' } \n")
archivo.write("  values: \n")

for j in range(8, len(lines)):
    valor = lines[j].strip().split()
    archivo.write(f"  - value: {valor[0]} \n")

archivo.close()

print(file1 + 'yaml')		
filename = Path(file1 + 'yaml')
out_file = filename.with_suffix('.yaml')
print(out_file)
oldname = file1 + 'yaml'

os.rename(oldname,out_file)
