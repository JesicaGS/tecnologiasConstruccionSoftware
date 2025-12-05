using System;
using malEjemplo;
using buenEjemplo;

namespace Miguelito
{
    static void Main(string[] args)
    {
        Console.WriteLine("Mal ejemplo");

        ZTE miZte = new ZTE("ZTE", 2019, 1000, 2);

        miZte.escribir();
        miZte.llamar();
        miZte.pagarConNFC();
        miZte.usarAsistenteVirtual();
        miZte.desbloquearConHuella();

        IPhone15 miIphone = new IPhone15("iPhone", 15, 200000, 8);
        miIphone.escribir();
        miIphone.llamar();
        miIphone.pagarConNFC();
        miIphone.usarAsistenteVirtual();
        miIphone.desbloquearConHuella();

        Xiaomi miXiaomi = new Xiaomi("xiaomi", 15, 200000, 8);
        miXiaomi.escribir();
        miXiaomi.llamar();
        miXiaomi.pagarConNFC();
        miXiaomi.usarAsistenteVirtual();
        miXiaomi.desbloquearConHuella();

        Console.WriteLine("Buen ejemplo");

        Zte2 miZte2 = new Zte2("ZTE", 2019, 1000, 2);
        miZte2.escribir();
        miZte2.llamar();

        Xiaomi12 miXiaomi12 = new Xiaomi12("Xiaomi", 2019, 1000, 2);
        miXiaomi12.escribir();
        miXiaomi12.llamar();
    }
}