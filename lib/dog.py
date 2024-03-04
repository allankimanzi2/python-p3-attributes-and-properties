#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
   
    def __init__(self,name = "",breed="Mutt"):
        if not isinstance(name,str) :
            print("Name must be string between 1 and 25 characters.")
        elif name == "":
             print("Name must be string between 1 and 25 characters.")
        elif len(name)>25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name
            if breed != "":
                
                if breed not in APPROVED_BREEDS:
                    print("Breed must be in list of approved breeds.")
                    self.breed = "Mutt"
                else:
                    self.breed = breed
             
