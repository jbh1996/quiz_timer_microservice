<p>To request data from the microservice, use zmq to connect to the /localhost:5555. Make sure the socket is of the zmq.REQ type. The message should be a string separated by a single space, with the first being the number of flashcards in the deck and the second being a float of the time of the quiz's start.</p>

<p>Example Call of the Microservice:
<img width="345" alt="image" src="https://github.com/user-attachments/assets/4143512f-5bf6-4c43-a017-3718152465ca" /></p>

<p>To receive data back from the microservice use the socket to receive a string back from the microservice. The return value will be a string of integers with the elapsed time in seconds, the average time per flashcard, and the time elapsed in minutes all separated by spaces.</p>

<p>Example Call of Microservice WITH receiving data from the microservice:
<img width="553" alt="image" src="https://github.com/user-attachments/assets/0f28b928-5af5-4349-968a-51c9eb6b12cf" /></p>

<p>UML Diagram:
<img width="1339" alt="image" src="https://github.com/user-attachments/assets/6c1b35e5-f945-4353-9a7d-0684e2e150ba" /></p>


