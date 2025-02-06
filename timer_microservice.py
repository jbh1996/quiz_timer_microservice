import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv_string()
    working_array = message.split()
    flashcards = int(working_array[0])
    start_time = float(working_array[1])
    cur_time = time.time()
    elapsed_time = cur_time - start_time
    elapsed_time = round(elapsed_time)
    average_time = elapsed_time/ flashcards
    average_time = round(average_time)
    minutes = elapsed_time / 60
    minutes = round(minutes)
    response_string = f"{elapsed_time} {average_time} {minutes}"
    time.sleep(1)
    socket.send_string(response_string)