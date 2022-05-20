# Oliwer Toth
# Tetek 20
# 2022-03-30



class Animal:
    
    def __init__(self, name, hibernate, awake, sleep, foodtime, place):

        self.name = name
        self.hibernate = hibernate
        self.awake = awake
        self.sleep = sleep
        self.foodtime = foodtime
        self.place = place
        

    def __str__(self) -> str:
        """String of Attributes

        Returns:
            str: Name and Place of the object
        """
        return f"{self.name} och dess plats är {self.place}."

    def get_all_attri(self):
        """returns all attributes

        Returns:
            str, str, int, int, int, str: All the attributes of the object
        """
        return self.name, self.hibernate, self.awake, self.sleep, self.foodtime, self.place

    def is_awake(self, date, arri_h, depa_h):
        """Awake time

        Args:
            date (str): month to compare with
            arri_h (int): hour for arrival of guest
            depa_h (int): hour for departure of guest

        Returns:
            bool: Returns if arrival is in Awake time
        """
        
        # Check when the animal is in hibernate
        if self.hibernate == date:
            return False

        # Check which animal is awake while you are there
        awake_h = int(self.awake[0:2])
        sleep_h = int(self.sleep[0:2])
        if arri_h >= awake_h:
            return True 
        elif depa_h <= sleep_h:
            return True
        else:
            return False


    def check_food(self, arri_m, arri_h):
        """Check if foodtime is in when the user is at the zoo

        Args:
            arri_m int: foodtime place 0 and 1
            arri_h int: foodtime place 3 and 4

        Returns:
            tuple(str, int, int)/bool: name, foodtime, foodtime
            or
            bool: False if not being fed within timeframe
        """
        # Checks when all animals are fed
        food_h = int(self.foodtime[0:2])
        food_m = int(self.foodtime[3:5])
        if food_h > arri_h:
            return (self.name, self.foodtime[0:2], self.foodtime[3:5])
        elif food_m >= arri_m:
            return (self.name, self.foodtime[0:2], self.foodtime[3:5])
        else:
            return False
    



# functions
def add_animal():
    """
        Adds object to the file
    """

    print("\tNu får du lägga till djuret.")
    name = input("\tnamn på djur: ")
    hibernate = input("\tIde: ")
    awake = input("\tVaken(hh:mm): ")
    sleep = input("\tSömn(hh:mm): ") 
    foodtime = input("\tMatdags(hh:mm): ") 
    place = input("\tPlats: ")
    with open("animal_file.txt", "a", encoding="utf8") as g:
        save_string = (f"{name}/{hibernate}/{awake}/{sleep}/{foodtime}/{place}\n")
        g.write(save_string)
    
        
def zoo(animals):
    """The user interface

    Args:
        animals (str): all the animals
    """
    
    print("\tVilken månad vill du till Oliwers zoo?:\n")
    date = input("\t")

    
    print(f"\tVilken dag i {date} vill du komma?")
    day = input("\t")
    # while True:
    #     if date == "januari" or date == "mars"or date == "maj" or date == "juli" or date == "augusti" or date == "oktober" or date == "december":
    #         if day <= 31:
    #             False
    #     elif date == "april" or date == "juni" or date == "september" or date == "november":
    #         if day <=30:
    #             False
    #     elif date == "februari":
    #         if day <=28:
    #             False
    #     else:print("fel interval i månaden")
    # Ask what time they want to come
    print("\tvilken tid vill du komma?(hh:mm): \n")
    arrival = input("\t")
    arri_h = int(arrival[0:2])
    arri_m = int(arrival[3:5])
    
    print("\tvilken tid vill du lämna?(hh:mm): \n")
    departure = input("\t")
    depa_h = int(departure[0:2])
    
    if date == "december" or date == "januari" or date == "februari":
        date = "vinter"
    else:
        date = "sommar"
    
    
    # Go through the list of animal objects to find which animals are awake
    available_animals = []

    for animal in animals:
        if animal.is_awake(date, arri_h, depa_h):
            available_animals.append(animal)

    # Check when the animals eat when you are there
    feeding_animals = []
    for animal in available_animals:
        feeding_animals.append(animal.check_food(arri_m, arri_h))

    # Print out the animal objects and whether they are fed while you are there
    print("\n")
    print("\tFöljande djur är tillgängliga under ditt besök!")
    for animal in available_animals:
        print(f"\t{animal}")
    print("\n")
        
    
    print("\t=================================\n")
    # Check if feeding is a bool
    print("\tFöljande djur matas under ditt besök!")
    for feeding in feeding_animals:
        if isinstance(feeding, bool):
            continue
        else:
            print(f"\t{feeding[0]} matas kl {feeding[1]}:{feeding[2]}.")

def load_animals():
    """Load all objects to file

    Returns:
        str: The object
    """
    # Open the animal file and reads it 
    with open("animal_file.txt", "r", encoding="utf8") as f:
        animal = []
    # Adds animal to the file
        for line in f.readlines():
            attributes = line.split("/")
            this_ani = Animal(attributes[0],
                                  attributes[1], 
                                  attributes[2], 
                                  attributes[3],
                                  attributes[4],
                                  attributes[5].rstrip("\n"))
            animal.append(this_ani)
    
    return animal    


def main():
    
    print("\tVälkommen till Oliwers zoo!\n")
    while True:
        print("\tVad vill du göra?")
        print("\t1. Besöka?")
        print("\t2. Lägga till?")
        print("\t0. Avsluta?")
        print("\n")

        # Makes the program work without errors
        chose = input("\t")
        if chose == "1":
            animals = load_animals()
            zoo(animals)
            break
        elif chose == "2":
            add_animal()
        elif chose == "0":
            break
        else:
            print("inmatat fel värde.")
            print("försök igen.")
    
    

if __name__=="__main__":
    main()