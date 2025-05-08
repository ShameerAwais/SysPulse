document.addEventListener("DOMContentLoaded", function() {
    const updateMetrics = () => {
        // Fetch CPU data
        fetch('/metrics/cpu')
            .then(response => response.json())
            .then(data => {
                document.getElementById('cpu-percent').textContent = data.cpu_percent;
            });

        // Fetch Memory data
        fetch('/metrics/memory')
            .then(response => response.json())
            .then(data => {
                document.getElementById('memory-percent').textContent = data.percent;
                document.getElementById('memory-total').textContent = data.total_gb;
                document.getElementById('memory-used').textContent = data.used_gb;
                document.getElementById('memory-free').textContent = data.free_gb;
            });

        // Fetch Disk data
        fetch('/metrics/disk')
            .then(response => response.json())
            .then(data => {
                document.getElementById('disk-percent').textContent = data.percent;
                document.getElementById('disk-total').textContent = data.total_gb;
                document.getElementById('disk-used').textContent = data.used_gb;
                document.getElementById('disk-free').textContent = data.free_gb;
            });
    };

    // Update the metrics every 5 seconds
    setInterval(updateMetrics, 5000);
    updateMetrics();  // Initial load
});
