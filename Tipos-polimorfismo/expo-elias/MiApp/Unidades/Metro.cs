namespace TiposdePolimorfismo.Unidades
{
    public class Metro
    {
        private double valor { set; get; }
        public Metro(double valor)
        {
            this.valor = valor;
        }

        public static explicit operator double(Metro m)
        {
            return m.valor;
        }

        public static implicit operator Metro(double d)
        {
            return new Metro(d);
        }
    }
}