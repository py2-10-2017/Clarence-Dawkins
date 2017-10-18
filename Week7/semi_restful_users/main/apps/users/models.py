from __future__ import unicode_literals

from django.db import models

class UserManager(models.Model):
    def validate(self,post_data):
        errors = {}

        #empty fields check
        for field,value in post_data.iteritems():
            if len(value)< 1:
                errors[field]="{} field is required".format(field.replace('_',''))

        #check field min length
            if field == "first_name" or field == "last_name":
                if not field in errors and len(value) < 3:
                    error[field] = "{} field "
        #check email            
            if not "email" in errors and not re.match(EMAIL_REGEX, post_data['email']):
                errors['email'] = "invalid email"
        #email valid check
        else:
            if len(self.filter(email=post_data['email'])) > 1:
                errors['email']="Email already taken"
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255) 
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.email
    
