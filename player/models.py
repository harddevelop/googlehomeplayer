from django.db import models

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=1024)
    duration = models.IntegerField()


class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TrackPlaylist(models.Model):
    track = models.ForeignKey(Track,on_delete=models.CASCADE)
    playlist = models.ManyToManyField(Playlist)

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    ip_address = models.CharField(max_length=15)
    port = models.CharField(max_length=5)
    friendly_name = models.CharField(max_length=60)
    model_name = models.CharField(max_length=20)
    uuid = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    duration = models.FloatField(default=0.0,null=True)
    current = models.FloatField(default=0.0,null=True)
    state = models.CharField(max_length=20,default="UNKNOWN",null=True)
    volume = models.FloatField(default=0.0,null=True)
    content = models.TextField(default="UNKNOWN",null=True)
    app = models.CharField(max_length=20,default="UNKNNOWN",null=True)
    updated = models.DateTimeField(auto_now_add=True)
