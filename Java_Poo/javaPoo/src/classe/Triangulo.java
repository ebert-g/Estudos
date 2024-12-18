package classe;

public class Triangulo implements PadraoGeometrico {
    private int base, altura;

    public Triangulo(int base, int altura){
        this.base = base;
        this.altura = altura;
    }


    @Override
    public int calcularArear() {
        int area = base * altura;
        return area;
    }
    
}
