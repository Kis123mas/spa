from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_secretary = models.BooleanField(blank=True, null=True, default=False)
    is_not_secretary = models.BooleanField(blank=True, null=True, default=False)
    is_admin = models.BooleanField(blank=True, null=True, default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # You can add more fields here like ['full_name']

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.user.email} Profile'



class ServiceRendered(models.Model):
    staff_name = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'is_not_secretary': True})
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    

    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('pos', 'POS'),
        ('transfer', 'Transfer'),
    ]
    mode_of_payment = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    
    # Type of service (Solo or Contract)
    SERVICE_TYPE_CHOICES = [
        ('solo', 'Solo'),
        ('contract', 'Contract'),
    ]
    service_type = models.CharField(max_length=10, choices=SERVICE_TYPE_CHOICES)

    # Type of service (Solo or Contract)
    SERVICE_TYPE_RENDERED = [
        ('Massage Therapy', 'Massage Therapy'),
        ('Facial Treatments', 'Facial Treatments'),
        ('Aromatherapy', 'Aromatherapy'),
        ('Body Scrubs', 'Body Scrubs'),
        ('Steam & Sauna', 'Steam & Sauna'),
        ('Nail Care', 'Nail Care'),
    ]
    service_rendered = models.CharField(max_length=20, null=True, blank=True, choices=SERVICE_TYPE_RENDERED)
    
    # Date when the service was rendered
    service_date = models.DateField(auto_now_add=True)
    
    # Additional description for the service
    description = models.TextField(null=True, blank=True)
    
    # Staff position or role for context
    staff_role = models.CharField(max_length=100, null=True, blank=True)
    
    # Optionally, the service can have a customer associated with it (if applicable)
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    
    # Optional field for tracking the invoice number
    invoice_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    
    # Timestamp for when the service record was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Optionally, a status field to track whether the payment has been confirmed or pending
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
    ]
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Service Rendered by {self.staff_name} on {self.service_date} - {self.amount}"

    class Meta:
        verbose_name = "Service Rendered"
        verbose_name_plural = "Services Rendered"
        ordering = ['-service_date']