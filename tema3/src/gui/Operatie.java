package gui;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Operatie {

    static List<Map<Integer, Double>> inmultireMatrice(List<Map<Integer, Double>> A, List<Map<Integer, Double>> B) {
        List<Map<Integer, Double>> inmMatrice = new ArrayList<>();
        for (int i = 0; i < A.size(); i++)
            inmMatrice.add(new TreeMap<>());
        double inm = 0.0;
        for (int i = 0; i < A.size(); i++) {
            for (int j = 0; j < A.size(); j++) {
                inm = 0;
                for (int k : A.get(i).keySet()) {
                    if (A.get(i).get(k) != null && B.get(k).get(j) != null)
                        inm += A.get(i).get(k) * B.get(k).get(j);
                }
                inmMatrice.get(i).put(j, inm);
            }

        }
        return inmMatrice;
    }

    static List<Map<Integer, Double>> sumaMatrice
            (List<Map<Integer, Double>> A, List<Map<Integer, Double>> B) {

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


    static boolean egalMatrice(List<Map<Integer, Double>> A, List<Map<Integer, Double>> B) {
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

    private static boolean checkCondition(double value) {
        return !(Math.abs(value) < Matrice.epsilon);
    }

}
