from django.db import models

# Create your models here.
import json


class Foobar(models.Model):
    foo = models.CharField(max_length=200)

    def set_foo(self, x):
        self.foo = json.dumps(x)

    def get_foo(self):
        return json.loads(self.foo)
