from collections import deque

command = input()
clients_queue = deque()
while command != "End":
    if command == "Paid":
        while clients_queue:
            print(clients_queue.popleft())
    else:
        clients_queue.append(command)
    command = input()
print(f"{len(clients_queue)} people remaining.")
