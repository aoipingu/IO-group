import numpy as np
import scipy


source = np.array([1,2,3], dtype = int)


class Materials_Table():
     pass


class Materials:
    #Name = str, All other properties should be floats?
    def __init__(self, name, emission, absorption, scattering):
        self.name = name
        self.emission = emission
        self.absorption = absorption
        self.scattering = scattering


    def display(self):
        print( f'{self.name} has values emission: {self.emission}   absorption: {self.absorption}   scattering: {self.scattering}')
    

Mat_0 = Materials('Skin', 5.0, 1.11, 3.14)




