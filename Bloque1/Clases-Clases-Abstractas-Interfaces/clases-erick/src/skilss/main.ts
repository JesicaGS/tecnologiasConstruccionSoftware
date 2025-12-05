import {Gato} from './animals/Gato.ts'
import {Paloma} from './animals/Paloma.ts'
import {Pato} from './animals/Pato.ts'

const paloma = new Paloma('La paloma');
paloma.nombre = 'La paloma';

paloma.hacerSonido();
paloma.volar();
paloma.dormir();

console.log('{---------}');

const gato = new Gato('El gato');
gato.nombre = 'El gato';

gato.hacerSonido();
gato.volar();
gato.dormir();

console.log('{---------}');

const pato = new Pato('El pato');
gato.nombre = 'El pato';

gato.hacerSonido();
gato.volar();
gato.dormir();
gato.nadar();