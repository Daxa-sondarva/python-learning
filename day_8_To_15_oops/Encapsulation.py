"""
Encapsulation (Data Hiding & Access Control)
Encapsulation means restricting direct access to certain attributes and allowing controlled access through methods.

✅ Concepts:
Public Attributes (self.name) = Accessible from anywhere.

Protected Attributes (self._name) = Should not be modified directly (convention only).

Private Attributes (self.__name) = Cannot be accessed directly from outside the class.


"""
import time
class AccountLockedError(Exception):
    """Custom exeption for a loked account."""
    pass
class InvalidPinError(Exception):
    """Custom exeption for a invalid pin entry."""
    pass

class BankAccount:
    
    def __init__(self,account_holder,balance,):
        self.account_holder = account_holder # Public Attribute
        self._balance = balance # Protected Attribute
        self.__pin = 1234  # Private Attribute
        self.__attempts = 3  # Maximum attempts allowed
        self.__failed_attempts = 0  # Track incorrect attempts
        self.__locked = False  # Lock status
        self.__transactions = []

    
    def __verify_pin(self):
        """Private method to check PIN with 3 attempts before locking the account"""

        if self.__locked:
            raise AccountLockedError("Account is loked due to too many failed attemts. Try again later.")


        for attempt in range(self.__attempts):

            try:
                pin = int(input("Enter PIN: "))
            except ValueError:
                print("❌ Please enter a valid 4-digit PIN.")
                continue 
            if pin == self.__pin:
                self.__failed_attempts = 0  # Reset failed attempts after a correct entry
                return True #Correct Pin
            self.__failed_attempts + 1
            remaining_attmpts = self.__attempts - (attempt + 1)
            if remaining_attmpts > 0 :
                print(f"Incorrect PIN. {remaining_attmpts} attempts remaining.")
            else:
                self.__locked = True
                print("Account Loked! Too many failed attempts.")
                raise AccountLockedError("Too many failed attemts. Account now loked.")

        return False  
        
    def __check_lock_status(self):
        """Check if the account is locked and introduce a delay"""
        if self.__locked:
            print("Account is locked. Please wait 10 seconds befor traing again.")
            time.sleep(10) # Check if the account is locked and introduce a delay
            self.__locked = False  # Unlock the account after delay
            self.__failed_attempts = 0  # Reset failed attempts
            print("Account is now unlocked. You may try again.")
    
    def deposit(self):
        """Deposit money into the account"""
        try:
            self.__check_lock_status()
            if not self.__verify_pin():
                return "Deposit denied. Incorrect PIN."
        
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                self._balance += amount
                self.__transactions.append(f"Deposited ${amount}. New balance: ${self._balance}")
                return f"Deposited ${amount}. New balance: ${self._balance}"
            return "Invalid deposit amount."
        except (ValueError, AccountLockedError) as e:
            return str(e)
    
    def withdraw(self):
        """Withdraw money from the account"""
        try:
            self.__check_lock_status()
            if not self.__verify_pin():
                return "Withdrawal denied. Incorrect PIN."

            amount = float(input("Enter withdrawal amount: "))
            if amount > 0 and amount <= self._balance:
                self._balance -= amount
                self.__transactions.append(f"Withdrawn ${amount}. Remaining balance: ${self._balance}")
                return f"Withdrawn ${amount}. Remaining balance: ${self._balance}"
            return "Insufficient funds or invalid amount."
        except (ValueError, AccountLockedError) as e:
            return str(e)
    
    def get_balance(self):
        """Check account balance"""
        try:
            self.__check_lock_status()
            if self.__verify_pin():
                return f"Account balance: ${self._balance}"
            return "Access denied."
        except AccountLockedError as e:
            return str(e)

    # def __get_pin(self): # Private Method (only accessible within the class)
    #     return self.__get_pin

    def update_pin(self):
        """Update the account PIN"""
        try:
            self.__check_lock_status()
            if not self.__verify_pin():
                return "PIN update denied. Incorrect PIN."

            new_pin = int(input("Enter new 4-digit PIN: "))
            if 1000 <= new_pin <= 9999:
                self.__pin = new_pin
                return "PIN Updated Successfully."
            return "Invalid PIN. It must be a 4-digit number."
        except (ValueError, AccountLockedError) as e:
            return str(e)

    def transaction_hestrory(self):
        return "\n".join(self.__transactions) if self.__transactions else "No transaction yet."
    def check_pin(self):
        """Check if the entered PIN matches the stored PIN"""
        try:
            self.__check_lock_status()
            if self.__verify_pin():
                return "Access granted."
            return "Access denied."
        except AccountLockedError as e:
            return str(e)
    def transfer(self, recipient):
        try:
            self.__check_lock_status()
            if not self.__verify_pin():
                return "Transfer denied. Incorrect PIN."

            amount = float(input(f"Enter amount to transfer to {recipient.account_holder}: "))
            if amount > 0 and amount <= self._balance:
                self._balance -= amount
                recipient._balance += amount
                self.__transactions.append(f"Transferred ${amount} to {recipient.account_holder}.")
                recipient.__transactions.append(f"Received ${amount} from {self.account_holder}.")
                return f"Transferred ${amount} to {recipient.account_holder}. Your new balance: ${self._balance}"
            return "Invalid transfer amount or insufficient funds."
        except (ValueError, AccountLockedError) as e:
            return str(e)

    def menu(self):
        """ Main menu to interact with the bank account. """
        while True:
            print("\n🔹 Bank Account Menu 🔹")
            print("1️⃣ Deposit")
            print("2️⃣ Withdraw")
            print("3️⃣ Check Balance")
            print("4️⃣ Update PIN")
            print("5️⃣ Show Transactoin")
            print("6 Check PIN")
            

            print("8 Exit")

            try:
                choice = int(input("choose an option: "))

                if choice == 1 :
                    print(self.deposit())
                elif choice == 2:
                    print(self.withdraw())
                elif choice == 3:
                    print(self.transfer())
                elif choice == 4:
                    print(self.update_pin())
                elif choice == 5:
                    print(self.transaction_hestrory())
                # elif choice == 5:
                #     print(self.check_pin())  # This will ask for the PIN and return access status.
                elif choice == 6:
                    print("Thank you for using our service. Good Bye !")
                    break
                else:
                    print("Invalid option! Please choose between 1-5.")
            except ValueError:
                print("Invaid  input! Please enter a number between 1-5.")

# Create an account and start the menu
acc = BankAccount("Daxa",1000)
print(acc.menu())

# print(acc.get_balance())
# print(acc.deposit())
# print(acc.withdraw())
# print(acc.update_pin())
# print(acc.check_pin())


# Accessing public attributes
# print(acc.account_holder)  # ✅ Works
# Accessing protected attributes (Not recommended, but possible)
# print(acc._balance)  # ✅ Works, but should be accessed through a method
# Accessing private attributes (❌ Will raise an error)
# print(acc.__pin)  # ❌ AttributeError
# Trying to access a private method (❌ Will raise an error)
# print(acc.__get_pin())  # ❌ AttributeError