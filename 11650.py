
test_no = int(input())
for test in range (test_no) :
    time_input = input().split(":")
    mirror_minute = int(time_input[1])
    mirror_hour = int(time_input[0])
    real_minute = 60 - mirror_minute if mirror_minute > 0 else mirror_minute
    if mirror_minute == 0:
        real_hour = 12 - mirror_hour if mirror_hour < 12 else mirror_hour
    else:
        real_hour = 11 - mirror_hour if mirror_hour <= 10 else 23 - mirror_hour

    print("{:02d}:{:02d}".format(real_hour, real_minute))
