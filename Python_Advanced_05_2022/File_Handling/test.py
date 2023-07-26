import time
import os
# from time import sleep

# for _ in range(10):
#     file = open("dem.txt", "a")
#     localtime = time.localtime()
#     result = time.strftime("%I:%M:%S %p", localtime)
#     file.write(result)
#     file.write(os.linesep)
#     sleep(2)
#     file.close()
for _ in range(10):
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)
    print("\r", end="")
    time.sleep(2)
