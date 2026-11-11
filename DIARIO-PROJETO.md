# Diário do projeto: Conhecimento para Todos

## 2026-11-11 | Etapa A: base do site
**O que foi feito:** repositório Git na branch `main`; `.gitignore`; estilo (`css/style.css`); script do menu, do tamanho da letra e do alto contraste (`js/main.js`); páginas Início, Trilhas, Sobre e Feedback; página provisória do Kit do Empreendedor; GLOSSARIO.md.

**Decisões e por quê:**
- Só HTML, CSS e JavaScript puro, sem bibliotecas: o site abre rápido mesmo com internet fraca e é fácil de publicar no GitHub Pages.
- Fontes do próprio aparelho, sem imagens pesadas: economiza internet.
- Menu copiado em cada página (e não montado por JavaScript): o site funciona mesmo se o JavaScript falhar.
- Botões de aumentar a letra e de alto contraste, com a escolha salva no navegador: o público tem níveis diferentes de visão e de familiaridade com tecnologia.
- Quando houve conflito entre beleza e leveza, a leveza venceu.
- Total de 37 aulas planejadas (9 de Excel e 7 de cada uma das outras quatro ferramentas). Cards de ferramentas sem página ficam como "Em breve".
- Link do Google Forms deixado como `LINK_DO_GOOGLE_FORMS`, em um único lugar (feedback.html), até o formulário ficar pronto.
- Os resultados do diagnóstico em Sobre estão como [PREENCHER]: ainda faltam os dados reais.

## 2026-11-11 | Etapa B: aulas de Excel
**O que foi feito:** página `excel.html` com 9 aulas (4 do nível Básico e 5 do Intermediário). O card do Excel em Trilhas passou de "Em breve" para link.

**Decisões e por quê:**
- Todas as aulas seguem a mesma estrutura (objetivos, explicação, passo a passo, dica, exercício e se funciona no celular), para o aluno saber o que esperar.
- Os exemplos usam situações de renda extra: venda de doces, gastos da semana, meta de vendas, tabela de preços.
- Cada aula tem um endereço próprio (`excel.html#excel-soma`, por exemplo), para ser compartilhada por WhatsApp.
- Aulas com fórmulas avisam que o Excel em português usa ponto e vírgula, e as que são difíceis no celular (PROCV, tabela dinâmica) recomendam o computador.

## 2026-11-11 | Etapa C: planilha e Kit do Jovem Empreendedor
**O que foi feito:** planilha `downloads/controle-financeiro.xlsx` (abas Como usar, Entradas, Saídas e Resumo mensal, com saldo do mês e saldo acumulado), gerada pelo script `ferramentas/gerar_planilha.py`; página `kit-empreendedor.html` com o download, o passo a passo do post no Canva e a explicação de como calcular o preço.

**Decisões e por quê:**
- A planilha vem com linhas de exemplo marcadas "(exemplo)", para a pessoa ver o resumo funcionando antes de usar. A aba Como usar manda apagá-las.
- O Resumo mensal soma por data, e o ano é escolhido numa célula, assim a mesma planilha serve para qualquer ano.
- Python e a biblioteca openpyxl foram usados só para gerar o arquivo. O script fica no projeto para a planilha poder ser refeita, mas não faz parte do site.
- Precificação em 3 passos (custo, margem, preço final) com um exemplo concreto de brigadeiro (valores de exemplo, não de pesquisa). Foram incluídos os erros mais comuns, como esquecer o gás e o tempo de trabalho.
- Pendência: a planilha foi conferida pelo conteúdo das fórmulas, mas não foi calculada em um programa de planilhas. Falta testar abrindo no Excel ou no Google Planilhas.

## 2026-11-11 | Etapa D: aulas de Canva
**O que foi feito:** página `canva.html` com 7 aulas (4 do nível Básico e 3 do Intermediário); card do Canva em Trilhas virou link; o passo a passo do post no Kit passou a apontar para a aula completa.

**Decisões e por quê:**
- Canva vem antes de Word, PowerPoint e Power BI na ordem de construção porque é o mais usado pelo celular e ajuda direto na divulgação de quem vende.
- As aulas mostram as limitações do plano gratuito (modelos com coroa, fundo transparente do logo) para evitar frustração.
- Os nomes de botões do Canva mudam com o tempo. Por isso as aulas descrevem a ideia ("menu lateral", "Compartilhar") e avisam que os nomes podem variar. Convém conferir as aulas no Canva real antes da divulgação.

## 2026-11-11 | Etapa E: aulas de Word
**O que foi feito:** página `word.html` com 7 aulas (4 do nível Básico e 3 do Intermediário); card do Word em Trilhas virou link.

