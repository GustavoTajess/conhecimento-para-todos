"""Gera downloads/controle-financeiro.xlsx (planilha do Kit do Jovem Empreendedor).

Uso (na raiz do projeto):  python ferramentas/gerar_planilha.py
Requer:  python -m pip install openpyxl

Só usa funções que existem no Excel (computador e celular), no Google Planilhas e no LibreOffice:
SOMASES (SUMIFS), SE (IF), SEERRO (IFERROR), DATA, CORRESP, MÍNIMO, MÁXIMO, ARRUMAR... Sem macros.
O openpyxl grava os nomes em inglês; cada programa mostra no idioma do usuário.
"""
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.chart.data_source import NumFmt
from openpyxl.chart.label import DataLabelList
from openpyxl.chart.series import SeriesLabel
from openpyxl.comments import Comment
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.properties import PageSetupProperties

SAIDA = Path(__file__).resolve().parent.parent / "downloads" / "controle-financeiro.xlsx"

# ---- Cores (as mesmas do site) ----
TEAL, CREME, LARANJA, VERDE, AMBAR = "0B5D5B", "FFF8EE", "B4441F", "1D6F42", "8A6100"
VERMELHO, ROSA, BRANCO, CINZA, TEXTO = "B00020", "FDE2E4", "FFFFFF", "7F7F7F", "1F2328"
AMARELO1, AMARELO2 = "FFFBE6", "FFF5CC"          # células onde a pessoa digita (zebrado bem claro)
MOEDA = '"R$" #,##0.00;[Red]-"R$" #,##0.00'
MOEDA_CARTAO = '"R$" #,##0.00;-"R$" #,##0.00'
DATA = "dd/mm/yyyy"
MESES = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
PRIM, ULT = 6, 505                                  # linhas de lançamentos (500 linhas)
LADO = Side(style="thin", color="E2D3B8")
BORDA = Border(left=LADO, right=LADO, top=LADO, bottom=LADO)
LARANJA_M = Side(style="medium", color=LARANJA)

# Listas iniciais (editáveis na aba Categorias)
CAT_ENTRADA = ["Vendas de doces", "Unhas", "Conserto de celular", "Outros serviços", "Outras entradas"]
CAT_SAIDA = ["Material / ingredientes", "Embalagem", "Transporte", "Alimentação", "Gás e energia",
             "Divulgação", "Equipamentos", "Moradia", "Estudos", "Lazer"]
FORMAS = ["Pix", "Dinheiro", "Cartão", "Transferência"]
TIPOS = ["Material do negócio", "Pessoal"]


# ---------- Ajudantes de estilo ----------
def preencher(cor):
    return PatternFill("solid", fgColor=cor)


def dif(cor):
    """Preenchimento para formatação condicional (o Excel lê a cor de fundo)."""
    return PatternFill(start_color=cor, end_color=cor, fill_type="solid")


def fonte(tam=11, negrito=False, itálico=False, cor=TEXTO):
    return Font(name="Calibri", size=tam, bold=negrito, italic=itálico, color=cor)


def mesclar(ws, ref, valor=None, bg=None, cor=TEXTO, tam=11, negrito=False, itálico=False,
            h="left", fmt=None, borda=None, quebrar=True):
    """Mescla um intervalo, pinta todas as células e formata a primeira."""
    ws.merge_cells(ref)
    primeira = ws[ref.split(":")[0]]
    if valor is not None:
        primeira.value = valor
    for linha in ws[ref]:
        for c in linha:
            if bg:
                c.fill = preencher(bg)
            if borda:
                c.border = borda
    primeira.font = fonte(tam, negrito, itálico, cor)
    primeira.alignment = Alignment(horizontal=h, vertical="center", wrap_text=quebrar)
    if fmt:
        primeira.number_format = fmt
    return primeira


def faixa_titulo(ws, ref, texto, altura=42, tam=20):
    """Título grande no topo, em uma faixa verde-petróleo mesclada."""
    mesclar(ws, ref, texto, bg=TEAL, cor=BRANCO, tam=tam, negrito=True, quebrar=False)
    ws.row_dimensions[ws[ref.split(":")[0]].row].height = altura


def cabecalho(ws, linha, titulos, col_ini=1):
    for i, t in enumerate(titulos):
        c = ws.cell(row=linha, column=col_ini + i, value=t)
        c.fill, c.font, c.border = preencher(TEAL), fonte(11, True, cor=BRANCO), BORDA
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[linha].height = 30


def larguras(ws, lista):
    for i, l in enumerate(lista, start=1):
        ws.column_dimensions[get_column_letter(i)].width = l


def nota(celula, texto, altura=110):
    c = Comment(texto, "Conhecimento para Todos")
    c.width, c.height = 280, altura
    celula.comment = c


def imprimir_paisagem(ws, area):
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 1
    ws.print_area = area
    ws.print_options.horizontalCentered = True
    ws.page_margins.left = ws.page_margins.right = 0.4
    ws.page_margins.top = ws.page_margins.bottom = 0.5


def lista(formula, titulo, msg, aviso=True):
    """Lista suspensa. Com aviso=True a pessoa pode usar um valor novo (só recebe um aviso)."""
    dv = DataValidation(type="list", formula1=formula.lstrip("="), allow_blank=True, showErrorMessage=True,
                        errorTitle=titulo, error=msg, errorStyle="warning" if aviso else "stop")
    return dv


