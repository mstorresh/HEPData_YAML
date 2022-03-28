#code created by: Manuel Sebastián Torres Hernández


import yaml
import os

# ------ reading the list of yaml files --------------- 1.
fileyamllist = 'texlist.txt'

in_fileyamllist = open(fileyamllist, 'r')

lines = in_fileyamllist.readlines()


# -------- reading the figure list ------------

fileplot = 'plotlist.txt'

in_fileplot = open(fileplot, 'r')

linesplot = in_fileplot.readlines()


# -----------------  reading the yaml files -----------------------------------------------


linesyaml = lines[0].strip()  #yaml list

print(str(linesyaml[:-5]))
print(len(lines))


linesn = linesplot[0].strip()
print(str(linesn[len(linesn)-3:]))
print(linesplot[0])
print(len(linesplot))

archivo = open('submission.txt', "w")

header1 = []
header2 = []
for nume in range(len(lines)):
    linesyaml = str(lines[nume].strip())
    print(linesyaml)
    with open(linesyaml, 'r') as file1:

        documents = yaml.load(file1, Loader=yaml.FullLoader)

        archivo.write("--- \n")
        archivo.write(f'#This is Table {nume} \n')
        for item, doc in documents.items():
        
            print(linesyaml)

            archivo.write("additional_resources: \n")
            for k in range(len(linesplot)):	#this loop is for connect the image with the yaml file
                linesn = linesplot[k].strip()
                if linesyaml[0:6] == linesn[0:6] and linesn[-2] == 'n':   
                    archivo.write(" - {description: Image file, location: " + f"{linesn}" + "} \n" )
                    #-------------------------------------------------------------------------------------------------------------
                    # the numbers is to connect by the names, [0:6]
                    # example: fig11_topzr.yaml  and fig11_topplot.png
                    #---------------------------------------------------------------------------------------------------------------
                else:
                    pass

            archivo.write(f"data_file:  {linesyaml} \n")
            archivo.write(f"description: {linesyaml[:-4]}  \n")
            archivo.write(f"keywords:   \n")
            archivo.write("- name: observables \n")
            archivo.write("  values: [Axes or in the paper] \n") #
            archivo.write("- name: reactions \n")
            archivo.write("  values: [Reaction] \n")
            archivo.write("- name: cmenergies \n")
            archivo.write("  values: [cm energy] \n")
            archivo.write("- name: phrases \n")
            archivo.write("  values: [Collisions] \n") #key words


            archivo.write(f"location: Data from Figure {linesyaml[3:5]}    \n")

            archivo.write(f'name: {linesyaml[:5]} ' +f'data table {nume} \n')  #add the number of the figure
            archivo.write("\n")

            header1.clear()
            header2.clear()


os.rename('submission.txt','submission.yaml')
