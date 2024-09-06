from django.db import models


class Foodhub(models.Model):
    foodhub_id = models.CharField(max_length=25, unique=True)  # Using snake_case for field names is the Django convention
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)  # Use TextField for larger text fields
    phone = models.CharField(max_length=64, null=True, blank=True)
    host = models.CharField(max_length=128, null=True, blank=True)
    url = models.CharField(max_length=128, null=True, blank=True)
    country = models.CharField(max_length=256, null=True, blank=True)
    region = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    street = models.CharField(max_length=128, null=True, blank=True)
    number = models.CharField(max_length=64, null=True, blank=True)
    postcode = models.CharField(max_length=64, null=True, blank=True)
    Latitude = models.CharField(max_length=64, null=True, blank=True)
    Longitude = models.CharField(max_length=64, null=True, blank=True)
    rating = models.CharField(max_length=16, null=True, blank=True)
    total_reviews = models.CharField(max_length=16, null=True, blank=True)
    opening_hours = models.CharField(max_length=256, null=True, blank=True)
    review_categories = models.CharField(max_length=256, null=True, blank=True)
    cuisines = models.CharField(max_length=256, null=True, blank=True)
    merchant_id = models.CharField(max_length=32, null=True, blank=True)
    delivery_time = models.CharField(max_length=32, null=True, blank=True)
    collection_time = models.CharField(max_length=32, null=True, blank=True)
    town = models.CharField(max_length=128, null=True, blank=True)
    facebook = models.CharField(max_length=128, null=True, blank=True)
    twitter = models.CharField(max_length=128, null=True, blank=True)
    android_link = models.CharField(max_length=128, null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    seo = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Foodhub'  # Specify the database table name explicitly

    def __str__(self):
        return self.name


class Justeat(models.Model):
    shop_id = models.CharField(max_length=16, null=True, blank=True)
    name = models.CharField(max_length=32, null=True, blank=True)
    uniqueName = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=16, null=True, blank=True)
    area = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=64, null=True, blank=True)
    postcode = models.CharField(max_length=32, null=True, blank=True)
    lng = models.CharField(max_length=32, null=True, blank=True)
    lat = models.CharField(max_length=32, null=True, blank=True)
    rating = models.CharField(max_length=16, null=True, blank=True)
    starRating = models.CharField(max_length=16, null=True, blank=True)
    isNew = models.CharField(max_length=16, null=True, blank=True)
    openingTimeLocal = models.CharField(max_length=64, null=True, blank=True)
    cuisines = models.CharField(max_length=256, null=True, blank=True)
    deliveryFees = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'Justeat'



class WTF(models.Model):
    shop_id = models.CharField(max_length=16, null=True, blank=True)
    name = models.CharField(max_length=32, null=True, blank=True)
    uniqueName = models.CharField(max_length=32, null=True, blank=True)
    url_map = models.CharField(max_length=64, null=True, blank=True)
    map_preview_url = models.CharField(max_length=64, null=True, blank=True)
    about_text = models.CharField(max_length=255, null=True, blank=True)
    email_business = models.CharField(max_length=32, null=True, blank=True)
    email = models.CharField(max_length=32, null=True, blank=True)
    instagram_url = models.CharField(max_length=64, null=True, blank=True)
    facebook_url = models.CharField(max_length=64, null=True, blank=True)
    twitter_url = models.CharField(max_length=64, null=True, blank=True)
    google_play_link = models.CharField(max_length=64, null=True, blank=True)
    app_store_link = models.CharField(max_length=64, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    main_text = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=50, null=True, blank=True)
    openingHoursReadable = models.CharField(max_length=100, null=True, blank=True)
    categories = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=64, null=True, blank=True)
    region = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=16, null=True, blank=True)
    postcode = models.CharField(max_length=16, null=True, blank=True)
    lat = models.CharField(max_length=50, null=True, blank=True)
    lng = models.CharField(max_length=50, null=True, blank=True)
    notes = models.CharField(max_length=255, null=True, blank=True)
    currency = models.CharField(max_length=50, null=True, blank=True)
    rating_count = models.CharField(max_length=16, null=True, blank=True)
    rating_average = models.CharField(max_length=16, null=True, blank=True)

    class Meta:
        db_table = 'WTF'



class UberEats(models.Model):
    shop_id = models.CharField(max_length=32, unique=True)
    shop_url = models.URLField(max_length=256)
    name = models.CharField(max_length=64, blank=True, null=True)
    shop_type = models.CharField(max_length=64, blank=True, null=True)
    rating = models.CharField(max_length=16, blank=True, null=True)
    Latitude = models.CharField(max_length=64, blank=True, null=True)
    Longitude = models.CharField(max_length=64, blank=True, null=True)


    class Meta:
        db_table = 'UberEats'
        constraints = [
            models.UniqueConstraint(fields=['shop_id'], name='UberEats_pk_2')
        ]

    def __str__(self):
        return self.name if self.name else f'Shop {self.shop_id}'


class Foodhouse(models.Model):
    url = models.CharField(max_length=256, null=True, blank=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    postcode = models.CharField(max_length=32, null=True, blank=True)
    phone = models.CharField(max_length=64, null=True, blank=True)
    social_media = models.CharField(max_length=256, null=True, blank=True)
    apps = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'Foodhouse'

    def __str__(self):
        return self.name