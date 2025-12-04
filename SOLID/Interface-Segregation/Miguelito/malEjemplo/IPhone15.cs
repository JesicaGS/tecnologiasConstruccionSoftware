using system;

namespace malEjemplo
{
    public class IPhone15 : Telefono
    {
        public IPhone15(string marca, int modelo, int precio, int RAM)
        {

        }

        public override void escribir()
        {
            Console.WriteLine($"Escribiendo desde mi {marca}");
        }

        public override void llamar()
        {
            Console.WriteLine($"Llamando desde mi {marca}");
        }

        public override void pagarConNFC()
        {
            Console.WriteLine($"Pagando con mi {marca}");
        }

        public override void usarAsistenteVirtual()
        {
            Console.WriteLine("Hablando con Siri");
        }

        public override void desbloquearConHuella()
        {
            Console.WriteLine("Este dispositivo no tiene acceso a esta función");
        }
    }
}