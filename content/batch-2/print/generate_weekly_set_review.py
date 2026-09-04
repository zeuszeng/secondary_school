#!/usr/bin/env python3
"""Generate the black-and-white A4 weekly set review worksheet."""

from pathlib import Path

from reportlab.lib.colors import black, HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas


ROOT = Path(__file__).parent
OUT = ROOT / "mya-weekly-set-review.pdf"
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
PAGE_W, PAGE_H = A4
MARGIN = 36
INK = HexColor("#151515")
SOFT = HexColor("#F2F2F2")
LINE = HexColor("#777777")


def setup_font():
    pdfmetrics.registerFont(TTFont("ArialUnicode", FONT_PATH))
    return "ArialUnicode"


def draw_text(c, text, x, y, size=10, font="ArialUnicode", leading=None):
    c.setFillColor(INK)
    c.setFont(font, size)
    c.drawString(x, y, text)


def paragraph(c, lines, x, top, size=9, leading=13, font="ArialUnicode"):
    for index, line in enumerate(lines):
        draw_text(c, line, x, top - index * leading, size, font)


def rule(c, x1, y1, x2, y2, width=0.7, dash=None):
    c.setStrokeColor(INK)
    c.setLineWidth(width)
    c.setDash(dash or [])
    c.line(x1, y1, x2, y2)
    c.setDash()


def rounded_box(c, x, y, width, height, fill=None, radius=6, stroke=INK):
    c.setStrokeColor(stroke)
    c.setLineWidth(0.8)
    if fill is not None:
        c.setFillColor(fill)
        c.roundRect(x, y, width, height, radius, stroke=1, fill=1)
    else:
        c.roundRect(x, y, width, height, radius, stroke=1, fill=0)


def writing_lines(c, x, y_top, width, count, gap=16):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.4)
    c.setDash(1.5, 2)
    for i in range(count):
        yy = y_top - i * gap
        c.line(x, yy, x + width, yy)
    c.setDash()


def header(c, page, title, subtitle):
    draw_text(c, "Mya 数学 · 周中复盘", MARGIN, PAGE_H - 39, 9)
    c.setFont("ArialUnicode", 19)
    c.drawString(MARGIN, PAGE_H - 66, title)
    draw_text(c, subtitle, MARGIN, PAGE_H - 84, 9)
    c.setFont("ArialUnicode", 8)
    c.drawRightString(PAGE_W - MARGIN, PAGE_H - 39, f"第 {page} / 2 页")
    rule(c, MARGIN, PAGE_H - 94, PAGE_W - MARGIN, PAGE_H - 94, 1.2)


