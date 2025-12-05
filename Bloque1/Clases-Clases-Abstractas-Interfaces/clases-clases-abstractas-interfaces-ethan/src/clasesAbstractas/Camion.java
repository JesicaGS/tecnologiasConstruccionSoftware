package clasesAbstractas;

public class Camion extends Carro {
    private int ejes;

    public Camion(String marca, int llantas, String color, int ejes){
        super(marca, llantas, color);
        this.ejes = ejes;
    }

    @Override
    public void acelerar(){
        System.out.println("RUUUUUUM");
    }
}
