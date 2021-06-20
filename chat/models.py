from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class Message(models.Model):
    auther=models.ForeignKey(User,related_name='author_messages',on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    reciever=models.ForeignKey(User,related_name='msg_reciever',on_delete=models.CASCADE)

    
    def __str__(self):
        return self.auther

class Room(models.Model):
    group_name=models.CharField(max_length=30)
    
    blocked=models.ForeignKey(User,related_name="blocked_user",on_delete=models.SET_NULL,null=True,blank=True)
    group_admin=models.ForeignKey(User,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.group_name

class groupMessage(models.Model):
    auther=models.ForeignKey(User,related_name='group_message_sender',on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    reciever=models.ForeignKey(Room,related_name='grp_msg_reciever',on_delete=models.CASCADE)
  
    def __str__(self):
        return self.reciever.group_name

