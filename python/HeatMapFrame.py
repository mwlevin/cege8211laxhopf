"""Displays a matrix as a heat map. Python version of ``laxhopf/HeatMapFrame.java``.

Uses matplotlib. Use the save icon in the plot window's toolbar to save a screenshot.
"""

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Same colors as Gradient.GRADIENT_GREEN_YELLOW_ORANGE_RED in the Java version
GRADIENT_GREEN_YELLOW_ORANGE_RED = LinearSegmentedColormap.from_list(
    "green_yellow_orange_red", ["#00ff00", "#ffff00", "#ffc800", "#ff0000"], N=500)


class HeatMapFrame:
    """A window showing data as a heat map, with time on the horizontal axis and distance on the vertical axis."""

    def __init__(self, name, data, xmax, ymax, xlabel, ylabel):
        """Creates the heat map. Call HeatMapFrame.showAll() once all heat maps have been created to display them.

        :param name: the window title
        :param data: matrix where data[r][c] is the value at the r-th time and the c-th distance
        :param xmax: the largest time, used to label the horizontal axis (which starts at 0)
        :param ymax: the largest distance, used to label the vertical axis (which starts at 0)
        :param xlabel: time units, e.g. "s"
        :param ylabel: distance units, e.g. "ft"
        """
        # transpose so that rows are distances (vertical axis) and columns are times (horizontal axis)
        columns = [list(col) for col in zip(*data)]

        self.figure, ax = plt.subplots(figsize=(7, 6), num=name)
        image = ax.imshow(columns, origin="lower", aspect="auto", interpolation="nearest",
                          extent=(0, xmax, 0, ymax), cmap=GRADIENT_GREEN_YELLOW_ORANGE_RED)
        ax.set_title(name)
        ax.set_xlabel(f"Time ({xlabel})")
        ax.set_ylabel(f"Distance ({ylabel})")
        self.figure.colorbar(image, ax=ax)
        self.figure.tight_layout()

    def screenshot(self, filename):
        """Saves this heat map as a PNG image, e.g. screenshot("density.png")."""
        if not filename.lower().endswith(".png"):
            filename += ".png"
        self.figure.savefig(filename)

    @staticmethod
    def showAll():
        """Displays all heat maps that have been created. Close the windows to end the program."""
        plt.show()
