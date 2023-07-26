from collections import deque


def time_decoder(strt_time, current_timer):
    time = (strt_time[2] + strt_time[1] * 60 + strt_time[0] * 60 * 60 + current_timer) % (24*60*60)  # time in seconds
    hours = time // (60 * 60)
    minutes = (time % (60 * 60)) // 60
    seconds = time % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def read_products():
    result = deque()
    pr = input()
    while pr != "End":
        result.append(pr)
        pr = input()
    return result


def read_robots():
    result = {}
    string_input = input().split(";")
    for data in string_input:
        name, processing_time = data.split("-")
        result[name] = int(processing_time)
    return result


robots = read_robots()
available_robots = [k for k in robots]
start_time = [int(x) for x in input().split(":")]
products = read_products()
processing_robots = {}

timer = 0
while products:
    timer += 1

    for robot_name in [k for k in processing_robots]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] == 0:
            processing_robots.pop(robot_name)

    current_product = products.popleft()

    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f"{robot_name} - {current_product} [{time_decoder(start_time, timer)}]")
            processing_robots[robot_name] = robots[robot_name]
            break
    else:
        products.append(current_product)
