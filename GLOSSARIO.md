# Glossário

Termos técnicos que aparecem no projeto, explicados de forma simples.

## HTML
- **O que é:** a linguagem que descreve o conteúdo de uma página: títulos, textos, links, botões.
- **Para que serve:** é o "esqueleto" do site.
- **Exemplo:** `<p>Olá!</p>` mostra o texto "Olá!" como um parágrafo.

## Tag
- **O que é:** uma marcação do HTML entre `<` e `>`. A maioria abre (`<p>`) e fecha (`</p>`).
- **Para que serve:** diz ao navegador o que cada pedaço do texto é.
- **Exemplo:** `<h1>` é um título; `<a>` é um link.

## Atributo
- **O que é:** uma informação extra dentro de uma tag.
- **Para que serve:** dá detalhes, como o destino de um link.
- **Exemplo:** em `<a href="sobre.html">`, o `href` é o atributo que diz para onde o link vai.

## HTML semântico
- **O que é:** usar a tag certa para cada função: `header` (topo), `nav` (menu), `main` (conteúdo), `footer` (rodapé).
- **Para que serve:** leitores de tela (programas que leem o site em voz alta) entendem a página e a pessoa navega mais fácil.
- **Exemplo:** `<main id="conteudo">` marca a parte principal da página.

## lang
- **O que é:** atributo que diz o idioma da página.
- **Para que serve:** o leitor de tela escolhe a pronúncia certa.
- **Exemplo:** `<html lang="pt-BR">` = português do Brasil.

## alt
- **O que é:** um texto que descreve uma imagem.
- **Para que serve:** quem não enxerga a imagem (ou está sem internet) entende o que ela mostra.
- **Exemplo:** `<img src="gato.png" alt="Gato dormindo">`.

## CSS
- **O que é:** a linguagem que define a aparência: cores, tamanhos, espaços.
- **Para que serve:** deixa o site bonito e organizado.
- **Exemplo:** `h1 { color: green; }` pinta os títulos de verde.

## Seletor
- **O que é:** a parte do CSS que escolhe quais elementos vão receber o estilo.
- **Para que serve:** aplicar um visual só onde você quer.
- **Exemplo:** em `.btn { ... }`, o seletor `.btn` escolhe tudo que tem a classe "btn".

## Classe
- **O que é:** um nome que você dá a elementos do HTML, escrito em `class="..."`.
- **Para que serve:** usar o mesmo estilo em vários lugares.
- **Exemplo:** `<a class="btn">` recebe o visual de botão.

## Variável CSS
- **O que é:** um valor com nome, criado com `--`, que pode ser reutilizado.
- **Para que serve:** trocar uma cor em um lugar só e mudar o site todo (foi assim que fizemos o alto contraste).
- **Exemplo:** `--verde: #0B5D5B;` e depois `color: var(--verde);`.

## rem
- **O que é:** uma unidade de tamanho que depende do tamanho da letra base da página.
- **Para que serve:** quando o usuário aumenta a letra, tudo cresce junto.
- **Exemplo:** `padding: 1rem` é um espaço do tamanho de uma letra base.

## Mobile-first
- **O que é:** criar primeiro para o celular e depois ajustar para telas maiores.
- **Para que serve:** a maioria do público usa o celular.
- **Exemplo:** o menu começa como lista vertical e vira horizontal em telas grandes.

## Media query
- **O que é:** uma regra de CSS que só vale em certas condições, como a largura da tela.
- **Para que serve:** mudar o layout para telas maiores ou respeitar preferências do usuário.
- **Exemplo:** `@media (min-width: 48rem) { ... }` vale só em telas largas.

## Flexbox
- **O que é:** um jeito de CSS de alinhar itens em linha ou coluna (`display: flex`).
- **Para que serve:** organizar menus e botões lado a lado.
- **Exemplo:** o topo do site usa flexbox para pôr logo e botões na mesma linha.

## Grid
- **O que é:** um jeito de CSS de organizar itens em colunas e linhas, como uma tabela.
- **Para que serve:** montar a grade de cards.
- **Exemplo:** `grid-template-columns: repeat(2, 1fr)` cria 2 colunas iguais.

