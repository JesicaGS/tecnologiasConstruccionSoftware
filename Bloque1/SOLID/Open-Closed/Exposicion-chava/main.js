import { PaymentService } from "./services/PaymentServices.js";
import { CreditCardPayment } from "./models/CreditCardPaymentMethod.js";
import { PaypalPayment } from "./models/PaypalPaymentMethod.js";
import { BitcoinPayment } from "./models/BitcointPaymentMethod.js";

const service = new PaymentService();
const creditCard = new CreditCardPayment();
const paypal = new PaypalPayment();
const bitcoin = new BitcoinPayment();

service.serviceProcess(creditCard, 200);
service.serviceProcess(paypal, 500);
service.serviceProcess(bitcoin, 1000);
