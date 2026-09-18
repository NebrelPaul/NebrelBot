#!/usr/bin/env python3
"""Drehbuch: AUFSTIEG UND SKANDAL – einfach für Klasse 7."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Flowable,
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

pdfmetrics.registerFont(
    TTFont("CourierNew", "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf")
)
pdfmetrics.registerFont(
    TTFont("CourierNew-Bold", "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf")
)

PAGE_W, PAGE_H = A4
FONT = "CourierNew"
FONT_BOLD = "CourierNew-Bold"
SIZE = 12


class RightAligned(Flowable):
    def __init__(self, text, font=FONT, size=SIZE):
        Flowable.__init__(self)
        self.text = text
        self.font = font
        self.size = size
        self.height = size * 1.4

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        return availWidth, self.height

    def draw(self):
        self.canv.setFont(self.font, self.size)
        self.canv.drawRightString(self.width, 2, self.text)


def make_styles():
    leading = 14
    return {
        "title_big": ParagraphStyle(
            "title_big",
            fontName=FONT_BOLD,
            fontSize=20,
            leading=26,
            alignment=TA_CENTER,
            spaceAfter=18,
        ),
        "center": ParagraphStyle(
            "center",
            fontName=FONT,
            fontSize=SIZE,
            leading=leading,
            alignment=TA_CENTER,
            spaceAfter=6,
        ),
        "center_small": ParagraphStyle(
            "center_small",
            fontName=FONT,
            fontSize=SIZE,
            leading=leading,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "action": ParagraphStyle(
            "action",
            fontName=FONT,
            fontSize=SIZE,
            leading=leading,
            alignment=TA_LEFT,
            spaceBefore=8,
            spaceAfter=6,
        ),
        "scene": ParagraphStyle(
            "scene",
            fontName=FONT_BOLD,
            fontSize=SIZE,
            leading=leading,
            alignment=TA_LEFT,
            spaceBefore=14,
            spaceAfter=6,
        ),
        "fade_in": ParagraphStyle(
            "fade_in",
            fontName=FONT,
            fontSize=SIZE,
            leading=leading,
            alignment=TA_LEFT,
            spaceBefore=0,
            spaceAfter=12,
        ),
        "char": ParagraphStyle(
            "char",
            fontName=FONT,
            fontSize=SIZE,
            leading=leading,
            alignment=TA_CENTER,
            leftIndent=5 * cm,
            rightIndent=2 * cm,
            spaceBefore=8,
            spaceAfter=0,
        ),
        "paren": ParagraphStyle(
            "paren",
            fontName=FONT,
            fontSize=SIZE,
            leading=leading,
            alignment=TA_CENTER,
            leftIndent=3.75 * cm,
            rightIndent=5 * cm,
            spaceBefore=0,
            spaceAfter=0,
        ),
        "dialogue": ParagraphStyle(
            "dialogue",
            fontName=FONT,
            fontSize=SIZE,
            leading=leading,
            alignment=TA_LEFT,
            leftIndent=2.5 * cm,
            rightIndent=2.5 * cm,
            spaceBefore=0,
            spaceAfter=4,
        ),
        "contact": ParagraphStyle(
            "contact",
            fontName=FONT,
            fontSize=SIZE,
            leading=leading,
            alignment=TA_RIGHT,
            spaceAfter=2,
        ),
    }


def add_page_number(canvas, doc):
    page = canvas.getPageNumber()
    if page <= 1:
        return
    canvas.saveState()
    canvas.setFont(FONT, SIZE)
    canvas.drawRightString(PAGE_W - 2 * cm, PAGE_H - 1.5 * cm, str(page - 1))
    canvas.restoreState()


def scene(styles, text):
    return Paragraph(text.upper(), styles["scene"])


def action(styles, text):
    return Paragraph(text, styles["action"])


def speech(styles, name, text, paren=None):
    items = [Paragraph(name.upper(), styles["char"])]
    if paren:
        items.append(Paragraph(f"({paren})", styles["paren"]))
    items.append(Paragraph(text, styles["dialogue"]))
    return items


def build():
    styles = make_styles()
    story = []

    # ========== TITELBLATT ==========
    story.append(Spacer(1, 4.5 * cm))
    story.append(Paragraph("AUFSTIEG UND SKANDAL", styles["title_big"]))
    story.append(Spacer(1, 0.8 * cm))
    story.append(Paragraph("von Paul", styles["center"]))
    story.append(Spacer(1, 0.6 * cm))
    story.append(
        Paragraph(
            "Nach wahren Begebenheiten<br/>aus dem Leben von Taylor Swift",
            styles["center"],
        )
    )
    story.append(
        Paragraph(
            "(Master-Skandal – einfach für die Schule)",
            styles["center_small"],
        )
    )
    story.append(Spacer(1, 5 * cm))
    story.append(Paragraph("2. Fassung, 18. September 2026", styles["contact"]))
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph("Paul", styles["contact"]))
    story.append(Paragraph("Musikklasse 7", styles["contact"]))
    story.append(Paragraph("ALLE RECHTE BEI DEN AUTOREN", styles["contact"]))
    story.append(PageBreak())

    # ========== DREHBUCH ==========
    # Nur 3 Orte (Klasse/Aula), 5 Rollen, kurze Dialoge, ~2–3 Min.
    story.append(Paragraph("AUFBLENDE:", styles["fade_in"]))

    # ----- SZENE 1: AUFSTIEG -----
    story.append(scene(styles, "INT. KLEINES ZIMMER - TAG"))
    story.append(
        action(
            styles,
            "Ein einfacher Raum. Ein Stuhl. Eine Gitarre. "
            "TAYLOR, 16, schüchtern, freundlich, mit "
            "Notizbuch, sitzt und tippt mit dem Stift auf "
            "den Tisch. RHYTHMUS.",
        )
    )
    story.append(
        action(
            styles,
            "Sie greift zur Gitarre und singt leise einen "
            "kurzen Songanfang. (Echte Taylor-Musik nur "
            "leise im Hintergrund – oder selbst summen.)",
        )
    )
    story.append(
        action(
            styles,
            "Die TÜR geht auf. SCOTT, 40, laut, selbstsicher, "
            "im Jackett, kommt rein. In der Hand: ein Vertrag.",
        )
    )
    story.extend(
        speech(
            styles,
            "SCOTT",
            "Taylor! Deine Songs sind super. Unterschreib "
            "hier – und du wirst berühmt.",
        )
    )
    story.extend(
        speech(
            styles,
            "TAYLOR",
            "Wirklich? Gehören die Songs dann mir?",
            paren="unsicher",
        )
    )
    story.extend(
        speech(
            styles,
            "SCOTT",
            "Du singst. Wir kümmern uns um den Rest. "
            "Vertrau mir.",
        )
    )
    story.append(
        action(
            styles,
            "Taylor zögert. Dann unterschreibt sie. "
            "KLICK. Scott lächelt.",
        )
    )
    story.extend(
        speech(
            styles,
            "SCOTT",
            "Willkommen im Showbusiness.",
        )
    )

    # ----- SZENE 2: STAR -----
    story.append(scene(styles, "INT. SCHULAULA - BÜHNE - TAG"))
    story.append(
        action(
            styles,
            "Taylor steht auf der Bühne mit Mikrofon. "
            "Sie trägt etwas Glitzer oder ein cooles "
            "Outfit. Vor der Bühne: FAN 1 und FAN 2 "
            "mit Schildern: TAYLOR! und #1.",
        )
    )
    story.append(
        action(
            styles,
            "APPLAUS von den Fans. Taylor verbeugt sich, "
            "lacht, winkt.",
        )
    )
    story.extend(
        speech(
            styles,
            "FAN 1",
            "Taylor, wir lieben dich!",
        )
    )
    story.extend(
        speech(
            styles,
            "TAYLOR",
            "Danke! Ohne euch geht gar nichts!",
        )
    )
    story.append(
        action(
            styles,
            "Fan 2 hält ein Handy hoch. Auf dem Display "
            "eine grosse Nachricht (Schild oder Papier "
            "aufs Handy kleben):",
        )
    )
    story.append(
        action(
            styles,
            "SKANDAL: Andere besitzen jetzt Taylors Songs!",
        )
    )
    story.append(
        action(
            styles,
            "LEISES MURMELN. Taylor sieht das Handy. "
            "Ihr Lächeln fällt.",
        )
    )

    # ----- SZENE 3: SKANDAL -----
    story.append(scene(styles, "INT. KLEINES ZIMMER - TAG"))
    story.append(
        action(
            styles,
            "Taylor sitzt wieder auf dem Stuhl. Diesmal "
            "ohne Gitarre. Handy in der Hand. Traurig.",
        )
    )
    story.append(
        action(
            styles,
            "FRIEND, 16, ehrlich, mutig, kommt herein.",
        )
    )
    story.extend(
        speech(
            styles,
            "FRIEND",
            "Stimmt das? Deine Songs gehören nicht mehr dir?",
        )
    )
    story.extend(
        speech(
            styles,
            "TAYLOR",
            "Ja. Ich habe sie geschrieben. Aber jemand "
            "anders besitzt sie jetzt.",
        )
    )
    story.extend(
        speech(
            styles,
            "FRIEND",
            "Das ist unfair!",
        )
    )
    story.extend(
        speech(
            styles,
            "TAYLOR",
            "Ich weiss. Aber ich gebe nicht auf.",
        )
    )
    story.append(
        action(
            styles,
            "Taylor steht auf. Nimmt die Gitarre. "
            "Entschlossen.",
        )
    )
    story.extend(
        speech(
            styles,
            "TAYLOR",
            "Ich nehme alles noch einmal auf. Diesmal "
            "gehören die Songs mir.",
        )
    )
    story.extend(
        speech(
            styles,
            "FRIEND",
            "Ich helfe dir.",
        )
    )
    story.append(
        action(
            styles,
            "Sie geben sich die Hand. KURZER MUSIK-AKKORD.",
        )
    )

    # ----- SZENE 4: COMEBACK -----
    story.append(scene(styles, "INT. SCHULAULA - BÜHNE - TAG"))
    story.append(
        action(
            styles,
            "Wieder die Bühne. Diesmal ein Schild an der "
            "Wand: TAYLOR'S VERSION. Taylor und Friend "
            "stehen zusammen am Mikrofon.",
        )
    )
    story.append(
        action(
            styles,
            "Fan 1 und Fan 2 klatschen. Scott steht seitlich "
            "und schaut überrascht.",
        )
    )
    story.extend(
        speech(
            styles,
            "TAYLOR",
            "Meine Songs. Meine Stimme. Meine Version.",
        )
    )
    story.append(
        action(
            styles,
            "Taylor spielt einen kurzen Akkord. Alle "
            "klatschen. Scott geht langsam ab.",
        )
    )
    story.extend(
        speech(
            styles,
            "FAN 2",
            "Wem gehören Songs?",
            paren="zur Kamera",
        )
    )
    story.extend(
        speech(
            styles,
            "TAYLOR",
            "Den Künstlerinnen und Künstlern!",
        )
    )
    story.append(
        action(
            styles,
            "APPLAUS. Taylor lächelt – diesmal echt.",
        )
    )

    story.append(Spacer(1, 1.2 * cm))
    story.append(RightAligned("ABBLENDE."))

    out = "/workspace/drehbuch/Aufstieg_und_Skandal_Drehbuch.pdf"
    doc = SimpleDocTemplate(
        out,
        pagesize=A4,
        leftMargin=2.5 * cm,
        rightMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
        title="AUFSTIEG UND SKANDAL – Drehbuch",
        author="Paul",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"Wrote {out}")
    return out


if __name__ == "__main__":
    build()
