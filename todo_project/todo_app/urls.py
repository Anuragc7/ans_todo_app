from django . urls import path
from . import views

urlpatterns = [
    path('',views.task_view,name='task_view'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('cbvtask/',views.taskListview.as_view(),name='cbvtask'),
    path('cbvdetail/<int:pk>',views.taskDetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>',views.taskUpdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>', views.taskDeleteview.as_view(), name='cbvdelete')
]