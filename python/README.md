# CEGE 8211 Lax-Hopf homework: Python version

This folder is a Python translation of the Java project in `../java`.

## Requirements

Python 3.8 or newer, and matplotlib for the heat maps:

```
pip install matplotlib
```

## Running

Run from inside this `python` folder:

```
python main.py
```

This computes N(t,x) and k(t,x) on a grid and opens a heat-map window for each. Close the windows to
end the program. Use the save icon in a window's toolbar to save the plot as an image.

## What to fill in

In `laxhopf.py`, write the parts marked `# fill this in`:

- `LaxHopf.__init__(v, K, initial_condition)`: store the inputs and compute the initial cumulative counts.
- `calculate_n(t, x)`: the cumulative count N(t,x), from the Lax-Hopf formula.
- `calculate_k(t, x)`: the density k(t,x).

`calculate_n_grid()` and `calculate_k_grid()` are already written. They call your methods at every
point of the grid.

| Java                                   | Python                                    |
|----------------------------------------|-------------------------------------------|
| `Main.java`                            | `main.py`                                 |
| `LaxHopf.java`                         | `laxhopf.py`                              |
| `calculateN(t, x)`, `calculateK(t, x)` | `calculate_n(t, x)`, `calculate_k(t, x)`  |
| `calculateN(t_start, ..., x_inc)`      | `calculate_n_grid(t_start, ..., x_inc)`   |
| `calculateK(t_start, ..., x_inc)`      | `calculate_k_grid(t_start, ..., x_inc)`   |
| `HeatMapFrame.java` and `heatMap/`     | `heatmap_frame.py` (uses matplotlib)      |
