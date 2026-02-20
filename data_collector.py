import stripe

class DataCollector:
    def __init__(self, api_key):
        self.stripe = stripe.Stripe(api_key)
        
    def collect_data(self):
        try:
            # Fetch historical transactions
            transactions = self.stripe.history.list()
            return transactions
        except stripe.error.APIError as e:
            raise RuntimeError(f"Failed to fetch data: {e}")