"""educa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path, include
from courses.views import CourseListView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('accounts/login/', auth_views.LoginView.as_view(),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('students/', include('students.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)