// Dummy function to simulate API call
function createApproval() {
    const header = document.getElementById('header').value;
    const value = document.getElementById('value').value;
    const type = document.getElementById('type').value;

    // Simulate API call to the backend
    const response = { status: 'Pending', message: 'Approval request submitted successfully.' };

    // Display the approval status
    document.getElementById('approvalStatus').innerText = `Status: ${response.status}\nMessage: ${response.message}`;
}