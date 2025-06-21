package ABC;
import javax.swing.*; 
import java.awt.event.*;

public class SimpleCalculator {
    public static void main(String[] args) {
        JFrame f = new JFrame("Calc");
        JTextField n1 = new JTextField(); n1.setBounds(30, 30, 50, 20);
        JTextField n2 = new JTextField(); n2.setBounds(100, 30, 50, 20);
        
        JButton add = new JButton("+"); add.setBounds(30, 70, 50, 30);
        JButton sub = new JButton("-"); sub.setBounds(100, 70, 50, 30);
        JButton mul = new JButton("*"); mul.setBounds(30, 110, 50, 30);
        JButton div = new JButton("/"); div.setBounds(100, 110, 50, 30);
        
        JLabel res = new JLabel(); res.setBounds(30, 160, 200, 20);
        
        add.addActionListener(e -> res.setText("Sum: " + (Integer.parseInt(n1.getText()) + Integer.parseInt(n2.getText()))));
        sub.addActionListener(e -> res.setText("Diff: " + (Integer.parseInt(n1.getText()) - Integer.parseInt(n2.getText()))));
        mul.addActionListener(e -> res.setText("Prod: " + (Integer.parseInt(n1.getText()) * Integer.parseInt(n2.getText()))));
        div.addActionListener(e -> {
            int denom = Integer.parseInt(n2.getText());
            if (denom != 0)
                res.setText("Quot: " + (Integer.parseInt(n1.getText()) / denom));
            else
                res.setText("Cannot divide by 0");
        });
        
        f.add(n1); f.add(n2); f.add(add); f.add(sub); f.add(mul); f.add(div); f.add(res);
        f.setSize(250,300); 
        f.setLayout(null); 
        f.setVisible(true); 
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}