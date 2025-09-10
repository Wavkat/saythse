from django.urls import path
from django.contrib.admin import AdminSite
from main.core.models import Contact
from main.core.admin import ContactAdmin
from main.core import views

# Custom admin sayt
class MyAdminSite(AdminSite):
    def index(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context['recent_actions'] = []  # recent actions'ni yashirish
        return super().index(request, extra_context=extra_context)

admin_site = MyAdminSite()
admin_site.site_header = "My Custom Admin"
admin_site.register(Contact, ContactAdmin)

urlpatterns = [
    path('', views.home, name='home'),
    path('ajax/search/', views.ajax_search, name='ajax_search'),

]
