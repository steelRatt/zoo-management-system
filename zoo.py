# The overarching class representing the zoo.

from animal import Animal, Reptile


class Zoo:

    def __init__(self, name="Zoo 1"):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        """Add an animal object to the zoo's list"""
        if isinstance(animal, Animal):  # Check if the passed object is an instance of Animal
            self.animals.append(animal)
        else:
            print("Invalid animal object.")

    def remove_animal(self, name):
        """Remove an animal from the zoo's list based on its name"""
        animal_to_remove = None
        for animal in self.animals:
            if animal.name == name:
                animal_to_remove = animal
                break

        if animal_to_remove:
            self.animals.remove(animal_to_remove)
        else:
            print(f"No animal named {name} found in the zoo.")

    def display_all_animals(self):
        """Display the details of all animals in the zoo using 'display_info' method of each animal"""
        print("\nANIMAL INFO:")
        if len(self.animals) == 0:
            print("No animals in the zoo!")
        else:
            for animal in self.animals:
                animal.display_info()

    def feed_all_animals(self, health_increment=10):
        """Feed all animals in the zoo, increasing their health using respective 'feed' methods"""
        for animal in self.animals:
            animal.feed(health_increment)

    def set_temperature(self):
        """Set the temperature of reptiles only"""

        # Creates a list of reptiles only by checking if each animal is of class Reptile
        reptiles = [animal for animal in self.animals if isinstance(animal, Reptile)]

        # If there are no reptiles
        if not reptiles:
            print("No reptiles in the zoo!")
            return

        # List all reptiles using enumerate to allow choosing by index number instead of name
        print("List of Reptiles:")
        for idx, reptile in enumerate(reptiles, 1):
            print(f"{idx}. {reptile.name}  (Preferred Temperature: {reptile.preferred_temperature} degrees)")

        # Uses a try except to handle errors more efficiently
        try:
            choice = int(input("Choose a reptile by name to set a new temperature for: "))

            if 1 <= choice <= len(reptiles):  # If choice is valid
                chosen_reptile = reptiles[choice - 1]

                print(f"\nCurrent temperature for {chosen_reptile.name}"
                      f" = {chosen_reptile.current_temperature}")

                new_temp = float(input(f"Set temperature for {chosen_reptile.name}: "))
                chosen_reptile.set_temperature(new_temp)

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")
