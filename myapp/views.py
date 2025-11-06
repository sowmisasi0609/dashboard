from django.shortcuts import render

def student_dashboard(request):
    student_name = "Sowmya"
    subjects = [
        {"name": "Maths", "mark": 85},
        {"name": "Science", "mark": 72},
        {"name": "English", "mark": 55},
        {"name": "Computer", "mark": 91},
        {"name": "History", "mark": 45},
    ]

    progress = 78  # static progress %

    return render(request, "dashboard/dashboard.html", {
        "student_name": student_name,
        "subjects": subjects,
        "progress": progress,
    })
