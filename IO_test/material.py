with open('Materials.csv', newline='') as csvfile: #Change name of csv.
    data = list(csv.reader(csvfile))

class Materials:
    #Name = str, All other properties should be floats?
    def __init__(self, name, n1, n2, prob_nano, absorption1, scattering1, absorption2, scattering2, hsv = [], tag):
        self.name = name
        self.n1 = n1
        self.n2 = n2
        self.prob_nano = prob_nano
        self.absorption1 = absorption1
        self.scattering1 = scattering1
        self.absorption2 = absorption2
        self.scattering2 = scattering2
        self.hsv = hsv
        self.tag = tag

    def display(self): #have to edit this and add more constants
        print( f'{self.name} has values emission: {self.emission}   absorption: {self.absorption}   scattering: {self.scattering}  hsv: {self.hsv}')


material = [] 
material.append(Materials('Skin', 5.0, 1.11, 3.14, [256,256,256]))
material.append(Materials('Duct', 5.8, 13.11, 2.14, [248,250,256]))

material[0].display()
material[1].display()