import { PaymentMethod } from "./PaymentMethod.js";

export class PaypalPayment extends PaymentMethod {
    pay(amount){
        console.log("Pago procesado por Paypal $" + amount);
        
    }
}