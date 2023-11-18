# your_app/management/commands/insert_dummy_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...models import Book, Author, Review, Order
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Inserts dummy data into the bookstore models'

    def handle(self, *args, **options):
        # Insert dummy data for testing purposes
        for _ in range(10):
            user = User.objects.create(username=fake.user_name(), password=fake.password())
            book = Book.objects.create(title=fake.word(), price=fake.random_int(), publication_date=fake.date())
            author = Author.objects.create(name=fake.name(), birth_date=fake.date_of_birth(), bio=fake.text())
            review = Review.objects.create(reviewer_name=user, content=fake.text(), rating=fake.random_int(1, 5))
            order = Order.objects.create(user=user, book=book)

        self.stdout.write(self.style.SUCCESS('Dummy data inserted successfully.'))
