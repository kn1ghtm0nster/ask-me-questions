# NOTE: THIS SCRIPT IS PURELY TO HELP YOU GENERATE A SECRET KEY FOR THE DJANGO PROJECT. DO NOT CHANGE UNLESS YOU KNOW
# WHAT YOU'RE DOING!

from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key()
print(SECRET_KEY)
