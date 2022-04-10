import time

# convert a time expressed in seconds since epoch to a readable string
# epoch = when your computer thinks time began (reference point)
print(time.ctime(0))

# return current seconds since epoch
print(time.time())

# current date, hour..
print(time.ctime(time.time()))

time_object = time.localtime()
time_object = time.gmtime()     # UTC time

print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)


time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)


# tuple -> day, hour
# (year, month, day, hours, minnutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)


# tuple -> number(seconds)
# (year, month, day, hours, minnutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)