wb = Workbook()
uso = wb.active
uso.title = "Como usar"
painel = wb.create_sheet("Painel")
entradas = wb.create_sheet("Entradas")
saidas = wb.create_sheet("Saídas")
resumo = wb.create_sheet("Resumo mensal")
metas = wb.create_sheet("Metas")
cats = wb.create_sheet("Categorias")
for ws, cor in [(uso, TEAL), (painel, LARANJA), (entradas, VERDE), (saidas, LARANJA),
                (resumo, TEAL), (metas, AMBAR), (cats, "6A3FB5")]:
    ws.sheet_properties.tabColor = cor

ENT = f"Entradas!$E${PRIM}:$E${ULT}"
ENT_D = f"Entradas!$A${PRIM}:$A${ULT}"
SAI = f"'Saídas'!$F${PRIM}:$F${ULT}"
SAI_D = f"'Saídas'!$A${PRIM}:$A${ULT}"
SAI_C = f"'Saídas'!$C${PRIM}:$C${ULT}"
SAI_T = f"'Saídas'!$D${PRIM}:$D${ULT}"

# =====================================================================
# 7. CATEGORIAS (listas usadas nas setinhas)
# =====================================================================
ws = cats
larguras(ws, [30, 30, 22, 24, 16, 14])
faixa_titulo(ws, "A1:F1", "Categorias: as listas das setinhas")
mesclar(ws, "A2:F2", "Estas listas aparecem nas setinhas (listas suspensas) das abas Entradas e Saídas. "
        "Para criar uma opção nova, escreva na primeira célula amarela vazia da coluna. "
        "Para trocar um nome, digite por cima. Não deixe espaços em branco no meio da lista.",
        bg=CREME, tam=11, itálico=True)
ws.row_dimensions[2].height = 52
cabecalho(ws, 4, ["Categorias de entrada", "Categorias de saída", "Formas de pagamento", "Tipo de gasto",
                  "Meses (Painel)", "Anos (Painel)"])
for i in range(30):                                  # A e B: 30 lugares
    for col, itens in ((1, CAT_ENTRADA), (2, CAT_SAIDA)):
        c = ws.cell(row=5 + i, column=col, value=itens[i] if i < len(itens) else None)
        c.fill, c.border, c.font = preencher(AMARELO1 if i % 2 == 0 else AMARELO2), BORDA, fonte()
for i in range(10):                                  # C e D: 10 lugares
    for col, itens in ((3, FORMAS), (4, TIPOS)):
        c = ws.cell(row=5 + i, column=col, value=itens[i] if i < len(itens) else None)
        c.fill, c.border, c.font = preencher(AMARELO1 if i % 2 == 0 else AMARELO2), BORDA, fonte()
for i, m in enumerate(["Ano todo"] + MESES):         # E: não é para editar
    c = ws.cell(row=5 + i, column=5, value=m)
    c.fill, c.border, c.font = preencher(CREME if i % 2 == 0 else BRANCO), BORDA, fonte(cor=CINZA)
for i in range(10):                                  # F: anos 2025 a 2034
    c = ws.cell(row=5 + i, column=6, value=2025 + i)
    c.fill, c.border, c.font = preencher(CREME if i % 2 == 0 else BRANCO), BORDA, fonte(cor=CINZA)
ws.freeze_panes = "A5"
nota(ws["A5"], "Escreva aqui as categorias de dinheiro que ENTRA no seu negócio. Elas aparecem na setinha da "
     "aba Entradas. Use a primeira célula amarela vazia para criar uma nova.")
nota(ws["B5"], "Escreva aqui as categorias de GASTO. Elas aparecem na setinha da aba Saídas e no gráfico do Painel.")
nota(ws["D5"], "Serve para separar o dinheiro do negócio do dinheiro pessoal. Mantenha estas duas opções.", 70)

# =====================================================================
# 3 e 4. ENTRADAS e SAÍDAS
# =====================================================================
def aba_lancamentos(ws, titulo, colunas, larg, col_valor, exemplos, cor_total, dicas):
    n = len(colunas)
    ultima = get_column_letter(n)
    vcol = get_column_letter(col_valor)
    larguras(ws, larg)
    faixa_titulo(ws, f"A1:{ultima}1", titulo, 40)
    mesclar(ws, f"A2:{ultima}2", "Escreva só nas células de fundo amarelo. Sempre preencha a data: sem ela, o valor "
            "não entra no Painel nem no Resumo mensal. Apague as linhas de exemplo (letra cinza) antes de começar.",
            bg=CREME, tam=10, itálico=True)
    ws.row_dimensions[2].height = 34
    cabecalho(ws, 5, colunas)
    for r in range(PRIM, ULT + 1):
        cor = AMARELO1 if (r - PRIM) % 2 == 0 else AMARELO2
        for c in range(1, n + 1):
            cel = ws.cell(row=r, column=c)
            cel.fill, cel.border, cel.font = preencher(cor), BORDA, fonte()
        ws.cell(row=r, column=1).number_format = DATA
        ws.cell(row=r, column=1).alignment = Alignment(horizontal="center")
        ws.cell(row=r, column=col_valor).number_format = MOEDA
    for i, linha in enumerate(exemplos):             # exemplos em cinza itálico
        for c, v in enumerate(linha, start=1):
            cel = ws.cell(row=PRIM + i, column=c, value=v)
            cel.font = fonte(11, False, True, CINZA)
    # total no topo
    mesclar(ws, f"A3:{get_column_letter(col_valor - 1)}3", dicas, bg=BRANCO, tam=10, itálico=True, cor=CINZA)
    t = ws.cell(row=3, column=col_valor, value=f"=SUM({vcol}{PRIM}:{vcol}{ULT})")
    t.number_format, t.font, t.fill = MOEDA_CARTAO, fonte(14, True, cor=BRANCO), preencher(cor_total)
    t.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[3].height = 30
    ws.freeze_panes = f"A{PRIM}"
    # validações
    dv_data = DataValidation(type="date", operator="greaterThanOrEqual", formula1="36526", allow_blank=True,
                             showErrorMessage=True, errorTitle="Data inválida",
                             error="Digite a data assim: 05/03/2026 (dia/mês/ano).")
    dv_valor = DataValidation(type="decimal", operator="greaterThanOrEqual", formula1="0", allow_blank=True,
                              showErrorMessage=True, errorTitle="Valor inválido",
                              error="Digite só números, sem R$ e sem letras. Exemplo: 25,50")
    dv_data.add(f"A{PRIM}:A{ULT}")
    dv_valor.add(f"{vcol}{PRIM}:{vcol}{ULT}")
    ws.add_data_validation(dv_data)
    ws.add_data_validation(dv_valor)
    nota(ws[f"A{PRIM}"], "DATA: digite assim: 05/03/2026. Sem data, o valor não aparece no Painel.", 70)
    nota(ws[f"{vcol}{PRIM}"], "VALOR: digite só o número, por exemplo 25,50. O R$ aparece sozinho.", 70)
    nota(ws["B5"], "Escreva o que foi: quem comprou, o que vendeu ou o que pagou.", 60)


