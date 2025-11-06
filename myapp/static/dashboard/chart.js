var ctx = document.getElementById('subjectChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Maths', 'Science', 'English', 'Computer', 'History'],
        datasets: [{
            label: 'Marks',
            data: [85, 72, 55, 91, 45]
        }]
    }
});
