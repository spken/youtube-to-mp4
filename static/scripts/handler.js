async function download(url) {
    try {
        const response = await fetch(`/download/${encodeURIComponent(url)}`);
        const data = await response.json();
        console.log(data.title);
    } catch (error) {
        console.error('Error:', error);
    }
}