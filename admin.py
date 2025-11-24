from django.contrib import admin
from .models import Customer, Branch
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