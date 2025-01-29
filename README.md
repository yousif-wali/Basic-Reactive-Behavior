# E-Puck Robot Navigation

## Overview

This project programs an **E-Puck** robot to navigate its environment by detecting obstacles and adjusting its movement accordingly. The robot follows a predefined behavior:

1. Moves **straight forward** until it detects an object within **5 cm**.
2. Performs a **180-degree turn** when it encounters the first obstacle (within **1.5 seconds**).
3. Continues forward and upon detecting a second object within **5 cm**, it executes a **90-degree right turn** (within **0.75 seconds**).
4. Stops when the left-side sensor detects that the object has been passed.

## Requirements

- **Webots** robotics simulator
- **Python (3.x)**
- **E-Puck Controller**

## Installation

Ensure you have Webots installed and configured with Python support. Clone this repository and run the script within the Webots environment.

```bash
git clone https://github.com/yousif-wali/basic-reactive-behavior.git
cd basic-reactive-behavior
```

## Code Breakdown

### Constants
- `TIME_STEP = 64` → Defines the time step for the robot controller.
- `MAX_SPEED = 3.14` → Sets the robot's maximum allowed speed.
- `FIVE_CM_THRESHOLD = 306` → Sensor threshold to detect objects within **5 cm**.

### Sensors
- The robot initializes **8 proximity sensors** (`ps0` to `ps7`), where:
  - `ps0` (front-left) and `ps7` (front-right) detect obstacles.
  - `ps5` checks if the object has been passed.

### Movement Behavior
- **Follow Mode (`FOLLOW`)**: The robot moves forward until an obstacle is detected.
- **Rotate 180 (`ROTATE180`)**: Turns **180 degrees** if it detects an object within **5 cm**.
- **Rotate 90 (`ROTATE90`)**: Turns **90 degrees right** when encountering a second object.

## Running the Simulation

Run the script in the Webots environment:

```bash
python robot_controller.py
```

## License

This project is licensed under the MIT License.
