from django.contrib import admin
from django.urls import path
from rag_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('upload/', views.upload_view, name='upload'),
    path('query/', views.query_view, name='query'),
]
