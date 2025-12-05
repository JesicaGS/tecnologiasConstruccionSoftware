namespace TiposdePolimorfismo.Figuras
{
    public class Rectangulo : Figura
    {
        private double ancho;
        private double alto;

        public Rectangulo(double ancho, double alto)
        {
            this.ancho = ancho;
            this.alto = alto;
        }

        public override double calcularArea()
        {
            return ancho * alto;
        }

        public override void dibujar()
        {
            Console.WriteLine("Dibujando un rectangulo de " + ancho + " x " + alto);
        }
    }
}