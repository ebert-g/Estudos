import java.util.ArrayList;
import java.util.Random;

import classe.*;

public class App {
    public static void main(String[] args) throws Exception {
        ArrayList<Integer> arrayDinanmico = new ArrayList<Integer>();
        Random random = new Random();
        int num = 0, soma = 0;
        while (num != 2) {
            num = random.nextInt(1, 51);
            soma += num;
            arrayDinanmico.add(soma);
        }
        for (int i = 0; i < arrayDinanmico.size(); i++) {
            System.out.println(arrayDinanmico.get(i));
        }
        System.out.println("DONE");

    }
}
