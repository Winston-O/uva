
while True:
    test_case =  input().split()
    if test_case == ["0","0","0","0"]:
        break
    sleep_hour = int(test_case[0])
    sleep_minute = int(test_case[1])
    alarm_hour = int(test_case[2])
    alarm_minute = int(test_case[3])

    total_sleep_minute = sleep_hour * 60 + sleep_minute if sleep_hour > 0 else (sleep_hour + 24) * 60 + sleep_minute
    total_alarm_minute = alarm_hour * 60 + alarm_minute if alarm_hour > 0 else (alarm_hour + 24) * 60 + alarm_minute
    total_rest_time = total_alarm_minute - total_sleep_minute if total_alarm_minute >= total_sleep_minute else \
        ((total_alarm_minute + (24 * 60)) - total_sleep_minute)
    print(total_rest_time)
