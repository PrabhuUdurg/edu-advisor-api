

from django.apps import AppConfig
from django.contrib import admin

# admin.site.register(User)
# admin.site.register(Survey)
#admin.site.register(Option)
#admin.site.register(Response)
#admin.site.register(Question)
class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    

