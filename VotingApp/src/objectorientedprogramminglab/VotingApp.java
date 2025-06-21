package objectorientedprogramminglab;

import javax.swing.*;
import java.awt.event.*;

public class VotingApp {
    static int a=0,b=0;
    public static void main(String[] args) {
        JFrame f = new JFrame("Vote");
        JButton c1 = new JButton("Candidate A"); c1.setBounds(30, 50, 120, 30);
        JButton c2 = new JButton("Candidate B"); c2.setBounds(160, 50, 120, 30);
        JLabel res = new JLabel(); res.setBounds(30, 100, 300, 20);
        c1.addActionListener(e -> res.setText("A: " + (++a) + " B: " + b));
        c2.addActionListener(e -> res.setText("A: " + a + " B: " + (++b)));
        f.add(c1); f.add(c2); f.add(res);
        f.setSize(350,200); f.setLayout(null); f.setVisible(true); f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}