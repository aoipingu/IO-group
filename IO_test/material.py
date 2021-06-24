master_dict = {}

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
     
    def list(self):
        pass
    def append_to_dict(self, dict):
        dict{
        "0": self.name,
        "1": self.n1,
            .
            .
            .
        }
       


material = [] 
skin = Materials()
skin.append_to_dict(dict) # master_dict[0] - skin.name,skin.n1,skin.scattering....  master_dict[1] - duct.name, duct.n1 .....
=Materials()
=Material()
...

skin.display()
skin.list() # 

material.append(Materials('Skin', 5.0, 1.11, 3.14, [256,256,256]))
material.append(Materials('Duct', 5.8, 13.11, 2.14, [248,250,256]))

material[0].display()
material[1].display()


# TODO Prepare a CSV template
# TODO read the CSV --> List --> into classes and instances (skin, duct, muscle, air ..)
# TODO decide the index of the materials (0 - Air, 1 - Duct, 2 - Muscle, 3 - , 4 -, 5- ,   6-)
# TODO transmit the data into master_dict with keys being index [0 to 5] and values being coefficients (absorption, n1, hsv etc etc)





