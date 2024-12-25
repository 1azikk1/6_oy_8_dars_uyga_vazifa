setTimeout(() => {
    document.querySelectorAll('.messages .alert').forEach(el => {
        el.classList.add('fade-out');
    });
}, 4000);

setTimeout(() => {
    const messagesDiv = document.querySelector('.messages');
    if (messagesDiv) {
        messagesDiv.remove();
    }
}, 5000);
