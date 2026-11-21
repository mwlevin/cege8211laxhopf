"""Python version of ``laxhopf/LaxHopf.java``."""

import math
import sys

# Stand-ins for "infinity" that match the Java version's Double.MAX_VALUE and Integer.MAX_VALUE
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

    def calculateN(self, *args):
        """Calculates the cumulative count N. Like the Java version, there are two ways to call it.

        calculateN(t, x) calculates the cumulative count at a specific (t,x) point:
            :param t: time (s)
            :param x: space (m)
            :return: N(t,x)

        calculateN(t_start, t_end, t_inc, x_start, x_end, x_inc) calculates N(t,x) for a specified grid
        of points and returns the output as a matrix (list of lists):
            :param t_start: the smallest t value
            :param t_end: the largest t value
            :param t_inc: the t increment
            :param x_start: the smallest x value
            :param x_end: the largest x value
            :param x_inc: the x increment
            :return: a matrix containing the cumulative count values at each (t,x) coordinate.
        """
        if len(args) == 6:
            t_start, t_end, t_inc, x_start, x_end, x_inc = args

            output = [[0.0] * int(math.ceil((x_end - x_start) / x_inc + 1))
                      for _ in range(int(math.ceil((t_end - t_start) / t_inc + 1)))]

            for r in range(len(output)):
                for c in range(len(output[r])):
                    t = t_start + r * t_inc
                    x = x_start + c * x_inc

                    output[r][c] = self.calculateN(t, x)

            return output

        t, x = args

        # fill this in
        return 0.0

    def calculateK(self, *args):
        """Calculates the density k. Like the Java version, there are two ways to call it.

        calculateK(t, x) calculates the density at a specific (t,x) point:
            :param t: time (s)
            :param x: space (m)
            :return: k(t,x)

        calculateK(t_start, t_end, t_inc, x_start, x_end, x_inc) calculates k(t,x) for a specified grid
        of points and returns the output as a matrix (list of lists):
            :param t_start: the smallest t value
            :param t_end: the largest t value
            :param t_inc: the t increment
            :param x_start: the smallest x value
            :param x_end: the largest x value
            :param x_inc: the x increment
            :return: a matrix containing the density values at each (t,x) coordinate.
        """
        if len(args) == 6:
            t_start, t_end, t_inc, x_start, x_end, x_inc = args

            output = [[0.0] * int(math.ceil((x_end - x_start) / x_inc + 1))
                      for _ in range(int(math.ceil((t_end - t_start) / t_inc + 1)))]

            for r in range(len(output)):
                for c in range(len(output[r])):
                    t = t_start + r * t_inc
                    x = x_start + c * x_inc

                    output[r][c] = self.calculateK(t, x) * 1609

            return output

        t, x = args

        # fill this in
        return 0.0
