# Conhecimento para Todos

Site estático com **37 aulas gratuitas** de Excel, Power BI, Word, PowerPoint e Canva, do básico ao intermediário, para pessoas sem acesso a cursos pagos, com foco em jovens que querem gerar renda extra. Território do projeto: Jardim Betânia, Sorocaba/SP.

É a intervenção de um projeto de extensão do curso de ADS (itinerário Economia Sustentável), de autoria de Gustavo. Trabalha os ODS 4, 8 e 10.

**Site no ar:** https://gustavotajess.github.io/conhecimento-para-todos/

## O que tem no site

| Página | Conteúdo |
|---|---|
| `index.html` | Início: o projeto, para quem é e como usar |
| `trilhas.html` | As 5 ferramentas e o total de aulas |
| `excel.html` | 9 aulas (4 básicas e 5 intermediárias) |
| `powerbi.html`, `word.html`, `powerpoint.html`, `canva.html` | 7 aulas cada (4 básicas e 3 intermediárias) |
| `kit-empreendedor.html` | Planilha de controle financeiro, post no Canva e dicas de preço |
| `feedback.html` | Botão para o formulário de opinião |
| `sobre.html` | Sobre o projeto, o autor, o território e os ODS |
| `404.html` | Página mostrada quando um endereço não existe (o GitHub Pages usa esta página sozinho) |

Cada aula tem um endereço próprio, por exemplo `excel.html#excel-soma`.

## Tecnologia

Somente HTML, CSS e JavaScript puro. Sem frameworks, sem build, sem bibliotecas externas e sem imagens pesadas, para abrir rápido mesmo com internet fraca.

## Pastas

```
index.html, trilhas.html, ...   páginas do site (na raiz)
css/style.css                   todo o visual
js/main.js                      menu, tamanho da letra e alto contraste
downloads/                      planilha para baixar
ferramentas/gerar_planilha.py   script que cria a planilha (não faz parte do site)
GLOSSARIO.md                    termos técnicos explicados
DIARIO-PROJETO.md               registro do que foi feito, para o relatório de extensão
```

## Como abrir no seu computador

**Jeito mais simples:** dê dois cliques em `index.html`. O site abre no navegador.

**Jeito mais próximo de um site de verdade:** abra um terminal na pasta do projeto e rode:

```
python -m http.server 8000
```

Depois acesse http://localhost:8000 no navegador. Para parar, aperte `Ctrl` + `C` no terminal.

## O que falta preencher

- **Link do formulário de opinião:** já está em `feedback.html` (é o único lugar do site com esse link). Para trocar de formulário, mude o endereço desse botão.
- **Resultados do diagnóstico:** em `sobre.html`, troque `[PREENCHER]` pelos resultados reais do questionário e das conversas.
- **Planilha:** confira abrindo no Excel ou no Google Planilhas e digitando valores de teste.

## Como refazer a planilha

```
python -m pip install openpyxl
python ferramentas/gerar_planilha.py
```

O arquivo novo aparece em `downloads/controle-financeiro.xlsx`.

## Como publicar no GitHub Pages

1. Crie um repositório **público** no GitHub (nome sugerido: `conhecimento-para-todos`), sem marcar README, .gitignore nem licença.
2. Na pasta do projeto: `git remote add origin <URL do repositório>` e `git push -u origin main`.
3. No GitHub: **Settings > Pages > Source: Deploy from a branch > Branch: main, pasta / (root) > Save**.
4. O endereço fica `https://<usuario>.github.io/conhecimento-para-todos/` e pode levar alguns minutos para aparecer.
5. Para atualizar depois: `git add .`, `git commit -m "mensagem"` e `git push`.

Todos os caminhos do site são relativos (como `css/style.css`), então ele funciona dentro de uma subpasta do GitHub Pages.

## Visual e recursos

Estilo "caderno de bairro": fundo pontilhado, marca-texto, adesivos, ondas entre as seções e um mascote em SVG. Todas as ilustrações são SVG feitos à mão no próprio código (sem fotos nem fontes externas), e os desenhos repetidos usam `<symbol>` e `<use>`. Em cada aula há um botão **Marcar aula como concluída**: o progresso aparece na trilha de bolinhas e em uma barra no alto da página, e fica salvo só no navegador de quem usa. Sem JavaScript, o botão não aparece e o resto do site funciona normalmente.

## Acessibilidade

Letra base de 18 px, botões para aumentar e diminuir a letra, modo de alto contraste (que esconde as decorações e as texturas), animações desligadas para quem prefere menos movimento, menu acessível por teclado, link "Pular para o conteúdo", páginas pensadas primeiro para o celular e áreas de toque de pelo menos 44 px. As escolhas de letra e contraste ficam salvas no navegador.
