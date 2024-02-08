import os
import django
import random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "health_tracker.settings")
django.setup()

from features.models import CommunityPost

fake = Faker()

def create_fake_posts(num_posts):
    for _ in range(num_posts):
        subject = fake.sentence()
        body = fake.paragraph()
        CommunityPost.objects.create(subject=subject, body=body)

if __name__ == "__main__":
    create_fake_posts(50)
