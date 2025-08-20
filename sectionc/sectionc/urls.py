
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('lay/', views.lay, name='lay'),
    path('portfolio/', include('py_portfolio.urls'),name='py_portfolio'),  # Include the portfolio app URLs
    path('coffee/', include('coffee.urls'),name='coffee'),  # Include newcoffee app URLs
]
