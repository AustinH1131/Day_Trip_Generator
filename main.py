import random

destinations=["Hawaii","Fiji","Taiwon","Japan"]
transportations=["Plane","Boat","Cruise","Private Jet"]
resturaunts=["Red lobster","Chilis","Sushi Bar","Pho"]
entertainments=["Fishing","Surfing","Snorkling","Whale watching"]


def random_trip(entertainment,resturaunt,transportation,destination): 
    finale_trip=destination+transportation+resturaunt+entertainment



Locked=True

while Locked is True:
    print("Type Go! to generate random trip")
    Key= input("")
    if Key =="Go!":
        Locked=False
        destination= random.choice(destinations)
        transportation=random.choice(transportations)
        resturaunt=random.choice(resturaunts)
        entertainment=random.choice(entertainments)
        print(f"You will be going to {destination} .You will take a {transportation} ,then eat {resturaunt} ending your day with {entertainment}")
    else:
        Locked=True
while Locked is False:
    print("Is this trip satisfying?")
    confirmation=input(" ")
    if confirmation=="Yes":
        print("Your trip has been confirmed.")
        print(f"You will be going to {destination} .You will take a {transportation} ,then eat {resturaunt} ending your day with {entertainment}")
        break
    else:Locked=True

    
            


    
       


           

































        
