1.   Description of Classes

	1) Board : This class initializes the board for the game by setting up the platgorm , sky, coins etc
	2) Person : All the characters of the game inherit from this 

	3) Player : Inheritted from the person class, The user controls this character and thereforw this has certain extra functions like mving left, right, collecting coins etc

	4) Enemy : The Enemy Class inherits the Person class. The class creates and manages the boss enemy that has several lives and need to be killed 

	5) Obstacles: This class manages and controls the obstacles(fire beam and magnet)


2.   Rules of the game

	
	2) Collect coins to get more points
	3) You get 4 lives and a timer to predict ur final score.
	4) In the end ,the boss will shoot ice 
	5) you have to kill the boss in the given time to win the game
	6) kill the boss with bullets and toss the ice 



4.   How to play 

	1)python3 game.py

	2) press a to move left, w to move up, d to moe right, s to shoot bullets, spacebar to activate shield and b to double up the speed