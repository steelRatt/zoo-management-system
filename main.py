# Zoo Management System

from zoo import Zoo
from animal import Mammal, Bird, Reptile


def get_animal_details():
    """Gets the name, species, age, and health of a new animal"""
    name = input("Enter animal name: ")
    species = input("Enter animal species: ")
    age = int(input("Enter animal age: "))
    health = int(input("Enter animal health: "))

    # Decide type of animal and gather specific attributes
    animal_type = input("Enter animal type (Mammal/Bird/Reptile): ").lower()
    if animal_type == "mammal":
        fur_colour = input("Enter fur colour: ")
        return Mammal(name, species, age, health, fur_colour)

    elif animal_type == "bird":
        wing_span = float(input("Enter wing span in meters: "))
        return Bird(name, species, age, health, wing_span)

    elif animal_type == "reptile":
        scale_type = input("Enter scale type: ")
        is_venomous = input("Is it venomous? (yes/no): ")
        preferred_temp = float(input("Enter preferred temperature: "))
        return Reptile(name, species, age, health, scale_type, is_venomous, preferred_temp)

    else:
        print("Invalid animal type.")
        return None


def main():
    my_zoo = Zoo()

    while True:
        print("\nZoo Management System")
        print("1. Add an animal\n2. Remove an animal\n3. Display all animals\n4. Feed all animals\n5. Set temperature\n"
              "6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            animal = get_animal_details()
            my_zoo.add_animal(animal)
            print(f"New animal added successfully: {animal.name} the {animal.species}")

        elif choice == "2":
            name = input("Enter the name of the animal to be removed: ")
            my_zoo.remove_animal(name)

        elif choice == "3":
            my_zoo.display_all_animals()

        elif choice == "4":
            my_zoo.feed_all_animals()

        elif choice == "5":
            my_zoo.set_temperature()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
