package gui;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class UI_Tema3 {
    public JTextArea textView;
    public JPanel panel1;
    private JButton MatriceaA;
    private JButton matriceaB;
    private JButton plusgui;
    private JButton Verificare;



    public UI_Tema3() {
        Matrice A = new Matrice();
        Matrice B = new Matrice();
        Matrice plus = new Matrice();
        Matrice inmultire = new Matrice();

        A.citireMatriceA("a.txt");
        B.citireMatriceB("b.txt");
        plus.citireMatriceA("aplusb.txt");
        inmultire.citireMatriceA("aorib.txt");

        String matriceatA = A.returnMatrice().toString();
        String matriceatB = B.returnMatrice().toString();
        String Plus = plus.returnMatrice().toString();
        String oRis = gui.Operatie.sumaMatrice(A.returnMatrice(), B.returnMatrice()).toString();

        panel1.setBounds(10, 10, 500, 1000);
        JScrollPane sp = new JScrollPane(textView, JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED, JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);
        panel1.add(sp);

        MatriceaA.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                textView.setText("");
                textView.append(matriceatA);

            }
        });
        matriceaB.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                textView.setText("");
                textView.append(matriceatB);

            }
        });
        plusgui.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                textView.setText("");
                textView.append(Plus + "\n" + oRis);
            }
        });
        Verificare.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                textView.setText("");

                textView.append("Adunare\n");
                if (gui.Operatie.egalMatrice(gui.Operatie.sumaMatrice(A.returnMatrice(), B.returnMatrice()), plus.returnMatrice())) {
                    textView.append("Matricile sunt egale\n");

                } else {
                    textView.append("Matricile nu sunt egale\n");
                }
                textView.append("Inmultire\n");

                if (gui.Operatie.egalMatrice(gui.Operatie.inmultireMatrice(A.returnMatrice(), B.returnMatrice()), inmultire.returnMatrice())) {
                    textView.append("Matricile sunt egale\n");
                } else {
                    textView.append("Matricile nu sunt egale");
                }
            }
        });
    }
}
