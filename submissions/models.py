from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    code_submission = models.TextField()
    feedback = models.TextField()
    improved_code = models.TextField()
    roast = models.TextField()    
    
    def __str__(self):
        return f"Code: {self.title} - received the following roast {self.roast}"