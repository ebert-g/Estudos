const validUser = "cauan.oliveira";
const validPass = "123456";

document.getElementById('loginForm').addEventListener('submit', function(event) {
  event.preventDefault(); // evitar envio padrão

  const userInput = document.getElementById('email').value.trim();
  const passInput = document.getElementById('senha').value;

  const errorDiv = document.getElementById('errorMessage');

  if (userInput === validUser && passInput === validPass) {
    // Login ok, redireciona
    window.location.href = "./frontend/feed.html";
  } else {
    // Mostrar erro
    errorDiv.textContent = "Usuário ou senha incorretos.";
    errorDiv.style.display = "block";
  }
});