from django.urls import path
from . import views


urlpatterns = [
    # Normal URL
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('book/', views.book, name='book'),   

    # path('reservations/', views.reservations, name="reservations"),
    # path('bookings', views.bookings, name='bookings'), 

    # API URL
    path('api/booking/', views.BookingView.as_view()),
    path('api/menu/', views.MenuItemsView.as_view()),
    path('api/menu/<int:pk>', views.SingleMenuView.as_view()),
]