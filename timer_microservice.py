import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


def process_string(input_message):
    """
    Processes input string and returns elapsed time in seconds,
    average time in seconds
    and minutes as concatenated string separated by a space
    """
    try:
        working_array = input_message.split()
        flashcards = int(working_array[0])
        start_time = float(working_array[1])
        cur_time = time.time()
        elapsed_time = cur_time - start_time
        elapsed_time = round(elapsed_time)
        average_time = elapsed_time / flashcards
        average_time = round(average_time)
        minutes = elapsed_time / 60
        minutes = round(minutes)
        socket.send_string(f"{elapsed_time} {average_time} {minutes}")
    except:
        socket.send_string("Error")


while True:
    message = socket.recv_string()
    print(f"Received Message: {message}")
    process_string(message)

