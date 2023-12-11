package task_4;

public class Square implements ICalculateShape {
    int sideLength;

    public void setSideLength(int sideLength) {
        this.sideLength = sideLength;
    }

    @Override
    public int area() {
        return this.sideLength * this.sideLength;
    }
}
