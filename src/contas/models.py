from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Categorias'


class Transactions(models.Model):
  date = models.DateField()
  description = models.CharField(max_length=100)
  value = models.DecimalField(max_digits=7, decimal_places=2)
  observations = models.TextField(null=True, blank=True)
  category=models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = 'Transações'