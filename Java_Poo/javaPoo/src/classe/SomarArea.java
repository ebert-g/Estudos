package classe;

public class SomarArea {

    public int somarArea(PadraoGeometrico figuraA, PadraoGeometrico figuraB){
        int somarArea = figuraA.calcularArear() + figuraB.calcularArear();
        return somarArea;
    }
}
