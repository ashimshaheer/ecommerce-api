from django.urls import include, path
from knox import views as knox_views
from .import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   path('login/',views.login_api),
   path('user/',views.get_user_data),
   path('register/',views.register_api),
   path('logout',knox_views.LoginView.as_view()),
   path('logout',knox_views.LogoutAllView.as_view()),

]