from django.urls import path
from .views import HomeView, DiscussionDetail
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('discussion/<int:primary_key>/<str:user_id>', views.DetailDiscussion,
         name='discussion-detail')
]
