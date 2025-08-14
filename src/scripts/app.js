import Alpine from "alpinejs";
import "htmx.org";
import { BrainTreePayment } from "./braintree";

window.Alpine = Alpine;

Alpine.data("braintree_payment_form", BrainTreePayment);

Alpine.start();