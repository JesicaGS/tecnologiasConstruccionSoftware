package interfaz;

public class Pato extends Animal implements Volador{

    private String color;

    public Pato(int age, String color) {
        super(age);
        this.color = color;
    }

    @Override
    public void hacerRuido() {
        System.out.println("MUUUU");
    }

    @Override
    public void volar() {
        System.out.println("Volar");
    }
}
