import random
import matplotlib.pyplot as plt

class Human:
    def __init__(self, name):
        self.name = name

class Robot:
    def __init__(self, id_number):
        self.id_number = id_number

class Planet:
    def __init__(self, name):
        self.name = name
        self.humans = []
        self.robots = []

    def add_human(self, human):
        self.humans.append(human)

    def add_robot(self, robot):
        self.robots.append(robot)

class Universe:
    def __init__(self):
        self.planets = []

    def generate(self):
        """Creates a new planet with a random number of humans and robots."""
        planet_name = f"Planet_{len(self.planets) + 1}"
        planet = Planet(planet_name)

        # Add a random number of humans (1-5)
        for i in range(random.randint(1, 5)):
            human = Human(f"Human_{i+1}")
            planet.add_human(human)

        # Add a random number of robots (1-5)
        for j in range(random.randint(1, 5)):
            robot = Robot(f"Robot_{j+1}")
            planet.add_robot(robot)

        self.planets.append(planet)

    def show_populations(self, selection):
        """
        Displays a bar chart of populations for each planet.
        If selection is 'human', shows number of humans.
        If selection is 'robot', shows number of robots.
        Otherwise, shows total population.
        """
        planet_names = [planet.name for planet in self.planets]
        if selection == "human":
            counts = [len(planet.humans) for planet in self.planets]
            title = "Number of Humans on Each Planet"
            ylabel = "Number of Humans"
        elif selection == "robot":
            counts = [len(planet.robots) for planet in self.planets]
            title = "Number of Robots on Each Planet"
            ylabel = "Number of Robots"
        else:
            counts = [len(planet.humans) + len(planet.robots) for planet in self.planets]
            title = "Total Population on Each Planet"
            ylabel = "Total Population"

        plt.figure(figsize=(8, 5))
        plt.bar(planet_names, counts, color='skyblue')
        plt.title(title)
        plt.xlabel("Planet")
        plt.ylabel(ylabel)
        plt.tight_layout()
        plt.show()

# Example usage and test
if __name__ == "__main__":
    universe = Universe()
    # Generate 4 planets with random populations
    for _ in range(4):
        universe.generate()

    # Show human populations
    universe.show_populations("human")
    # Show robot populations
    universe.show_populations("robot")
    # Show total populations
    universe.show_populations("anything_else")