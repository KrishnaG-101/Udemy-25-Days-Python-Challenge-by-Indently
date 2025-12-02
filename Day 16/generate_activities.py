# This file contains code to help users generate activity based on their requirements.

import json
from typing import Any
from dataclasses import dataclass

@dataclass
class Activity:
    activity_name : str
    activity_type : str
    activity_cost : int
    activity_people : int


def load_activities(file_name : str) -> list[Activity]:
    activities : list[Activity] = list()
    try:
        with open(file_name, "r") as file:
            activity_dictionaries : list[dict[str, Any]] = json.load(file)
            
        for activity in activity_dictionaries:
            activities.append(
                Activity(
                    activity_name = activity["activity"],
                    activity_type = activity["type"],
                    activity_cost = activity["cost"],
                    activity_people = activity["people"],
                )
            )
    except FileNotFoundError as error:
        print(f"\n{error}\nThe file cannot be found in the specified path. Returning empty list of Activities.\n")
    except KeyError as error:
        print(f"\n{error}\nThe file is not in proper format. Returning empty or partial list of Activities.\n")
    
    return activities

def generate_activities(activity_list : list[Activity]) -> None:
    # 1. Input
    # Taking user inputs for activity cost, type and number of people participating.
    try:
        activity_type_input : str = input("\nEnter the type of activity you want to participate in (indoor or outdoor): ").lower().strip()
        activity_cost_input : int = int(input("Enter your budget for the activity (per person): "))
        activity_people_input : int = int(input("Enter the number of people participating in the activity: "))
    except ValueError as error:
        print(f"\n{error}\nPlease only enter numerical values.\n")
        return None
    
    # 2. Calculation / Processsing
    # fixing input errors for activity type input.
    if "i" in activity_type_input:
        activity_type_input = "indoor"
    else:
        activity_type_input = "outdoor"
    
    # will contain activities that match user's requirements.
    matched_activities : list[Activity] = list()
    
    # for checing which activities meet user's requirements.
    for activity in activity_list:
        if ((activity.activity_cost <= activity_cost_input) and \
            (activity.activity_people <= activity_people_input) and \
            (activity.activity_type == activity_type_input)):
            
            matched_activities. append(activity)
    
    # 3. Output
    # Printing output
    print()
    if matched_activities:
        for index, activity in enumerate(matched_activities, start=1):
            print(f"{index}. {activity.activity_name}: {activity.activity_cost}$ per person [{activity_people_input}p : {activity_people_input * activity.activity_cost}$]")
    else:
        print("No activities meet your requirements.")
    print()
    
    return None

def main() -> None:
    activities_loaded : list[Activity] = load_activities("./activities.json")
    generate_activities(activity_list=activities_loaded)


if __name__ == "__main__":
    main()

# We can add more to activity type in json file, make activity type a list containing the attributes of the activity. e.g. activity_type = ("indoor", "adventure", "gambling", "etc.")
# Instead of creating a list for matched activites we can directly print the activities and use a simple boolean variable to check if any activity was matched.
# Add more annotations and docstrings.