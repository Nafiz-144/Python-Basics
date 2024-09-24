import time
print(time.ctime(1000000))
print(time.time())

to = time.localtime()
time = time.gmtime()
# print(to)

time.strftime(format, to)
