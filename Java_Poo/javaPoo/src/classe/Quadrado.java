package classe;

public class Quadrado implements PadraoGeometrico {
    private int lado;

    public Quadrado(int lado) {
        this.lado = lado;
    }

    @Override
    public int calcularArear() {
        int areaQuadrado = lado * lado;
        return areaQuadrado;
    }
}
