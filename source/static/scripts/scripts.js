document.addEventListener('DOMContentLoaded', function () {
    // Notification Toggle Persistence Functionality
    const toggleSwitch = document.getElementById('notificationToggle');

    toggleSwitch.addEventListener('change', function () {
        const status = this.checked;
        fetch('/toggle_notification', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({'status': status}),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Notification status updated:', data.success);
        })
        .catch(error => console.error('Error updating notification status:', error));
    });

    fetch('/get_notification_status')
    .then(response => response.json())
    .then(data => {
        toggleSwitch.checked = data.status === 1; // Adjusted to correctly handle integer status
    });

    // New Popup Functionality for Tasks Due Today and Tomorrow
    // Check if notification is enabled, then fetch due tasks
    fetch('/get_notification_status')
    .then(response => response.json())
    .then(data => {
        if (data.status === 1) { // If notifications are on
            fetchDueTasks();
        }
    });

    function fetchDueTasks() {
        fetch('/due_tasks')
        .then(response => response.json())
        .then(tasks => {
            if (tasks.length > 0) {
                displayPopup(tasks);
            }
        })
        .catch(error => console.error('Error fetching due tasks:', error));
    }

    function displayPopup(tasks) {
        let popup = document.createElement('div');
        popup.setAttribute('class', 'popup');
        let html = '<span class="close" onclick="this.parentElement.style.display=\'none\';">&times;</span>';
        html += '<h2>Tasks Due Soon:</h2><ul>';
        tasks.forEach(task => {
            html += `<li>${task.task} - Due Date: ${task.due_date}</li>`;
        });
        html += '</ul>';
        popup.innerHTML = html;
        document.body.appendChild(popup);
    }

    // Highlight overdue tasks
    // Select all elements that contain the due dates
    let dueDateItems = document.querySelectorAll('.due-date');

    // Get current date and set time to 00:00:00
    let currentDate = new Date();
    currentDate.setHours(0, 0, 0, 0);

    // Iterate over the due date items
    dueDateItems.forEach(function(dueDateItem) {
    // Get the text content and convert it to a date
    let dueDateString = dueDateItem.textContent || dueDateItem.innerText;
    let dueDate = new Date(dueDateString);

    // Compare the due date with the current date
    if (dueDate < currentDate) {
        // If the due date is before the current date, highlight it in red
        dueDateItem.style.backgroundColor = 'red';
        dueDateItem.style.color = 'white';
    }
});


});






