import java.io.IOException;
import java.util.List;

public class EmployeeDAO {
    public List<Employee> getAllEmployees() throws IOException {
        return CSVUtil.readEmployees();
    }

    public void addEmployee(Employee employee) throws IOException {
        List<Employee> employees = CSVUtil.readEmployees();
        employee.setId(CSVUtil.generateId(employees));
        employees.add(employee);
        CSVUtil.writeEmployees(employees);
    }

    public void updateEmployee(Employee updatedEmployee) throws IOException {
        List<Employee> employees = CSVUtil.readEmployees();
        for (Employee emp : employees) {
            if (emp.getId() == updatedEmployee.getId()) {
                emp.setName(updatedEmployee.getName());
                emp.setPosition(updatedEmployee.getPosition());
                emp.setSalary(updatedEmployee.getSalary());
                break;
            }
        }
        CSVUtil.writeEmployees(employees);
    }

    public void deleteEmployee(int id) throws IOException {
        List<Employee> employees = CSVUtil.readEmployees();
        employees.removeIf(emp -> emp.getId() == id);
        CSVUtil.writeEmployees(employees);
    }
}
