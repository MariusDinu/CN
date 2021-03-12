package gui;

import javax.swing.*;

public class DinuMarius_NassarMahmoud_tema3CN {
    public static void main(String[] args) {
        Matrice A = new Matrice();
        Matrice B = new Matrice();
        Matrice plus = new Matrice();
        Matrice inmultire = new Matrice();

        A.citireMatriceA("a.txt");
        B.citireMatriceB("b.txt");
        plus.citireMatriceA("aplusb.txt");
        inmultire.citireMatriceA("aorib.txt");

        UI_Tema3 ui_tema3 = new UI_Tema3();

        JFrame frame = new JFrame("Tema3");
        frame.setContentPane(ui_tema3.panel1);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);


        //System.out.println(A.returnMatrice().toString());
        // System.out.println(B.returnMatrice().toString());
        //System.out.println(plus.returnMatrice().toString());
        //System.out.println(gui.Operatie.sumaMatrice(A.returnMatrice(), B.returnMatrice()).toString());
//        System.out.println("Adunare:");
//        if (gui.Operatie.egalMatrice(gui.Operatie.sumaMatrice(A.returnMatrice(), B.returnMatrice()), plus.returnMatrice())) {
//            System.out.println("Matricile sunt egale");
//        } else {
//            System.out.println("Matricile nu sunt egale");
//        }
//        System.out.println("Inmultire:");
//        if (gui.Operatie.egalMatrice(gui.Operatie.inmultireMatrice(A.returnMatrice(), B.returnMatrice()), inmultire.returnMatrice())) {
//            System.out.println("Matricile sunt egale");
//        } else {
//            System.out.println("Matricile nu sunt egale");
//        }
   }

}
