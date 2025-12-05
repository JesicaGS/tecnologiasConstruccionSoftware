package mal_ejemplo;

public class ServicioNoti {
    private Correo correo =  new Correo();

    public void enviar(String mensaje){
        correo.enviar(mensaje);
    }
}
