"""Entry point for running the project. Python version of ``laxhopf/Main.java``.

Run from the python/ folder with::

    python main.py
"""

import heatmap_frame
from heatmap_frame import HeatMapFrame
from laxhopf import LaxHopf


def main():
    # the order of conditions is [x_min, x_max, k]
    initial_condition = [
        [0, 500, 0.01],
        [500, 600, 0.04],
        [600, 950, 0.025],
        [950, 1000, 0.02],
    ]

    test = LaxHopf(20, 0.2, initial_condition)

    N = test.calculate_n_grid(0, 50, 1, 0, 500, 1)

    display_n = HeatMapFrame("Cumulative count", N, 50, 500, "s", "ft")

    k = test.calculate_k_grid(0, 50, 1, 0, 500, 1)

    display_k = HeatMapFrame("density", k, 50, 500, "s", "ft")

    heatmap_frame.show()


if __name__ == "__main__":
    main()