**Decisões e por quê:**
- As aulas intermediárias (currículo, orçamento, panfleto) resolvem problemas reais de quem busca renda extra ou emprego.
- A aula do currículo mostra como valorizar quem nunca teve carteira assinada (trabalhos informais, voluntariado, cursos feitos neste site), porque esse é o caso de muitos do público.
- Onde o Word no celular é pouco prático (orçamento e panfleto), a aula avisa e sugere o computador ou o Canva, em vez de prometer o que não funciona bem.

## 2026-11-11 | Etapa F: aulas de PowerPoint
**O que foi feito:** página `powerpoint.html` com 7 aulas (4 do nível Básico e 3 do Intermediário); card do PowerPoint em Trilhas virou link.

**Decisões e por quê:**
- A aula "Apresentação de um produto" ensina uma estrutura de 6 slides (capa, problema, solução, preços, como pedir, contato) que o aluno pode usar para vender.
- Animações entram só no nível Intermediário e com o aviso de usar pouco, para evitar apresentações confusas.
- A aula final ensina a exportar para PDF e imagem, porque o público costuma compartilhar tudo por WhatsApp.

## 2026-11-11 | Etapa G: aulas de Power BI
**O que foi feito:** página `powerbi.html` com 7 aulas (4 do nível Básico e 3 do Intermediário); card do Power BI em Trilhas virou link. Com isso, as 5 ferramentas e as 37 aulas estão no ar.

**Decisões e por quê:**
- O Power BI Desktop só roda em Windows e o aplicativo de celular só mostra painéis prontos. Isso foi dito com clareza no começo da página e em cada aula, para ninguém perder tempo tentando pelo celular.
- As aulas reaproveitam a lista de vendas do Excel (aula de tabela dinâmica), para o aluno ligar uma trilha à outra.
- Ficou como Intermediário um painel de vendas com cartão, dois gráficos e um filtro, que responde às três perguntas básicas de um pequeno negócio.

## 2026-11-11 | Etapa H: README e revisão final
**O que foi feito:** README.md (o que é, como abrir no computador, o que falta preencher, como refazer a planilha e como publicar) e revisão automática de todas as páginas com o Playwright, no celular (360 px) e no computador (1280 px), no modo normal e no de alto contraste.

**O que a revisão conferiu:** 37 aulas encontradas; um único título principal por página; títulos em ordem; idioma pt-BR; letra base de 18 px; nenhuma rolagem horizontal; contraste de texto adequado nos dois modos; link "Pular para o conteúdo"; menu abrindo e fechando pelo teclado (Enter e Esc); escolha de letra e de alto contraste lembrada ao recarregar; site ainda navegável com o JavaScript desligado; nenhum link ou âncora quebrado; nenhum erro no console; páginas entre 15 e 34 KB.

**O que foi corrigido:** os links do índice de aulas e os títulos dos cards de trilhas tinham 37 a 38 px de altura, abaixo dos 44 px da meta de toque. Foram aumentados. Também foram corrigidos dois saltos de nível de título (h1 para h4, e h2 para h4) em Power BI e Kit.

**Pendências para o Gustavo:** trocar `LINK_DO_GOOGLE_FORMS` em feedback.html; preencher os resultados do diagnóstico em sobre.html (`[PREENCHER]`); testar a planilha no Excel ou no Google Planilhas; conferir as aulas de Canva, Word, PowerPoint e Power BI nos programas reais, já que os nomes dos botões mudam com o tempo; testar o site em um celular de verdade.

## 2026-11-11 | Etapa I: novo visual (mais bonito e detalhado, ainda leve)
**O que foi feito:** o visual do site inteiro foi refeito, sem fotos, sem fontes e sem bibliotecas externas.
- **Identidade:** fundo pontilhado de caderno, marca-texto colorido nos títulos, adesivos inclinados, seções com fundos alternados e ondas entre elas, e um mascote (caderninho com carinha) em 3 versões: acenando (início, Sobre e Feedback), apontando (Trilhas e 404) e comemorando (Kit e rodapé).
- **Início:** capa com ilustração (jovem com notebook e celular, gráficos e ícones das ferramentas flutuando), faixa "Como funciona" em 3 passos ligados por linha pontilhada, vitrine das 5 trilhas, destaque do Kit com planilha e moedas, e "Para quem é" com 4 perfis (doces, unhas, conserto de celular, emprego), cada um levando a uma aula ou ao Kit.
- **Trilhas e aulas:** cards com ícone e cor de cada ferramenta, cabeçalho colorido em cada página de ferramenta, sumário em forma de trilha de bolinhas numeradas, botão "Marcar aula como concluída" com barra de progresso (salvo no navegador, com try/catch), passo a passo ligado por linha, caixas Dica, Pratique e Celular com ícones próprios e mini-telas ilustradas (Excel, PowerPoint, Word, Canva e Power BI).
- **Kit:** cards em destaque, botão grande de download com o tamanho do arquivo, exemplo visual de post e o esquema custo → margem → preço final.
- **Detalhes:** rodapé com ondas e mascote, página 404, elementos que aparecem suavemente ao rolar e mascote flutuando (tudo desligado com prefers-reduced-motion).

