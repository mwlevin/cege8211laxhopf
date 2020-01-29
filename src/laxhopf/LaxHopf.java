/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package laxhopf;

import heatmap.Gradient;
import heatmap.HeatMap;
import java.util.Map;

/**
 *
 * @author mlevin
 */
public class LaxHopf 
{

    /**
     * 
     * @param v the free flow speed (/s)
     * @param K the jam density (veh/s)
     * @param initialCondition a matrix including the initial conditions {x_min, x_max, k, initial N}. Initial N will be calculated internally. Row 1 has x=0, and x values are consecutive afterwards.
     */
    public LaxHopf(double v, double K, double[]... initialCondition)
    {
        // fill this in
    }
    
    
    
    /**
     * Calculates N(t,x) for a specified grid of points and returns the output as a matrix.
     * @param t_start the smallest t value
     * @param t_end the largest t value
     * @param t_inc the t increment
     * @param x_start the smallest x value
     * @param x_end the largest x value
     * @param x_inc the x increment
     * @return a matrix containing the cumulative count values at each (t,x) coordinate. 
     */
    public double[][] calculateN(double t_start, double t_end, double t_inc, double x_start, double x_end, double x_inc)
    {
        double[][] output = new double[(int)Math.ceil((t_end - t_start)/t_inc+1)][(int)Math.ceil((x_end - x_start)/x_inc+1)];
        
        for(int r = 0; r < output.length; r++)
        {
            for(int c = 0; c < output[r].length; c++)
            {
                double t = t_start + r * t_inc;
                double x = x_start + c * x_inc;
                
                output[r][c] = calculateN(t, x);
            }
        }
        
        return output;
    }


    
    /**
     * Calculates k(t,x) for a specified grid of points and returns the output as a matrix.
     * @param t_start the smallest t value
     * @param t_end the largest t value
     * @param t_inc the t increment
     * @param x_start the smallest x value
     * @param x_end the largest x value
     * @param x_inc the x increment
     * @return a matrix containing the cumulative count values at each (t,x) coordinate. 
     */
    public double[][] calculateK(double t_start, double t_end, double t_inc, double x_start, double x_end, double x_inc)
    {
        double[][] output = new double[(int)Math.ceil((t_end - t_start)/t_inc+1)][(int)Math.ceil((x_end - x_start)/x_inc+1)];
        
        for(int r = 0; r < output.length; r++)
        {
            for(int c = 0; c < output[r].length; c++)
            {
                double t = t_start + r * t_inc;
                double x = x_start + c * x_inc;
                
                output[r][c] = calculateK(t, x) * 1609;
            }
        }
        
        return output;
    }
    
    /**
     * Calculates the density at a specific (t,x) point
     * @param t time (s)
     * @param x space (m)
     * @return k(t,x)
     */
    public double calculateK(double t, double x)
    {
        // fill this in
        return 0.0;
    }
    
    
    /**
     * Calculates the cumulative count at a specific (t,x) point
     * @param t time (s)
     * @param x space (m)
     * @return N(t,x)
     */
    public double calculateN(double t, double x)
    {
        // fill this in
        return 0.0;
    }
    
}
