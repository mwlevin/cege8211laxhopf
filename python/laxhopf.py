"""Python version of ``laxhopf/LaxHopf.java``."""

import math
import sys

# Stand-ins for "infinity" that match the Java version's Double.MAX_VALUE and Integer.MAX_VALUE
DOUBLE_MAX_VALUE = sys.float_info.max
INTEGER_MAX_VALUE = 2147483647


class LaxHopf:

    def __init__(self, v, K, initial_condition):
        """
        :param v: the free flow speed (/s)
        :param K: the jam density (veh/s)
        :param initial_condition: a list of initial conditions, each [x_min, x_max, k]. The initial N
            should be calculated internally. Row 1 has x=0, and x values are consecutive afterwards.
        """
        # fill this in
        pass

    def calculate_n_grid(self, t_start, t_end, t_inc, x_start, x_end, x_inc):
        """Calculates N(t,x) for a specified grid of points and returns the output as a matrix.

        :param t_start: the smallest t value
        :param t_end: the largest t value
        :param t_inc: the t increment
        :param x_start: the smallest x value
        :param x_end: the largest x value
        :param x_inc: the x increment
        :return: a matrix (list of lists) where output[r][c] is the cumulative count at
            t = t_start + r*t_inc and x = x_start + c*x_inc
        """
        rows = int(math.ceil((t_end - t_start) / t_inc + 1))
        cols = int(math.ceil((x_end - x_start) / x_inc + 1))
        output = [[0.0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                t = t_start + r * t_inc
                x = x_start + c * x_inc

                output[r][c] = self.calculate_n(t, x)

        return output

    def calculate_k_grid(self, t_start, t_end, t_inc, x_start, x_end, x_inc):
        """Calculates k(t,x) for a specified grid of points and returns the output as a matrix.

        :param t_start: the smallest t value
        :param t_end: the largest t value
        :param t_inc: the t increment
        :param x_start: the smallest x value
        :param x_end: the largest x value
        :param x_inc: the x increment
        :return: a matrix (list of lists) where output[r][c] is the density at
            t = t_start + r*t_inc and x = x_start + c*x_inc
        """
        rows = int(math.ceil((t_end - t_start) / t_inc + 1))
        cols = int(math.ceil((x_end - x_start) / x_inc + 1))
        output = [[0.0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                t = t_start + r * t_inc
                x = x_start + c * x_inc

                output[r][c] = self.calculate_k(t, x) * 1609

        return output

    def calculate_k(self, t, x):
        """Calculates the density at a specific (t,x) point.

        :param t: time (s)
        :param x: space (m)
        :return: k(t,x)
        """
        # fill this in
        return 0.0

    def calculate_n(self, t, x):
        """Calculates the cumulative count at a specific (t,x) point.

        :param t: time (s)
        :param x: space (m)
        :return: N(t,x)
        """
        # fill this in
        return 0.0
