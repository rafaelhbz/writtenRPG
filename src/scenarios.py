import json

# Define scenarios
scenarios = [
    {
        "id": 1,
        "title": "Apartament in São Paulo",
        "description": "This is your last day in Brazil, you are lying down in your sofa and looking at the celling. \n You packed your bags. Everything is ready, now you just need to sleep to wake up on up early tomorrow",
        "options": [
            {"text": "Sleep", "next_scenario_id": 2}
        ]
    },
    {
        "id": 2,
        "title": "Wake up",
        "description": "You wake up early as planned, but you checked on the fridge and there is nothing to eat. \n You check the time on your Iph  one, you have 8 hours until your flight. \Are you going to supermarket and buy supplies, ",
        "options": [
            {"text": "Explore further into the cave", "next_scenario_id": 4},
            {"text": "Retreat from the cave", "next_scenario_id": 5}
        ]
    },
    {
        "id": 3,
        "title": "Safe Travels",
        "description": "You continue on your journey, leaving the mysterious cave behind. The path ahead is clear.",
        "options": []
    },
    # Add more scenarios as needed
]

# Write scenarios to a JSON file
with open("scenarios.json", "w") as f:
    json.dump(scenarios, f, indent=4)
