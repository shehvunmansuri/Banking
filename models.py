from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.account_number}"
    
class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=25, unique=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.branch_name} - {self.branch_code}"
    
class Transaction(models.Model):
    account = models.ForeignKey(Customer, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} on {self.timestamp} for {self.account.account_number}"
    
class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.loan_type} - {self.amount} - {self.customer.account_number}"
    