aba_lancamentos(
    entradas, "Entradas: dinheiro que entrou",
    ["Data", "Descrição", "Categoria", "Forma de recebimento", "Valor"], [14, 40, 26, 24, 18], 5,
    [(date(2026, 3, 2), "Venda de brigadeiros (exemplo)", "Vendas de doces", "Pix", 150),
     (date(2026, 3, 9), "Manicure de uma cliente (exemplo)", "Unhas", "Dinheiro", 80),
     (date(2026, 3, 15), "Troca de tela de celular (exemplo)", "Conserto de celular", "Pix", 120)],
    VERDE, "Total de entradas (tudo o que está na lista):")
aba_lancamentos(
    saidas, "Saídas: dinheiro que saiu",
    ["Data", "Descrição", "Categoria", "Tipo", "Forma de pagamento", "Valor"], [14, 36, 26, 24, 22, 18], 6,
    [(date(2026, 3, 1), "Chocolate e leite condensado (exemplo)", "Material / ingredientes", "Material do negócio", "Cartão", 60),
     (date(2026, 3, 5), "Embalagens (exemplo)", "Embalagem", "Material do negócio", "Dinheiro", 25),
     (date(2026, 3, 10), "Lanche e passagem (exemplo)", "Alimentação", "Pessoal", "Dinheiro", 30)],
    LARANJA, "Total de saídas (tudo o que está na lista):")
# Pessoas podem digitar uma categoria nova (só aparece um aviso)
av = "Essa opção não está na lista. Clique em Sim para usar mesmo assim, ou adicione na aba Categorias."
dv = lista("=Categorias!$A$5:$A$34", "Categoria nova", av)
dv.add(f"C{PRIM}:C{ULT}")
entradas.add_data_validation(dv)
dv = lista("=Categorias!$C$5:$C$14", "Forma nova", av)
dv.add(f"D{PRIM}:D{ULT}")
entradas.add_data_validation(dv)
dv = lista("=Categorias!$B$5:$B$34", "Categoria nova", av)
dv.add(f"C{PRIM}:C{ULT}")
saidas.add_data_validation(dv)
dv = lista("=Categorias!$D$5:$D$14", "Tipo de gasto", "Escolha Material do negócio ou Pessoal.", aviso=False)
dv.add(f"D{PRIM}:D{ULT}")
saidas.add_data_validation(dv)
dv = lista("=Categorias!$C$5:$C$14", "Forma nova", av)
dv.add(f"E{PRIM}:E{ULT}")
saidas.add_data_validation(dv)
nota(entradas[f"C{PRIM - 1}"], "Clique na setinha da célula para escolher. Para criar uma categoria nova, use a aba Categorias.", 70)
nota(saidas[f"D{PRIM - 1}"], "Material do negócio = o que você gastou para trabalhar (ingredientes, embalagem). "
     "Pessoal = gastos da sua vida. Assim você vê quanto sobrou de verdade no negócio.", 110)
# Resumo do tipo de gasto no topo das Saídas (negócio x pessoal)
saidas["A3"].value = (f'=IFERROR("Material do negócio: R$ "&FIXED(SUMIFS(F{PRIM}:F{ULT},D{PRIM}:D{ULT},Categorias!$D$5),2)'
                      f'&"   |   Pessoal: R$ "&FIXED(SUMIFS(F{PRIM}:F{ULT},D{PRIM}:D{ULT},Categorias!$D$6),2)&"   |   Total de saídas:","")')
for planilha in (entradas, saidas):
    planilha["A3"].alignment = Alignment(horizontal="right", vertical="center", wrap_text=True)

