import java.util.ArrayList;
import java.util.List;
 
public class EmployeeManager {
 
    private List<String> employees = new ArrayList<>();
 
    public void addEmployee(String name) {
        employees.add(name);
    }
 
    public void printEmployees() {
        for (String employee : employees) {
            System.out.println(employee);
        }
    }
 
    public static void main(String[] args) {
 
        EmployeeManager manager = new EmployeeManager();
 
        manager.addEmployee("John Smith");
        manager.addEmployee("Jane Doe");
        manager.addEmployee("Mike Johnson");
 
        manager.printEmployees();
    }
}