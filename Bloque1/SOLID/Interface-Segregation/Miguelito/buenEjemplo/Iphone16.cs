using System;

namespace buenEjemplo
{
    public class Iphone16 : TelefonoBasico, NFC, AsistenteVirtual, DesbloqueoBiometrico
    {
        public Iphone16(string marca, int modelo, int precio, int RAM) : base(marca, modelo, precio, RAM)
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

        public void pagarConNFC()
        {
            Console.WriteLine("Pagando con mi NFC");
        }

        public void usarAsistenteVirtual()
        {
            Console.WriteLine("Hablando con Siri")
        }
    }
}