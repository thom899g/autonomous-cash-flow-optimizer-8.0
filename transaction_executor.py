import stripe

class TransactionExecutor:
    def __init__(self, api_key):
        self.stripe = stripe.Stripe(api_key)
        
    def execute(self, plan):
        try:
            # Example: Send a payment
            payment_intent = self.stripe.PaymentIntent.create(
                amount=plan['predicted_cash_flow'],
                currency='usd'
            )
            return True, payment_intent
        except stripe.error.APIError as e:
            return False, f"Transaction failed: {e}"