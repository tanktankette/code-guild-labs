from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Address(models.Model):
    name = models.CharField(max_length=127)
    street_name = models.CharField(max_length=127)
    city = models.CharField(max_length=127)
    zip = models.IntegerField()
    phone_number = models.IntegerField()
    notes = models.TextField()

    def get_full_address(self):
        return "{}, {} {}".format(self.street_name, self.city, self.zip)

    def __str__(self):
        return "{} at {}".format(self.name, self.street_name)

    class Meta:
        verbose_name_plural = "Addresses"


class Order(models.Model):
    address = models.ForeignKey('Address')
    total = models.FloatField(default=0)
    entered_by = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return "{}: {}".format(self.pk, self.address.get_full_address())

    def update_total(self):
        pies = Pizza.objects.filter(order__pk=self.pk)
        total = 0
        for p in pies:
            total += p.price
        self.total = total

    # def save(self, *args, **kwargs):
    #     super().save()
    #     pies = Pizza.objects.filter(order__pk=self.pk)
    #     total = 0
    #     for p in pies:
    #         total += p.price
    #     self.total = total
    #     super().save(args, kwargs)


class Pizza(models.Model):
    order = models.ForeignKey('Order')
    size = models.CharField(max_length=127)
    toppings = models.ManyToManyField('Topping')
    price = models.FloatField()

    def __str__(self):
        return "Pizza for order {}".format(self.order.pk)

    def save(self, *args, **kwargs):
        super().save(args, kwargs)
        self.order.update_total()


class Topping(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name