# =====================================================================
# 5. RESUMO MENSAL
# =====================================================================
ws = resumo
larguras(ws, [16, 20, 20, 20, 22, 18])
faixa_titulo(ws, "A1:F1", "Resumo mensal", 40)
ws["A2"].value, ws["A2"].font = "Ano:", fonte(12, True, cor=TEAL)
ws["A2"].alignment = Alignment(horizontal="right", vertical="center")
ws["B2"].value, ws["B2"].font = "=Painel!$D$5", fonte(14, True, cor=LARANJA)
ws["B2"].alignment = Alignment(horizontal="center", vertical="center")
mesclar(ws, "C2:F2", "(Para mudar o ano, escolha na aba Painel.)", tam=10, itálico=True, cor=CINZA)
ws.row_dimensions[2].height = 26
cabecalho(ws, 4, ["Mês", "Entradas", "Saídas", "Saldo do mês", "Saldo acumulado", "Situação"])


def soma_mes(intervalo, datas, mes):
    return (f'=IFERROR(SUMIFS({intervalo},{datas},">="&DATE($B$2,{mes},1),'
            f'{datas},"<"&DATE($B$2,{mes + 1},1)),0)')


for m in range(1, 13):
    r = m + 4
    bg = CREME if m % 2 else BRANCO
    ws.cell(row=r, column=1, value=MESES[m - 1])
    ws.cell(row=r, column=2, value=soma_mes(ENT, ENT_D, m))
    ws.cell(row=r, column=3, value=soma_mes(SAI, SAI_D, m))
    ws.cell(row=r, column=4, value=f"=B{r}-C{r}")
    ws.cell(row=r, column=5, value=f"=D{r}" if m == 1 else f"=E{r - 1}+D{r}")
    ws.cell(row=r, column=6, value=f'=IF(AND(B{r}=0,C{r}=0),"-",IF(D{r}>=0,"No azul","No vermelho"))')
    for c in range(1, 7):
        cel = ws.cell(row=r, column=c)
        cel.fill, cel.border, cel.font = preencher(bg), BORDA, fonte(11, c == 1)
        cel.alignment = Alignment(horizontal="center" if c in (1, 6) else "right", vertical="center")
        if 2 <= c <= 5:
            cel.number_format = MOEDA
    ws.row_dimensions[r].height = 22
ws["A17"].value = "Total do ano"
ws["B17"].value, ws["C17"].value = "=SUM(B5:B16)", "=SUM(C5:C16)"
ws["D17"].value, ws["E17"].value = "=B17-C17", "=E16"
ws["F17"].value = '=IF(AND(B17=0,C17=0),"-",IF(D17>=0,"No azul","No vermelho"))'
for c in range(1, 7):
    cel = ws.cell(row=17, column=c)
    cel.fill, cel.font = preencher("FFE3CC"), fonte(12, True, cor=TEAL)
    cel.border = Border(top=LARANJA_M, bottom=LARANJA_M, left=LADO, right=LADO)
    cel.alignment = Alignment(horizontal="center" if c in (1, 6) else "right", vertical="center")
    if 2 <= c <= 5:
        cel.number_format = MOEDA
ws.row_dimensions[17].height = 28
# formatação condicional: saldo positivo = verde; negativo = vermelho com fundo rosado
verde_f, verm_f = Font(color=VERDE, bold=True), Font(color=VERMELHO, bold=True)
for rng, ref in (("D5:D17", "$D5"), ("E5:E17", "$E5"), ("F5:F17", "$D5")):
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f"{ref}<0"], font=verm_f, fill=dif(ROSA)))
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f"AND({ref}>0,OR($B5<>0,$C5<>0))"], font=verde_f))
ws.freeze_panes = "A5"
nota(ws["D4"], "Saldo do mês = Entradas menos Saídas. Verde = sobrou dinheiro. Vermelho = gastou mais do que ganhou.", 70)
nota(ws["E4"], "Saldo acumulado = quanto você tem somando todos os meses até este.", 60)
imprimir_paisagem(ws, "A1:F17")

# =====================================================================
# 6. METAS
# =====================================================================
ws = metas
ws.sheet_view.showGridLines = False
larguras(ws, [2, 36, 18, 16, 16, 14, 16, 16])
faixa_titulo(ws, "B1:H1", "Metas: seus objetivos de dinheiro", 42)
mesclar(ws, "B2:H2", "Escreva só nas células de fundo amarelo. O resto se calcula sozinho.",
        bg=CREME, tam=11, itálico=True)


def secao(ws, ref, texto):
    mesclar(ws, ref, texto, bg=CREME, cor=TEAL, tam=14, negrito=True,
            borda=Border(bottom=LARANJA_M))
    ws.row_dimensions[ws[ref.split(":")[0]].row].height = 28


def rotulo(ws, cel, texto):
    ws[cel].value, ws[cel].font = texto, fonte(11, True)
    ws[cel].alignment = Alignment(vertical="center", wrap_text=True)


def entrada(cel, valor=None, fmt=None, h="right"):
    c = cel
    c.value = valor
    c.fill, c.border, c.font = preencher(AMARELO1), BORDA, fonte(12, True)
    c.alignment = Alignment(horizontal=h, vertical="center")
    if fmt:
        c.number_format = fmt


def calculada(cel, formula, fmt=None, h="right", tam=12, negrito=True, cor=TEXTO):
    cel.value = formula
    cel.border, cel.font = BORDA, fonte(tam, negrito, cor=cor)
    cel.alignment = Alignment(horizontal=h, vertical="center", wrap_text=True)
    if fmt:
        cel.number_format = fmt


