# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebApp.settings')
# import django
# django.setup()
# import random
# from .models import BloodValidator
# from faker import Faker

# fakegen = Faker()#object for faker class
# fake_request_id = fakegen.request_id()

# def add_BloodValidator():
#     s = BloodValidator.objects.create(request_id=random)
#     s.save()
#     return s

# def populate(N=100):
#     for entry in range(N):
#         request_id = add_BloodValidator()
#         fake_request_id= fakegen.request_id()
#         fakegen.isbn5()

# if __name__ == '__main__':
#     print("Populating")
#     populate(150)
#     print("Popolating")