import { PaymentMethod } from "./PaymentMethod.js";

export class BitcoinPayment extends PaymentMethod {
    pay(amount){
        console.log("Pago procesado por Bitcoin $" + amount);
        
    }
}