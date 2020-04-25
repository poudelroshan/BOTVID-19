# This is used to print current database contents to the screen

import sys
import user_database, state_database, scrape

try:
    command = sys.argv[1]
    if command != "":
        if command == "get_total_users()":
            print("Total users: ", user_database.get_total_users())
        elif command == "get_users()":
            print("Following is the user list:")
            for users in user_database.get_users():
                print(users)
        elif command == "get_update_data()":
            print(state_database.get_tabulated_data())
        elif command == "get_all_state_data()":
            print(state_database.get_all_state_data())
        elif command == "help":
            print("* get_total_users() : prints total users in the database\n")
            print("* get_users() : prints a list of users in the database\n")
            print("* get_update_data(): prints the current data to be sent to users\n")
            print("* get_all_state_data(): prints everything stored in state database\n")
            print("* help: prints all available commandline inputs")
        else:
            print("* Sorry, the command you asked for is not listed\n")
            print("* use 'help' to get a list of available commands\n")
except:
    print("* This script is used for checking database contents\n")
    print("* Please call this script with a commandline argument\n")
    print("* use 'help' as a commandline argument to learn about available commandline arguments\n")
    
        
        
