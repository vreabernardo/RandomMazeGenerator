# RandomMazeGenerator

This is a simple maze generator created using Python and Pygame. It generates a maze using the Recursive Backtracking algorithm, and the user can watch as the algorithm creates the maze and navigates through the cells until it reaches the end.

<p align="center">
    <img width=45% src="https://user-images.githubusercontent.com/45080358/219528690-c872c9ed-b7d4-4446-a954-3ddc036a1fce.gif">
</p>


Pseudocode:

Choose a starting cell at random and mark it as visited.

While there are unvisited cells:

  a. Choose a random neighbor of the current cell that has not been visited.
  
  b. If all neighbors have been visited or there are no neighbors, backtrack to the previous cell.
  
  c. Mark the chosen neighbor as visited and remove the wall between the current cell and the chosen neighbor.
  
  d. Set the chosen neighbor as the current cell.

Done.
