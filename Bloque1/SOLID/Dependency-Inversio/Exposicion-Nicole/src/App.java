import buen_ejemplo.Email;
import buen_ejemplo.ServicioNotificador;
import mal_ejemplo.ServicioNoti;

public class App {
    public static void main(String[] args) {
        ServicioNoti servicioNoti = new ServicioNoti();
        servicioNoti.enviar("Hola mundo");

        Email email = new Email();
    }
}
