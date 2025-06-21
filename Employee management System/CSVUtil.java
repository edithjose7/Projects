import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class CSVUtil {
    private static final String FILE_PATH = "employees.csv";

    // Read all employee records from the CSV file
    public static List<Employee> readEmployees() throws IOException {
        List<Employee> employees = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new FileReader(FILE_PATH));
        String line;

        // Skip the header
        reader.readLine();

        while ((line = reader.readLine()) != null) {
            String[] data = line.split(",");
            Employee employee = new Employee(Integer.parseInt(data[0]), data[1], data[2], Double.parseDouble(data[3]));
            employees.add(employee);
        }

        reader.close();
        return employees;
    }

    // Write all employee records to the CSV file
    public static void writeEmployees(List<Employee> employees) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_PATH));
        writer.write("ID,Name,Position,Salary\n");  // Write header

        for (Employee employee : employees) {
            writer.write(employee.getId() + "," + employee.getName() + "," + employee.getPosition() + "," + employee.getSalary() + "\n");
        }

        writer.close();
    }

    // Generate a new ID for a new employee
    public static int generateId(List<Employee> employees) {
        if (employees.isEmpty()) {
            return 1;
        } else {
            return employees.get(employees.size() - 1).getId() + 1;
        }
    }
}
