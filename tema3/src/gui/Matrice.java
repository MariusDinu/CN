package gui;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Matrice {

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


