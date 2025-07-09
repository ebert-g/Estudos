const ongs = [
    {
        nome: "Instituto Esperança",
        valor: 2000,
        cidade: "São Paulo",
        data: "10/05/2024",
        avatar: "./assets/img/Instituto_Esperança.png",
        icone: "https://img.icons8.com/color/48/000000/prize.png",
    },
    {
        nome: "Associação Vida Nova",
        valor: 1750,
        cidade: "Belo Horizonte",
        data: "08/05/2024",
        avatar: "./assets/img/Associação_Vida_Nova.png",
        icone: "",
    },
    {
        nome: "Amigos do Bem",
        valor: 1500,
        cidade: "Rio de Janeiro",
        data: "05/05/2024",
        avatar: "./assets/img/Amigos_do_Bem.png",
        icone: "",
    },
    {
        nome: "Projeto Sementes",
        valor: 1400,
        cidade: "Salvador",
        data: "02/05/2024",
        avatar: "./assets/img/Projeto_Sementes.png",
        icone: "",
    },
    {
        nome: "Ação Solidária",
        valor: 1300,
        cidade: "Fortaleza",
        data: "01/05/2024",
        avatar: "./assets/img/Ação_Solidária.png",
        icone: "",
    },
    {
        nome: "Cuidar Mais",
        valor: 1250,
        cidade: "Recife",
        data: "29/04/2024",
        avatar: "./assets/img/Cuidar_Mais.jpeg",
        icone: "",
    },
    {
        nome: "Luz para Todos",
        valor: 1200,
        cidade: "Manaus",
        data: "27/04/2024",
        avatar: "./assets/img/Luz_Para_Todos.png",
        icone: "",
    },
    {
        nome: "Mãos Unidas",
        valor: 1150,
        cidade: "Curitiba",
        data: "26/04/2024",
        avatar: "./assets/img/Maos_Unidas.png",
        icone: "",
    },
    {
        nome: "Casa Rubro-Negra",
        valor: 1800,
        cidade: "Salvador - BA",
        data: "25/04/2024",
        avatar: "./assets/img/vitoria.png",
        icone: "",
    },
    {
        nome: "ONG do Bem",
        valor: 1000,
        cidade: "Porto Alegre",
        data: "24/04/2024",
        avatar: "./assets/img/ONG_do_Bem.png",
        icone: "",
    },
];

const lista = document.getElementById("lista-ongs");

function renderizarOngs() {
    ongs.forEach((ong, index) => {
        const card = document.createElement("div");
        let medalha = "";
        if (index === 0) {
            medalha = "./assets/img/medalha-de-ouro.png";
        } else if (index === 1) {
            medalha = "./assets/img/medalha-de-prata.png";
        } else if (index === 2) {
            medalha = "./assets/img/medalha-de-bronze.png";
        }
        card.className = "d-flex align-items-start gap-3 mb-3";
        card.innerHTML = `
    <div class="d-flex flex-column align-items-center justify-content-center" style="width: 50px;">
  ${
      medalha
          ? `<img src="${medalha}" alt="Medalha" width="24" style="margin-left:-6px;" />`
          : ""
  }
  <span class="fw-bold">${index + 1}º</span>
</div>
        <img
            src="${ong.avatar}"
            alt="Logo ONG"
            class="rounded-circle"
            width="48"
        />
        <div>
            <h6 class="mb-0 fw-bold">${ong.nome}</h6>
            <p class="mb-0 text-success">
                R$ ${ong.valor.toFixed(2).replace(".", ",")}
            </p>
            <small class="text-muted"
                >${ong.cidade}<br />Última doação: ${ong.data}</small
            >
        </div>`;
        lista.appendChild(card);
    });
}
function simularDoacoes() {
    const index = Math.floor(Math.random() * ongs.length);
    const valor = Math.floor(Math.random() * 91 + 10);
    ongs[index].valor += valor;
    const hoje = new Date();
    ongs[index].data = hoje.toLocaleDateString("pt-br");
    ongs.sort((a, b) => b.valor - a.valor);
    lista.innerHTML = "";
    renderizarOngs();
}

setInterval(simularDoacoes, 100);


