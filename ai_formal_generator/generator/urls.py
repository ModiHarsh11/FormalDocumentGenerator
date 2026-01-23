from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("generate/", views.generate_document, name="generate_document"),
    path("download/pdf/", views.download_pdf, name="download_pdf"),
    path("download/docx/", views.download_docx, name="download_docx"),
]
