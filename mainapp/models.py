from django.db import models


# -----------------------------
# USER MODEL (Admin / Restaurant / User)
# -----------------------------

class User(models.Model):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('restaurant', 'Restaurant'),
        ('user', 'User'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    image = models.ImageField(upload_to='restaurant_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_restaurant_photo(self):
        if self.image:
            try:
                return self.image.url
            except Exception:
                pass
        
        name_lower = self.name.lower()
        if 'biryani' in name_lower or 'royal' in name_lower or 'curry' in name_lower or 'indian' in name_lower:
            return 'https://images.unsplash.com/photo-1589302168068-964664d93dc0?auto=format&fit=crop&w=600&q=80'
        elif 'cafe' in name_lower or 'coffee' in name_lower or 'bean' in name_lower or 'brew' in name_lower:
            return 'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80'
        elif 'spice' in name_lower or 'seoul' in name_lower or 'korean' in name_lower or 'asian' in name_lower:
            return 'https://images.unsplash.com/photo-1552566626-52f8b828add9?auto=format&fit=crop&w=600&q=80'
        elif 'italia' in name_lower or 'bella' in name_lower or 'pizza' in name_lower or 'kitchen' in name_lower:
            return 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80'
        elif 'fire' in name_lower or 'bbq' in name_lower or 'grill' in name_lower or 'burger' in name_lower:
            return 'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80'
        elif 'cookie' in name_lower or 'crumble' in name_lower or 'bakery' in name_lower or 'sweet' in name_lower:
            return 'https://images.unsplash.com/photo-1558961363-fa8fdf82db35?auto=format&fit=crop&w=600&q=80'
        
        photos = [
            'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=600&q=80',
            'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80',
            'https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?auto=format&fit=crop&w=600&q=80',
            'https://images.unsplash.com/photo-1537047902294-62a40c20a6ae?auto=format&fit=crop&w=600&q=80',
            'https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=600&q=80'
        ]
        return photos[self.id % len(photos)]



# -----------------------------
# CATEGORY MODEL
# -----------------------------

class Category(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# -----------------------------
# FOOD ITEM MODEL
# -----------------------------

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# -----------------------------
# CART MODEL
# -----------------------------

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.food.name}"


# -----------------------------
# ORDER MODEL
# -----------------------------

class Order(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders')
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurant_orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    payment_status = models.CharField(max_length=20, default='Unpaid')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


# -----------------------------
# ORDER ITEM MODEL
# -----------------------------

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.food.name} (Order {self.order.id})"
# -----------------------------
# FEEDBACK MODEL
# -----------------------------

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurant_feedbacks')
    message = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} -> {self.restaurant.name}"
