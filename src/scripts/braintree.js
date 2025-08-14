import dropin from "braintree-web-drop-in";

const BrainTreePaymentForm = () => ({
  instance: null,
  ableToSubmit: false,

  async init() {
    const token = this.$el.dataset.token;

    this.instance = await dropin.create({
      container: this.$refs.dropin,
      authorization: token,
    });
    this.ableToSubmit = true;
  },
  onSubmit() {
    console.log(this.instance);
  },
});

export { BrainTreePaymentForm };