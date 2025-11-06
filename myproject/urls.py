from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('', lambda request: redirect('student_dashboard')),
]


