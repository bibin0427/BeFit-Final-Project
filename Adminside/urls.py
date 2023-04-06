from django.urls import path
from.import views

urlpatterns=[
    path('indexfile/', views.indexfile, name="indexfile"),
    path('adminpage/', views.adminpage, name="adminpage"),
    path('admindata/', views.admindata, name="admindata"),
    path('displayadmin/', views.displayadmin, name="displayadmin"),
    path('editcustm/<int:dataid>/', views.editcustm, name="editcustm"),
    path('updatedata/<int:dataid>/', views.updatedata, name="updatedata"),
    path('deletedata/<int:dataid>/', views.deletedata, name="deletedata"),
    path('catpage/', views.catpage, name="catpage"),
    path('catdata/', views.catdata, name="catdata"),
    path('displaycat/', views.displaycat, name="displaycat"),
    path('editcat/<int:dataid>/', views.editcat, name="editcat"),
    path('updatecatdata/<int:dataid>/', views.updatecatdata, name="updatecatdata"),
    path('deletecatdata/<int:dataid>/', views.deletecatdata, name="deletecatdata"),
    path('productpage/', views.productpage, name="productpage"),
    path('productdata/', views.productdata, name="productdata"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteprodata/<int:dataid>/', views.deleteprodata, name="deleteprodata"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
]