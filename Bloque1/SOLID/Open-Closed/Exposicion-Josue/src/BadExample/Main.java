package BadExample;

public class Main {
    public static void main(String[] args) {
        Caricatura homero = new Caricatura("Homero");
        Caricatura bart = new Caricatura("Bart");

        Simpson.hablar(Homero);
        Simpson.hablar(Bart);
    }
}
