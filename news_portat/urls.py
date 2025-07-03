from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='flatpages/default.html'), name='default'),
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact_page/', TemplateView.as_view(template_name='contact_page.html'), name='contact'),
    path('products/', include('products.urls')),
    path('news/', include('news.urls')),
    path('sing/', include('sing.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
]