def question_box(c, number, title, prompt, y_top, height, lines, solution_label="演算 / 说明"):
    x = MARGIN
    width = PAGE_W - 2 * MARGIN
    y = y_top - height
    rounded_box(c, x, y, width, height)
    c.setFillColor(INK)
    c.circle(x + 18, y_top - 18, 10, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(x + 18, y_top - 21.5, str(number))
    draw_text(c, title, x + 36, y_top - 22, 11)
    paragraph(c, prompt, x + 16, y_top - 43, size=9, leading=13)
    # Keep the writing label below the last prompt line, even in the compact cards.
    label_y = y + (len(lines) * 16)
    draw_text(c, solution_label, x + 16, label_y + 4, 8)
    writing_lines(c, x + 16, label_y - 4, width - 32, len(lines), gap=16)


def page_one(c):
    header(c, 1, "集合小复盘", "主题：集合概念、属于关系与表示法  ·  建议 10–15 分钟")
    x, w = MARGIN, PAGE_W - 2 * MARGIN
    card_top, card_h = PAGE_H - 109, 76
    rounded_box(c, x, card_top - card_h, w, card_h, fill=SOFT)
    draw_text(c, "学习卡", x + 14, card_top - 19, 11)
    paragraph(c, [
        "核心：对象能确定才是集合；元素对集合用 ∈/∉，集合对集合才用 ⊆。",
        "提醒：先圈左边对象。a 和 {a} 不是同一个对象；描述法要写对象、范围、条件。",
    ], x + 14, card_top - 38, size=9, leading=15)
    draw_text(c, "完成四题后再翻页", x + w - 121, card_top - 19, 8)

    question_box(c, 1, "集合的确定性", [
        "“高一（3）班身高超过 170 cm 的同学”能否组成一个集合？",
        "写出判断，并说明你检查的依据。",
    ], 639, 123, ["", ""])
    question_box(c, 2, "看整体，填关系符号", [
        "已知 A={-1,0,{0},2}，填：0 __ A；{0} __ A；1 __ A；2 __ A。",
        "再写一句：为什么看到 {0} 不能直接断定 0 的关系？",
    ], 504, 132, ["", "", ""])
    question_box(c, 3, "元素还是集合？", [
        "已知 B={{1,2},3}。填：{1,2} __ B，1 __ B。",
        "小岚写“1⊆B”。请改正，并用左右两边对象类型解释。",
    ], 360, 132, ["", "", ""])
    question_box(c, 4, "两种表示法", [
        "（1）把 C={x∈Z|-2≤x<3} 改写成列举法。",
        "（2）把 D={2,4,6,8} 改写成描述法（对象、整数范围、条件齐全）。",
    ], 216, 142, ["", "", "", ""])
    draw_text(c, "自查：我有没有把元素关系 ∈ 和集合关系 ⊆ 混用？", MARGIN, 39, 8)
    c.showPage()


def hint_block(c, number, title, top, lines):
    x, w = MARGIN, PAGE_W - 2 * MARGIN
    h = 119
    rounded_box(c, x, top - h, w, h)
    draw_text(c, f"{number}. {title}", x + 14, top - 20, 11)
    rule(c, x + 14, top - 29, x + w - 14, top - 29, 0.5)
    label_x = x + 14
    body_x = x + 74
    labels = ["一级提示", "二级提示", "答案"]
    for idx, (label, content) in enumerate(zip(labels, lines)):
        yy = top - 48 - idx * 23
        draw_text(c, label, label_x, yy, 8)
        paragraph(c, content, body_x, yy, size=8.6, leading=10.5)


def page_two(c):
    header(c, 2, "提示与答案", "先独立完成第一页；只在需要时逐级查看")
    x, w = MARGIN, PAGE_W - 2 * MARGIN
    rounded_box(c, x, 678, w, 45, fill=SOFT)
    draw_text(c, "使用方法", x + 14, 705, 10)
    paragraph(c, ["先看一级提示；仍卡住再看二级；核对答案后，用自己的话补写关键理由。"], x + 82, 705, size=8.7, leading=11)
    hint_block(c, 1, "集合的确定性", 662, [
        ["看每位同学能否按同一个数值标准被判断。"],
        ["“超过 170 cm”就是身高大于 170 cm，标准明确。"],
        ["能组成集合；集合成员能被唯一确定。"],
    ])
    hint_block(c, 2, "看整体，填关系符号", 531, [
        ["把 A 中逗号分开的每个整体框起来。"],
        ["A 的元素依次是 -1、0、{0}、2。"],
        ["依次为 ∈、∈、∉、∈。A 同时列了 0 与 {0}；不可拆开对象或凭另一项推断。"],
    ])
    hint_block(c, 3, "元素还是集合？", 400, [
        ["把 {1,2} 整体与 B 的元素比较。"],
        ["B 的元素是集合 {1,2} 和数字 3。"],
        ["{1,2}∈B，1∉B；应改为 1∉B。1 是元素、B 是集合，⊆ 两边应都是集合。"],
    ])
    hint_block(c, 4, "两种表示法", 269, [
        ["第（1）问从 -2 起逐个列整数，3 不取；第（2）问找共同特征。"],
        ["D 是 2 到 8 的偶整数，别漏 x∈Z。"],
        ["C={-2,-1,0,1,2}；D={x∈Z|2≤x≤8 且 2|x}。范围与偶数条件完整的同义写法也正确。"],
    ])
    draw_text(c, "复盘一句话：元素—集合用 ∈/∉；集合—集合才讨论 ⊆。", MARGIN, 39, 8)
    c.showPage()


def main():
    font = setup_font()
    canvas = Canvas(str(OUT), pagesize=A4, pageCompression=1)
    canvas.setTitle("Mya 周中集合复盘单")
    canvas.setAuthor("Secondary School Content Team")
    canvas.setSubject("集合概念、属于关系与表示法｜黑白打印练习")
    canvas.setCreator("ReportLab")
    page_one(canvas)
    page_two(canvas)
    canvas.save()
    print(OUT)


if __name__ == "__main__":
    main()
