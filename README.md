# Interactive Fractal Generator (FractalDrawer)

![Static Badge](https://img.shields.io/badge/ErikBjornson-FractalsDrawer-FractalsDrawer)
![GitHub top language](https://img.shields.io/github/languages/top/ErikBjornson/FractalsDrawer)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ErikBjornson/FractalsDrawer)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/ErikBjornson/FractalsDrawer)

This GitHub repository contains a Python program that creates a graphical user interface (GUI) using the tkinter library. The GUI displays a window with two widgets: a Canvas and a ProgressBar.

## Project Overview

The program allows users to interactively generate a Chaos Game Fractal on the Canvas. Here's how it works:

1. **Setting Up Base Points**: When the Canvas is clicked once, a reference point is placed. The first three clicks place red reference points, and the fourth click places a green starting point.

2. **Generating the Fractal**: After all base points have been set up, a double-click triggers the fractal generation process. The program selects a random base point, calculates the midpoint between the starting point and the selected base point, and then draws a white point at that midpoint. The starting point is then updated to the coordinates of the newly drawn point. This process is repeated a certain number of times to create the fractal.

## Usage

1. Clone the repository to your local machine.

2. Ensure you have Python and the tkinter library installed.

3. Run the program using a Python interpreter.

4. Follow the on-screen instructions to set up base points and generate the fractal.

## Code Comments

The codebase includes comments that provide additional insights into the program's functionality. I recommend reading these comments to gain a deeper understanding of the code. The comments explain the purpose of functions, the logic behind key sections of the code, and any assumptions or considerations made during implementation.

## Dependencies

- Python 3.x

- tkinter library
