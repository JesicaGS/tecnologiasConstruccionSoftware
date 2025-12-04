package BadExample;

public class Simpson {
    public static void hablar(Caricatura personaje) {
        switch (personaje.name){
            case "Homero":
                System.out.println("OU!");
                break;
            case "Bart":
                System.out.println("Ay caramba");
                break;
            case "Lisa":
                System.out.println("Siendo honesta no lo se");
                break;
            default:
                System.out.println("Personaje incorrecto");
                break;
        }
    }
}
