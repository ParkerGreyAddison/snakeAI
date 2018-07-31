# snakeAI

###### July 30 
> I redesigned the snake game again.  I feel bad for doing this since it seems redundant, but I realized that the reason I was making zero progress on the actual neural net was because I kept running into roadblocks in the game code.
>
> I massively simplified the code for the game, making it more efficient and easier to access/create observations.
>
> I have a few approaches in mind for the AI implementation:
> 1. Provide the entire game board and the score as input nodes (starting small-ish at 8x8 or 10x10)
> 2. Generate observations e.g. adjacency to a collision in each of the 4 directions, direction towards food, etc.  This would be much faster but would pretty much feel like playing the snake game in first person.
> 3. Provide the entire game board *and* some observations, as a sort of helping hand to mimic patters that a human would see quickly.  Even though this is more information than the first approach, I would be interested in seeing if this progresses in less time than the first approach since some general rules would be much easier to figure out.
