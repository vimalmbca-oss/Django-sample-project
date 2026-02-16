from django.urls import path
from.views import *

app_name='blog'

# urlpatterns = [path('index/<int:id>/',index),path('old/',old_url,name="old_page"),
#                path('new/',new_url,name="new_page")
#                ]
#-----------------------------------------------------------------------------
# urlpatterns = [path('home/',Home)]

# urlpatterns = [path('list/' ,student_lists, name = "student_list"),
#                path('',add_studentinfo,name = "add_info"),
#                path('delete/<int:id>/',delete_info,name = "delete_std"),
#                path('edit/<int:id>/',edit_info,name = "update_std")
#                ] 
#-------------------------------------------------------------------------------
urlpatterns = [path('',main,name='info'),
               path('detail/<str:slug>/',detail,name='about'),
               path("contact/",contact, name="contact")
               ]