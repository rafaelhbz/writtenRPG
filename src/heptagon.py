import numpy as np
import matplotlib.pyplot as plt

class HeptagonCreator:
    def __init__(self, radius, center=(0, 0), num_heptagons=4):
        self.radius = radius
        self.center = center
        self.num_heptagons = num_heptagons
        self.labels = []

    def regular_heptagon(self, radius):
        """Generate coordinates for a regular heptagon."""
        angles = np.linspace(0, 2 * np.pi, 8)[:-1]
        x = radius * np.cos(angles) + self.center[0]
        y = radius * np.sin(angles) + self.center[1]
        return x, y

    def generate_heptagons(self):
        """Generate coordinates for concentric heptagons."""
        heptagons = []
        for i in range(self.num_heptagons):
            smaller_radius = self.radius * (1 - i / self.num_heptagons)
            x, y = self.regular_heptagon(smaller_radius)
            heptagons.append((x, y))
        return heptagons

    def plot_heptagons(self):
        """Plot concentric heptagons."""
        heptagons = self.generate_heptagons()
        for x, y in heptagons:
            plt.plot(x, y, color='black')  # Paint borders

        # Set axis equal and remove grid
        plt.axis('equal')
        plt.grid(False)

        # Show plot
        plt.show()

# Parameters
radius = 1  # Radius of the largest heptagon
num_heptagons = 4  # Number of concentric heptagons

# Create HeptagonCreator instance
creator = HeptagonCreator(radius, num_heptagons=num_heptagons)

# Plot concentric heptagons
creator.plot_heptagons()
