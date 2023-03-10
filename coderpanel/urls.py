from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard,name="dashboard"),
    path('login/', views.dashboardLogin,name="dashboardLogin"),
    path('logout/', views.dashboardLogout,name="dashboardLogout"),
    # PATH FOR EDIT PORTFOLIO
    path('portfolio/showRoleName/', views.showRoleName,name="showRoleName"),
    path('portfolio/deleteRoleName/<str:id>/', views.deleteRoleName,name="deleteRoleName"),
    path('portfolio/editRoleName/<str:id>/', views.editRoleName,name="editRoleName"),
    path('portfolio/activeRoleName/<str:id>/', views.activeRoleName,name="activeRoleName"),
    # ABout section title
    path('portfolio/showAboutSectionTitle/', views.showAboutSectionTitle,name="showAboutSectionTitle"),
    path('portfolio/deleteAboutSectionTitle/<str:id>/', views.deleteAboutSectionTitle,name="deleteAboutSectionTitle"),
    path('portfolio/editAboutSectionTitle/<str:id>/', views.editAboutSectionTitle,name="editAboutSectionTitle"),
    path('portfolio/activeAboutSectionTitle/<str:id>/', views.activeAboutSectionTitle,name="activeAboutSectionTitle"),
    # ABout shortintro section
    path('portfolio/showShortIntro/', views.showShortIntro,name="showShortIntro"),
    path('portfolio/deleteShortIntro/<str:id>/', views.deleteShortIntro,name="deleteShortIntro"),
    path('portfolio/editShortIntro/<str:id>/', views.editShortIntro,name="editShortIntro"),
    path('portfolio/activeShortIntro/<str:id>/', views.activeShortIntro,name="activeShortIntro"),


    
]