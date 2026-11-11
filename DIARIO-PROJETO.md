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
