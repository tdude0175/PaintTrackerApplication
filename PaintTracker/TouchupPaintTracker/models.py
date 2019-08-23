from django.db import models

# Create your models here.
# Model for recording TouchUp paints in stock, The code of the paint, The model of the car the paint is for,
# if there is any in stock and if it is being used
class TouchUpPaint(models.Model):
    paint_name = models.CharField(max_length=300)
    paint_code = models.CharField(max_length=10)
    car_model = models.CharField(max_length=100)
    is_in_possession = models.BooleanField(default=False)
    in_use = models.BooleanField(default=False)

    def __str__(self):
        return self.paint_code