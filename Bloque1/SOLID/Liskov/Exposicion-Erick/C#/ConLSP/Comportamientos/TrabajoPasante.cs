using System;
using ConLSP.Interfaces;

namespace ConLSP.Comportamientos
{
    public class TrabajoPasante : ITrabajador
    {
        public void Trabajar()
        {
            Console.WriteLine("Aprendiendo y apoyando en tareas");
        }
    }
}