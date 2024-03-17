import json
import os
# here i am setting up a json object for the main menu

main_menu_info = {
    "r" : "Register a user",
    "a" : "Adding a task",
    "va" : "View all tasks",
    "vm" : "View my task(s)",
    "gr" : "Generate reports",
    "ds" : "Display statistics",
    "e" : "Exit"
}

with open("mainmenu_info.json", "w") as jsonfile:
    json.dump(main_menu_info, jsonfile)
    mainmenu_file_path = os.path.basename("./mainmenu_info.json")
    print(f"Written successfully to {mainmenu_file_path}")