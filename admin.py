from django.contrib import admin
from .models import Customer, Branch, Transaction, Loan
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_number', 'account_type', 'balance', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('name', 'account_number', 'account_type')
    list_filter = ('account_type', 'is_deleted', 'created_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):    
    list_display = ('branch_name', 'branch_code', 'address', 'phone_number', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('branch_name', 'branch_code', 'phone_number')
    list_filter = ('is_deleted', 'created_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'transaction_type', 'amount', 'timestamp')
    search_fields = ('account__account_number', 'transaction_type')
    list_filter = ('transaction_type', 'timestamp')
    readonly_fields = ('timestamp',)

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):  
    list_display = ('customer', 'loan_type', 'amount', 'interest_rate', 'start_date', 'end_date', 'is_approved')
    search_fields = ('customer__account_number', 'loan_type')
    list_filter = ('loan_type', 'is_approved', 'start_date')
    readonly_fields = ()