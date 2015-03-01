from PreClass.runner import Runner

while True:
    error_msg = "Please try again, Select an option using the numbers provided"

    print(("\n"
           "\tIP management Tool\n"
           "\t1 - Add a Network (CIDR)\n"
           "\t2 - Add a Host (IP)\n"
           "\t3 - Show hosts in network\n"
           "\t4 - Flush networks and hosts \n"
           "\t5 - Quit\n"
           "\t"
    ))
    try:
        valid = [1, 2, 3, 4, 5]
        action = int(input("Please select an option ->"))
        if action in valid:
            if action == 1:
                Runner.add_network()
            elif action == 2:
                Runner.add_host()
            elif action == 3:
                Runner.show_hosts()
            elif action == 4:
                Runner.flush_data()
            elif action == 5:
                print("Good bye")
                exit()
            else:
                print(error_msg)
        else:
            print(error_msg)
    except ValueError:
        print(error_msg)
