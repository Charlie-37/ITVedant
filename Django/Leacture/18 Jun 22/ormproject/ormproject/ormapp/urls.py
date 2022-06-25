
from django.urls import path
from .import views as v
urlpatterns = [
    path('', v.home),
    path('insert',v.insert1),
    path('insert2',v.insert2),
    path('insert3',v.insert3),
    path('insert4',v.insert4),
    path('ulist',v.user_list),
    path('delete_emp',v.emp_delete),
    path('delete_emp2/<int:id>',v.emp_delete2),
     path('editemp/<int:id>',v.emp_edit),
]
