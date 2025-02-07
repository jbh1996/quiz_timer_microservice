import zmq


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
socket.send_string(time_string)
message = socket.recv_string()
