public class main {
    public static void main(String[] args) {

        Matrice A1 = new Matrice();
        Matrice F1 = new Matrice();
        Matrice A2 = new Matrice();
        Matrice F2 = new Matrice();
        Matrice A3 = new Matrice();
        Matrice F3 = new Matrice();
        Matrice A4 = new Matrice();
        Matrice F4 = new Matrice();
        Matrice A5 = new Matrice();
        Matrice F5 = new Matrice();
        Matrice A6 = new Matrice();
        Matrice F6 = new Matrice();


        A1.citireMatriceA("a1.txt");
        A2.citireMatriceA("a2.txt");
        A3.citireMatriceA("a3.txt");
        A4.citireMatriceA("a4.txt");
        A5.citireMatriceA("a5.txt");
        A6.citireMatriceA("a6.txt");

        System.out.println(A5.returnMatriceA());
        A5.Verification(A5.returnMatriceA());

        //  F1.citireMatriceF("f1.txt");
       // F2.citireMatriceF("f2.txt");
       // F3.citireMatriceF("f3.txt");
       // F4.citireMatriceF("f4.txt");
         F5.citireMatriceF("f5.txt");
        //F6.citireMatriceF("f6.txt");


       // double[] f=A6.gaussSeidel(A6.returnMatriceA(),F6.returnMatriceF());
        double[] f1=A5.gaussSeidel(A5.returnMatriceA(),F5.returnMatriceF());
        A5.compare(f1,F5.returnMatriceF());






    }

}
