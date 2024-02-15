const loader = document.getElementById('loader');
const error = document.getElementById('error');
const video = document.getElementById('video');

async function download(url) {
    resetStyles();

    try {
        loader.style.display = 'block';

        const response = await fetch(`/download?url=${encodeURIComponent(url)}`);
        const data = await response.json();

        loader.style.display = 'none';

        if (data.video === 'No video found.') {
            error.textContent = data.video;
        } else {
            video.style.display = 'block';
            video.src = data.video;
            // TODO: maybe instant download too?
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function resetStyles() {
    loader.style.display = 'none';
    video.style.display = 'none';
    error.textContent = '';
}