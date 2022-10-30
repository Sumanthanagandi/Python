command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car is already started!")
        else:
            started = True
            print("The car has started")
    elif command == "stop":
        if not started:
            print("The car is already stopped")
        else:
            started = False
            print("The car has stopped")
    elif command == "help":
        print("""
start - To Start the car
stop - To Stop the car
quit - To Quit
        """)
    elif command == "quit":
        break
    else:
        print("I Don't understand that!")
