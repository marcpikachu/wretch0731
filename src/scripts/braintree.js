import dropin from "braintree-web-drop-in"

const BrainTreePaymentForm = () => ({
  instance: null,
  ableToSubmit: false,
  nonce: "",

  async init() {
    const token = this.$el.dataset.token

    this.instance = await dropin.create({
      container: this.$refs.dropin,
      authorization: token,
    })
    this.ableToSubmit = true
  },

  async onSubmit() {
    this.ableToSubmit = false

    const { nonce } = await this.instance.requestPaymentMethod()
    if (nonce) {
      this.nonce = nonce

      this.$nextTick(() => {
        this.$el.submit()
      })
    }
  },
})

export { BrainTreePaymentForm }