## viewport
- **O que é:** a área visível da página na tela do aparelho.
- **Para que serve:** a tag `<meta name="viewport">` faz o site se ajustar à tela do celular em vez de aparecer minúsculo.
- **Exemplo:** `width=device-width` usa a largura real do aparelho.

## SVG
- **O que é:** um tipo de imagem feita de formas matemáticas.
- **Para que serve:** fica nítida em qualquer tamanho e pesa muito pouco, bom para internet fraca.
- **Exemplo:** o logo do site é um SVG.

## JavaScript
- **O que é:** a linguagem que dá comportamento à página: reagir a cliques, abrir menus.
- **Para que serve:** fazer o menu, os botões de letra e o alto contraste funcionarem.
- **Exemplo:** ao clicar em "A+", o JavaScript aumenta a letra.

## Evento
- **O que é:** algo que acontece na página, como um clique ou uma tecla apertada.
- **Para que serve:** o JavaScript "escuta" o evento e responde.
- **Exemplo:** `addEventListener('click', ...)` roda uma ação quando alguém clica.

## localStorage
- **O que é:** uma memória do navegador onde o site guarda pequenas informações.
- **Para que serve:** lembrar sua escolha de tamanho de letra e de contraste na próxima visita.
- **Exemplo:** `localStorage.setItem('cpt-alto', '1')`.

## try/catch
- **O que é:** um bloco que tenta executar algo e, se der erro, segue sem quebrar.
- **Para que serve:** se o navegador bloquear o localStorage, o site continua funcionando.
- **Exemplo:** `try { ... } catch (e) { ... }`.

## ARIA (aria-expanded, aria-pressed...)
- **O que é:** atributos que dão informação extra para leitores de tela.
- **Para que serve:** dizer se um menu está aberto ou se um botão está ligado.
- **Exemplo:** `aria-expanded="true"` avisa que o menu está aberto.

## Foco
- **O que é:** o elemento que está "selecionado" ao navegar com a tecla Tab.
- **Para que serve:** quem não usa mouse precisa ver onde está; por isso o site desenha um contorno no foco.
- **Exemplo:** aperte Tab e veja o contorno azul nos links.

## Contraste
- **O que é:** a diferença de cor entre o texto e o fundo.
- **Para que serve:** quanto maior, mais fácil de ler. O mínimo recomendado é 4,5 para 1.
- **Exemplo:** texto preto no fundo creme tem contraste alto; cinza claro no branco, não.

## Acessibilidade
- **O que é:** fazer o site funcionar para todas as pessoas, inclusive com baixa visão ou usando só o teclado.
- **Para que serve:** ninguém fica de fora.
- **Exemplo:** link "Pular para o conteúdo" no topo.

## Git
- **O que é:** um programa que guarda o histórico de todas as mudanças do projeto.
- **Para que serve:** voltar atrás se algo der errado e saber o que mudou e quando.
- **Exemplo:** `git init` começa a acompanhar uma pasta.

## Repositório
- **O que é:** a pasta do projeto com todo o histórico do Git (fica numa pasta oculta `.git`).
- **Para que serve:** guardar o projeto e sua história.
- **Exemplo:** a pasta "Trabalho faculdade" agora é um repositório.

## Commit
- **O que é:** um "retrato" do projeto num momento, com uma mensagem explicando o que mudou.
- **Para que serve:** marcar etapas concluídas.
- **Exemplo:** `git commit -m "Adiciona a página inicial"`.

## Branch (main)
- **O que é:** uma linha de histórico do projeto. A principal se chama `main`.
- **Para que serve:** organizar o trabalho; o GitHub Pages publica a `main`.
- **Exemplo:** `git init -b main` cria o repositório já na `main`.

## .gitignore
- **O que é:** um arquivo que lista o que o Git deve ignorar.
- **Para que serve:** não guardar nem publicar arquivos que não fazem parte do site.
- **Exemplo:** a linha `.claude/` ignora a pasta das skills.
