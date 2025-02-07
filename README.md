Example Call of the Microservice:
To request data from the microservice, use zmq to connect to the /localhost:5555. Make sure the socket is of the zmq.REQ type. The message should be a string separated by a single space, with the first being the number of flashcards in the deck and the second being a float of the time of the quiz's start
<img width="345" alt="image" src="https://github.com/user-attachments/assets/4143512f-5bf6-4c43-a017-3718152465ca" />

Example Call of Microservice WITH receiving data from the microservice:
<img width="553" alt="image" src="https://github.com/user-attachments/assets/0f28b928-5af5-4349-968a-51c9eb6b12cf" />

