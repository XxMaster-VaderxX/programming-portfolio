# Band name generator
import random


titles = ["squeamish", "spiky", "lively", "dapper", "false", "foregoing", "steadfast",
          "endurable", "wet", "bewildered", "awake", "jagged", "victorious", "vengeful",
          "precious", "redundant", "scientific", "faded"]

adjs = ["animated", "honorable", "wonderful", "rampant", "momentous", "tame",
        "thoughtless", "fair", "cool", "foolish", "far", "volatile", "tightfisted",
        "changeable", "ignorant", "deez", "giant", "beautiful", "cold", "windy"]
        
plural_nouns = ["dogs", "liquids", "nuts", "hills", "airplanes", "trucks", "crows",
                "skins", "behaviors", "irons", "bedrooms", "stomachs", "clubs", "horses",
                "creatures", "verses", "cables", "keys", "carriages"]
                
def title():
    ''' This function chooses a random title for the name'''
    return random.choice(titles)
    
def adj():
    ''' This function chooses a random adj for the band '''
    return random.choice(adjs)
    
def plural_noun():
    return random.choice(plural_nouns)
    
def main():
    while True:
        name = raw_input("Enter your name: ")
        if name == "q":
            break
        random.seed(name)
        print title(), name, "and the", adj(), plural_noun()
        
main()                   
                
                          
			