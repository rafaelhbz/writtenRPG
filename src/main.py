import json
from package_checker import check_and_install_packages

class Character:
    def __init__(self, name):
        self.name = name
        self.traits = {
            "Trait1": 50,
            "Trait2": 50,
            "Trait3": 50,
            "Trait4": 50,
            "Trait5": 50,
            "Trait6": 50,
            "Trait7": 50
        }

    def update_trait(self, trait, value):
        if trait in self.traits:
            self.traits[trait] += value
            print(f"{self.name}'s {trait} has been updated to {self.traits[trait]}")
        else:
            print("Trait not found.")

# Load scenarios from JSON file
def load_scenarios_from_json(file_path):
    with open(file_path, 'r') as file:
        scenarios = json.load(file)
    return scenarios

# Main game function
def play_game(character, scenarios):
    current_scenario_id = 1
    while True:
        # Find the current scenario
        current_scenario = next((s for s in scenarios if s["id"] == current_scenario_id), None)
        if current_scenario is None:
            print("Scenario not found!")
            break
        
        # Display scenario information
        print(f"\n{current_scenario['title']}")
        print(current_scenario['description'])
        
        # Display options
        print("\nOptions:")
        for i, option in enumerate(current_scenario['options'], start=1):
            print(f"{i}. {option['text']}")
        
        # Get player choice
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= len(current_scenario['options']):
            next_scenario_id = current_scenario['options'][choice - 1]['next_scenario_id']
            # Update character traits based on choice
            # For example:
            # character.update_trait("Trait1", 10)
            current_scenario_id = next_scenario_id
        else:
            print("Invalid choice. Please try again.")

def main():
    # List of required packages
    required_packages = ["numpy", "pandas", "matplotlib", "arrow"]

    # Check and install missing packages
    check_and_install_packages(required_packages)

    # Load scenarios from JSON file
    scenarios = load_scenarios_from_json('scenarios.json')

    # Initialize character
    main_character = Character("YourCharacterName")

    # Start playing the game
    play_game(main_character, scenarios)

if __name__ == "__main__":
    main()