secao(ws, "B4:H4", "1. Meta de economia por mês")
rotulo(ws, "B5", "Quanto quero guardar por mês")
entrada(ws["C5"], 200, MOEDA_CARTAO)
mesclar(ws, "D5:H5", "Guardar = o que sobra depois de pagar tudo (o saldo).", tam=10, itálico=True, cor=CINZA)
rotulo(ws, "B6", "Meta no período do Painel")
calculada(ws["C6"], "=IFERROR(C5*IF(Painel!$L$5=0,12,1),0)", MOEDA_CARTAO)
mesclar(ws, "D6:H6", "(Se o Painel está em 'Ano todo', vale 12 meses.)", tam=10, itálico=True, cor=CINZA)
rotulo(ws, "B7", "Quanto sobrou nesse período (saldo)")
calculada(ws["C7"], "=IFERROR(Painel!$H$9,0)", MOEDA_CARTAO)
rotulo(ws, "B8", "Quanto da meta já foi atingido")
calculada(ws["C8"], "=IFERROR(MAX(0,C7)/C6,0)", "0%")
BARRA = '=IFERROR(REPT("█",ROUND(MIN(1,{p})*{n},0))&REPT("░",{n}-ROUND(MIN(1,{p})*{n},0)),"")'
mesclar(ws, "D8:H8", BARRA.format(p="C8", n=24), cor=VERDE, tam=13, negrito=True, h="left", quebrar=False)
rotulo(ws, "B9", "Situação")
mesclar(ws, "C9:H9", '=IFERROR(IF(C6=0,"Escreva sua meta na célula amarela.",IF(MAX(0,C7)>=C6,"Meta batida! Parabéns!",'
        '"Falta guardar R$ "&FIXED(C6-MAX(0,C7),2)&" para bater a meta.")),"")', tam=12, negrito=True, cor=LARANJA)
for r in range(5, 10):
    ws.row_dimensions[r].height = 26

secao(ws, "B11:H11", "2. Metas de compra")
cabecalho(ws, 12, ["O que quero comprar", "Valor da meta", "Já guardado", "Falta", "% atingida", "Progresso", ""], 2)
ws.merge_cells("G12:H12")
for r, (item, meta, guardado) in enumerate([("Comprar uma batedeira (exemplo)", 300, 120), (None, None, None),
                                            (None, None, None)], start=13):
    entrada(ws[f"B{r}"], item, h="left")
    entrada(ws[f"C{r}"], meta, MOEDA_CARTAO)
    entrada(ws[f"D{r}"], guardado, MOEDA_CARTAO)
    if item:
        for col in "BCD":
            ws[f"{col}{r}"].font = fonte(12, False, True, CINZA)
    calculada(ws[f"E{r}"], f'=IFERROR(IF(C{r}="","",MAX(0,C{r}-D{r})),"")', MOEDA_CARTAO)
    calculada(ws[f"F{r}"], f'=IFERROR(IF(C{r}="","",MIN(1,D{r}/C{r})),"")', "0%", h="center")
    mesclar(ws, f"G{r}:H{r}", f'=IFERROR(IF(C{r}="","",REPT("█",ROUND(F{r}*12,0))&REPT("░",12-ROUND(F{r}*12,0))),"")',
            cor=VERDE, tam=13, negrito=True, h="left", quebrar=False)
    ws.row_dimensions[r].height = 28
mesclar(ws, "B17:H17", "Dica: escolha uma coisa de cada vez e guarde um pouco a cada mês. Quando bater a meta, comemore!",
        bg=CREME, tam=11, itálico=True)
ws.row_dimensions[17].height = 30
nota(ws["C5"], "Escreva quanto você quer guardar por mês, só o número. Exemplo: 200. O Painel mostra quanto dessa meta você atingiu.", 90)
nota(ws["C13"], "VALOR DA META: quanto custa o que você quer comprar.", 60)
nota(ws["D13"], "JÁ GUARDADO: quanto você já separou para essa compra. Atualize sempre que guardar mais.", 70)
imprimir_paisagem(ws, "A1:H17")

# =====================================================================
# 2. PAINEL
# =====================================================================
ws = painel
ws.sheet_view.showGridLines = False
larguras(ws, [2] + [12] * 12 + [2])
ws.row_dimensions[1].height = 8
faixa_titulo(ws, "B2:M2", "Painel: como está o seu dinheiro", 46, 22)
mesclar(ws, "B3:M3", "Escolha o ano e o mês nas células amarelas. Tudo abaixo se atualiza sozinho.",
        bg=CREME, tam=11, itálico=True)
ws.row_dimensions[3].height = 24
mesclar(ws, "B5:C5", "Ano:", tam=13, negrito=True, cor=TEAL, h="right")
entrada(ws["D5"], 2026, "0", "center")
ws.merge_cells("D5:E5")
for c in ws["D5:E5"][0]:
    c.fill, c.border = preencher(AMARELO1), BORDA
ws["D5"].font = fonte(14, True, cor=LARANJA)
mesclar(ws, "G5:H5", "Mês:", tam=13, negrito=True, cor=TEAL, h="right")
entrada(ws["I5"], "Ano todo", None, "center")
ws.merge_cells("I5:J5")
for c in ws["I5:J5"][0]:
    c.fill, c.border = preencher(AMARELO1), BORDA
