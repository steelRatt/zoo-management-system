# Represents animals in the zoo


class Animal:

    def __init__(self, name, species, age, health):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.happiness = "Happy"

    def display_info(self):
        """Prints the animal's name, species, age, and health"""
        print(f"\nName: {self.name}\nSpecies: {self.species}\nAge: {self.age}\nHealth: {self.health}"
              f"\nHappiness: {self.happiness}")

    def feed(self, value):
        """Increases health by a specified value, but maximum health should not exceed 100"""
        if value + self.health > 100:
            self.health = 100  # Cap health at 100
            print(f"{self.name} is now at full health!")
        else:
            self.health += value
            print(f"{self.name} was fed successfully! Health has increased to {self.health}.")


class Mammal(Animal):

    def __init__(self, name, species, age, health, fur_colour):
        super().__init__(name, species, age, health)  # Calls the parent class constructor
        self.fur_colour = fur_colour

    def display_info(self):  # Overriding the parent class method
        super().display_info()  # Call the parent class method to display common details
        print(f"Fur Colour: {self.fur_colour}")


class Bird(Animal):

    def __init__(self, name, species, age, health, wing_span):
        super().__init__(name, species, age, health)
        self.wing_span = wing_span

    def display_info(self):
        super().display_info()
        print(f"Wing Span: {self.wing_span}m")


class Reptile(Animal):

    def __init__(self, name, species, age, health, scale_type, is_venomous, preferred_temperature):
        super().__init__(name, species, age, health)
        self.scale_type = scale_type
        self.is_venomous = is_venomous
        self.preferred_temperature = preferred_temperature
        self.current_temperature = 60

        # Determine initial happiness
        if self.current_temperature != self.preferred_temperature:
            self.happiness = "Unhappy"
        else:
            self.happiness = "Happy"

    def display_info(self):
        super().display_info()
        print(f"Scale Type: {self.scale_type}")
        print(f"Venomous? {self.is_venomous}")

    def warm_up(self, value=5):
        """Increases reptile health by 5"""
        if value + self.health > 100:
            self.health = 100  # Cap at 100, same as feed method
            print(f"{self.name} is now at full health!")
        else:
            self.health += value
            print(f"{self.name} was warmed up successfully! Health increased to {self.health}.")

    def set_temperature(self, new_temperature):
        """Sets reptile temperature to a specified value"""
        self.current_temperature = new_temperature

        # Update happiness accordingly
        if self.current_temperature == self.preferred_temperature:
            self.happiness = "Happy"
