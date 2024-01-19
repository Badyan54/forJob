from django.db import models

class DB_output(models.Model):

    value = models.CharField('value', max_length = 50)

    def __str__(self):
        return f"DB_output: {self.value}"

    class Meta:
        verbose_name = "DB_output"

