class digital_banking:
    def __init__(self, name, balance, pin):
        self.name = name
        self.__balance = balance
        self.__pin = pin
        self._history = []

    def pin_code(self, Pin_code):
        if self.__pin == Pin_code:
            print(f"{self.name} balance: {self.__balance} RS")
        else:
            print("INVALID PIN CODE")

    def consignee(self, reciever_name):
        print(f"{self.name} to {reciever_name}")

    def send_amount(self, amount, reciever, Pin_code):
        if self.__pin != Pin_code:
            print("INVALID PIN CODE")
            self._history.append("FAIL, INVALID PIN CODE")
            return self.__balance

        if amount <= 0:
            print("INVALID AMOUNT")
            self._history.append("FAIL, INVALID AMOUNT")
            return self.__balance

        if amount > self.__balance:
            print("INSUFFICIENT BALANCE")
            self._history.append("FAIL, BALANCE IS LESS THAN SENDING AMOUNT")
            return self.__balance

        self.__balance -= amount
        reciever.__balance += amount
        self.consignee(reciever.name)
        self._history.append(
            f"Send {amount} RS to {reciever.name}. Remaining balance is {self.__balance} RS"
        )
        reciever._history.append(
            f"Received {amount} RS from {self.name}. Balance is {reciever.__balance} RS"
        )
        print(
            f"Sent {amount} RS to {reciever.name}. Remaining balance: {self.__balance} RS"
        )


ali = digital_banking("ALI", 15000, 1122)
ahmad = digital_banking("AHMAD", 1000, 1122)

# This transfer should fail (15000 is less than 18100)
ali.send_amount(18100, ahmad, 1122)

# This transfer should succeed after PIN check
ali.send_amount(8000, ahmad, 1122)

print("Ali history:", ali._history)
print("Ahmad history:", ahmad._history)
ali.pin_code(1122)
ahmad.pin_code(1122)
