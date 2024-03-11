document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('#sugestao_form');
    var mensagem = document.querySelector('#mensagem');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Previne o envio padrão do formulário

        // Limpa os campos do formulário
        form.reset();

        // Exibe a mensagem de sucesso
        mensagem.textContent = "Sugestão enviada com sucesso! Redirecionando...";

        // Redireciona para outra página após um pequeno atraso
        setTimeout(function() {
            window.location.href = ' /'; // Substitua '/outra-pagina/' pela URL desejada
        }, 2000); // Atraso de 2 segundos (2000 milissegundos)
    });
});
