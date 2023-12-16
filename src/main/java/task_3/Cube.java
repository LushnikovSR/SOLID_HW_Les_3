package task_3;

import task_3.Interfaces.Shape2D;
import task_3.Interfaces.Shape3D;

public class Cube implements Shape2D, Shape3D {
    private int edge;
    public Cube(int edge) {
        this.edge = edge;
    }
    @Override
    public double area() {
        return 6 * edge * edge;
    }
    @Override
    public double volume() {
        return edge * edge * edge;
    }
}
