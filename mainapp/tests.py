from django.test import TestCase, Client
from django.urls import reverse
from mainapp.models import User, Category, FoodItem, Cart, Order, OrderItem, Feedback

class FoodDeliveryTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Create test admin user
        self.admin = User.objects.create(
            name='Test Admin',
            email='admin_test@gmail.com',
            password='adminpassword',
            role='admin'
        )
        
        # Create test restaurant
        self.restaurant = User.objects.create(
            name='Test Restaurant',
            email='rest_test@gmail.com',
            password='restpassword',
            role='restaurant'
        )
        
        # Create test customer user
        self.user = User.objects.create(
            name='Test User',
            email='user_test@gmail.com',
            password='userpassword',
            role='user'
        )
        
        # Create category
        self.category = Category.objects.create(
            name='Main Course',
            restaurant=self.restaurant
        )
        
        # Create food item
        self.food = FoodItem.objects.create(
            name='Test Pizza',
            description='Delicious cheese pizza',
            price=299.00,
            category=self.category,
            restaurant=self.restaurant,
            is_available=True
        )

    def test_user_registration(self):
        response = self.client.post(reverse('user_register'), {
            'name': 'New Customer',
            'email': 'newcust@gmail.com',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(email='newcust@gmail.com').exists())

    def test_user_login(self):
        response = self.client.post(reverse('user_login'), {
            'email': 'user_test@gmail.com',
            'password': 'userpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session.get('user_id'), self.user.id)

    def test_logout(self):
        session = self.client.session
        session['user_id'] = self.user.id
        session['role'] = 'user'
        session.save()
        
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('user_id', self.client.session)

    def test_browse_restaurants(self):
        response = self.client.get(reverse('browse_restaurants'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Restaurant')

    def test_view_menu(self):
        response = self.client.get(reverse('view_menu', args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Pizza')

    def test_add_to_cart_and_view_cart(self):
        session = self.client.session
        session['user_id'] = self.user.id
        session['role'] = 'user'
        session.save()
        
        response = self.client.get(reverse('add_to_cart', args=[self.food.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Cart.objects.filter(user=self.user, food=self.food).exists())
        
        response_cart = self.client.get(reverse('view_cart'))
        self.assertEqual(response_cart.status_code, 200)
        self.assertContains(response_cart, 'Test Pizza')

    def test_place_order(self):
        session = self.client.session
        session['user_id'] = self.user.id
        session['role'] = 'user'
        session.save()
        
        Cart.objects.create(user=self.user, food=self.food, quantity=2)
        
        response = self.client.get(reverse('place_order'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Order.objects.filter(user=self.user).exists())
        self.assertFalse(Cart.objects.filter(user=self.user).exists())

    def test_recommended_foods(self):
        session = self.client.session
        session['user_id'] = self.user.id
        session['role'] = 'user'
        session.save()
        
        response = self.client.get(reverse('recommended_foods'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Pizza')

    def test_admin_dashboard(self):
        session = self.client.session
        session['user_id'] = self.admin.id
        session['role'] = 'admin'
        session.save()
        
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Restaurant')

    def test_restaurant_dashboard(self):
        session = self.client.session
        session['user_id'] = self.restaurant.id
        session['role'] = 'restaurant'
        session.save()
        
        response = self.client.get(reverse('restaurant_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Pizza')
