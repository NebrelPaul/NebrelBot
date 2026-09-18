#!/usr/bin/env python3
"""Generate Taylor Swift screenplay PDF per Urs Bühler / screenwriter.ch format."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    KeepTogether,
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
            fontSize=22,
            leading=28,
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
    """Page number top-right; skip title page."""
    page = canvas.getPageNumber()
    if page <= 1:
        return
    canvas.saveState()
    canvas.setFont(FONT, SIZE)
    # Script pages start at 1 after title page
    canvas.drawRightString(PAGE_W - 2 * cm, PAGE_H - 1.5 * cm, str(page - 1))
    canvas.restoreState()


def scene(styles, text):
    return Paragraph(text.upper(), styles["scene"])


def action(styles, text):
    return Paragraph(text, styles["action"])


def char(styles, name, paren=None):
    items = [Paragraph(name.upper(), styles["char"])]
    if paren:
        items.append(Paragraph(f"({paren})", styles["paren"]))
    return items


def dialogue(styles, text):
    return Paragraph(text, styles["dialogue"])


def speech(styles, name, text, paren=None):
    items = char(styles, name, paren)
    items.append(dialogue(styles, text))
    return items


def build():
    styles = make_styles()
    story = []

    # ========== TITELBLATT ==========
    story.append(Spacer(1, 4.5 * cm))
    story.append(Paragraph("WAS MIR GEHÖRT", styles["title_big"]))
    story.append(Spacer(1, 0.8 * cm))
    story.append(Paragraph("von Paul", styles["center"]))
    story.append(Spacer(1, 0.6 * cm))
    story.append(
        Paragraph(
            "Nach wahren Begebenheiten aus dem Leben<br/>der Musikerin Taylor Swift",
            styles["center"],
        )
    )
    story.append(
        Paragraph(
            "(Der Master-Skandal / Big Machine Records)",
            styles["center_small"],
        )
    )
    story.append(Spacer(1, 5 * cm))
    story.append(Paragraph("1. Fassung, 18. September 2026", styles["contact"]))
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph("Paul", styles["contact"]))
    story.append(Paragraph("Musikklasse 8", styles["contact"]))
    story.append(Paragraph("ALLE RECHTE BEI DEN AUTOREN", styles["contact"]))
    story.append(PageBreak())

    # ========== DREHBUCH ==========
    story.append(Paragraph("AUFBLENDE:", styles["fade_in"]))

    # SZENE 1
    story.append(scene(styles, "INT. AUFNAHMESTUDIO - NASHVILLE - NACHT"))
    story.append(
        action(
            styles,
            "Ein dunkler Raum, voller Kabel und Mikrofone. Eine rote "
            "AUFNAHME-LAMPE blinkt.",
        )
    )
    story.append(
        action(
            styles,
            "TAYLOR SWIFT, 19, schlank, konzentriert, mit leuchtenden Augen, "
            "sitzt mit einer Gitarre vor dem Mikrofon. Sie trägt einen "
            "schlichten Pullover und Jeans. Neben ihr: ein Notizbuch voller "
            "Songtexte.",
        )
    )
    story.append(
        action(
            styles,
            "Am Mischpult sitzt SCOTT BORCHETTA, ende vierzig, selbstbewusst, "
            "im Anzug ohne Krawatte. Er lächelt.",
        )
    )
    story.extend(
        speech(
            styles,
            "SCOTT",
            "Das war magisch, Taylor. Die Welt wird diesen Song kennen.",
        )
    )
    story.extend(
        speech(
            styles,
            "TAYLOR",
            "Wirklich?",
            paren="leise, hoffnungsvoll",
        )
    )
    story.extend(
        speech(
            styles,
            "SCOTT",
            "Unterschreib hier. Big Machine Records macht dich gross. "
            "Die Master-Aufnahmen gehören zum Label – so läuft das "
            "Geschäft. Du schreibst die Hits. Wir besitzen die Bänder.",
        )
    )
    story.append(
        action(
            styles,
            "Taylor zögert einen Moment. Dann nimmt sie den Stift. "
            "Unterschreibt.",
        )
    )
    story.append(
        action(
            styles,
            "KLICK der Kugelschreiberspitze. Die AUFNAHME-LAMPE erlischt.",
        )
    )

    # SZENE 2
    story.append(scene(styles, "INT. KONZERTHALLE - BÜHNE - NACHT (JAHRE SPÄTER)"))
    story.append(
        action(
            styles,
            "Donnernder APPLAUS. Scheinwerfer. Taylor, jetzt mitte "
            "zwanzig, steht im Glitzerkleid vor tausenden Fans. Sie "
            "verbeugt sich, strahlt – eine Superstarin.",
        )
    )
    story.append(
        action(
            styles,
            "Ein HANDY in der ersten Reihe filmt. Auf dem Display "
            "blinkt eine PUSH-NACHRICHT:",
        )
    )
    story.append(
        action(
            styles,
            '"BREAKING: Scooter Braun kauft Big Machine Records – '
            'inkl. aller Taylor-Swift-Master."',
        )
    )

    # SZENE 3
    story.append(scene(styles, "INT. HOTELSUITE - NACHT"))
    story.append(
        action(
            styles,
            "Taylor sitzt auf dem Bett, immer noch im Bühnen-Outfit. "
            "In der Hand: ihr Handy. Das Gesicht ist blass.",
        )
    )
    story.append(
        action(
            styles,
            "Neben ihr sitzt ihre Freundin und Beraterin TREE, 30, "
            "ruhig, klar, in schwarzer Jacke.",
        )
    )
    story.extend(
        speech(
            styles,
            "TREE",
            "Er besitzt jetzt jeden Song, den du zwischen 2006 und "
            "2017 aufgenommen hast. Alle Master. Alle Rechte.",
        )
    )
    story.extend(
        speech(
            styles,
            "TAYLOR",
            "Meine Lieder. Meine Nächte. Mein ganzes Leben in diesen "
            "Alben – und ich darf nicht einmal darüber bestimmen?",
        )
    )
    story.extend(
        speech(
            styles,
            "TREE",
            "Nicht mehr. Es gehört ihm.",
        )
    )
    story.append(
        action(
            styles,
            "Taylor steht auf. Geht zum Fenster. Die Stadt blinkt unten. "
            "Sie ballt die Faust – öffnet sie wieder.",
        )
    )
    story.extend(
        speech(
            styles,
            "TAYLOR",
            "Dann hole ich sie mir zurück.",
        )
    )
    story.extend(
        speech(
            styles,
            "TREE",
            "Wie?",
        )
    )
    story.extend(
        speech(
            styles,
            "TAYLOR",
            "Ich nehme alles noch einmal auf. Note für Note. "
            "Taylor's Version. Diesmal gehören die Master mir.",
        )
    )

    # SZENE 4
    story.append(scene(styles, "EXT. STRASSE VOR DEM HOTEL - TAG"))
    story.append(
        action(
            styles,
            "Ein Meer aus Kameras und Mikrofonen. Blitzlicht. "
            "JOURNALISTEN drängen sich vor.",
        )
    )
    story.extend(
        speech(
            styles,
            "JOURNALISTIN",
            "Taylor! Ist das wahr? Wirst du deine alten Alben "
            "noch einmal aufnehmen?",
        )
    )
    story.extend(
        speech(
            styles,
            "TAYLOR",
            "Künstlerinnen sollten die Rechte an ihrer eigenen "
            "Musik haben. Punkt.",
        )
    )
    story.append(
        action(
            styles,
            "Hinter ihr halten Fans Schilder hoch: "
            '"WE STAND WITH TAYLOR" – "OWN YOUR MASTERS".',
        )
    )
    story.append(
        action(
            styles,
            "SMARTPHONE-KAMERAS klicken. Ein TikTok-SOUND startet "
            "irgendwo in der Menge.",
        )
    )

    # SZENE 5
    story.append(scene(styles, "INT. NACHRICHTENSTUDIO - TAG"))
    story.append(
        action(
            styles,
            "Ein NACHRICHTENSPRECHER, 45, seriös, sitzt hinter einem "
            "Schreibtisch. Hinter ihm eine Grossaufnahme von Taylor.",
        )
    )
    story.extend(
        speech(
            styles,
            "NACHRICHTENSPRECHER",
            "Was als Vertrag zwischen einem jungen Star und einem "
            "Label begann, ist zum lautesten Streit der Musikindustrie "
            "geworden. Die Frage lautet: Wem gehören eigentlich Songs?",
        )
    )

    # SZENE 6
    story.append(scene(styles, "INT. AUFNAHMESTUDIO - TAG"))
    story.append(
        action(
            styles,
            "Dieselbe Art Raum wie am Anfang – aber heller, grösser. "
            "Taylor, jetzt erwachsen und entschlossen, steht wieder "
            "am Mikrofon. Vor ihr: ein Notenständer mit dem Titel "
            '"Love Story (Taylor\'s Version)".',
        )
    )
    story.append(
        action(
            styles,
            "Die Band wartet. Der Tontechniker hebt den Daumen.",
        )
    )
    story.extend(
        speech(
            styles,
            "TONTECHNIKER",
            "Ready when you are.",
        )
    )
    story.append(
        action(
            styles,
            "Taylor atmet tief ein. Schliesst kurz die Augen. "
            "Öffnet sie wieder – klar und ruhig.",
        )
    )
    story.extend(
        speech(
            styles,
            "TAYLOR",
            "Diesmal gehört jede Note mir.",
        )
    )
    story.append(
        action(
            styles,
            "Sie nickt. Der METRONOM-KLICK setzt ein. Taylor beginnt "
            "zu singen. Stark. Frei.",
        )
    )
    story.append(
        action(
            styles,
            "Die Kamera fährt langsam zurück. An der Studio-Wand "
            "hängt ein neues Schild: TAYLOR'S VERSION.",
        )
    )

    # SZENE 7 - kurzer Epilog
    story.append(scene(styles, "INT. KLASSENZIMMER - TAG"))
    story.append(
        action(
            styles,
            "Ein ganz normales Klassenzimmer. An der Tafel steht: "
            "MUSIK – TAYLOR SWIFT & DER MASTER-SKANDAL.",
        )
    )
    story.append(
        action(
            styles,
            "Eine SCHÜLERIN, 14, hebt die Hand.",
        )
    )
    story.extend(
        speech(
            styles,
            "SCHÜLERIN",
            "Also... wenn ich einen Song schreibe – gehört der dann mir?",
        )
    )
    story.append(
        action(
            styles,
            "Der MUSIKLEHRER, 40, freundlich, zeigt auf das Tafelbild "
            "mit den Worten URHEBERRECHT und MASTER-RECHTE.",
        )
    )
    story.extend(
        speech(
            styles,
            "MUSIKLEHRER",
            "Genau das ist die Frage. Und genau deshalb schauen wir "
            "uns heute Taylor Swift an.",
        )
    )
    story.append(
        action(
            styles,
            "Aus einem Lautsprecher tönt leise ein Song – "
            "Taylor's Version. Die Klasse hört zu.",
        )
    )

    story.append(Spacer(1, 1.2 * cm))
    story.append(RightAligned("ABBLENDE."))

    out = "/workspace/drehbuch/Was_mir_gehoert_Taylor_Swift_Drehbuch.pdf"
    doc = SimpleDocTemplate(
        out,
        pagesize=A4,
        leftMargin=2.5 * cm,
        rightMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
        title="WAS MIR GEHÖRT – Drehbuch",
        author="Paul",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"Wrote {out}")
    return out


if __name__ == "__main__":
    build()
