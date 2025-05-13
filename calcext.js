function somar(a, b) {
    return a + b;
  }
  
  function subtrair(a, b) {
    return a - b;
  }
  
  function multiplicar(a, b) {
    return a * b;
  }
  
  function dividir(a, b) {
    return b === 0 ? "Divisão por zero não é permitida" : a / b;
  }
  
  function potencia(a, b) {
    return Math.pow(a, b);
  }
  
  function executar() {
    const a = Number(document.getElementById("v1").value);
    const b = Number(document.getElementById("v2").value);
    const op = document.getElementById("op").value;
  
    const resultado =
      op === "soma"
        ? somar(a, b)
        : op === "subtracao"
        ? subtrair(a, b)
        : op === "multiplicacao"
        ? multiplicar(a, b)
        : op === "divisao"
        ? dividir(a, b)
        : op === "potencia"
        ? potencia(a, b)
        : "Operação inválida";
  
    document.getElementById("resultado").innerHTML = `resultado: ${resultado}`;
  }