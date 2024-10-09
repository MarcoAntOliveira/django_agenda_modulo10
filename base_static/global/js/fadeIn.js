// Função para adicionar classe 'fade-in' quando o elemento entra na visualização
function fadeInOnScroll() {
    const elements = document.querySelectorAll('.fade-in');

    elements.forEach(element => {
        const elementPosition = element.getBoundingClientRect().top;
        const viewHeight = window.innerHeight;

        if (elementPosition < viewHeight - 100) {
            element.classList.add('visible');
        }
    });
}

// Escutar o evento de scroll
window.addEventListener('scroll', fadeInOnScroll);

// Chamar a função uma vez na carga da página
document.addEventListener('DOMContentLoaded', fadeInOnScroll);
