async function download(url) {
    try {
        const response = await fetch(`/download?url=${encodeURIComponent(url)}`);
        const data = await response.json();
        console.log(data.video);

        const video = document.getElementById('video');
        video.style.display = 'block';
        video.src = data.video;

        // TODO: add "loading" functionality
    } catch (error) {
        console.error('Error:', error);
    }
}