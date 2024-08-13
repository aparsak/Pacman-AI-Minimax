## 🚧 Work in Progress

Please note that this README is still a work in progress. I am actively working on adding more details and improving the documentation. Check back soon for updates and more comprehensive information about the project. Thank you for your patience!


# 🎮 Simple Pacman with Minimax AI

Welcome to **Simple Pacman with Minimax AI**! This project is a Python-based implementation of the classic Pacman game, enhanced with AI gameplay using the Minimax algorithm with Alpha-Beta pruning. The AI navigates Pacman through a maze, collecting points and avoiding ghosts.

## 🎬 Program Demo 
![pacman minimax demo](/demo.mp4)

## 📋 Overview

- **Minimax Algorithm with Alpha-Beta Pruning:** Advanced techniques for optimal decision-making.
- **Simple Text-Based Interface:** Easy visualization of the game and AI decisions.
- **Classic Gameplay:** Experience the nostalgia of Pacman with an intelligent twist.

## 🛠️ Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/simple-pacman-minimax.git
    ```

2. Navigate to the project directory:
    ```bash
    cd simple-pacman-minimax
    ```

3. Run the game:
    ```bash
    python pacman.py
    ```

## 🕹️ Gameplay Instructions

- The AI controls Pacman, navigating through the maze.
- Pacman earns points by eating dots and avoids ghosts.
- The game ends if Pacman collides with a ghost or all dots are eaten.

## ⚙️ How It Works

- **Minimax AI:** Evaluates possible moves by simulating both Pacman’s and the ghosts’ potential moves.
- **Alpha-Beta Pruning:** Optimizes the Minimax algorithm by eliminating unnecessary calculations, improving efficiency.
- **Scoring:** The AI aims to maximize the score by collecting points and minimizing the risk of being caught by ghosts.

## 🧠 Key Concepts

- **Manhattan Distance:** Calculates the shortest path in the grid.
- **Utility Function:** Evaluates game states based on Pacman’s proximity to points and ghosts.

## 📈 Performance

- **Depth Control:** Adjust the depth of the Minimax algorithm for better performance or more strategic gameplay.
- Modify the `depth` variable in the `pacman.py` file to experiment with different AI complexities.


## 🧠 Utility Function Explained

The **Utility Function** in the context of the Pacman game evaluates the desirability of a game state from Pacman's perspective. The AI aims to maximize this utility, leading Pacman to collect more points while avoiding ghosts. Here’s how it works:

### Components of the Utility Function

- **Ghost Distance:** 
    - The AI calculates the Manhattan distance between Pacman and the ghosts.
    - The farther away the ghosts are, the higher the utility.
    - If a ghost is very close, the utility is penalized to avoid Pacman getting caught.

- **Point Distance:** 
    - Considers how far Pacman is from the nearest point (dot).
    - Shorter distances result in higher utility, encouraging Pacman to move towards points.

- **Eaten Points:** 
    - Rewards Pacman for points already eaten, adding to the overall score.

- **Move Cost:** 
    - A small penalty for each move discourages unnecessary wandering and promotes efficient paths to points.

- **Safety Factor:** 
    - Applies severe penalties if Pacman is in a dangerous position, ensuring the AI prioritizes survival.

### Utility Function Formula

Conceptually, the utility function can be summarized as:

```plaintext
Utility = (Point Score) + (Eaten Points Score) + (Ghost Distance Score) - (Move Cost) - (Danger Penalty)
```

Where:

- **Point Score:** Positively correlates with proximity to the nearest point.
- **Eaten Points Score:** Increases as Pacman eats more points.
- **Ghost Distance Score:** Increases with distance from the nearest ghost.
- **Move Cost:** Subtracted for each move to promote efficiency.
- **Danger Penalty:** Large negative value if Pacman is in immediate danger from ghosts.

### Why It Matters

The utility function encapsulates Pacman’s strategic goals into a single numeric value, balancing the need to gather points with avoiding danger. It drives the AI's decisions to maximize Pacman’s chances of survival and success.

### Example in Action

Imagine Pacman is two tiles away from a point and three tiles away from a ghost. The utility function will weigh the benefit of collecting the point against the risk of being caught by the ghost. If the benefit outweighs the risk, the AI will choose that move. If the ghost is too close, the danger penalty will likely lead to a safer move.

### Customizing the Utility Function

You can adjust the coefficients in the utility function to experiment with different strategies:

- Increase the point score to make Pacman more aggressive in pursuing points.
- Increase the ghost penalty to make Pacman more cautious and prioritize survival.
  

## 👨‍💻 Contributing

Contributions are welcome! If you find a bug or have a feature request, feel free to open an issue or submit a pull request.
