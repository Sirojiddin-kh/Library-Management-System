from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Received)
admin.site.register(Menu)
admin.site.register(SideBar)
admin.site.register(SubMenu)
admin.site.register(HLog)

# Register your models here.
