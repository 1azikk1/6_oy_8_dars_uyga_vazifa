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

//for form confirmation

document.querySelectorAll('.delete-comment-form').forEach(form => {
    form.addEventListener('submit', function(event) {
        if (!confirm("Siz rostdan ham bu izohni o'chirmoqchimisiz?")) {
            event.preventDefault();
        }
    });
});
