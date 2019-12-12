package laxhopf;

import heatmap.Gradient;
import heatmap.HeatMap;
import javax.swing.*;
import java.awt.*;

/**
 * <p>This class is a very simple example of how to use the HeatMap class.</p>
 *
 * <hr />
 * <p><strong>Copyright:</strong> Copyright (c) 2007, 2008</p>
 *
 * <p>HeatMap is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.</p>
 *
 * <p>HeatMap is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.</p>
 *
 * <p>You should have received a copy of the GNU General Public License
 * along with HeatMap; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA</p>
 *
 * @author Matthew Beckler (matthew@mbeckler.org)
 * @author Josh Hayes-Sheen (grey@grevian.org), Converted to use BufferedImage.
 * @author J. Keller (jpaulkeller@gmail.com), Added transparency (alpha) support, data ordering bug fix.
 * @version 1.6
 */

public class HeatMapFrame extends JFrame
{
    HeatMap panel;

    public HeatMapFrame(String name, double[][] data, double xmax, double ymax) throws Exception
    {
        super(name);
        boolean useGraphicsYAxis = false;
        
        // you can use a pre-defined gradient:
        panel = new HeatMap(data, useGraphicsYAxis, Gradient.GRADIENT_GREEN_YELLOW_ORANGE_RED);
        

        // set miscelaneous settings
        panel.setDrawLegend(true);

        panel.setXAxisTitle("Time (s)");
        panel.setDrawXAxisTitle(true);

        panel.setYAxisTitle("Distance (ft)");
        panel.setDrawYAxisTitle(true);

        panel.setCoordinateBounds(0, xmax, 0, ymax);
        panel.setDrawXTicks(true);
        panel.setDrawYTicks(true);

        panel.setColorForeground(Color.black);
        panel.setColorBackground(Color.white);

        this.getContentPane().add(panel);
        
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(500,500);
        setVisible(true);
    }

}
