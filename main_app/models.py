from django.db import models
from django.urls import reverse
from datetime import date

TUNINGS = (
    ('S', 'Standard'),
    ('D', 'Drop D'),
    ('C', 'Drop C'),
    ('G', 'Open G'),
)

# Create your models here.
class Guitar(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    age = models.IntegerField()

    def tuned_for_today(self):
        return self.tuning_set.filter(date=date.today()).count() >= 1

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})
        
class Tuning(models.Model):
    date = models.DateField('tuning date')
    tune = models.CharField(
        max_length=1,
        choices=TUNINGS,
        default=TUNINGS[0][0]
        )
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__(self):
        # nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_tune_display()} on {self.date}"

    # change the default sort order
    class Meta:
        ordering = ['-date']