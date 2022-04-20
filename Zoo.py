# Oliwer Toth
# Tetek 20
# 2022-03-30

class Animal:
    
    def __init__(self, name, hibernate, awake, foodtime):
        
        self.name = name
        self.hibernate = hibernate
        self.awake = awake
        self.foodtime = foodtime

    def get_all_attri(self):
        return self.name, self.hibernate, self.awake, self.foodtime

    def is_awake(self):
        # Detta funkar inte, men ungefär såhär kan koden fungera
        if self.name in self.awake:
            return True
        else:
            return False


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
        date = int(input("Vilken månad vill du till Oliwers zoo? "))
        if date >= 2 and date <=10:
            print("Då är inget djur i ide")
        elif date < 2 and date > 10:
            print("då är ")
        # Fråga vilken tid de vill komma
        time = (int(input("vilken tid vill du komma? ")))
        time1 = int(input("vilken tid vill du lämna? "))
        time_interval = time and time1        
        
        # Gå igenom listan med djurobjekt för att finna vilka djur som är vakna
        for i in save_animal:
            print(i)
        # Skriv ut djurobjekten samt om de matas under tiden man är där
def main():
    
    animals = []
    animal = Animal("Björn", "vintern", "8,16", "13")
    animal1 = Animal("tiger", "-", "3,17", "12")
    animal2 = Animal("älg", "-", "7,20","15")
    save_animal(animal)
    save_animal(animal1)
    save_animal(animal2)
    animals.append(animal)
    animals.append(animal1)
    animals.append(animal2)
    
   
    zoo()    
    

if __name__=="__main__":
    main()