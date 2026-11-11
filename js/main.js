// Conhecimento para Todos: menu do celular, tamanho da letra e alto contraste
(function () {
  var html = document.documentElement;
  html.classList.add('js'); // avisa o CSS que o JavaScript está funcionando

  // Ler/gravar na memória do navegador (localStorage). O try/catch evita erro se ela estiver bloqueada.
  function ler(chave) { try { return localStorage.getItem(chave); } catch (e) { return null; } }
  function gravar(chave, valor) { try { localStorage.setItem(chave, valor); } catch (e) { /* segue sem salvar */ } }

  var tamanho = parseInt(ler('cpt-fonte'), 10); // 0 = normal, 1 = grande, 2 = maior
  if (!(tamanho >= 0 && tamanho <= 2)) tamanho = 0;
  var alto = ler('cpt-alto') === '1';

  function aplicar() {
    html.classList.remove('f0', 'f1', 'f2');
    html.classList.add('f' + tamanho);
    html.classList.toggle('alto', alto);
  }
  aplicar(); // roda já no início para a página não "piscar"

  document.addEventListener('DOMContentLoaded', function () {
    var menu = document.getElementById('menu');
    var botaoMenu = document.querySelector('.menu-btn');
    var menos = document.querySelector('[data-fonte="-"]');
    var mais = document.querySelector('[data-fonte="+"]');
    var botaoAlto = document.querySelector('[data-contraste]');

    function atualizarBotoes() {
      menos.setAttribute('aria-disabled', tamanho === 0);
      mais.setAttribute('aria-disabled', tamanho === 2);
      botaoAlto.setAttribute('aria-pressed', alto);
    }
    atualizarBotoes();

    menos.addEventListener('click', function () {
      if (tamanho > 0) { tamanho--; gravar('cpt-fonte', tamanho); aplicar(); atualizarBotoes(); }
    });
    mais.addEventListener('click', function () {
      if (tamanho < 2) { tamanho++; gravar('cpt-fonte', tamanho); aplicar(); atualizarBotoes(); }
    });
    botaoAlto.addEventListener('click', function () {
      alto = !alto; gravar('cpt-alto', alto ? '1' : '0'); aplicar(); atualizarBotoes();
    });

    // Menu hambúrguer (só aparece no celular)
    botaoMenu.addEventListener('click', function () {
      var aberto = menu.classList.toggle('aberto');
      botaoMenu.setAttribute('aria-expanded', aberto);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('aberto')) {
        menu.classList.remove('aberto');
        botaoMenu.setAttribute('aria-expanded', 'false');
        botaoMenu.focus();
      }
    });

    // "Link desta aula": copia o endereço da aula (se o navegador deixar)
    document.querySelectorAll('.copiar').forEach(function (a) {
      a.addEventListener('click', function (e) {
        if (!navigator.clipboard) return; // sem copiar, o link comum continua funcionando
        e.preventDefault();
        var ancora = a.getAttribute('href');
        var texto = a.textContent;
        navigator.clipboard.writeText(location.href.split('#')[0] + ancora).then(function () {
          a.textContent = 'Link copiado!';
          history.replaceState(null, '', ancora);
          setTimeout(function () { a.textContent = texto; }, 2000);
        }, function () { location.hash = ancora; });
      });
    });
  });
})();
