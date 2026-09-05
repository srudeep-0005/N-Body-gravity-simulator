import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider

# ============================================================
# N-BODY GRAVITY SIMULATOR — V4
# Interactive Portfolio Edition
# ============================================================

G = 1.0
BASE_DT = 0.01
SOFTENING = 0.15

# ---------------------- INITIAL SYSTEM ----------------------

initial_masses = np.array([1000.0, 1.0, 0.5, 0.3])

initial_positions = np.array([
    [0.0, 0.0],
    [10.0, 0.0],
    [-8.0, 0.0],
    [0.0, 12.0]
], dtype=float)

initial_velocities = np.array([
    [0.0, 0.0],
    [0.0, 9.0],
    [0.0, -10.0],
    [-7.0, 0.0]
], dtype=float)

masses = initial_masses.copy()
positions = initial_positions.copy()
velocities = initial_velocities.copy()

paused = False
simulation_time = 0.0
speed_multiplier = 1.0

trail_length = 300

trail_x = [[] for _ in masses]
trail_y = [[] for _ in masses]

selected_body = None


# ============================================================
# PHYSICS
# ============================================================

def calculate_accelerations(pos):

    accelerations = np.zeros_like(pos)

    for i in range(len(masses)):

        for j in range(len(masses)):

            if i == j:
                continue

            displacement = pos[j] - pos[i]

            distance_squared = (
                np.sum(displacement ** 2)
                + SOFTENING ** 2
            )

            distance = np.sqrt(distance_squared)

            accelerations[i] += (
                G
                * masses[j]
                * displacement
                / (distance_squared * distance)
            )

    return accelerations


def calculate_energy():

    kinetic = 0.5 * np.sum(
        masses[:, None] * velocities ** 2
    )

    potential = 0.0

    for i in range(len(masses)):

        for j in range(i + 1, len(masses)):

            distance = np.linalg.norm(
                positions[j] - positions[i]
            )

            distance = max(distance, SOFTENING)

            potential -= (
                G * masses[i] * masses[j] / distance
            )

    return kinetic + potential


# ============================================================
# RESET
# ============================================================

def reset_simulation(event=None):

    global positions
    global velocities
    global masses
    global simulation_time
    global selected_body

    positions = initial_positions.copy()
    velocities = initial_velocities.copy()
    masses = initial_masses.copy()

    simulation_time = 0.0
    selected_body = None

    for i in range(len(masses)):
        trail_x[i].clear()
        trail_y[i].clear()

    status_text.set_text("● RUNNING")
    selection_text.set_text("NO BODY SELECTED")


# ============================================================
# PAUSE / PLAY
# ============================================================

def toggle_pause(event=None):

    global paused

    paused = not paused

    if paused:
        status_text.set_text("● PAUSED")
    else:
        status_text.set_text("● RUNNING")


# ============================================================
# SPEED
# ============================================================

def change_speed(value):

    global speed_multiplier

    speed_multiplier = value


# ============================================================
# BODY SELECTION
# ============================================================

def select_body(event):

    global selected_body

    if event.inaxes != ax:
        return

    if event.xdata is None or event.ydata is None:
        return

    mouse_position = np.array([
        event.xdata,
        event.ydata
    ])

    distances = np.linalg.norm(
        positions - mouse_position,
        axis=1
    )

    closest = np.argmin(distances)

    # Only select if reasonably close
    if distances[closest] < 1.5:

        selected_body = closest

        selection_text.set_text(
            f"BODY {closest + 1}  |  "
            f"MASS {masses[closest]:.2f}  |  "
            f"POS ({positions[closest,0]:.2f}, "
            f"{positions[closest,1]:.2f})  |  "
            f"VEL {np.linalg.norm(velocities[closest]):.2f}"
        )


# ============================================================
# ANIMATION UPDATE
# ============================================================

