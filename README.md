# DungeonExplorer
Trying to make an ai that explores a randomly generated maze

## The Process
### The Basic Environment
One of the biggest hurdles thats stopped me from starting this project is creating the randomly generated maze. I'm not exactly sure how to efficiently create and store a valid puzzle. Unfortunately I have to decide on a structure before beginning on the agent so Ill be starting here with a simple start and end point maze with no flourishes.

### The Agent
I want to create a goal based agent with a simple state space that it builds on its own without and hard coding of maze size or edges. As it visits each coordinate of the maze it will log any information it gains (paths, doors, etc.) and use that to explore the maze searching for the exit.

### The Future
For now my plan is to make a simple maze but I will expand on that in the future. I want to add doors with keys with the possiblility that some keys only work on specific doors. I want to add obstacles and items that are nessecary to pass them. At first the agent will simply randomly try any item in its inventory on any obstacle, but after completion of the obstacle functionality I hope to add a machine learning aspect to its logic functions.

## The Code
I will be using a MVC structure for the maze Explorer as I plan on needing to change huge parts of the structure in the future. I expect my original algorithms will not be efficient enough to scale effectively and hopefully will fix that eventually. The core library will be constructed in python but I may revisit and port it to other languages such as javascript for distribution on the web
