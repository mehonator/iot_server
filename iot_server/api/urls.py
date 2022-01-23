from django.urls import path
from api.views import WakeOnLan, PersonalCompueterListView

urlpatterns = [
    path("wake-on-lan/<int:id>/", WakeOnLan.as_view()),
    path(
        "personal-computers/",
        PersonalCompueterListView.as_view({"get": "list"}),
    ),
]
