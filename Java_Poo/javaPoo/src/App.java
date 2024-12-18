import classe.*;

public class App {
    public static void main(String[] args) throws Exception {
        SomarArea calcularArea = new SomarArea();
        Quadrado quadrado = new Quadrado(4);
        Triangulo triangulo = new Triangulo(3, 3);
        System.out.println(triangulo.calcularArear());
        System.out.println();
        System.out.println(quadrado.calcularArear());
        System.out.println(calcularArea.somarArea(triangulo, triangulo));

        


     }
}
