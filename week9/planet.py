# planet.py

class Human:
    """A simple Human class for demonstration."""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Human('{self.name}')"

    def __str__(self):
        return self.name

class Robot:
    """A simple Robot class for demonstration."""
    def __init__(self, model):
        self.model = model

    def __repr__(self):
        return f"Robot('{self.model}')"

    def __str__(self):
        return self.model

class Planet:
    """
    Represents a planet with human and robot inhabitants,
    stored in a single dictionary for better structure.
    """
    def __init__(self, name):
        self.name = name
        # Dictionary to store lists of humans and robots
        self.inhabitants = {
            'humans': [],
            'robots': []
        }

    def add_human(self, human):
        """Add a human object to the planet."""
        self.inhabitants['humans'].append(human)

    def remove_human(self, human):
        """Remove a human object from the planet."""
        if human in self.inhabitants['humans']:
            self.inhabitants['humans'].remove(human)

    def add_robot(self, robot):
        """Add a robot object to the planet."""
        self.inhabitants['robots'].append(robot)

    def remove_robot(self, robot):
        """Remove a robot object from the planet."""
        if robot in self.inhabitants['robots']:
            self.inhabitants['robots'].remove(robot)

    def __repr__(self):
        return (f"Planet(name='{self.name}', "
                f"inhabitants={self.inhabitants})")

    def __str__(self):
        human_names = ', '.join(str(h) for h in self.inhabitants['humans']) or "No humans"
        robot_names = ', '.join(str(r) for r in self.inhabitants['robots']) or "No robots"
        return (f"Planet: {self.name}\n"
                f"Humans: {human_names}\n"
                f"Robots: {robot_names}")

# Example usage and test
if __name__ == "__main__":
    # Create some humans and robots
    alice = Human("Alice")
    bob = Human("Bob")
    r2d2 = Robot("R2D2")
    c3po = Robot("C3PO")

    # Create a planet
    mars = Planet("Mars")

    # Add humans and robots
    mars.add_human(alice)
    mars.add_human(bob)
    mars.add_robot(r2d2)
    mars.add_robot(c3po)

    # Print informal and formal representations
    print(mars)         # Informal
    print(repr(mars))   # Formal

    # Remove a human and a robot
    mars.remove_human(bob)
    mars.remove_robot(r2d2)

    print("\nAfter removal:")
    print(mars)