ws["I5"].font = fonte(14, True, cor=LARANJA)
ws["K5"].value, ws["K5"].font = "nº do mês", fonte(9, False, True, CINZA)
ws["K5"].alignment = Alignment(horizontal="right", vertical="center")
ws["L5"].value = '=IFERROR(MATCH($I$5,Categorias!$E$6:$E$17,0),0)'
ws["L5"].font, ws["L5"].alignment = fonte(9, False, True, CINZA), Alignment(horizontal="center", vertical="center")
ws.row_dimensions[5].height = 30
mesclar(ws, "B6:D6", "Período analisado:", tam=11, itálico=True, cor=CINZA, h="right")
mesclar(ws, "E6:F6", '=IFERROR(IF($L$5=0,DATE($D$5,1,1),DATE($D$5,$L$5,1)),"")', tam=11, negrito=True, h="center", fmt=DATA)
ws["G6"].value, ws["G6"].font = "até", fonte(11, False, True, CINZA)
ws["G6"].alignment = Alignment(horizontal="center", vertical="center")
mesclar(ws, "H6:I6", '=IFERROR(IF($L$5=0,DATE($D$5,12,31),DATE($D$5,$L$5+1,1)-1),"")', tam=11, negrito=True, h="center", fmt=DATA)
dv = DataValidation(type="list", formula1="Categorias!$F$5:$F$14", allow_blank=False, showErrorMessage=True,
                    errorTitle="Ano inválido", error="Escolha um ano na lista (clique na setinha).")
dv.add("D5")
ws.add_data_validation(dv)
dv = DataValidation(type="list", formula1="Categorias!$E$5:$E$17", allow_blank=False, showErrorMessage=True,
                    errorTitle="Mês inválido", error="Escolha Ano todo ou um mês da lista (clique na setinha).")
dv.add("I5")
ws.add_data_validation(dv)
nota(ws["D5"], "ANO: clique na setinha e escolha o ano que você quer ver.", 60)
nota(ws["I5"], "MÊS: escolha um mês (Jan a Dez) ou 'Ano todo'. Os cartões e os gráficos mudam sozinhos.", 70)

# cartões grandes
ENT_P = f'=IFERROR(SUMIFS({ENT},{ENT_D},">="&$E$6,{ENT_D},"<="&$H$6),0)'
SAI_P = f'=IFERROR(SUMIFS({SAI},{SAI_D},">="&$E$6,{SAI_D},"<="&$H$6),0)'
cartoes = [("B", "D", "Total de entradas", ENT_P, VERDE, MOEDA_CARTAO),
           ("E", "G", "Total de saídas", SAI_P, LARANJA, MOEDA_CARTAO),
           ("H", "J", "Saldo (entradas - saídas)", "=B9-E9", TEAL, MOEDA_CARTAO),
           ("K", "M", "Meta de economia atingida", "=IFERROR(MAX(0,H9)/(Metas!$C$5*IF($L$5=0,12,1)),0)", AMBAR, "0%")]
for c1, c2, rot, formula, cor, fmt in cartoes:
    mesclar(ws, f"{c1}8:{c2}8", rot, bg=cor, cor=BRANCO, tam=12, negrito=True, h="center")
    mesclar(ws, f"{c1}9:{c2}11", formula, bg=cor, cor=BRANCO, tam=24, negrito=True, h="center", fmt=fmt, quebrar=False)
ws.row_dimensions[8].height = 24
for r in (9, 10, 11):
    ws.row_dimensions[r].height = 22
ws.conditional_formatting.add("H8:J11", FormulaRule(formula=["$H$9<0"], fill=dif("C0392B"), font=Font(color=BRANCO, bold=True)))
nota(ws["B9"], "Tudo o que entrou no período escolhido. Os números vêm da aba Entradas.", 60)
nota(ws["K9"], "Quanto da sua meta de economia você já bateu. A meta se escreve na aba Metas.", 70)
mesclar(ws, "B13:M13", '=IFERROR(IF(AND(B9=0,E9=0),"Anote suas entradas e saídas para ver o resumo aqui.",'
        'IF(H9>0,"Você está no azul! Sobrou R$ "&FIXED(H9,2)&".",'
        'IF(H9=0,"Você fechou no zero: ganhou e gastou o mesmo valor.",'
        '"Atenção: você gastou R$ "&FIXED(-H9,2)&" a mais do que ganhou."))),"")',
        bg=CREME, cor=TEAL, tam=15, negrito=True, h="center",
        borda=Border(left=LARANJA_M, right=LARANJA_M, top=LARANJA_M, bottom=LARANJA_M))
ws.row_dimensions[13].height = 38

# tabelas de apoio (alimentam os gráficos)
mesclar(ws, "B33:G33", "Gastos por categoria (números do gráfico)", bg=CREME, cor=TEAL, tam=13, negrito=True,
        borda=Border(bottom=LARANJA_M))
mesclar(ws, "I33:M33", "Negócio x pessoal", bg=CREME, cor=TEAL, tam=13, negrito=True, borda=Border(bottom=LARANJA_M))
for ref, t in (("B34:D34", "Categoria"), ("E34:F34", "Valor"), ("G34:G34", "%"), ("I34:K34", "Tipo de gasto"), ("L34:M34", "Valor")):
    if ref.split(":")[0] != ref.split(":")[1]:
        mesclar(ws, ref, t, bg=TEAL, cor=BRANCO, negrito=True, h="center", borda=BORDA)
    else:
        c = ws[ref.split(":")[0]]
        c.value, c.fill, c.font, c.border = t, preencher(TEAL), fonte(11, True, cor=BRANCO), BORDA
        c.alignment = Alignment(horizontal="center", vertical="center")
