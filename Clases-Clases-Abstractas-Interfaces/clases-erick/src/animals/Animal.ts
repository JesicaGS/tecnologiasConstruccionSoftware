export abstract class Animal {
    constructor(protected name: string){}

    abstract hacerSonido();

    dormir(): void{
        console.log(`${this.name} esta durmiendo`);
    }

    getNombre(): string {
        return this.name
    }
}