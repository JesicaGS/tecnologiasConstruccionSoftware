package clases;

public class Perro {
    private String nombre;
    private int edad;
    private String raza;

    public Perro(String nombre, int edad, String raza) {
        this.nombre = nombre;
        this.edad = edad;
        this.raza = raza;
    }

    public void ladrar(){
        System.out.println("Ladroooooo");
    }

    public void comer(){
        System.out.println("Comer");
    }

    public void jugar(){
        System.out.println("Jugar");
    }
}
