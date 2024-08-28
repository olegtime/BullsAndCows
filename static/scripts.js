document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.flash');
    flashMessages.forEach(flash => {
        setTimeout(() => {
            flash.classList.add('fade-out');
        }, 3000);
    });

    document.addEventListener('animationend', function(e) {
        if (e.animationName === 'fadeOut') {
            e.target.remove();
        }
    });
});
