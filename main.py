import random

place_to_go=["Hawaii","Fiji","Taiwan","Japan"]
mobility=["Plane","Boat","Cruise","Private Jet"]
place_to_eat=["Red lobster","Chilis","Sushi Bar","Pho"]
stuff_to_do=["Fishing","Surfing","Snorkling","Whale watching"]
            #Function that generates a random vacation with confirmation.
def random_trip(destination,transportation,resturaunt,entertainment): 
    Locked=True
    while Locked is True:
        print("Type Go! to generate random trip")
        Key= input("")
        if Key =="Go!":    
             #Generate randoms from list above.
            destinations= random.choice(destination)
            transportations=random.choice(transportation)
            resturaunts=random.choice(resturaunt)
            entertainments=random.choice(entertainment)
            print(f"You will be going to {destinations}.You will take a {transportations},then eat {resturaunts} ending your day with {entertainments}.")
        
            #Confirmation that trip is good or not/loops back if not.
            print("Is this trip satisfying?")
            confirmation=input(" ")
            if confirmation=="Yes":
                print("Your trip has been confirmed.")
                print(f"You will be going to {destinations}.You will take a {transportations},then eat {resturaunts} ending your day with {entertainments}.")
                break
            else:Locked=True
random_trip(place_to_go,mobility,place_to_eat,stuff_to_do)
    
            


    
       


           

































        
