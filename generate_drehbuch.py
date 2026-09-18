#!/usr/bin/env python3
"""Drehbuch: AUFSTIEG UND SKANDAL – mind. 10 Seiten, ca. 10 Min. Film, Klasse 7."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Flowable
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
            "title_big", fontName=FONT_BOLD, fontSize=20, leading=26,
            alignment=TA_CENTER, spaceAfter=18,
        ),
        "center": ParagraphStyle(
            "center", fontName=FONT, fontSize=SIZE, leading=leading,
            alignment=TA_CENTER, spaceAfter=6,
        ),
        "center_small": ParagraphStyle(
            "center_small", fontName=FONT, fontSize=SIZE, leading=leading,
            alignment=TA_CENTER, spaceAfter=4,
        ),
        "action": ParagraphStyle(
            "action", fontName=FONT, fontSize=SIZE, leading=leading,
            alignment=TA_LEFT, spaceBefore=8, spaceAfter=6,
        ),
        "scene": ParagraphStyle(
            "scene", fontName=FONT_BOLD, fontSize=SIZE, leading=leading,
            alignment=TA_LEFT, spaceBefore=14, spaceAfter=6,
        ),
        "fade_in": ParagraphStyle(
            "fade_in", fontName=FONT, fontSize=SIZE, leading=leading,
            alignment=TA_LEFT, spaceBefore=0, spaceAfter=12,
        ),
        "char": ParagraphStyle(
            "char", fontName=FONT, fontSize=SIZE, leading=leading,
            alignment=TA_CENTER, leftIndent=5 * cm, rightIndent=2 * cm,
            spaceBefore=8, spaceAfter=0,
        ),
        "paren": ParagraphStyle(
            "paren", fontName=FONT, fontSize=SIZE, leading=leading,
            alignment=TA_CENTER, leftIndent=3.75 * cm, rightIndent=5 * cm,
            spaceBefore=0, spaceAfter=0,
        ),
        "dialogue": ParagraphStyle(
            "dialogue", fontName=FONT, fontSize=SIZE, leading=leading,
            alignment=TA_LEFT, leftIndent=2.5 * cm, rightIndent=2.5 * cm,
            spaceBefore=0, spaceAfter=4,
        ),
        "contact": ParagraphStyle(
            "contact", fontName=FONT, fontSize=SIZE, leading=leading,
            alignment=TA_RIGHT, spaceAfter=2,
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
    s = make_styles()
    story = []

    # ========== TITELBLATT ==========
    story.append(Spacer(1, 4 * cm))
    story.append(Paragraph("AUFSTIEG UND SKANDAL", s["title_big"]))
    story.append(Spacer(1, 0.6 * cm))
    story.append(Paragraph("von Paul", s["center"]))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph(
        "Nach wahren Begebenheiten<br/>aus dem Leben von Taylor Swift",
        s["center"],
    ))
    story.append(Paragraph(
        "(Master-Skandal / Big Machine Records)",
        s["center_small"],
    ))
    story.append(Spacer(1, 0.8 * cm))
    story.append(Paragraph(
        "Kurzfilm ca. 10 Minuten<br/>für Musik Klasse 7",
        s["center_small"],
    ))
    story.append(Spacer(1, 4 * cm))
    story.append(Paragraph("3. Fassung, 18. September 2026", s["contact"]))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph("Paul", s["contact"]))
    story.append(Paragraph("Musikklasse 7", s["contact"]))
    story.append(Paragraph("ALLE RECHTE BEI DEN AUTOREN", s["contact"]))
    story.append(PageBreak())

    # ========== DREHBUCH ==========
    story.append(Paragraph("AUFBLENDE:", s["fade_in"]))

    # --- 1 ---
    story.append(scene(s, "INT. KLEINES ZIMMER - TAG"))
    story.append(action(s,
        "Ein einfacher Raum. Bett. Schreibtisch. Poster an der "
        "Wand. Eine Gitarre lehnt am Stuhl."
    ))
    story.append(action(s,
        "TAYLOR, 15, schüchtern, freundlich, mit langen Haaren "
        "und einem Notizbuch voller Texte, sitzt am Schreibtisch. "
        "Sie schreibt. Streicht durch. Schreibt neu."
    ))
    story.append(action(s,
        "Sie greift zur Gitarre. Spielt drei einfache Akkorde. "
        "Summt leise. Stoppt. Lächelt."
    ))
    story.extend(speech(s, "TAYLOR",
        "Das klingt... fast wie ein richtiger Song."))
    story.append(action(s,
        "Sie tippt den Titel auf die Seite: MEIN ERSTER HIT. "
        "Dann schreibt sie darunter: Noch geheim."
    ))
    story.append(action(s,
        "Die TÜR geht auf. FRIEND, 15, ehrlich, mutig, mit "
        "Kapuze, kommt rein und setzt sich aufs Bett."
    ))
    story.extend(speech(s, "FRIEND",
        "Schon wieder Songs schreiben? Du hörst nie auf!"))
    story.extend(speech(s, "TAYLOR",
        "Weil Musik das Einzige ist, das sich echt anfühlt."))
    story.extend(speech(s, "FRIEND",
        "Irgendwann hört dich die ganze Welt."))
    story.extend(speech(s, "TAYLOR",
        "Träum weiter.", paren="lacht leise"))
    story.append(action(s,
        "Friend zeigt auf die Gitarre."
    ))
    story.extend(speech(s, "FRIEND",
        "Spiel den neuen. Nur für mich."))
    story.append(action(s,
        "Taylor spielt kurz. Friend klatscht. Beide lachen. "
        "HANDY VIBRIERT auf dem Tisch."
    ))
    story.extend(speech(s, "TAYLOR",
        "Unbekannte Nummer..."))
    story.append(action(s,
        "Sie nimmt ab. Hält das Handy ans Ohr."
    ))

    # --- 2 ---
    story.append(scene(s, "INT. KLEINES ZIMMER - TAG (WEITER)"))
    story.append(action(s,
        "Aus dem Lautsprecher (Handy): die Stimme von SCOTT."
    ))
    story.extend(speech(s, "SCOTT (O.S.)",
        "Hallo Taylor? Hier ist Scott von Big Machine "
        "Records. Ich habe deine Demo gehört."))
    story.extend(speech(s, "TAYLOR",
        "Ernsthaft?!", paren="Augen weit"))
    story.extend(speech(s, "SCOTT (O.S.)",
        "Kommt morgen in mein Büro. Bring die Gitarre mit."))
    story.append(action(s,
        "Taylor legt auf. Schreit vor Freude. Friend springt auf."
    ))
    story.extend(speech(s, "FRIEND",
        "WAS?! Sag alles!"))
    story.extend(speech(s, "TAYLOR",
        "Ein Label! Die wollen mich!"))
    story.extend(speech(s, "FRIEND",
        "Dann gehst du hin. Und ich komme mit."))
    story.append(action(s,
        "Sie umarmen sich. Kurzer MUSIKSTINGER – hoffnungsvoll."
    ))

    # --- 3 ---
    story.append(scene(s, "INT. BÜRO - TAG"))
    story.append(action(s,
        "Ein Schreibtisch. Ein Stuhl. Ein Schild auf dem Tisch: "
        "BIG MACHINE RECORDS. (Klassenzimmer-Ecke reicht.)"
    ))
    story.append(action(s,
        "SCOTT, 40, laut, selbstsicher, im Jackett, sitzt da. "
        "Vor ihm ein Vertrag und ein Stift."
    ))
    story.append(action(s,
        "Taylor und Friend kommen rein. Taylor hält die Gitarre "
        "fest, als wäre sie ein Schild."
    ))
    story.extend(speech(s, "SCOTT",
        "Da ist unser neuer Star! Setz dich."))
    story.append(action(s,
        "Taylor setzt sich. Friend bleibt stehen."
    ))
    story.extend(speech(s, "SCOTT",
        "Deine Songs sind gut. Wirklich gut. Wir machen dich "
        "gross. Radio. Bühne. Fans."))
    story.extend(speech(s, "TAYLOR",
        "Und die Songs? Gehören die dann mir?"))
    story.extend(speech(s, "SCOTT",
        "Du schreibst. Du singst. Wir besitzen die "
        "Master-Aufnahmen. So läuft das Geschäft."))
    story.extend(speech(s, "FRIEND",
        "Das klingt komisch.", paren="zu Taylor"))
    story.extend(speech(s, "SCOTT",
        "Ohne uns keine Bühne. Ohne Vertrag kein Traum."))
    story.append(action(s,
        "Stille. Taylor sieht Friend an. Dann den Vertrag. "
        "Dann Scott."
    ))
    story.extend(speech(s, "TAYLOR",
        "Ich will singen. Ich unterschreibe."))
    story.append(action(s,
        "Sie unterschreibt. KLICK des Stifts. Scott gibt "
        "ihr die Hand."
    ))
    story.extend(speech(s, "SCOTT",
        "Willkommen im Showbusiness, Taylor Swift."))
    story.append(action(s,
        "Friend schaut skeptisch. Taylor strahlt trotzdem."
    ))

    # --- 4 ---
    story.append(scene(s, "INT. RADIOSTUDIO - TAG"))
    story.append(action(s,
        "Ein Tisch. Zwei Mikrofone. Ein Schild: RADIO HIT FM. "
        "RADIO-DJ, 30, locker, mit Kopfhörern, sitzt bereit."
    ))
    story.append(action(s,
        "Taylor sitzt gegenüber, nervös, aber aufgeregt."
    ))
    story.extend(speech(s, "RADIO-DJ",
        "Live bei uns: Taylor Swift! Dein Song läuft gerade "
        "überall. Wie fühlt sich das an?"))
    story.extend(speech(s, "TAYLOR",
        "Wie ein Traum. Ich habe das Lied in meinem Zimmer "
        "geschrieben. Und jetzt hören es Fremde."))
    story.extend(speech(s, "RADIO-DJ",
        "Und der nächste Plan?"))
    story.extend(speech(s, "TAYLOR",
        "Mehr Songs. Mehr Ehrlichkeit. Und vielleicht... "
        "eine grosse Tour."))
    story.append(action(s,
        "Der DJ drückt einen Knopf. KURZER SONG-AUSSCHNITT "
        "aus dem Lautsprecher. Taylor schliesst die Augen "
        "und hört zu."
    ))

    # --- 5 ---
    story.append(scene(s, "INT. SCHULAULA - BÜHNE - ABEND"))
    story.append(action(s,
        "Scheinwerfer (Taschenlampen reichen). Taylor steht "
        "im coolen Outfit am Mikrofon."
    ))
    story.append(action(s,
        "Vor der Bühne: FAN 1 und FAN 2 mit Schildern "
        "TAYLOR! und WE LOVE YOU. Friend filmt mit dem Handy."
    ))
    story.append(action(s,
        "APPLAUS. Taylor atmet tief durch."
    ))
    story.extend(speech(s, "TAYLOR",
        "Dieser Song ist für alle, die an sich glauben!"))
    story.append(action(s,
        "Sie spielt und singt einen kurzen Teil. Die Fans "
        "mitsingen. Scott steht seitlich und klatscht – "
        "zufrieden wie ein Chef."
    ))
    story.extend(speech(s, "FAN 1",
        "Noch einen! Noch einen!"))
    story.extend(speech(s, "TAYLOR",
        "Okay... einen letzten!"))
    story.append(action(s,
        "Noch ein kurzer Refrain. Grosser APPLAUS. Taylor "
        "verbeugt sich. Strahlt."
    ))
    story.extend(speech(s, "FAN 2",
        "Du bist die Beste!"))
    story.extend(speech(s, "TAYLOR",
        "Ohne euch wäre ich nichts!"))
    story.append(action(s,
        "Scott kommt auf die Bühne, legt Taylor den Arm "
        "um die Schulter für ein Foto. Blitzlicht. "
        "Handy-KLICKS."
    ))

    # --- 6 ---
    story.append(scene(s, "INT. FLUR VOR DER AULA - ABEND"))
    story.append(action(s,
        "Taylor und Friend kommen lachend raus. Scott "
        "telefoniert ein paar Meter weiter."
    ))
    story.extend(speech(s, "FRIEND",
        "Das war riesig. Du hast die Halle gerockt!"))
    story.extend(speech(s, "TAYLOR",
        "Ich will das für immer machen."))
    story.append(action(s,
        "Scott beendet das Gespräch. Kommt herüber."
    ))
    story.extend(speech(s, "SCOTT",
        "Gute Show. Morgen Interview. Übermorgen Studio. "
        "Schlaf wenig – Stars schlafen nie."))
    story.extend(speech(s, "TAYLOR",
        "Alles klar. Ich bin bereit."))
    story.extend(speech(s, "FRIEND",
        "Und Pause? Freundschaft? Normales Leben?"))
    story.extend(speech(s, "SCOTT",
        "Später. Jetzt zählt nur der Erfolg."))
    story.append(action(s,
        "Scott geht. Friend sieht Taylor besorgt an. "
        "Taylor zuckt mit den Schultern – noch glücklich."
    ))

    # --- 7 ---
    story.append(scene(s, "INT. NACHRICHTENSTUDIO - TAG"))
    story.append(action(s,
        "Ein Schreibtisch. Eine Kamera (Handy auf Stativ). "
        "NACHRICHTENSPRECHER, 35, seriös, mit Blatt Papier."
    ))
    story.extend(speech(s, "NACHRICHTENSPRECHER",
        "Gute Nachrichten für die Fans: Taylor Swift ist "
        "der grösste Popstar des Jahres. Alben. Awards. "
        "Ausverkaufte Shows."))
    story.append(action(s,
        "Ein Bild von Taylor wird hochgehalten (ausgedrucktes "
        "Foto oder Handy-Display)."
    ))
    story.extend(speech(s, "NACHRICHTENSPRECHER",
        "Doch hinter den Hits steht ein Vertrag – und der "
        "könnte bald zum Problem werden."))
    story.append(action(s,
        "DUNKLES MUSIKSTINGER. Schnitt."
    ))

    # --- 8 ---
    story.append(scene(s, "INT. KLEINES ZIMMER - NACHT"))
    story.append(action(s,
        "Jahre später. Taylor, jetzt älter wirkend (anderes "
        "Outfit, selbstbewusster), packt eine Tasche. "
        "Viele Awards-Fotos an der Wand (selbst gemalt)."
    ))
    story.append(action(s,
        "Friend kommt rein mit Chips. Setzt sich."
    ))
    story.extend(speech(s, "FRIEND",
        "Erinnerst du dich an dein erstes Notizbuch?"))
    story.extend(speech(s, "TAYLOR",
        "Klar. Da stand: Noch geheim."))
    story.extend(speech(s, "FRIEND",
        "Und jetzt kennt dich jeder."))
    story.extend(speech(s, "TAYLOR",
        "Manchmal fühlt es sich an, als gehöre mein Leben "
        "nicht mehr mir."))
    story.append(action(s,
        "HANDY KLINGELT. Taylor nimmt ab."
    ))
    story.extend(speech(s, "TAYLOR",
        "Hallo?"))
    story.extend(speech(s, "JOURNALISTIN (O.S.)",
        "Taylor, können Sie den Verkauf bestätigen? "
        "Big Machine – inklusive Ihrer Master?"))
    story.extend(speech(s, "TAYLOR",
        "Welcher Verkauf?", paren="verwirrt"))
    story.append(action(s,
        "Sie legt auf. Tippt wild auf dem Handy. Liest. "
        "Das Gesicht wird blass."
    ))
    story.extend(speech(s, "FRIEND",
        "Was ist los?"))
    story.extend(speech(s, "TAYLOR",
        "Jemand hat das Label gekauft. Mit allen meinen "
        "alten Songs. Die Master gehören nicht mehr mir."))
    story.append(action(s,
        "Stille. Die Gitarre lehnt noch am Stuhl – wie am "
        "ersten Tag."
    ))

    # --- 9 ---
    story.append(scene(s, "EXT. SCHULHOF / VOR DEM EINGANG - TAG"))
    story.append(action(s,
        "JOURNALISTIN, 28, schnell, neugierig, mit Mikrofon "
        "(Besenstiel + Schaumstoff). Fan 1 und Fan 2 halten "
        "Handys hoch."
    ))
    story.append(action(s,
        "Taylor kommt raus. Blitzlicht-Geräusche. "
        "Fragen fliegen durcheinander."
    ))
    story.extend(speech(s, "JOURNALISTIN",
        "Taylor! Stimmt der Skandal? Haben Sie die Kontrolle "
        "über Ihre Musik verloren?"))
    story.extend(speech(s, "FAN 1",
        "Sag uns, dass es nicht wahr ist!"))
    story.extend(speech(s, "TAYLOR",
        "Ich habe jede Note geschrieben. Jede Zeile. Und "
        "trotzdem gehören die Aufnahmen jetzt jemand anderem."))
    story.extend(speech(s, "JOURNALISTIN",
        "Was sagen Sie zu Scott und dem Label?"))
    story.extend(speech(s, "TAYLOR",
        "Ich sage: Künstlerinnen sollten die Rechte an "
        "ihrer eigenen Musik haben."))
    story.append(action(s,
        "Friend zieht Taylor sanft weg. Die Journalistin "
        "ruft hinterher."
    ))
    story.extend(speech(s, "JOURNALISTIN",
        "Eine letzte Frage – was kommt jetzt?"))
    story.append(action(s,
        "Taylor dreht sich um. Klarer Blick."
    ))
    story.extend(speech(s, "TAYLOR",
        "Jetzt kämpfe ich."))

    # --- 10 ---
    story.append(scene(s, "INT. NACHRICHTENSTUDIO - TAG"))
    story.append(action(s,
        "Wieder der Nachrichtensprecher. Diesmal ernster."
    ))
    story.extend(speech(s, "NACHRICHTENSPRECHER",
        "Der Fall Taylor Swift ist zum lauten Streit der "
        "Musikindustrie geworden. Fans protestieren online. "
        "Hashtags überall."))
    story.append(action(s,
        "Fan 1 und Fan 2 halten Schilder hoch: "
        "OWN YOUR MASTERS und WE STAND WITH TAYLOR."
    ))
    story.extend(speech(s, "FAN 2",
        "Ihre Songs. Ihre Stimme. Ihre Rechte!"))
    story.extend(speech(s, "NACHRICHTENSPRECHER",
        "Die grosse Frage lautet: Wem gehören Songs "
        "eigentlich – dem Label oder der Künstlerin?"))

    # --- 11 ---
    story.append(scene(s, "INT. KLEINES ZIMMER - NACHT"))
    story.append(action(s,
        "Taylor sitzt auf dem Boden. Notizbücher um sie herum. "
        "Friend sitzt daneben."
    ))
    story.extend(speech(s, "TAYLOR",
        "Ich fühle mich betrogen. Als wäre mein Tagebuch "
        "verkauft worden."))
    story.extend(speech(s, "FRIEND",
        "Weil es so ist. Deine Songs sind dein Tagebuch."))
    story.extend(speech(s, "TAYLOR",
        "Was kann ich tun? Ich kann die Vergangenheit "
        "nicht löschen."))
    story.append(action(s,
        "Friend denkt nach. Nimmt die Gitarre. Gibt sie "
        "Taylor."
    ))
    story.extend(speech(s, "FRIEND",
        "Dann schreib die Zukunft neu."))
    story.extend(speech(s, "TAYLOR",
        "Wie?"))
    story.extend(speech(s, "FRIEND",
        "Nimm alles noch einmal auf. Note für Note. "
        "Taylor's Version. Diesmal gehören die Master dir."))
    story.append(action(s,
        "Taylor starrt die Gitarre an. Dann nickt sie langsam."
    ))
    story.extend(speech(s, "TAYLOR",
        "Das wird hart. Und lange."))
    story.extend(speech(s, "FRIEND",
        "Dann machen wir es zusammen. Ich bin dein Team."))
    story.append(action(s,
        "Sie schlagen ein. Erster AKKORD – entschlossen."
    ))

    # --- 12 ---
    story.append(scene(s, "INT. BÜRO - TAG"))
    story.append(action(s,
        "Scott am Schreibtisch. Taylor steht vor ihm. "
        "Friend im Hintergrund."
    ))
    story.extend(speech(s, "SCOTT",
        "Du willst die alten Alben neu aufnehmen? Das ist "
        "verrückt."))
    story.extend(speech(s, "TAYLOR",
        "Verrückt war der Vertrag. Das hier ist fair."))
    story.extend(speech(s, "SCOTT",
        "Die Fans wollen die Originale. Nicht Kopien."))
    story.extend(speech(s, "TAYLOR",
        "Das sind keine Kopien. Das bin ich – erwachsen. "
        "Mit meinen Rechten."))
    story.extend(speech(s, "SCOTT",
        "Du wirst scheitern."))
    story.extend(speech(s, "TAYLOR",
        "Vielleicht. Aber ich versuche es trotzdem."))
    story.append(action(s,
        "Taylor dreht sich um und geht. Friend folgt. "
        "Scott bleibt allein zurück – unsicher zum ersten Mal."
    ))

    # --- 13 ---
    story.append(scene(s, "INT. AUFNAHMESTUDIO - TAG"))
    story.append(action(s,
        "Mikrofon. Kopfhörer. Ein Stuhl. Schild: STUDIO. "
        "TONTECHNIKER, 25, ruhig, sitzt am „Mischpult“ "
        "(Laptop oder Karton mit Knöpfen)."
    ))
    story.append(action(s,
        "Taylor mit Gitarre. Friend als Backup. Fan 1 und "
        "Fan 2 schauen durch die Tür."
    ))
    story.extend(speech(s, "TONTECHNIKER",
        "Track eins. Love Story – Taylor's Version. Ready?"))
    story.extend(speech(s, "TAYLOR",
        "Ready."))
    story.append(action(s,
        "METRONOM-KLICK. Taylor singt einen kurzen Teil "
        "klar und stark. Stopp."
    ))
    story.extend(speech(s, "TONTECHNIKER",
        "Klingt besser als das Original."))
    story.extend(speech(s, "FRIEND",
        "Weil es jetzt wirklich dir gehört."))
    story.append(action(s,
        "Schnelle Montage (kurze Einstellungen): Taylor "
        "schreibt. Taylor singt. Friend klatscht. "
        "Schilder werden gebastelt: TAYLOR'S VERSION."
    ))
    story.extend(speech(s, "TAYLOR",
        "Nächster Song. Und der nächste. Bis alle wieder "
        "meine sind."))

    # --- 14 ---
    story.append(scene(s, "INT. SCHULAULA - BÜHNE - ABEND"))
    story.append(action(s,
        "Grosses Schild: TAYLOR'S VERSION – LIVE. Fans mit "
        "Schildern. Journalistin am Rand. Scott steht weit "
        "hinten."
    ))
    story.append(action(s,
        "Taylor und Friend betreten die Bühne. APPLAUS."
    ))
    story.extend(speech(s, "TAYLOR",
        "Heute singe ich nicht nur Hits. Heute hole ich "
        "meine Geschichte zurück."))
    story.extend(speech(s, "FAN 1",
        "Wir sind bei dir!"))
    story.extend(speech(s, "FAN 2",
        "Taylor's Version forever!"))
    story.append(action(s,
        "Taylor spielt. Alle mitsingen. Scott senkt den "
        "Blick. Die Journalistin notiert etwas."
    ))
    story.append(action(s,
        "Am Ende hält Taylor inne. Blickt in die Kamera."
    ))
    story.extend(speech(s, "TAYLOR",
        "Wenn ihr etwas erschafft – Kunst, Songs, Texte – "
        "dann gehört es euch. Kämpft dafür."))
    story.append(action(s,
        "Friend tritt neben sie."
    ))
    story.extend(speech(s, "FRIEND",
        "Aufstieg. Skandal. Und Comeback."))
    story.extend(speech(s, "TAYLOR",
        "Meine Songs. Meine Stimme. Meine Version."))
    story.append(action(s,
        "Grosser APPLAUS. Lichter. Taylor lächelt – echt."
    ))
    story.extend(speech(s, "JOURNALISTIN",
        "Taylor! Ein Satz zum Schluss – für alle jungen "
        "Musikerinnen und Musiker?"))
    story.extend(speech(s, "TAYLOR",
        "Lest Verträge. Fragt nach. Und gebt eure "
        "Kunst nicht leichtfertig weg."))
    story.extend(speech(s, "SCOTT",
        "Du hast gewonnen.", paren="leise, von hinten"))
    story.extend(speech(s, "TAYLOR",
        "Nein. Die Musik hat gewonnen."))
    story.append(action(s,
        "Friend hebt die Gitarre. Alle klatschen im Takt. "
        "Kurzer FINAL-SONG (selbst summen oder erlaubte "
        "Instrumentalmusik)."
    ))

    # --- 15 Epilog ---
    story.append(scene(s, "INT. KLASSENZIMMER - TAG"))
    story.append(action(s,
        "Tafel: MUSIK – AUFSTIEG UND SKANDAL. Die Klasse "
        "sitzt. MUSIKLEHRER, 40, freundlich, zeigt auf "
        "die Wörter URHEBERRECHT und MASTER-RECHTE."
    ))
    story.extend(speech(s, "MUSIKLEHRER",
        "Was haben wir gelernt?"))
    story.append(action(s,
        "Eine SCHÜLERIN, 13, hebt die Hand. (Kann Fan 2 "
        "oder Friend spielen.)"
    ))
    story.extend(speech(s, "SCHÜLERIN",
        "Dass man auf Verträge achten muss. Und dass "
        "Songs den Künstlerinnen gehören sollten."))
    story.extend(speech(s, "MUSIKLEHRER",
        "Genau. Taylor Swift hat aus einem Skandal eine "
        "starke Geschichte gemacht – und neue Musik."))
    story.append(action(s,
        "Ein SCHÜLER hebt die Hand."
    ))
    story.extend(speech(s, "SCHÜLER",
        "Und dass Freunde wichtig sind. Ohne Friend "
        "wäre Taylor vielleicht aufgegeben."))
    story.extend(speech(s, "MUSIKLEHRER",
        "Sehr gut. Aufstieg. Skandal. Zusammenhalt. "
        "Und dann: eigene Version."))
    story.append(action(s,
        "Leise MUSIK unter dem Schlussbild. Die Kamera "
        "fährt auf die Tafel: AUFSTIEG UND SKANDAL."
    ))
    story.append(action(s,
        "Ein letztes Schild wird hochgehalten: "
        "THE END? NEIN – TAYLOR'S VERSION."
    ))
    story.append(action(s,
        "Die Klasse klatscht. Abspann beginnt (Namen der "
        "Schüler:innen auf Papier vor die Kamera halten)."
    ))

    story.append(Spacer(1, 1.2 * cm))
    story.append(RightAligned("ABBLENDE."))

    # Anhang: Rollen & Drehtipps als Extra-Seite im PDF? 
    # Better keep pure screenplay; tipps in txt.

    out = "/workspace/drehbuch/Aufstieg_und_Skandal_Drehbuch.pdf"
    doc = SimpleDocTemplate(
        out, pagesize=A4,
        leftMargin=2.5 * cm, rightMargin=2.5 * cm,
        topMargin=2.5 * cm, bottomMargin=2.5 * cm,
        title="AUFSTIEG UND SKANDAL – Drehbuch",
        author="Paul",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"Wrote {out}")
    return out


if __name__ == "__main__":
    build()
