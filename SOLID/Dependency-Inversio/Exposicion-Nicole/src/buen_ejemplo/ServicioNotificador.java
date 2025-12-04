package buen_ejemplo;

public class ServicioNotificador {

    private final Notificador notificador;

    public ServicioNotificador(Notificador notificador) {
        this.notificador = notificador;
    }
    
    public void notificar(String mensaje){
        notificador.enviar(mensaje);
    }
}
