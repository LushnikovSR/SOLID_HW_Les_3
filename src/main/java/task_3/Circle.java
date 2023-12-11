package task_3;

import task_3.Interfaces.Shape2D;

public class Circle implements Shape2D {
    private double radius;
    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double area() {
        return 2 * 3.14 * radius;
    }
}
