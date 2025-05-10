// Function to format numbers to 2 decimal places
function formatNumber(num) {
    return Number(num).toFixed(2);
}

// Function to update the timestamp
function updateTimestamp() {
    const now = new Date();
    document.getElementById('last-update').textContent = now.toLocaleString();
}

// Function to fetch and update metrics
async function fetchMetrics() {
    try {
        const response = await fetch('/api/metrics');
        const data = await response.json();
        
        // Update CPU metrics
        document.getElementById('cpu-percent').textContent = formatNumber(data.cpu.percent);
        
        // Update Memory metrics
        document.getElementById('memory-percent').textContent = formatNumber(data.memory.percent);
        document.getElementById('memory-total').textContent = formatNumber(data.memory.total);
        document.getElementById('memory-used').textContent = formatNumber(data.memory.used);
        document.getElementById('memory-free').textContent = formatNumber(data.memory.free);
        
        // Update Disk metrics
        document.getElementById('disk-percent').textContent = formatNumber(data.disk.percent);
        document.getElementById('disk-total').textContent = formatNumber(data.disk.total);
        document.getElementById('disk-used').textContent = formatNumber(data.disk.used);
        document.getElementById('disk-free').textContent = formatNumber(data.disk.free);
        
        // Update timestamp
        updateTimestamp();
    } catch (error) {
        console.error('Error fetching metrics:', error);
        // Show error state in UI
        document.querySelectorAll('.metric-card span').forEach(span => {
            span.textContent = 'Error';
            span.style.color = '#e74c3c';
        });
    }
}

// Function to refresh metrics (called by button click)
function refreshMetrics() {
    const button = document.querySelector('.refresh-button');
    button.textContent = 'Refreshing...';
    button.disabled = true;
    
    fetchMetrics().finally(() => {
        button.textContent = 'Refresh Metrics';
        button.disabled = false;
    });
}

// Initial load
fetchMetrics();

// Auto-refresh every 30 seconds
setInterval(fetchMetrics, 30000);