def update(frame):

    global positions
    global velocities
    global simulation_time

    if not paused:

        dt = BASE_DT * speed_multiplier

        acceleration = calculate_accelerations(
            positions
        )

        velocities += acceleration * dt

        positions += velocities * dt

        simulation_time += dt

        for i in range(len(masses)):

            trail_x[i].append(
                positions[i, 0]
            )

            trail_y[i].append(
                positions[i, 1]
            )

            if len(trail_x[i]) > trail_length:

                trail_x[i].pop(0)
                trail_y[i].pop(0)

            trails[i].set_data(
                trail_x[i],
                trail_y[i]
            )

    scatter.set_offsets(positions)

    energy = calculate_energy()

    info_text.set_text(
        f"TIME       {simulation_time:8.2f}\n"
        f"BODIES     {len(masses):8d}\n"
        f"GRAVITY    {G:8.2f}\n"
        f"ENERGY     {energy:8.2f}\n"
        f"SPEED      {speed_multiplier:8.2f}x"
    )

    return [
        scatter,
        *trails,
        info_text,
        status_text,
        selection_text
    ]


# ============================================================
# VISUALIZATION
# ============================================================

plt.style.use("dark_background")

fig, ax = plt.subplots(
    figsize=(12, 10)
)

fig.subplots_adjust(
    bottom=0.20
)

ax.set_facecolor("#02040a")

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

ax.set_aspect("equal")

ax.set_title(
    "N-BODY GRAVITY SIMULATOR",
    fontsize=22,
    fontweight="bold",
    pad=18
)

ax.text(
    0.5,
    1.01,
    "INTERACTIVE MULTI-BODY GRAVITATIONAL DYNAMICS",
    transform=ax.transAxes,
    ha="center",
    fontsize=9,
    alpha=0.6
)

ax.set_xlabel(
    "X POSITION",
    fontsize=9
)

ax.set_ylabel(
    "Y POSITION",
    fontsize=9
)

ax.grid(alpha=0.08)


# ============================================================
# STAR FIELD
# ============================================================

np.random.seed(7)

star_count = 600

stars_x = np.random.uniform(-30, 30, star_count)
stars_y = np.random.uniform(-30, 30, star_count)
stars_size = np.random.uniform(1, 7, star_count)
stars_alpha = np.random.uniform(0.15, 0.8, star_count)

ax.scatter(
    stars_x,
    stars_y,
    s=stars_size,
    alpha=stars_alpha,
    linewidths=0
)


# ============================================================
# BODIES
# ============================================================

sizes = np.array([
    1000,
    85,
    60,
    50
])

scatter = ax.scatter(
    positions[:, 0],
    positions[:, 1],
    s=sizes,
    alpha=0.95
)


# ============================================================
# TRAILS
# ============================================================

trails = []

for i in range(len(masses)):

    line, = ax.plot(
        [],
        [],
        linewidth=1.3,
        alpha=0.5
    )

    trails.append(line)


# ============================================================
# INFORMATION
# ============================================================

info_text = ax.text(
    0.025,
    0.96,
    "",
    transform=ax.transAxes,
    verticalalignment="top",
    fontsize=10,
    family="monospace"
)

status_text = ax.text(
    0.975,
    0.96,
    "● RUNNING",
    transform=ax.transAxes,
    verticalalignment="top",
    horizontalalignment="right",
    fontsize=10,
    family="monospace"
)

selection_text = ax.text(
    0.5,
    0.02,
    "NO BODY SELECTED",
    transform=ax.transAxes,
    horizontalalignment="center",
    fontsize=9,
    family="monospace"
)


# ============================================================
# BUTTONS
# ============================================================

pause_ax = fig.add_axes(
    [0.25, 0.065, 0.14, 0.055]
)

reset_ax = fig.add_axes(
    [0.41, 0.065, 0.12, 0.055]
)

pause_button = Button(
    pause_ax,
    "PAUSE / PLAY"
)

reset_button = Button(
    reset_ax,
    "RESET"
)

pause_button.on_clicked(
    toggle_pause
)

reset_button.on_clicked(
    reset_simulation
)


# ============================================================
# SPEED SLIDER
# ============================================================

speed_ax = fig.add_axes(
    [0.60, 0.085, 0.25, 0.025]
)

speed_slider = Slider(
    speed_ax,
    "SPEED",
    0.1,
    3.0,
    valinit=1.0
)

speed_slider.on_changed(
    change_speed
)


# ============================================================
# MOUSE INTERACTION
# ============================================================

fig.canvas.mpl_connect(
    "button_press_event",
    select_body
)


# ============================================================
# START
# ============================================================

animation = FuncAnimation(
    fig,
    update,
    interval=16,
    blit=True,
    cache_frame_data=False
)

plt.show()