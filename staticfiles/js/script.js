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

document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('#deletecomment');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            const confirmation = confirm("Bu izohni o'chirishni xohlaysizmi?");
            if (!confirmation) {
                event.preventDefault();
            }
        });
    });
});