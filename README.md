# Wordle Solver Project Overview

## Objective
The project aimed to create an efficient Wordle solver using Python, focusing on optimizing strategies to solve the word puzzle game with minimal guesses.

## Methods

- **Preparation**: Filtered a Scrabble word list to include only 5-letter words.
- **Simulation**: Implemented a Python-based Wordle game to evaluate guesses and outcomes.
- **Optimization**: Employed frequency analysis and a letter score method, along with a hybrid approach combining both techniques.

## Results

- **Simulation**: Tested over 5000 Wordle game sessions.
- **Findings**: 
  - The hybrid approach was most effective, achieving a higher win rate.
  - The average number of guesses required per game was significantly reduced using the hybrid method compared to standalone frequency analysis or letter score methods.
- **Numerical Outcomes**:
  - **Hybrid Approach**: Achieved a win rate of 98.68% with an average of 3.88 guesses per game.
  - **Frequency Analysis and Letter Score Methods**: Showed lower efficiency, with win rates and average guesses not surpassing the hybrid's performance.


## Code
Please view the [Jupyter Notebook](https://github.com/srogalsky8/wordle-ai/blob/main/WordleSolver.ipynb) for detailed code and methodology.