for i in range(12):                                  # 12 categorias da aba Categorias
    r = 35 + i
    bg = CREME if i % 2 == 0 else BRANCO
    mesclar(ws, f"B{r}:D{r}", f'=IF(Categorias!$B${5 + i}="","",Categorias!$B${5 + i})', bg=bg, borda=BORDA, quebrar=False)
    mesclar(ws, f"E{r}:F{r}", f'=IFERROR(IF(B{r}="",0,SUMIFS({SAI},{SAI_C},B{r},{SAI_D},">="&$E$6,{SAI_D},"<="&$H$6)),0)',
            bg=bg, borda=BORDA, h="right", fmt=MOEDA_CARTAO)
    c = ws[f"G{r}"]
    c.value, c.fill, c.border, c.font = f"=IFERROR(E{r}/$E$9,0)", preencher(bg), BORDA, fonte()
    c.number_format, c.alignment = "0%", Alignment(horizontal="center")
mesclar(ws, "B47:D47", "Outras categorias", bg=CREME, borda=BORDA, itálico=True)
mesclar(ws, "E47:F47", "=IFERROR(MAX(0,$E$9-SUM(E35:E46)),0)", bg=CREME, borda=BORDA, h="right", fmt=MOEDA_CARTAO)
ws["G47"].value, ws["G47"].number_format = "=IFERROR(E47/$E$9,0)", "0%"
ws["G47"].fill, ws["G47"].border, ws["G47"].alignment = preencher(CREME), BORDA, Alignment(horizontal="center")
mesclar(ws, "B48:D48", "Total", bg="FFE3CC", negrito=True, borda=BORDA)
mesclar(ws, "E48:F48", "=SUM(E35:E47)", bg="FFE3CC", negrito=True, borda=BORDA, h="right", fmt=MOEDA_CARTAO)
for r, (nome, crit) in enumerate([("=Categorias!$D$5", "Categorias!$D$5"), ("=Categorias!$D$6", "Categorias!$D$6")], start=35):
    mesclar(ws, f"I{r}:K{r}", nome, bg=CREME if r == 35 else BRANCO, borda=BORDA, quebrar=False)
    mesclar(ws, f"L{r}:M{r}", f'=IFERROR(SUMIFS({SAI},{SAI_T},{crit},{SAI_D},">="&$E$6,{SAI_D},"<="&$H$6),0)',
            bg=CREME if r == 35 else BRANCO, borda=BORDA, h="right", fmt=MOEDA_CARTAO)
mesclar(ws, "I37:K37", "Sem tipo", bg=CREME, borda=BORDA, itálico=True)
mesclar(ws, "L37:M37", "=IFERROR(MAX(0,$E$9-L35-L36),0)", bg=CREME, borda=BORDA, h="right", fmt=MOEDA_CARTAO)
mesclar(ws, "I38:K38", "Total", bg="FFE3CC", negrito=True, borda=BORDA)
mesclar(ws, "L38:M38", "=SUM(L35:L37)", bg="FFE3CC", negrito=True, borda=BORDA, h="right", fmt=MOEDA_CARTAO)
mesclar(ws, "I40:M41", "Dica: o dinheiro do negócio e o pessoal não se misturam. Anote o tipo de cada gasto na aba Saídas.",
        tam=10, itálico=True, cor=CINZA)

# gráficos
c1 = BarChart()
c1.type, c1.grouping, c1.gapWidth = "col", "clustered", 70
c1.title = "Entradas x Saídas por mês"
c1.add_data(Reference(resumo, min_col=2, max_col=3, min_row=4, max_row=16), titles_from_data=True)
c1.set_categories(Reference(resumo, min_col=1, min_row=5, max_row=16))
c1.series[0].graphicalProperties.solidFill = VERDE
c1.series[1].graphicalProperties.solidFill = LARANJA
c1.y_axis.numFmt = NumFmt(formatCode='"R$" #,##0', sourceLinked=False)
c1.x_axis.delete = c1.y_axis.delete = False
c1.legend.position = "b"
c1.width, c1.height = 14.2, 8.2
ws.add_chart(c1, "B15")
c2 = BarChart()
c2.type, c2.gapWidth = "bar", 50
c2.title = "Gastos por categoria"
c2.add_data(Reference(ws, min_col=5, min_row=35, max_row=47), titles_from_data=False)
c2.set_categories(Reference(ws, min_col=2, min_row=35, max_row=47))
c2.series[0].tx = SeriesLabel(v="Gasto")
c2.series[0].graphicalProperties.solidFill = LARANJA
c2.x_axis.scaling.orientation = "maxMin"             # primeira categoria em cima
c2.y_axis.crosses = "max"
c2.y_axis.numFmt = NumFmt(formatCode='"R$" #,##0', sourceLinked=False)
c2.x_axis.delete = c2.y_axis.delete = False
c2.legend = None
c2.dataLabels = DataLabelList()
c2.dataLabels.showVal = True
c2.dataLabels.showSerName = c2.dataLabels.showCatName = c2.dataLabels.showLegendKey = c2.dataLabels.showPercent = False
c2.width, c2.height = 14.2, 8.2
ws.add_chart(c2, "H15")
imprimir_paisagem(ws, "A1:N48")

# =====================================================================
# 1. COMO USAR
# =====================================================================
ws = uso
ws.sheet_view.showGridLines = False
larguras(ws, [2, 9, 16, 16, 16, 16, 16, 16])
ws.row_dimensions[1].height = 6
faixa_titulo(ws, "B2:H2", "Controle financeiro do jovem empreendedor", 48, 22)
mesclar(ws, "B3:H3", "Planilha grátis do projeto Conhecimento para Todos, feita para quem está começando.",
        bg=CREME, tam=11, itálico=True, h="center")
