from django.urls import path
from .views import home, add_job, delete_job, update_status, accepted_jobs, rejected_jobs, none

urlpatterns = [
    path('', home, name='home'),
    path('add-job/', add_job, name='add_job'),
    path('delete-job/<int:job_id>/', delete_job, name='delete_job'),
    path('update-status/<int:job_id>/<str:status>/', update_status, name='update_status'),
    path('accepted-jobs/', accepted_jobs, name='accepted_jobs'),
    path('rejected-jobs/', rejected_jobs, name='rejected_jobs'),
    path('None/', none, name='none')
]