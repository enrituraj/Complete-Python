class Payment:
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def process_payment(self):
        print("Processing credit card payment")

class PayPalPayment(Payment):
    def process_payment(self):
        print("Processing PayPal payment")

# Test polymorphism
def process(payment):
    payment.process_payment()

credit_card = CreditCardPayment()
paypal = PayPalPayment()

process(credit_card)  
# Output: Processing credit card payment
process(paypal)       