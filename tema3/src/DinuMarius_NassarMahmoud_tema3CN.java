import java.io.*;
import java.util.*;


public class DinuMarius_NassarMahmoud_tema3CN {
    public static void main(String[] args) {
        Matrice A = new Matrice();
        Matrice B = new Matrice();
        Matrice plus = new Matrice();
        Matrice inmultire=new Matrice();

        A.citireMatriceA("a.txt");
        B.citireMatriceB("b.txt");
        plus.citireMatriceA("aplusb.txt");
        inmultire.citireMatriceA("aorib.txt");

        // System.out.println(A.returnMatrice().toString());
        // System.out.println(B.returnMatrice().toString());
        //System.out.println(plus.returnMatrice().toString());
        //System.out.println(Operatie.sumaMatrice(A.returnMatrice(), B.returnMatrice()).toString());
        System.out.println("Adunare:");
        if (Operatie.egalMatrice(Operatie.sumaMatrice(A.returnMatrice(),B.returnMatrice()), plus.returnMatrice())) {
            System.out.println("Matricile sunt egale");
        } else {
            System.out.println("Matricile nu sunt egale");
        }
        System.out.println("Inmultire:");
        if (Operatie.egalMatrice(Operatie.inmultireMatrice(A.returnMatrice(),B.returnMatrice()), inmultire.returnMatrice())) {
            System.out.println("Matricile sunt egale");
        } else {
            System.out.println("Matricile nu sunt egale");
        }
    }

}


class Matrice {

    static final double epsilon = Math.pow(10, -7);
    private final List<Map<Integer, Double>> matrice;
//constructor


    Matrice() {
        this.matrice = new ArrayList<>();
    }

    void citireMatriceB(String cale) {
        int copyN = 0;
        ArrayList<Double> a = new ArrayList<Double>();
        ArrayList<Double> b = new ArrayList<Double>();
        ArrayList<Double> c = new ArrayList<Double>();
        FileReader fr = null;
        try {

            fr = new FileReader(cale);
            BufferedReader br = new BufferedReader(fr);
            String line;
            boolean aCheck = true;
            boolean bCheck = false;
            boolean cCheck = false;
            double first;
            double second;
            double third;
            int n = Integer.parseInt(br.readLine());
            copyN = n;
            int p = Integer.parseInt(br.readLine());
            int q = Integer.parseInt(br.readLine());
            for (int i = 0; i < n; i++)
                this.matrice.add(new TreeMap<>());
            int count = 0;
            while ((line = br.readLine()) != null) {
                if (aCheck) {
                    if (count < n) {
                        first = Double.parseDouble(line);
                        //vectorul a
                        a.add(count, first);
                        count++;
                    } else {
                        count = 0;
                        aCheck = false;
                        bCheck = true;
                    }
                }

                if (bCheck) {
                    if (count < n - 1) {
                        second = Double.parseDouble(line);
                        //vectorul b
                        b.add(count, second);
                        count++;
                    } else {
                        count = 0;
                        bCheck = false;
                        cCheck = true;
                    }
                }
                if (cCheck) {
                    if (count < n - 1) {
                        third = Double.parseDouble(line);
                        //vectorul c
                        c.add(count, third);
                        count++;
                    } else {
                        count = 0;
                        cCheck = false;
                    }
                }


            }
        } catch (FileNotFoundException e) {
            System.out.println("Fisier inexistent");
            System.exit(2);
        } catch (IOException e) {
            System.out.println("Eroare de ccitire");
            System.exit(3);
        }
        for (int aPos = 0; aPos < copyN; aPos++) {
            this.matrice.get(aPos).put(aPos, a.get(aPos));
        }
        for (int bPos = 0; bPos < copyN - 1; bPos++) {
            this.matrice.get(bPos).put(bPos + 1, b.get(bPos));

        }
        for (int cPos = 0; cPos < copyN - 1; cPos++) {
            this.matrice.get(cPos + 1).put(cPos, c.get(cPos));
        }
    }

    void citireMatriceA(String cale) {

        FileReader fr = null;
        try {

            fr = new FileReader(cale);
            BufferedReader br = new BufferedReader(fr);
            String line;
            int n = Integer.parseInt(br.readLine());
            for (int i = 0; i < n; i++)
                this.matrice.add(new TreeMap<>());
            while ((line = br.readLine()) != null) {
                String[] data = line.split(", ");
                //parsare linie,coloana,valoare
                double first = Double.parseDouble(data[0]);
                int second = Integer.parseInt(data[1]);
                int third = Integer.parseInt(data[2]);
                //schema de memorie
                this.matrice.get(second).put(third, first);
            }
        } catch (FileNotFoundException e) {
            System.out.println("Fisier inexistent");
            System.exit(2);
        } catch (IOException e) {
            System.out.println("Eroare de ccitire");
            System.exit(3);
        }
    }


    public List<Map<Integer, Double>> returnMatrice() {
        return matrice;
    }
}


class Operatie {
    static List<Map<Integer, Double>> inmultireMatrice(List<Map<Integer, Double>> A, List<Map<Integer, Double>> B) {
        List<Map<Integer, Double>> inmMatrice = new ArrayList<>();
        for (int i = 0; i < A.size(); i++)
            inmMatrice.add(new TreeMap<>());
        double inm = 0.0;
        for (int i = 0; i < A.size(); i++) {
            for (int j = 0; j < A.size(); j++) {
                inm = 0;
                for (int k:A.get(i).keySet()) {
                    if(A.get(i).get(k)!=null && B.get(k).get(j)!=null)
                        inm += A.get(i).get(k) * B.get(k).get(j);
                }
                inmMatrice.get(i).put(j, inm);
            }

        }
        return inmMatrice;
    }
        static List<Map<Integer, Double>> sumaMatrice
        (List < Map < Integer, Double >> A, List < Map < Integer, Double >> B){

            List<Map<Integer, Double>> sum = new ArrayList<>();
            double first = 0.0;
            for (int i = 0; i < A.size(); i++)
                sum.add(new TreeMap<>());
            for (int i = 0; i < A.size(); i++)
                for (int j = 0; j < A.size(); j++) {
                    if (A.get(i).get(j) == null && B.get(i).get(j) != null) {
                        first = B.get(i).get(j);
                        sum.get(i).put(j, first);
                    } else if (B.get(i).get(j) == null && A.get(i).get(j) != null) {
                        first = A.get(i).get(j);
                        sum.get(i).put(j, first);
                    } else if (B.get(i).get(j) == null && A.get(i).get(j) == null) {
                        first = 0;
                    } else {
                        first = A.get(i).get(j) + B.get(i).get(j);
                        sum.get(i).put(j, first);
                    }

                }

            return sum;
        }


        static boolean egalMatrice (List < Map < Integer, Double >> A, List < Map < Integer, Double >> B){
            int n = B.size();

            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++) {
                    if (B.get(i).get(j) == null && A.get(i).get(j) == null) {

                    } else if (B.get(i).get(j) != null && A.get(i).get(j) != null) {
                        if (checkCondition(A.get(i).get(j) - B.get(i).get(j))) {

                        }
                    }

                }
            return true;
        }

        private static boolean checkCondition ( double value){
            return !(Math.abs(value) < Matrice.epsilon);
        }
    }
