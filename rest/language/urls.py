from django.urls import path,include
from rest_framework import routers
from language import views
from .views import *
router=routers.DefaultRouter()
router.register('languages',views.LanguageView)
router.register('paradigms',views.paradigmView)
router.register('programmer',views.programmerView)

urlpatterns = [
    path('',include(router.urls)),
   
]
