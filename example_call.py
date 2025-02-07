import zmq
import time
import random

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for num in range(10):
    start_time = time.time()
    start_time -= random.randint(15, 700)
    flash_cards = random.randint(6, 50)
    print(f"Sending request for {flash_cards} flash cards, and time: {start_time}")
    time_string = f"{flash_cards} {start_time}"
    socket.send_string(time_string)
    message = socket.recv_string()
    print(message)