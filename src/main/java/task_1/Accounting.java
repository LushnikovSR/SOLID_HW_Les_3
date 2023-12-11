package task_1;

public class Accounting {
    private Employee employee;

    public Accounting(Employee employee) {
        this.employee = employee;
    }

    public int calculateNetSalary() {
        int tax = (int) (employee.getBaseSalary() * 0.25);
        return employee.getBaseSalary() - tax;
    }
}
