import unicodedata
import random
# -*- coding: utf-8 -*-

def read_file(path):
    file_ = open(path, "r", encoding='utf8')
    data = file_.readlines()
    return data
    
    
def main():
    list_sujet = read_file("./list_sujet.txt")
    id_ = random.randint(0, len(list_sujet)-1)
    avis = "Pour"
    if random.randint(0,1) == 0:
        avis = "Contre"
        
    print("\n ==========================\n")
    print(list_sujet[id_])
    print("Si avis neccessaire tu dois etre : ", avis)
    print("\n ==========================\n")
    


main()

# i = input("Press Enter to continue: ")
