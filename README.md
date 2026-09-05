# N-Body-gravity-simulator



\# 🌌 N-Body Gravity Simulator



\### A visual experiment in gravitational chaos, motion, and interaction.



What happens when multiple objects in space are allowed to interact only through gravity?



That is the question behind this project.



The N-Body Gravity Simulator is an interactive Python-based simulation that models multiple bodies moving through space while continuously influencing one another through gravitational forces.



Instead of simply displaying an animation, the project calculates the gravitational interaction between every body at every simulation step and turns those calculations into a real-time visual experience.



\---



\## 🚀 The Idea



Imagine placing several objects in an empty universe.



Each object has:



\- Mass

\- Position

\- Velocity



There are no predefined paths.



There are no fixed orbits.



Every body continuously responds to every other body.



A tiny change in position changes the gravitational force, which changes the velocity, which changes the next position.



And that process continues thousands of times.



The result is a system where simple physical rules can produce surprisingly complex motion.



\---



\## 🧠 How It Works



The simulator calculates gravitational acceleration using Newton's law of universal gravitation.



The gravitational force between two bodies follows:



\*\*F = G × (m₁ × m₂) / r²\*\*



For every simulation step, the program:



1\. Calculates the distance between bodies.

2\. Determines the gravitational influence of every other body.

3\. Calculates the resulting acceleration.

4\. Updates the velocity.

5\. Updates the position.

6\. Draws the new state on the screen.

7\. Repeats the process.



This creates the continuously evolving motion seen in the simulation.



\---



\## 🪐 What We Built



The project was developed progressively rather than being created as one large program.



\### V1 — Physics Engine



The first version focused on getting the mathematics working.



It introduced:



\- Multiple bodies

\- Gravitational interaction

\- Position updates

\- Velocity updates

\- Numerical simulation

\- Real-time animation



The goal was simple:



\*\*Make the physics work first.\*\*



\---



\### V2 — Interactive Visualization



Once the physics was working, the simulation was upgraded visually.



We added:



\- Motion trails

\- Simulation information

\- Pause / Play

\- Reset

\- Simulation speed control

\- Improved visualization



The project started becoming an interactive simulation instead of just a physics calculation.



\---



\### V3 — Visual Experience



The next iteration focused on making the simulation more visually engaging.



We introduced:



\- Space-like background

\- Hundreds of background stars

\- Longer particle trails

\- Simulation timer

\- Real-time energy calculation

\- Improved presentation



The goal became:



\*\*Make the mathematics something people can actually see and explore.\*\*



\---



\### V4 — Interactive Portfolio Edition



The final version added another layer of interaction.



Current features include:



\- 🌌 Multi-body gravitational simulation

\- 🪐 Multiple interacting bodies

\- ✨ Star-field background

\- 🌀 Motion trails

\- ⏯️ Pause / Play

\- 🔄 Reset

\- ⚡ Adjustable simulation speed

\- 📊 Real-time simulation statistics

\- ⚙️ Total energy calculation

\- 🖱️ Interactive body selection

\- 📍 Position information

\- 🚀 Velocity information

\- 🔭 Real-time animation



\---



\## 🎮 Controls



| Control | What it does |

|---|---|

| \*\*PAUSE / PLAY\*\* | Stops or resumes the simulation |

| \*\*RESET\*\* | Returns the system to its initial state |

| \*\*SPEED\*\* | Changes simulation speed |

| \*\*Mouse Click\*\* | Selects a nearby body and displays its information |



\---



\## 📊 Simulation Information



The interface displays live information such as:



\- Simulation time

\- Number of bodies

\- Gravitational constant

\- Total system energy

\- Current simulation speed



Selecting a body also displays information about that body, including:



\- Mass

\- Position

\- Velocity



\---



\## 🛠️ Technologies



This project was built using:



\- \*\*Python\*\*

\- \*\*NumPy\*\*

\- \*\*Matplotlib\*\*



\### NumPy



Used for numerical calculations and efficient handling of positions, velocities, and physical quantities.



\### Matplotlib



Used to create the real-time visualization, animation, controls, and interactive interface.



\---



\## 📁 Project Structure



```text

n-body-gravity-simulator/

│

├── main.py

├── README.md

└── .gitignore

