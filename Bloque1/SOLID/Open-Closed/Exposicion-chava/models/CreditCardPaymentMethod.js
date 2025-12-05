import { PaymentMethod } from "./PaymentMethod.js";

export class CreditCardPayment extends PaymentMethod {
    pay(amount){
        console.log("Pago procesado por Tarjeta de credito $" + amount);
    }
}