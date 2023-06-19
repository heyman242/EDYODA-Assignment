from django.contrib import admin
from .models import NewUser, PrivateMusicRecord, PublicMusicRecord, ProtectedMusicRecord

admin.site.register(NewUser)

admin.site.register(PrivateMusicRecord)
admin.site.register(ProtectedMusicRecord)
admin.site.register(PublicMusicRecord)
# Register your models here.
