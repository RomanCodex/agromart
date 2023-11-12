from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = ((1, "SiteAdmin"), (2, "Seller"), (3, "Consumer"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class AgroAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "AgroAdmin"
    
class Consumer(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    address = models.TextField(max_length=255, default="")
    profile_pic = models.FileField(blank=True)
    objects = models.Manager()

class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name_of_establishment = models.CharField(max_length=255, default="")
    address_of_establishment = models.TextField()
    email = models.CharField(max_length=255, default="")
    approved = models.BooleanField(default=False)
    cac_document = models.FileField(blank=True)
    farm_picture1 = models.FileField(blank=True)
    farm_picture2 = models.FileField(blank=True)
    farm_picture3 = models.FileField(blank=True)
    farm_picture4 = models.FileField(blank=True)
    farm_picture5 = models.FileField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    objects = models.Manager()

class Produce(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField(default=1)
    description = models.TextField()
    category = models.CharField(max_length=255)
    picture1 = models.FileField(blank=True)
    picture2 = models.FileField(blank=True)
    picture3 = models.FileField(blank=True)
    picture4 = models.FileField(blank=True)
    picture5 = models.FileField(blank=True)
    tags = models.TextField(blank=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Produce"
    
class Order(models.Model):
    # produce = models.OneToOneField(Produce, on_delete=models.CASCADE)
    # quantity = models.PositiveSmallIntegerField()
    # order_by = models.CharField(max_length=255)
    # created_on = models.DateField(auto_now_add=True)
    pass
# class Category(models.Model):

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type==1:
             AgroAdmin.objects.create(admin=instance)
        if instance.user_type==2:
            Seller.objects.create(admin=instance)
        if instance.user_type==3:
            Consumer.objects.create(admin=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type==1:
        instance.agroadmin.save()
    if instance.user_type==2:
        instance.seller.save()
    if instance.user_type==3:
        instance.consumer.save()