from django.contrib import admin
from django.urls import path
from . import views
from .views import person_list

app_name= "jquery"

urlpatterns=[
path('admin/', admin.site.urls),
path('personlist/', person_list.as_view(), name='person-list'),
path('form/', views.formsubmit ,name="form"),
path('delete/<int:person_id>',views.delete,name='delete'),
path('update/<int:id>',views.update,name='update'),
path('map/',views.address_submit,name='address'),
path('delete1/<int:map_id>',views.deletemap,name='delete')
]
