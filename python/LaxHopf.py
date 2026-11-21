import math
import sys

# Stand-ins for "infinity"
DOUBLE_MAX_VALUE = sys.float_info.max
INTEGER_MAX_VALUE = 2147483647


class LaxHopf:

    def __init__(self, v, K, initialCondition):
        """
        :param v: the free flow speed (/s)
        :param K: the jam density (veh/s)
        :param initialCondition: a matrix including the initial conditions, each row {x_min, x_max, k}.
            Initial N will be calculated internally. Row 1 has x=0, and x values are consecutive afterwards.
        """
        # fill this in
        pass

    def calculateNGrid(self, t_start, t_end, t_inc, x_start, x_end, x_inc):
        """Calculates N(t,x) for a specified grid of points and returns the output as a matrix.

        :param t_start: the smallest t value
        :param t_end: the largest t value
        :param t_inc: the t increment
        :param x_start: the smallest x value
        :param x_end: the largest x value
        :param x_inc: the x increment
        :return: a matrix (list of lists) containing the cumulative count values at each (t,x) coordinate.
        """
        output = [[0.0] * int(math.ceil((x_end - x_start) / x_inc + 1))
                  for _ in range(int(math.ceil((t_end - t_start) / t_inc + 1)))]

        for r in range(len(output)):
            for c in range(len(output[r])):
                t = t_start + r * t_inc
                x = x_start + c * x_inc

                output[r][c] = self.calculateN(t, x)

        return output

    def calculateKGrid(self, t_start, t_end, t_inc, x_start, x_end, x_inc):
        """Calculates k(t,x) for a specified grid of points and returns the output as a matrix.

        :param t_start: the smallest t value
        :param t_end: the largest t value
        :param t_inc: the t increment
        :param x_start: the smallest x value
        :param x_end: the largest x value
        :param x_inc: the x increment
        :return: a matrix (list of lists) containing the density values at each (t,x) coordinate.
        """
        output = [[0.0] * int(math.ceil((x_end - x_start) / x_inc + 1))
                  for _ in range(int(math.ceil((t_end - t_start) / t_inc + 1)))]

        for r in range(len(output)):
            for c in range(len(output[r])):
                t = t_start + r * t_inc
                x = x_start + c * x_inc

                output[r][c] = self.calculateK(t, x) * 1609

        return output

    def calculateK(self, t, x):
        """Calculates the density at a specific (t,x) point.

        :param t: time (s)
        :param x: space (m)
        :return: k(t,x)
        """
        # fill this in
        return 0.0

    def calculateN(self, t, x):
        """Calculates the cumulative count at a specific (t,x) point.

        :param t: time (s)
        :param x: space (m)
        :return: N(t,x)
        """
        # fill this in
        return 0.0
