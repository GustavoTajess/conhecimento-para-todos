"""Gera downloads/controle-financeiro.xlsx (planilha do Kit do Jovem Empreendedor).

Uso (na raiz do projeto):  python ferramentas/gerar_planilha.py
Requer:  python -m pip install openpyxl
"""
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

SAIDA = Path(__file__).resolve().parent.parent / "downloads" / "controle-financeiro.xlsx"
ULTIMA_LINHA = 1000                      # quantas linhas as fórmulas do Resumo olham
MOEDA = '"R$" #,##0.00;[Red]-"R$" #,##0.00'   # negativos aparecem em vermelho
DATA = "dd/mm/yyyy"
MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

CABECALHO_FILL = PatternFill("solid", fgColor="0B5D5B")
CABECALHO_FONT = Font(bold=True, color="FFFFFF", size=12)


def cabecalho(ws, linha, titulos):
    for col, titulo in enumerate(titulos, start=1):
        c = ws.cell(row=linha, column=col, value=titulo)
        c.fill, c.font = CABECALHO_FILL, CABECALHO_FONT
        c.alignment = Alignment(horizontal="center", vertical="center")


def aba_lancamentos(wb, nome, exemplos):
    """Cria a aba Entradas ou Saídas: Data, Descrição, Categoria, Valor."""
    ws = wb.create_sheet(nome)
    cabecalho(ws, 1, ["Data", "Descrição", "Categoria", "Valor"])
    for i, linha in enumerate(exemplos, start=2):
        for col, valor in enumerate(linha, start=1):
            ws.cell(row=i, column=col, value=valor)
    for i in range(2, 501):              # formata 500 linhas para você só digitar
        ws.cell(row=i, column=1).number_format = DATA
        ws.cell(row=i, column=4).number_format = MOEDA
    for col, largura in enumerate([14, 42, 20, 16], start=1):
        ws.column_dimensions[get_column_letter(col)].width = largura
    ws.freeze_panes = "A2"               # o cabeçalho fica visível ao rolar


wb = Workbook()

# --- Aba 1: Como usar ---
uso = wb.active
uso.title = "Como usar"
linhas = [
    ("Controle financeiro: como usar", "titulo"),
    ("", None),
    ("1. Na aba Entradas, anote todo dinheiro que entrou: data, descrição, categoria e valor.", None),
    ("2. Na aba Saídas, anote tudo que você gastou, do mesmo jeito.", None),
    ("3. Na aba Resumo mensal, escreva o ano na célula B1. Os totais de cada mês aparecem sozinhos.", None),
    ("4. Saldo do mês = Entradas menos Saídas. Saldo acumulado = quanto sobrou somando todos os meses até aquele.", None),
    ("5. As linhas marcadas com (exemplo) são só para você ver como funciona. Apague o conteúdo delas antes de começar.", None),
    ("", None),
    ("Dicas", "titulo"),
    ("• Digite a data assim: 05/03/2026 (dia/mês/ano).", None),
    ("• Digite o valor só com números, por exemplo 25,50. O R$ aparece sozinho.", None),
    ("• Saldo negativo aparece em vermelho: significa que você gastou mais do que ganhou.", None),
    ("• Salve de vez em quando com Ctrl + S.", None),
]
for i, (texto, estilo) in enumerate(linhas, start=1):
    c = uso.cell(row=i, column=1, value=texto)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    if estilo == "titulo":
        c.font = Font(bold=True, size=14, color="0B5D5B")
uso.column_dimensions["A"].width = 95

# --- Abas 2 e 3: Entradas e Saídas ---
aba_lancamentos(wb, "Entradas", [
    (date(2026, 3, 2), "Venda de brigadeiros (exemplo)", "Vendas", 150),
    (date(2026, 3, 9), "Venda de bolo (exemplo)", "Vendas", 80),
    (date(2026, 3, 15), "Serviço de arte no Canva (exemplo)", "Serviços", 120),
])
aba_lancamentos(wb, "Saídas", [
    (date(2026, 3, 1), "Chocolate e leite condensado (exemplo)", "Ingredientes", 60),
    (date(2026, 3, 5), "Embalagens (exemplo)", "Embalagens", 25),
    (date(2026, 3, 10), "Gás (exemplo)", "Gás", 30),
])

# --- Aba 4: Resumo mensal ---
r = wb.create_sheet("Resumo mensal")
r["A1"], r["B1"] = "Ano:", 2026
r["A1"].font = Font(bold=True, size=12)
r["B1"].font = Font(bold=True, size=12, color="B4441F")
r["B1"].alignment = Alignment(horizontal="center")
cabecalho(r, 3, ["Mês", "Entradas", "Saídas", "Saldo do mês", "Saldo acumulado"])


def soma_mes(aba, mes):
    """SOMASES (em inglês SUMIFS): soma os valores com data dentro do mês."""
    ini = f"DATE($B$1,{mes},1)"
    fim = f"DATE($B$1,{mes + 1},1)"      # mês 13 vira janeiro do ano seguinte
    datas = f"'{aba}'!$A$2:$A${ULTIMA_LINHA}"      # aspas simples protegem o nome da aba (acento)
    valores = f"'{aba}'!$D$2:$D${ULTIMA_LINHA}"
    return f'=SUMIFS({valores},{datas},">="&{ini},{datas},"<"&{fim})'


for mes in range(1, 13):
    linha = mes + 3                      # Janeiro na linha 4 ... Dezembro na linha 15
    r.cell(row=linha, column=1, value=MESES[mes - 1])
    r.cell(row=linha, column=2, value=soma_mes("Entradas", mes))
    r.cell(row=linha, column=3, value=soma_mes("Saídas", mes))
    r.cell(row=linha, column=4, value=f"=B{linha}-C{linha}")
    r.cell(row=linha, column=5, value=f"=D{linha}" if mes == 1 else f"=E{linha - 1}+D{linha}")
r["A16"] = "Total do ano"
r["B16"], r["C16"], r["D16"] = "=SUM(B4:B15)", "=SUM(C4:C15)", "=SUM(D4:D15)"
for col in "ABCDE":
    r[f"{col}16"].font = Font(bold=True)
for linha in range(4, 17):
    for col in range(2, 6):
        r.cell(row=linha, column=col).number_format = MOEDA
for col, largura in enumerate([16, 18, 18, 18, 20], start=1):
    r.column_dimensions[get_column_letter(col)].width = largura
r.freeze_panes = "A4"

SAIDA.parent.mkdir(exist_ok=True)
wb.save(SAIDA)
print("Planilha criada em", SAIDA)
