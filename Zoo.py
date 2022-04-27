# Oliwer Toth
# Tetek 20
# 2022-03-30



class Animal:
    
    def __init__(self, name, hibernate, awake, sleep, foodtime, place):
        # Alla djurens attribut
        self.name = name
        self.hibernate = hibernate
        self.awake = awake
        self.sleep = sleep
        self.foodtime = foodtime
        self.place = place

    def __str__(self) -> str:
        return f"{self.name} Och dess plats är {self.place}"

    def get_all_attri(self):
        return self.name, self.hibernate, self.awake, self.foodtime

    def is_awake(self, date, arri_h, depa_h):
        
        # Kollar när djuret är i ide
        if self.hibernate == date:
            return False

        # Kollar vilket djur som är vaken under tiden man är där
        awake_h = int(self.awake[0:2])
        # awake_m = (self.awake[3:5])
        sleep_h = int(self.sleep[0:2])
        if arri_h >= awake_h:
            return True 
        elif depa_h <= sleep_h:
            return True
        else:
            return False


    def check_food(self, arri_m, arri_h):
        # Kollar när alla djuren matas
        food_h = int(self.foodtime[0:2])
        food_m = int(self.foodtime[3:5])
        if food_h > arri_h:
            return (self.name, self.foodtime[0:2], self.foodtime[3:5])
        elif food_m >= arri_m:
            return (self.name, self.foodtime[0:2], self.foodtime[3:5])
        else:
            return False



# functions

def zoo(animals):
        print("Välkommen till Oliwers zoo")
        # Fråga vilket datum användaren vill komma
        date = int(input("Vilken månad vill du till Oliwers zoo?(månadstal 1-12) "))
        if date >= 2 and date <= 10:
            date = "sommar"
        else:
            date = "vinter"
        # Fråga vilken tid de vill komma
        arrival = input("vilken tid vill du komma?(hh:mm) ")
        arri_h = int(arrival[0:2])
        arri_m = int(arrival[3:5])
        
        departure = input("vilken tid vill du lämna?(hh:mm) ")
        depa_h = int(departure[0:2])
        # depa_m = int(departure[3:5])
        
        
        # Gå igenom listan med djurobjekt för att finna vilka djur som är vakna
        # Tom lista som appendas där nere med djur som är vakna under tiden man är på zooet
        available_animals = []

        for animal in animals:
            if animal.is_awake(date, arri_h, depa_h):
                available_animals.append(animal)
        # Kollar när djuren äter när man är där
        feeding_animals = []
        for animal in available_animals:
            feeding_animals.append(animal.check_food(arri_m, arri_h))

        # Skriv ut djurobjekten samt om de matas under tiden man är där
        # skriver ut vilka djur som är tillängliga
        print("\n")
        print("\tFöljande djur är tillgängliga under ditt besök!")
        for animal in available_animals:
            print(f"\t{animal}")
        print("\n")
            
        
        print("\t===========================\n")
        # Skriver ut när djuren äter
        print("\tFöljande djur matas under ditt besök!")
        for feeding in feeding_animals:
            if isinstance(feeding, bool):
                continue
            else:
                print(f"\t{feeding[0]} matas kl {feeding[1]}:{feeding[2]}.")
def main():
    
    animals = [] #load_animals()
    animal = Animal("Björn", "vinter", "08:00" ,"16:00", "13:00", "längst bort")
    animal1 = Animal("Tiger", "-", "03:00" ,"17:00", "12:30", "vänstra hörnet")
    animal2 = Animal("Älg", "-", "07:00", "20:00", "15:00", "högra hörnet")
    animals.append(animal)
    animals.append(animal1)
    animals.append(animal2)
    
   
    zoo(animals)    
    

if __name__=="__main__":
    main()