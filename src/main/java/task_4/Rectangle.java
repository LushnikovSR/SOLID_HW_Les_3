package task_4;

public class Rectangle implements ICalculateShape{
    private int width;
    private int height;
    public void setWidth(int width) {
        this.width = width;
    }
    public void setHeight(int height) {
        this.height = height;
    }
    @Override
    public int area() {
        return this.width * this.height;
    }
}
