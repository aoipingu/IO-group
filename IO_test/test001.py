import csv
import numpy as np

class Materials:
    '''
    A class used to store material coefficients for use in the Simulation later
    
    ...Elaboration...
    
    Attributes
    ----------
    name : str
        Either 'Air' 'Skin' 'Duct' 'Muscle' 'Fat' or 'Bone'
    n1 : int
        represents the refractive index for a light beam entering from Air
    n2 : int
        represents the refractive index for a light beam exiting the material into ..?..
    prob_nano : int
        the probability of ..?..
    absorption1 : int
        the ratio of intensities of the exiting light beam to the entering light beam
    scattering1 : int
        the amount of scattering ...idfk...
    absorption2 : int
        the amount of absorption ...idfk...
    scattering2 : int
        the amount of scattering2 ...idfk...
    hsv : list
        hue, saturation and visibility for the material when viewed with a SEM ...IDFK...
    
    Methods
    -------
    data_to_list(data):
        converts the csv file into a single list ...idk...
    
    
    
    '''
    def __init__(self, name, n1, n2, prob_nano, absorption1, scattering1, absorption2, scattering2, hsv = []):
        self.name = name.lower() # just so that Air, air, AIR come out as the same 
        self.n1 = n1
        self.n2 = n2
        self.prob_nano = prob_nano
        self.absorption1 = absorption1
        self.scattering1 = scattering1
        self.absorption2 = absorption2
        self.scattering2 = scattering2
        self.hsv = hsv
    
    def data_to_list (data):
        ''' Ensures that Air is located in the top and has a tag of zero. This function receives'''
        data = np.array(data)
        a = int(np.where(data[1:,0] == "Air")[0])
        temp = data[a + 1].copy()
        data[a + 1] = data[1]
        data[1] = temp
        data = data.tolist()

        #Saves all material classes into a comibned list called "mat_list". This collates values of H, S, and V as a single list and helps in tagging.
        mat_list = []
        for i in data[1:]:
            i[0] = Materials(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], [i[8], i[9], i[10]]) #May change into int or floats? Currently as strings.
            mat_list.append(i[0])
        
        #Converts list into a dict called "mat_dict". The key is the tag.
        mat_dict = {}
        for i in range(len(mat_list)):
            mat_dict[i] = mat_list[i]

        return mat_dict

#Copies data from "data.csv" and converts into list/
with open("data.csv", newline='') as csvfile: # Probable change the name of the csv.
    data = list(csv.reader(csvfile))

#mat_dict is the master dictionary with the tag as the key and the material class as the value.
mat_dict = Materials.data_to_list(data)

#Tests based on csv with pseudo values. 
print(mat_dict)
print(mat_dict[1].hsv)
