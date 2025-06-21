import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.event.*;
import java.io.IOException;
import java.util.List;

public class EmployeeApp {
    private JPanel panelMain;
    private JTextField textName;
    private JTextField textPosition;
    private JTextField textSalary;
    private JButton addButton;
    private JButton updateButton;
    private JButton deleteButton;
    private JTable tableEmployees;
    private JTextField textId;
    private EmployeeDAO employeeDAO;

    public EmployeeApp() {
        // Initialize panelMain manually
        panelMain = new JPanel();
        panelMain.setLayout(new BoxLayout(panelMain, BoxLayout.Y_AXIS));  // Set layout manager

        // Initialize the components
        textName = new JTextField(20);
        textPosition = new JTextField(20);
        textSalary = new JTextField(20);
        textId = new JTextField(5);
        
        addButton = new JButton("Add");
        updateButton = new JButton("Update");
        deleteButton = new JButton("Delete");

        // Initialize JTable and wrap it in JScrollPane
        tableEmployees = new JTable();
        JScrollPane scrollPane = new JScrollPane(tableEmployees);

        // Add components to panelMain
        panelMain.add(scrollPane);  // Add JTable inside the JScrollPane to the panel
        panelMain.add(new JLabel("Name:"));
        panelMain.add(textName);
        panelMain.add(new JLabel("Position:"));
        panelMain.add(textPosition);
        panelMain.add(new JLabel("Salary:"));
        panelMain.add(textSalary);
        panelMain.add(addButton);
        panelMain.add(updateButton);
        panelMain.add(deleteButton);

        employeeDAO = new EmployeeDAO();
        loadEmployeeData();

        // Add action listeners for buttons
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = textName.getText();
                String position = textPosition.getText();
                double salary = Double.parseDouble(textSalary.getText());

                try {
                    employeeDAO.addEmployee(new Employee(0, name, position, salary));
                    loadEmployeeData();
                    clearFields();
                } catch (IOException ex) {
                    JOptionPane.showMessageDialog(null, "Error adding employee: " + ex.getMessage());
                }
            }
        });

        updateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int id = Integer.parseInt(textId.getText());
                String name = textName.getText();
                String position = textPosition.getText();
                double salary = Double.parseDouble(textSalary.getText());

                try {
                    employeeDAO.updateEmployee(new Employee(id, name, position, salary));
                    loadEmployeeData();
                    clearFields();
                } catch (IOException ex) {
                    JOptionPane.showMessageDialog(null, "Error updating employee: " + ex.getMessage());
                }
            }
        });

        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int id = Integer.parseInt(textId.getText());

                try {
                    employeeDAO.deleteEmployee(id);
                    loadEmployeeData();
                    clearFields();
                } catch (IOException ex) {
                    JOptionPane.showMessageDialog(null, "Error deleting employee: " + ex.getMessage());
                }
            }
        });

        tableEmployees.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                int row = tableEmployees.getSelectedRow();
                textId.setText(tableEmployees.getValueAt(row, 0).toString());
                textName.setText(tableEmployees.getValueAt(row, 1).toString());
                textPosition.setText(tableEmployees.getValueAt(row, 2).toString());
                textSalary.setText(tableEmployees.getValueAt(row, 3).toString());
            }
        });
    }

    private void loadEmployeeData() {
        try {
            List<Employee> employees = employeeDAO.getAllEmployees();
            DefaultTableModel model = new DefaultTableModel();
            model.addColumn("ID");
            model.addColumn("Name");
            model.addColumn("Position");
            model.addColumn("Salary");

            for (Employee emp : employees) {
                model.addRow(new Object[]{emp.getId(), emp.getName(), emp.getPosition(), emp.getSalary()});
            }

            tableEmployees.setModel(model);  // Set the table model with the updated data
        } catch (IOException ex) {
            JOptionPane.showMessageDialog(null, "Error loading employee data: " + ex.getMessage());
        }
    }

    private void clearFields() {
        textId.setText("");
        textName.setText("");
        textPosition.setText("");
        textSalary.setText("");
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Employee Management App");
        frame.setContentPane(new EmployeeApp().panelMain);  // Use panelMain here
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
