#include <iostream>

class Volador
{
public:
    virtual ~Volador() = default;
    virtual void volar() const = 0;
};

class Nadador
{
public:
    virtual ~Nadador() = default;
    virtual void nadar();
}

class Pato : public Volador, public Nadador {
    public:
    void volar() const {std::cout << "El pato vuela!" << std::endl; }
}
{
}