ws.row_dimensions[3].height = 26


def secao_uso(linha, texto):
    mesclar(ws, f"B{linha}:H{linha}", texto, bg=CREME, cor=TEAL, tam=16, negrito=True, borda=Border(bottom=LARANJA_M))
    ws.row_dimensions[linha].height = 30


secao_uso(5, "Passo a passo")
passos = [("1", "Confira a aba Categorias e adapte as listas ao seu negócio (doces, unhas, conserto de celular...).", TEAL),
          ("2", "Anote cada venda na aba Entradas: data, descrição, categoria, forma de recebimento e valor.", VERDE),
          ("3", "Anote cada gasto na aba Saídas. Marque se é Material do negócio ou Pessoal.", LARANJA),
          ("4", "Abra a aba Painel, escolha o ano e o mês, e veja como está o seu dinheiro.", AMBAR)]
for i, (n, texto, cor) in enumerate(passos):
    r = 6 + i
    c = ws[f"B{r}"]
    c.value, c.fill, c.font = n, preencher(cor), fonte(24, True, cor=BRANCO)
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.border = Border(top=Side(style="medium", color=BRANCO), bottom=Side(style="medium", color=BRANCO))
    mesclar(ws, f"C{r}:H{r}", texto, bg=CREME if i % 2 == 0 else BRANCO, tam=12, borda=BORDA)
    ws.row_dimensions[r].height = 42

secao_uso(11, "Dicas")
dicas = ["Escreva só nas células de fundo amarelo. As células sem cor fazem as contas sozinhas: não precisa mexer.",
         "Sempre preencha a data. Sem data, o valor não aparece no Painel nem no Resumo mensal.",
         "Digite os valores só com números, por exemplo 25,50. O R$ aparece sozinho.",
         "Nas listas (categoria, forma de pagamento), clique na setinha para escolher. Para criar uma opção nova, use a aba Categorias.",
         "As linhas com letra cinza e a palavra (exemplo) são só para você ver como funciona. Apague antes de começar.",
         "Salve de vez em quando com Ctrl + S. No celular, o aplicativo salva sozinho."]
for i, texto in enumerate(dicas):
    r = 12 + i
    mesclar(ws, f"B{r}:H{r}", "• " + texto, bg=CREME, tam=11)
    ws.row_dimensions[r].height = 32
ult = 12 + len(dicas) - 1
for r in range(12, ult + 1):                         # caixa com borda laranja
    for col in "BCDEFGH":
        ws[f"{col}{r}"].border = Border(left=Side(style="thick", color=LARANJA) if col == "B" else None,
                                        right=LARANJA_M if col == "H" else None,
                                        top=LARANJA_M if r == 12 else None,
                                        bottom=LARANJA_M if r == ult else None)

linha = ult + 2
secao_uso(linha, "O que significa cada aba")
mesclar(ws, f"B{linha + 1}:C{linha + 1}", "Aba", bg=TEAL, cor=BRANCO, negrito=True, h="center", borda=BORDA)
mesclar(ws, f"D{linha + 1}:H{linha + 1}", "Para que serve", bg=TEAL, cor=BRANCO, negrito=True, h="center", borda=BORDA)
abas = [("Painel", "O resumo visual: totais, saldo, meta, gráficos e uma frase dizendo como você está."),
        ("Entradas", "Onde você anota todo dinheiro que entra: vendas e serviços."),
        ("Saídas", "Onde você anota todo gasto, separando negócio e pessoal."),
        ("Resumo mensal", "O saldo de cada mês, de janeiro a dezembro, e o total do ano."),
        ("Metas", "Sua meta de guardar dinheiro por mês e metas de compra, com barra de progresso."),
        ("Categorias", "As listas das setinhas. Dá para adicionar categorias novas."),
        ("Como usar", "Esta página: o passo a passo e as dicas.")]
for i, (aba, txt) in enumerate(abas):
    r = linha + 2 + i
    bg = CREME if i % 2 == 0 else BRANCO
    mesclar(ws, f"B{r}:C{r}", aba, bg=bg, negrito=True, cor=TEAL, borda=BORDA)
    mesclar(ws, f"D{r}:H{r}", txt, bg=bg, borda=BORDA)
    ws.row_dimensions[r].height = 34
leg = linha + 2 + len(abas) + 1
c = ws[f"B{leg}"]
c.value, c.fill, c.border, c.font = "Amarelo", preencher(AMARELO2), BORDA, fonte(10, True)
c.alignment = Alignment(horizontal="center", vertical="center")
mesclar(ws, f"C{leg}:E{leg}", "= onde você digita", tam=11)
c = ws[f"F{leg}"]
c.value, c.border, c.font = "Sem cor", BORDA, fonte(10, True)
c.alignment = Alignment(horizontal="center", vertical="center")
mesclar(ws, f"G{leg}:H{leg}", "= conta feita sozinha", tam=11)
ws.row_dimensions[leg].height = 26
imprimir_paisagem(ws, f"A1:H{leg}")
ws.page_setup.orientation = "portrait"

# abrir já na aba Como usar
wb.active = 0
for planilha in wb.worksheets:
    planilha.sheet_view.tabSelected = planilha is uso

SAIDA.parent.mkdir(exist_ok=True)
wb.save(SAIDA)
print("Planilha criada em", SAIDA)
