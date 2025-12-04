#include <iostream>

class Animal
{
public:
    virtual ~Animal() {};
    void respirar() const { std::cout << "Respirando" << std::endl; }
};

struct Perro : public Animal
{
    void ladra() const { std::cout << "Guau" << std::endl; }
};

struct Gato : public Animal
{
    void maulla() const { std::cout << "Miau" << std::endl; }
};

int main()
{
    Perro p;
    Gato g;

    p.respirar();
    p.ladra();

    g.respirar();
    g.maulla();
}