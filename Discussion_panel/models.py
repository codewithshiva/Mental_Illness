# from django.db import models
# from django.contrib.auth.models import User
# from django.utils.timezone import now
# from django.db import models
# import datetime
# from django.utils.timezone import now


# class discussion(models.Model):
#     sno= models.AutoField(primary_key=True)
#     chat=models.TextField()
#     user=models.ForeignKey(User, on_delete=models.CASCADE)
#     # post=models.ForeignKey(Post, on_delete=models.CASCADE)
#     parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
#     timestamp= models.DateTimeField(default=now)
