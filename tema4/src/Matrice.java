import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Matrice {

    static final double epsilon = Math.pow(10, -4);
    private final List<Map<Integer, Double>> matrice;
    private List<Double> matrixF;
//constructor


    Matrice() {
        this.matrice = new ArrayList<>();
        this.matrixF = new ArrayList<>();
    }


    void Verification(List<Map<Integer, Double>> Matrix) {
        int count = 0;
        for (int i = 0; i < Matrix.size(); i++) {
            for (int j = 0; j < Matrix.size(); j++) {
                if (i == j)
                    if (Matrix.get(i).get(j) > epsilon) {
                        count++;
                    }
            }
        }
        if (count == Matrix.size()) {
            System.out.println("Totul ok!");
        }
    }

    void citireMatriceF(String cale) {
        List<Double> a = new ArrayList<Double>();
        FileReader fr = null;
        try {

            fr = new FileReader(cale);
            BufferedReader br = new BufferedReader(fr);
            String line;
            int n = Integer.parseInt(br.readLine());
            while ((line = br.readLine()) != null) {
                this.matrixF.add(Double.parseDouble(line));
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    void citireMatriceA(String cale) {
        int copyN = 0;
        List<Double> a = new ArrayList<Double>();
        List<Double> b = new ArrayList<Double>();
        List<Double> c = new ArrayList<Double>();
        List<Double> copy = new ArrayList<Double>();
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
            double eps = 0.0000000001;
            int n = Integer.parseInt(br.readLine());
            copyN = n;
            int p = Integer.parseInt(br.readLine());
            int q = Integer.parseInt(br.readLine());
            for (int i = 0; i < n; i++)
                this.matrice.add(new TreeMap<>());
            int count = 0;
            int count2 = 0;
            while ((line = br.readLine()) != null) {
                if (aCheck) {
                    if (count < n) {
                        first = Double.parseDouble(line);
                        if (first > eps) {
                            copy.add(count, first);
                            count2++;
                        }

                        count++;


                    } else if (count == count2) {
                        a = copy;
                        count = 0;
                        aCheck = false;
                        bCheck = true;
                    } else {
                    }
                }

                if (bCheck) {
                    if (count < n - 1) {
                        second = Double.parseDouble(line);
                        //vectorul b
                        c.add(count, second);
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
                        b.add(count, third);
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

    public double[] gaussSeidel(List<Map<Integer, Double>> matrixA, List<Double> matrixF) {

        int iteration = 0;
        double norm = 0;
        double diff = 0;
        double[] x = new double[matrixA.size()];
        Arrays.fill(x, 0.0);

        while (true) {
            for (int i = 0; i < matrixA.size(); i++) {
                double x0 = 0.0;
                for (int k = 0; k < matrixA.size(); k++) {
                    if (i != k && matrixA.get(i).get(k) != null) {
                        x0 += matrixA.get(i).get(k) * x[k];
                    } else {
                        x0 += 0 * x[k];
                    }
                }
                if (matrixA.get(i).get(i) != null) {
                    x[i] = (matrixF.get(i) - x0) / matrixA.get(i).get(i);

                }
            }
            iteration++;
            diff = norm - getNorm(x);
            norm = getNorm(x);
            if (!Double.isNaN(diff) && !Double.isInfinite(diff)) {
                if (Math.abs(diff) < epsilon) {
                    break;
                }
            } else {
                break;
            }
        }
        return x;
    }

    public double getNorm(double[] x) {
        double norm = 0;
        for (double i : x) {
            norm += Math.pow(i, 2);
        }
        return Math.sqrt(norm);
    }

    public List<Double> returnMatriceF() {
        return matrixF;
    }

    public void compare(double[] y, List<Double> mat) {
        boolean ok = true;
        for (int i = 0; i < y.length; i++) {
            if (y[i] == mat.get(i)) {

            } else {
                System.out.println("sunt diferite");
                ok = false;
                break;
            }

        }
        if (ok) {
            System.out.println("Sunt ok!");
        }
    }

    public List<Map<Integer, Double>> returnMatriceA() {
        return matrice;
    }
}