from django.db import models

# Create your models here.
class Code_Input(models.Model):
    code_reference_name = models.CharField(max_length=250)
    input_code = models.TextField()

    def __str__(self):
        return f"{self.code_reference_name}"

class Code_Response(models.Model):
    link_to_input_code = models.ForeignKey(Code_Input, on_delete=models.CASCADE)
    feedback = models.TextField()
    new_code = models.TextField()
    roast = models.TextField()

    def __str__(self):
        return f"{self.link_to_input_code} - {self.roast}"