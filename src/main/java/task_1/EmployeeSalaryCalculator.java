package task_1;

public class EmployeeSalaryCalculator {
    private int baseSalary;

    public EmployeeSalaryCalculator(int baseSalary) {
        this.baseSalary = baseSalary;
    }

    public int calculateNetSalary(){
        int tax = (int) (baseSalary * 0.25);
        return baseSalary - tax;
    }
}
