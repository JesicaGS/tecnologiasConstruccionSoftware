import {Animal} from './Animal.ts'

export class Gato extends Animal {
    constructor(protected nombre: string){
        super(nombre);
    }

    hacerSonido():void {
        console.log('miiaaaaaau')
    }
}