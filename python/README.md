# CEGE 8211 Lax-Hopf homework: Python version

This folder is a Python translation of the Java project in `../java`. Classes and methods have the same
names as in Java, and each class is in a file with the same name (`LaxHopf.java` → `LaxHopf.py`).

## Requirements

Python 3.8 or newer, and matplotlib for the heat maps:

```
pip install matplotlib
```

## Running

Run from inside this `python` folder:

```
python Main.py
```

This computes N(t,x) and k(t,x) on a grid and opens a heat-map window for each. Close the windows to
end the program. Use the save icon in a window's toolbar, or `HeatMapFrame.screenshot("file.png")`,
to save a plot as an image.

## What to fill in

In `LaxHopf.py`, write the parts marked `# fill this in`:

- the constructor `LaxHopf(v, K, initialCondition)` (`__init__` in Python),
- `calculateN(t, x)`: the cumulative count N(t,x),
- `calculateK(t, x)`: the density k(t,x).

Python does not allow two methods with the same name, so `calculateN` and `calculateK` each accept
either form, as the Java overloads do: `calculateN(t, x)` returns one value, and
`calculateN(t_start, t_end, t_inc, x_start, x_end, x_inc)` returns a matrix. The matrix form is already
written; it calls your `calculateN(t, x)` at every point. You only need to write the `(t, x)` part.

`HeatMapFrame.py` replaces the Java `HeatMapFrame` and `heatMap` classes with matplotlib.
