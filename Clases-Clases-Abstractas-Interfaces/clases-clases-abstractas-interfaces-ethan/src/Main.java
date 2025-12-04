import clasesAbstractas.Camion;
import interfaz.Pato;

public class Main {
    public static void main(String[] args) {
        Camion miCamion = new Camion("Chevrolet", 4, "Azul", 4);
        miCamion.encender();
        miCamion.acelerar();

        Pato feo = new Pato(2, "azul");
        feo.hacerRuido();
    }
}
