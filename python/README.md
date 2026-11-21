# CEGE 8211 Lax-Hopf homework: Python

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

- the constructor `LaxHopf(v, K, initialCondition)` (`__init__`),
- `calculateN(t, x)`: the cumulative count N(t,x),
- `calculateK(t, x)`: the density k(t,x).

`calculateNGrid()` and `calculateKGrid()` are already written. They call your `calculateN(t, x)` and
`calculateK(t, x)` at every point of a grid.