**Decisões e por quê:**
- A leveza continuou vencendo: tudo é SVG e CSS, os desenhos repetidos usam `<symbol>` e `<use>`, e a maior página (Excel) tem 70 KB somando HTML, CSS e JS (o limite era 150 KB).
- No alto contraste, as decorações, os mascotes, as ilustrações e as texturas são escondidos, e o site fica só com texto, bordas e amarelo sobre preto.
- O botão de progresso só existe com JavaScript. Sem ele, as aulas continuam completas.
- Os ícones das ferramentas foram desenhados por nós (inspirados em planilha, gráfico, página, slide e paleta), e não são os logos oficiais das marcas.
- O "404" foi feito como a página 404.html do GitHub Pages.

**Revisão automática (Playwright, 360 e 1280 px, normal e alto contraste):** 37 aulas; sem rolagem horizontal; títulos em ordem; contraste dentro do mínimo; decorações escondidas no alto contraste; progresso salvo ao recarregar e mostrado nos cards; menu por teclado; site funcionando sem JavaScript; links e âncoras sem erro; nenhuma página acima de 150 KB. Foram corrigidos: um código longo que estourava a largura no celular (Excel), um cartão do Kit que esticava a grade e setas sem aria-hidden.

## 2026-11-11 | Etapa J: nova planilha de controle financeiro
**O que foi feito:** a planilha `downloads/controle-financeiro.xlsx` foi refeita pelo script `ferramentas/gerar_planilha.py`, no mesmo visual do site (verde-petróleo, creme e laranja-tijolo). Passou a ter 7 abas, nesta ordem: Como usar, Painel, Entradas, Saídas, Resumo mensal, Metas e Categorias. A planilha abre já na aba Como usar. O tamanho indicado no Kit passou de 16 KB para 47 KB.
- **Painel:** escolha de ano e de mês (lista), quatro cartões (entradas, saídas, saldo e % da meta de economia), frase automática ("Você está no azul!" ou "Atenção: você gastou R$ X a mais"), gráfico de colunas de entradas x saídas por mês, gráfico de barras de gastos por categoria e quadro de negócio x pessoal.
- **Entradas e Saídas:** 500 linhas formatadas, listas suspensas de categoria e forma de pagamento, campo Tipo (Material do negócio ou Pessoal) nas saídas, validação de data e de valor, total no topo e três linhas de exemplo em cinza itálico.
- **Resumo mensal, Metas e Categorias:** saldo do mês e acumulado com cores condicionais (verde e vermelho com fundo rosado), meta de economia e metas de compra com barra de progresso feita com REPT, e listas de categorias que a própria pessoa pode ampliar.
- **Facilidades:** células amarelas só onde se digita, fórmulas com SEERRO (IFERROR) para nunca aparecer erro, notas explicativas nas células principais e impressão do Painel e do Resumo mensal em uma página paisagem.

**Decisões e por quê:**
- Só funções que existem no Excel (computador e celular), no Google Planilhas e no LibreOffice: SOMASES, SE, SEERRO, DATA, CORRESP, MÁXIMO, MÍNIMO, REPT, ARRUMAR (FIXED). Sem macros, sem tabelas dinâmicas e sem funções de versões novas.
- Nas listas de categoria, quem digitar um nome novo só recebe um aviso (não é bloqueado), para não travar iniciantes. Só o campo Tipo é estrito.
- O ano escolhido no Painel vale para o Resumo mensal inteiro, para existir um único lugar de mudar o ano.
- A planilha traz exemplos de março de 2026, e o Painel abre em "2026" e "Ano todo", então já mostra números de exemplo (entradas R$ 350,00, saídas R$ 115,00, saldo R$ 235,00).

**Verificação feita:** arquivo relido com o openpyxl (abas, validações, formatações condicionais, gráficos, impressão e comentários) e 138 fórmulas conferidas (parênteses, funções permitidas e nomes de abas). O LibreOffice não está instalado neste computador, então as fórmulas **não foram recalculadas**. Pendência: abrir a planilha no Excel e no Google Planilhas e testar (ver lista no resumo da etapa).
