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
        // Fetch CPU metrics
        const cpuResponse = await fetch('/metrics/cpu');
        const cpuData = await cpuResponse.json();
        
        // Fetch Memory metrics
        const memoryResponse = await fetch('/metrics/memory');
        const memoryData = await memoryResponse.json();
        
        // Fetch Disk metrics
        const diskResponse = await fetch('/metrics/disk');
        const diskData = await diskResponse.json();
        
        // Update CPU metrics
        document.getElementById('cpu-percent').textContent = formatNumber(cpuData.cpu_percent);
        
        // Update Memory metrics
        document.getElementById('memory-percent').textContent = formatNumber(memoryData.percent);
        document.getElementById('memory-total').textContent = formatNumber(memoryData.total_gb);
        document.getElementById('memory-used').textContent = formatNumber(memoryData.used_gb);
        document.getElementById('memory-free').textContent = formatNumber(memoryData.free_gb);
        
        // Update Disk metrics
        document.getElementById('disk-percent').textContent = formatNumber(diskData.percent);
        document.getElementById('disk-total').textContent = formatNumber(diskData.total_gb);
        document.getElementById('disk-used').textContent = formatNumber(diskData.used_gb);
        document.getElementById('disk-free').textContent = formatNumber(diskData.free_gb);
        
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
