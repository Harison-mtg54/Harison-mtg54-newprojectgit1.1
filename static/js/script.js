console.log ("newproject garregado com sucesso!!");
document.addEventListener("DOMContentLoaded", function () {
    const botao = document.getElementById("botaoBoasVindas");

    if (botao) {
        botao.addEventListener("click", function () {
            alert("A área de cadastro será disponibilizada em breve.");
        });
    }

    const links = document.querySelectorAll(".menu-card");

    links.forEach(function (link) {
        link.addEventListener("click", function (event) {
            const destino = link.getAttribute("href");

            if (destino === "#") {
                event.preventDefault();
                alert("Esta opção ainda está em desenvolvimento.");
            }
        });
    });
});
