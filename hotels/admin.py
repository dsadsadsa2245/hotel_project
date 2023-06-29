from django.contrib import admin
from .models import Hotel, Room, Reservation, Like, Permission

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Like)
admin.site.register(Permission)