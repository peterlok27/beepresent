from django.db import models


# Create your models here.
actions = [('display','Display'),('spinHeart','Spin The Heart'),('blinkLEDs','Blink LEDS')]
class Message(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    actions = models.CharField(choices=actions ,default='display',max_length=100)
    read = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User',related_name='message', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ['created'] 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)