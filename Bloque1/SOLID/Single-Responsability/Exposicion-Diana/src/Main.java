public class Main {
    public static void main(String[] args) {
        SistemaPedidos pedidos = new SistemaPedidos("Niconiconi", "Espresso");
        MaquinaCafe cafe = new MaquinaCafe("Espresso");
        Factura factura = new Factura("Niconiconi", 82.50);
        Notificacion notificacion = new Notificacion("Niconiconi", "Tu pedido está lleno");

        pedidos.tomarPedido();
        cafe.prepararCafe();
        factura.generarFactura();
        notificacion.enviarMensaje();
    }


}
