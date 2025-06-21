package ABC;
import javax.swing.*;
import java.awt.event.*;

public class LoginScreen {
    public static void main(String[] args) {
        JFrame f = new JFrame("Login");
        JTextField user = new JTextField(); user.setBounds(50, 50, 150, 20);
        JPasswordField pass = new JPasswordField(); pass.setBounds(50, 80, 150, 20);
        JButton b = new JButton("Login"); b.setBounds(80, 120, 80, 30);
        JLabel res = new JLabel(); res.setBounds(50, 160, 200, 20);
        b.addActionListener(e -> res.setText(user.getText().equals("admin") && new String(pass.getPassword()).equals("1234") ? "Success" : "Fail"));
        f.add(user); f.add(pass); f.add(b); f.add(res);
        f.setSize(300,300); f.setLayout(null); f.setVisible(true); f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
} 