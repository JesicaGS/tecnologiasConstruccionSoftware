import {Animal} from './Animal'
import {Volar} from '../skilss/Volar.ts'

export class Paloma extends Animal implements Volar {
    constructor(public nombre: string){
        super(nombre)
    }

    hacerSonido(): void {
        console.log(`${this.name} hacer brrrr`);
    }

    volar(): void {
        console.log(`${this.nombre} vuela por las nubes`);
    }
}