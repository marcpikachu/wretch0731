import Alpine from "alpinejs";
import "htmx.org";
import { BrainTreePaymentForm } from "./braintree";

window.Alpine = Alpine;

Alpine.data("braintree_payment_form", BrainTreePaymentForm);

Alpine.start();