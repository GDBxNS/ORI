class User:
    def __init__(self, *args, **kwargs):
        self.CUST_ID = kwargs['CUST_ID']
        self.BALANCE = kwargs['BALANCE']
        self.BALANCE_FREQUENCY = kwargs['BALANCE_FREQUENCY']
        self.PURCHASES = kwargs['PURCHASES']
        self.ONEOFF_PURCHASES = kwargs['ONEOFF_PURCHASES']
        self.INSTALLMENTS_PURCHASES = kwargs['INSTALLMENTS_PURCHASES']
        self.CASH_ADVANCE = kwargs['CASH_ADVANCE']
        self.PURCHASES_FREQUENCY = kwargs['PURCHASES_FREQUENCY']
        self.ONEOFF_PURCHASES_FREQUENCY = kwargs['ONEOFF_PURCHASES_FREQUENCY']
        self.PURCHASES_INSTALLMENTS_FREQUENCY = kwargs['PURCHASES_INSTALLMENTS_FREQUENCY']
        self.CASH_ADVANCE_FREQUENCY = kwargs['CASH_ADVANCE_FREQUENCY']
        self.CASH_ADVANCE_TRX = kwargs['CASH_ADVANCE_TRX']
        self.PURCHASES_TRX = kwargs['PURCHASES_TRX']
        self.CREDIT_LIMIT = kwargs['CREDIT_LIMIT']
        self.PAYMENTS = kwargs['PAYMENTS']
        self.MINIMUM_PAYMENTS = kwargs['MINIMUM_PAYMENTS']
        self.PRC_FULL_PAYMENT = kwargs['PRC_FULL_PAYMENT']
        self.TENURE = kwargs['TENURE']

    def __repr__(self):
        return "CUST_ID: " + self.CUST_ID + " BALANCE: " + self.BALANCE