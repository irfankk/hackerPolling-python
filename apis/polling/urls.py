from django.conf.urls import url, include

from rest_framework import routers

from apis.polling import views

router = routers.DefaultRouter()
router.register(r'list', views.CandidateListView, basename='candidate-list')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'best-candidate/', views.BestCandidateView.as_view()),
    url(r'start/',views.PollingView.as_view()),
]