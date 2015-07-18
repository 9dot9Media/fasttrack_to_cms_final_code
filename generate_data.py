"""
This nifty script can be used to fill up your newly created Django database
with some filler data so you can actually see something in the website without
needing to manually add this data.

Even during development it's good to have a way to fill your database with test
data to see if everything is working properly.

While this script is intended to work with the CMS as it was developed in the
FastTrack, you can easily modify it to work with the CMS in all stages. Simply
comment out code generating data that is not needed.
"""
import django
import os
import random

# In order for the following import to work you need to have fake-factory
# installed
try:
    from faker import Factory
except ImportError:
    import sys
    print('The fake-factory package for Python is required for this script to '
          'function but was not found \nInstall it with:\n\n'
          '   pip install fake-factory')
    sys.exit()

from django.conf import settings
from django.utils.text import slugify

os.environ['DJANGO_SETTINGS_MODULE'] = 'mycms.settings'
django.setup()

from cms.models import *

fake = Factory.create()

# Here we list the tags we want in our test website. Feel free to add, remove
# or modify items on this list.
tag_names = [
    'cats',
    'video',
    'twitter',
    'selfie',
    'potato',
    'GlaDOS',
    'tehnology',
    'apple',
    'ludonarritive',
    'finance',
    'facebook',
    'google',
    'android'
    'linux',
    'python',
    'django',
    'musical',
    'paradox',
    'rabbit',
    'cyborgs',
    'cms',
]

# These are the categories that will be added to the test websit when this
# script is run
category_names = [
    'Sports',
    'Finance',
    'Politics',
    'Cats',
    'Entertainment',
    'Health and Fitness',
    'Science',
]

# We have set the default directory for media files (i.e. files uploaded to the 
# website) as the dirctory called 'media' in our project folder. 
# This following line of code compiles the names of image files in the 'media' 
# folder.
# In it are some sample images that will be included in our cms. You can add / 
# remove images in this folder. Images in this folder will appear on the site 
# and will automatically and randomly be chosen to be included in articles, 
# categories and galleries.
image_files = os.listdir('media')

# This for loop iterates over the tags listed above and adds each one to the 
# database.
for tag in tag_names:
    print('Adding tag {}'.format(tag))
    t = Tag()
    t.name = tag
    # The slugify function takes some regular text and makes a URL-friendly but 
    # readable version of it
    t.slug = slugify(tag)
    t.save()

# Here we use the collect a list of all the newly inserted tag objects from the 
# database and put them in a list to easily include them in articles.  
tags = list(Tag.objects.all())


#Like with tags, we here add the categories to database
for category in category_names:
    print('Adding category {}'.format(category))
    c = Category()
    c.name = category
    c.slug = slugify(category)
    # Here we see the fake factory package in action. This generates a fake 
    # paragraph of text for us.
    c.description = fake.paragraph()
    # This line uses the Python standard random library to select a random image
    # from our list of images generated from the contents of the media folder
    c.image = random.choice(image_files)
    c.save()

categories = list(Category.objects.all())

# Now we add users to our database. Fake Factory can create convincing fake 
# names, usernames and email addresses. 
for _ in range(10):
    u = User()
    u.first_name = fake.first_name()
    u.last_name = fake.last_name()
    # Our CMS cannot currently handle username like `first.last` that have a 
    # period in them. If fake factory generates such a username we will replace 
    # the period with an underscore. 
    u.username = fake.user_name().replace('.', '_') 
    u.email = fake.email()
    print('Adding user {} {}'.format(u.first_name, u.last_name))
    u.save()

authors = list(User.objects.all())

# Now we add articles to our databaase. 
for ctr in range(100):
    a = Article()
    a.title = fake.sentence()[:-1]
    print('Adding article {}: {}'.format(ctr + 1, a.title))
    a.slug = slugify(a.title)
    # Select a random author.
    a.author = random.choice(authors)
    # This code will generate a random number (between 5 and 15) of paragraphs 
    # for this article. 
    a.content = '\n\n'.join(fake.paragraphs(random.randrange(5, 15)))
    a.featured_image = random.choice(image_files)
    a.publish_status = fake.boolean()
    a.category = random.choice(categories)
    # The article needs to be saved once before it gets an ID and hence we can 
    # add tags to it.
    a.save()
    # Here we take a random sample of a random number (between 2 and 7) of tags.
    a.tags = random.sample(tags, random.randrange(2, 7))
    a.save()

# Here we create a database entry for each image file in the media folder. 
for image in image_files:
    i = Image()
    i.name = fake.bs()
    i.slug = slugify(i.name)
    i.alt_text = fake.paragraph()
    i.image = random.choice(image_files)
    print('Adding image {}'.format(i.image))
    i.save()

images = list(Image.objects.all())

# Finally we add the galleries. The number of galleries is 1/3rd the number of 
# images. 
for _ in range(int(len(images)/3)):
    g = Gallery()
    g.name = fake.bs()
    print('Adding gallery {}'.format(g.name))
    g.slug = slugify(g.name)
    g.description = fake.paragraph()
    g.layout = random.choice(['LINK', 'HORI', 'VERT'])
    g.save()
    # Galleries should have a random selection of between 5 and 10 images.  
    g.images = random.sample(images, random.randrange(5, 10))
    g.save()
