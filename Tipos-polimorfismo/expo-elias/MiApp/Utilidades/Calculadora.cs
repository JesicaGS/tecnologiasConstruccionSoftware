namespace TiposdePolimorfismo.Utilidades
{
    public class Calculadora
    {
        public int sumar(int a, int b)
        {
            return a + b;
        }

        public double sumar(double a, double b)
        {
            return a + b;
        }

        public static Calculadora operator +(Calculadora c1, Calculadora c2)
        {
            return new Calculadora();
        }
    }
}