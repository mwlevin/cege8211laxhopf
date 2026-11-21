"""Entry point for running the project. Python version of ``laxhopf/Main.java``.

Run from the python/ folder with::

    python Main.py
"""

from HeatMapFrame import HeatMapFrame
from LaxHopf import LaxHopf


def main():
    # the order of conditions is {x_min, x_max, k}
    initialCondition = [
        [0, 500, 0.01],
        [500, 600, 0.04],
        [600, 950, 0.025],
        [950, 1000, 0.02],
    ]

    test = LaxHopf(20, 0.2, initialCondition)

    N = test.calculateN(0, 50, 1, 0, 500, 1)

    displayN = HeatMapFrame("Cumulative count", N, 50, 500, "s", "ft")

    k = test.calculateK(0, 50, 1, 0, 500, 1)

    displayK = HeatMapFrame("density", k, 50, 500, "s", "ft")

    HeatMapFrame.showAll()


if __name__ == "__main__":
    main()
