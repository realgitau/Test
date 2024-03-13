from django.db import models

PARENT_CATEGORY_CHOICES = (
    ('Phones & Tablets', 'Phones & Tablets'),
    ('TVs Audios and Cameras', 'TVs Audios and Cameras'),
    ('Home Appliances', 'Home Appliances'),
    ('Computing', 'Computing'),
    ('Gaming', 'Gaming'),
    ('Fashion', 'Fashion'),
    ('Health & Beauty', 'Health & Beauty'),
    ('Baby Products', 'Baby Products'),
    ('Automobile', 'Automobile'),
    ('Other Categories', 'Other Categories'),
)



class Category(models.Model):
    title = models.CharField(max_length=100, choices=PARENT_CATEGORY_CHOICES, null=True, blank=True)
    sub_category = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

# mapping of main categories to subcategories
SUBCATEGORIES_MAPPING = {
    'Phones & Tablets': 'Accessories,Mobile Phones,Tablets',
    'TVs Audios and Cameras': 'TVs,Audio,Cameras',
    # Define subcategories for other main categories here
}

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return f"{self.category.title} - {self.title}"
    
    def create_subcategories():
        for main_category, subcategories in SUBCATEGORIES_MAPPING.items():
            category = Category.objects.get_or_create(title=main_category)[0]
            for subcategory_title in subcategories.split(','):
                SubCategory.objects.get_or_create(category=category, title=subcategory_title.strip())

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # Add more fields as needed for your product model

    def __str__(self):
        return self.title