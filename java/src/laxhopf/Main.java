/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package laxhopf;

import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author mlevin
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws Exception
    {
        // the order of conditions is {x_min, x_max, k}
        double[][] initialCondition = new double[][]{
            new double[]{0, 500, 0.01},
            new double[]{500, 600, 0.04},
            new double[]{600, 950, 0.025},
            new double[]{950, 1000, 0.02}
        };
    
        LaxHopf test = new LaxHopf(20, 0.2, initialCondition);


        
        double[][] N = test.calculateN(0, 50, 1, 0, 500, 1);

        HeatMapFrame displayN = new HeatMapFrame("Cumulative count", N, 50, 500, "s", "ft");
        
        double[][] k = test.calculateK(0, 50, 1, 0, 500, 1);
        
        HeatMapFrame displayK = new HeatMapFrame("density", k, 50, 500, "s", "ft");
        
    }
    
}
