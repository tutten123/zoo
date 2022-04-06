# Oliwer Toth
# Tetek 20
# 2022-03-30

from calendar import calendar


class Animal:
    
    def __init__(self, name, hibernate, awake, foodtime):
        
        self.name = name
        self.hibernate = hibernate
        self.awake = awake
        self.foodtime = foodtime
    def get_all_attri(self):
        return self.name, self.hibernate, self.awake, self.foodtime



# functions
def save_animal(animal : Animal):
        """
        Tar in djuren, Bryter ner dens attribut och sparar ner på fil.
        
        Args, animal (Animal): Det objekt som ska sparas ner på fil.
        """
        name, hibernate, awake, foodtime = animal.get_all_attri()
        with open("djur_fil.txt", "w", encoding="utf8") as f:
            save_string = f"{name}/{hibernate}/{awake}/{foodtime}\n"
            f.write(save_string)
            print(f"{name} har sparats.")
def zoo():
    print("Välkommen till Oliwers zoo")

    # Fråga vilket datum användaren vill komma
    date = input("Vilket datum vill du till Oliwers zoo? ")
    time = input("vilken tid vill du komma? ")
    # Gå igenom listan med djurobjekt för att finna vilka djur som är vakna
    
        


    # Fråga vilken tid de vill komma
    
    # Skriv ut djurobjekten samt om de matas under tiden man är där

def main():
    animal = Animal("Björn", "vintern", "8-16", "13")
    animal1 = Animal("Nattuggla", "-", "21-5", "24")
    animal2 = Animal("älg", "-", "7-20","15")
    save_animal(animal)
    save_animal(animal1)
    save_animal(animal2)

if __name__=="__main__":
    main()