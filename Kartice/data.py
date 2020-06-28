import csv
from user import User


class Data:

    def __init__(self):
        self.users = []
        self.header = []
        self.read()
        self.load_header()

    def read(self):
        with open('credit_card_data.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row_list = []
                """user = User(CUST_ID=row['CUST_ID'], BALANCE=row['BALANCE'], 
                BALANCE_FREQUENCY=row['BALANCE_FREQUENCY'], PURCHASES=row['PURCHASES'], ONEOFF_PURCHASES=row['ONEOFF_PURCHASES'], 
                INSTALLMENTS_PURCHASES=row['INSTALLMENTS_PURCHASES'], CASH_ADVANCE=row['CASH_ADVANCE'], PURCHASES_FREQUENCY=row['PURCHASES_FREQUENCY'], 
                ONEOFF_PURCHASES_FREQUENCY=row['ONEOFF_PURCHASES_FREQUENCY'], PURCHASES_INSTALLMENTS_FREQUENCY=row['PURCHASES_INSTALLMENTS_FREQUENCY'], 
                CASH_ADVANCE_FREQUENCY=row['CASH_ADVANCE_FREQUENCY'], CASH_ADVANCE_TRX=row['CASH_ADVANCE_TRX'], PURCHASES_TRX=row['PURCHASES_TRX'], 
                CREDIT_LIMIT=row['CREDIT_LIMIT'], PAYMENTS=row['PAYMENTS'], MINIMUM_PAYMENTS=row['MINIMUM_PAYMENTS'], PRC_FULL_PAYMENT=row['PRC_FULL_PAYMENT'], 
                TENURE=row['TENURE'])"""
                
                row_list.append(eval(row['BALANCE']))
                row_list.append(eval(row['BALANCE_FREQUENCY']))
                row_list.append(eval(row['PURCHASES']))
                row_list.append(eval(row['ONEOFF_PURCHASES']))
                row_list.append(eval(row['INSTALLMENTS_PURCHASES']))
                row_list.append(eval(row['CASH_ADVANCE']))
                row_list.append(eval(row['PURCHASES_FREQUENCY']))
                row_list.append(eval(row['ONEOFF_PURCHASES_FREQUENCY']))
                row_list.append(eval(row['PURCHASES_INSTALLMENTS_FREQUENCY']))
                row_list.append(eval(row['CASH_ADVANCE_FREQUENCY']))
                row_list.append(eval(row['CASH_ADVANCE_TRX']))
                row_list.append(eval(row['PURCHASES_TRX']))
                try:
                    row_list.append(eval(row['CREDIT_LIMIT']))
                except:
                    row_list.append(0)

                row_list.append(eval(row['PAYMENTS']))
                try:
                    row_list.append(eval(row['MINIMUM_PAYMENTS']))
                except:
                    row_list.append(0)

                row_list.append(eval(row['PRC_FULL_PAYMENT']))
                row_list.append(eval(row['TENURE']))
                self.users.append(row_list)

    def print10(self):
        if len(self.users) >= 10:
            for index in range(10):
                print(self.users[index])
        else:
            raise ("Podaci nisu ucitani")

    def load_header(self):
        file = open('credit_card_data.csv', 'r')
        row = file.readline()
        file.close()
        rowTokens = row.split(",")
        for item in rowTokens:
            if(item!="CUST_ID"):
                self.header.append(item)
