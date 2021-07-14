import csv
import numpy as np

class Materials:
    '''
    A class used to store material properties for use in the Simulation later. The class also contains the "data_to_dict" fucntion to pack the material properties into a dictionary, where the keys and the values are the material tags and material objects repectively. Takes data from "material.csv".
    
    Attributes
    ----------
    name : str
        Name of the material. Materials can be "Air", "Skin", "Muscle", "Duct", etcetera.
    n1 : float
        Represents the refractive index of material when an "Excitation Wavelength" is employed.
    n2 : float
        Represents the refractive index of material when an "Emission Wavelength" is employed.
    prob_nano : float
        Represents the probability of nanoparticles attaching to the material.
    absorption1 : float
        Represents the absorption coefficient of material when an "Excitation Wavelength" is employed.
    scattering1 : float
        Represents the scattering coefficient of material when an "Excitation Wavelength" is employed.
    absorption2 : float
        Represents the absorption coefficient of material when an "Emission Wavelength" is employed.
    scattering2 : float
        Represents the scattering coefficient of material when an "Emission Wavelength" is employed.
    hsv : list of int
        Hue, Saturation and Visibility of the material.
    
    Function
    -------
    data_to_dict(data):
        Input: data (list)
        Output: mat_dict (dictionary)
    -------
    '''

    def __init__(self, name, n1, n2, prob_nano, absorption1, scattering1, absorption2, scattering2, hsv = []):
        self.name = name
        self.n1 = n1
        self.n2 = n2
        self.prob_nano = prob_nano
        self.absorption1 = absorption1
        self.scattering1 = scattering1
        self.absorption2 = absorption2
        self.scattering2 = scattering2
        self.hsv = hsv
    
    def data_to_dict (data):
        #Ensures that "Air" is located in the top and has a tag of zero.
        data = np.array(data)
        a = int(np.where(data[1:,0] == "Air")[0])
        temp = data[a + 1].copy()
        data[a + 1] = data[1]
        data[1] = temp
        data = data.tolist()

        #Saves all material classes into a comibned list called "mat_list". This collates values of H, S, and V as a single list and helps in tagging.
        mat_list = []
        for i in data[1:]:
            i[0] = Materials(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], [int(i[8]), int(i[9]), int(i[10])])
            mat_list.append(i[0])
        
        #Converts list into a dict called "mat_dict". The key is the tag and the value is the respective "Material" object.
        mat_dict = {}
        for i in range(len(mat_list)):
            mat_dict[i] = mat_list[i]

        return mat_dict


### Main Body

#Copies data from "data.csv" and converts into list/
with open("material.csv", newline='') as csvfile: # Probably change the name of the csv.
    data = list(csv.reader(csvfile))

#mat_dict is the master dictionary with the tag as the key and the material class as the value.
mat_dict = Materials.data_to_dict(data)

#Tests based on csv with pseudo values.
print(mat_dict)
print(mat_dict[1].hsv)
print(Materials.__doc__)