# paddleBall
This is a modified version of a paddle ball game from "Hello World" (3rd ed.) by Warren and Carter Sande.
Most of the mechanics are the same, but the visuals and some gameplay mechanics have been changed.

-Josef Gisis 08/28/2023

Changes:
1. A "get ready" message has been added before each new ball is released. 
2. The ball is changed from an image to a Pygame surface object to give the game a more retro look.
3. The lives are displayed as these surfaces as well. 
4. The paddle is assigned a width variable to allow it to be shrunk to later increase the difficulty
5. The timer triggers an increase in the frame rate as well as shrinks the width of the paddle to
increase the difficulty (the paddle width is scalable to 0, at which point, the player is presumed to
have lost).
6. The ball is checked to see if it has hit the side of the paddle, at which point it bounces off the side.
