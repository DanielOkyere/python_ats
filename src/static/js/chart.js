/**
 * JS For Handling Chart on result
 */

const ctx = document.getElementById('resultChart')
const chartData = document.getElementById('tableData')
const hard = chartData.getAttribute('data-hard')
const soft = chartData.getAttribute('data-soft')
const general = chartData.getAttribute('data-general')

const results = [
    hard * 100,
    soft * 100,
    general * 100
]
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Hard Skills', 'Soft Skills', 'General Skills'],
        datasets: [{
           
            data: results,
            backgroundColor: [
                'rgb(255,99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)'
            ],
            hoverOffset: 4,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
})