import { Animal } from "./Animal";
import {Volar} from '../skilss/Volar';

export class Pato extends Animal implements Volar {
    constructor(public nombre: string){
        super(nombre);
    }


    hacerSonido():void {
        console.log(`${this.name} cuak!`)
    }

    nadar(): void {
        console.log(`${this.name} nadando`)
    }
}