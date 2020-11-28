test_case = int(input()) #<=100
count = 0
for test in range (test_case):
    test_input = input().split(" ")
    bus_no = int(test_input[0])

    current_time = test_input[1]
    current_time_list = current_time.split(":")
    current_hour = int(current_time_list [0])
    current_minute = int(current_time_list [1]) + ( int(current_time_list [0]) * 60 )
    min_time = 9999999
    #min_time = 0
    for bus_time in range (bus_no): #1<=bus_no<=100
        time_input = input().split(" ")
        bus_arrival = time_input [0]
        travel_time = int(time_input [1]) #0<=travel_time<=1000
        wait_time = bus_arrival.split(":")
        wait_hour = int(wait_time [0])
        wait_minute = int(wait_time [1]) + (int(wait_time [0]) * 60)

        if wait_minute < current_minute:
            wait_minute += (24 * 60)

        home_time = ( wait_minute - current_minute ) + travel_time

        if min_time == 0 or home_time <= min_time :
            min_time = min(min_time, home_time)
            #min_time = home_time

    count += 1

    print ("Case {}: {}".format(count, min_time))
