from django.db import models

class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    manager_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"Warehouse {self.warehouse_id} - {self.address}"

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('Жіночий', 'Жіночий'),
        ('Чоловічий', 'Чоловічий'),
        ('Дитячий', 'Дитячий')
    ]

    product_id = models.AutoField(primary_key=True)
    product_type = models.CharField(max_length=50, choices=PRODUCT_TYPE_CHOICES)
    product_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity_on_hand = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} ({self.product_type})"

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    client_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    contact_person = models.CharField(max_length=100)

    def __str__(self):
        return self.client_name

class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    sale_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Sale {self.sale_id} on {self.sale_date}"
