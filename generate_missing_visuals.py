#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generiše namenske infografike za preostale slajdove (2, 7, 11, 12, 22, 23, 28, 40)
kako bi se u potpunosti eliminisale neusaglašene generičke slike iz brending PDF-a.
"""

import os
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = "/Users/markozivkovic/PREZENTACIJA ZA ROYAL NANNY/extracted_assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# Royal Nanny Palette
C_DARK = (71, 52, 46)        # #47342E Espresso
C_TERRA = (118, 85, 53)      # #765535 Cognac / Terakota
C_SAND = (205, 187, 160)     # #CDBBA0 Sand Beige
C_LINEN = (240, 233, 215)    # #F0E9D7 Light Linen
C_BG = (247, 245, 240)       # #F7F5F0 Warm Linen Canvas
C_GOLD = (209, 174, 102)     # #D1AE66 Gold
C_SAGE = (139, 144, 109)     # #8B906D Sage Green
C_CARD = (255, 255, 255)     # Card White
C_RED = (185, 65, 55)        # Emergency Coral / Red
C_ALERT_BG = (253, 246, 245)

W, H = 1200, 1500

def get_fonts():
    try:
        f_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", 44)
        f_serif = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 30)
        f_badge = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 23)
        f_card_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", 32)
        f_bold = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 29)
        f_body = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 26)
        f_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
    except Exception:
        f_title = f_serif = f_badge = f_card_title = f_bold = f_body = f_small = ImageFont.load_default()
    return f_title, f_serif, f_badge, f_card_title, f_bold, f_body, f_small

F_TITLE, F_SERIF, F_BADGE, F_CARD_TITLE, F_BOLD, F_BODY, F_SMALL = get_fonts()

def create_base_canvas(badge_text, title_text, subtitle_text):
    img = Image.new("RGB", (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    
    # Header badge
    bbox_b = draw.textbbox((0, 0), badge_text.upper(), font=F_BADGE)
    bw = (bbox_b[2] - bbox_b[0]) + 44
    draw.rounded_rectangle([(W//2 - bw//2, 16), (W//2 + bw//2, 64)], radius=8, fill=C_DARK)
    draw.text((W//2, 40), badge_text.upper(), fill=C_LINEN, font=F_BADGE, anchor="mm")
    
    # Main title with auto-fit width
    bbox = draw.textbbox((0, 0), title_text, font=F_TITLE)
    t_width = bbox[2] - bbox[0]
    if t_width > 1100:
        f_title_use = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", 34)
    else:
        f_title_use = F_TITLE
    draw.text((W//2, 92), title_text, fill=C_DARK, font=f_title_use, anchor="mm")
    
    # Subtitle with auto-fit width
    if subtitle_text:
        s_box = draw.textbbox((0, 0), subtitle_text, font=F_SERIF)
        s_w = s_box[2] - s_box[0]
        if s_w > 1080:
            f_sub_use = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 24)
        else:
            f_sub_use = F_SERIF
        draw.text((W//2, 132), subtitle_text, fill=C_TERRA, font=f_sub_use, anchor="mm")
        
    return img, draw

def draw_badge(draw, x, y, text, font, fill_color, text_color, radius=8, padding_x=34, height=52):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = (bbox[2] - bbox[0]) + padding_x
    draw.rounded_rectangle([(x, y), (x + w, y + height)], radius=radius, fill=fill_color)
    draw.text((x + padding_x // 2, y + height // 2), text, fill=text_color, font=font, anchor="lm")
    return x + w

def draw_item(draw, x, y, label, desc, font_lbl=F_BOLD, font_desc=F_BODY, col_lbl=C_DARK, col_desc=C_DARK, line_gap=34):
    draw.text((x, y), label, fill=col_lbl, font=font_lbl)
    cur_y = y + line_gap
    draw.text((x, cur_y), desc, fill=col_desc, font=font_desc)
    return cur_y + 28

def draw_banner_title(draw, y, text, fill_color, max_width=1040, default_font=F_CARD_TITLE):
    bbox = draw.textbbox((0, 0), text, font=default_font)
    w = bbox[2] - bbox[0]
    if w > max_width:
        scale = max_width / w
        new_size = max(18, int(32 * scale))
        font_use = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", new_size)
    else:
        font_use = default_font
    draw.text((W//2, y), text, fill=fill_color, font=font_use, anchor="mm")

# -------------------------------------------------------------
# SLIDE 02: STRUKTURA EDUKATIVNOG PROGRAMA (4 MODULA / 37 TEMA)
# -------------------------------------------------------------
def make_slide02():
    img, draw = create_base_canvas(
        "ROYAL NANNY AKADEMIJA • STRUKTURA PROGRAMA",
        "KURIKULUM EDUKACIJE ZA PREDAVAČE",
        "4 ključna modula i 37 standardizovanih kliničkih tema"
    )
    
    modules = [
        ("MODUL 1: HIGIJENA I NEGA NOVOROĐENČETA (8 TEMA)", C_TERRA, [
            ("Priprema prostora i kupanje:", "Soba, oprema, mikroklima, stanica za kupanje i nega kože."),
            ("Medicinska toaleta i nega:", "Nega pupčanika, čula (oči, uši, nos, nokti), oblačenje i san."),
            ("Higijena pribora:", "Održavanje garderobe, pranje na 60-90°C i sterilizacija flašica.")
        ]),
        ("MODUL 2: DOJENJE I ISHRANA NOVOROĐENČETA (10 TEMA)", C_SAGE, [
            ("Biološki značaj i laktacija:", "Prednosti dojenja, nega dojki, lanolin i let-down refleks."),
            ("Položaji i hvat dojke:", "Ergonomija, asimetrični hvat, prevencija ragada i mastitisa."),
            ("Izmazanje i formula:", "Čuvanje izdojenog mleka i bezbedna priprema formule (70°C).")
        ]),
        ("MODUL 3: NEGA I RAZVOJ ODOJČETA (6 TEMA)", C_DARK, [
            ("Rast i motorika:", "Kalendar vakcinacije, zdrav motorni razvoj i vežbe na stomaku."),
            ("Ishrana i boravak napolju:", "Šetnja u kolicima, uvođenje čvrste hrane (pravilo 3 dana)."),
            ("Denticija i putovanja:", "Nicanje zubića, oralna higijena i bezbednost u vožnji (auto-sedište).")
        ]),
        ("MODUL 4: NEGA BOLESNOG DETETA I HITNA STANJA (13 TEMA)", C_RED, [
            ("Digestivni i kožni problemi:", "Grčevi (kolike), pelenski osip, infekcije oka i zapušen nos."),
            ("Febrilnost i prva pomoć:", "Visoka temperatura, gušenje (udarci po leđima), padovi, opekotine."),
            ("Apoteka i lekovi:", "Zarazne bolesti, ujedi insekata/krpelji, alergije i davanje lekova.")
        ])
    ]
    
    y = 155
    for title, col, items in modules:
        draw.rounded_rectangle([(35, y), (W-35, y + 270)], radius=12, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 50, y + 14, title, F_CARD_TITLE, col, C_CARD, height=46)
        
        item_y = y + 72
        for lbl, desc in items:
            draw_item(draw, 60, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, line_gap=32)
            item_y += 64
        y += 288
        
    # Footer accreditation banner
    draw.rounded_rectangle([(35, 1330), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1365), "STRUČNA AKREDITACIJA KURIKULUMA", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1415, "Spec. strukovna medicinska sestra Jelena Aleksić", C_LINEN)
    
    img.save(os.path.join(ASSETS_DIR, "slide02_curriculum_structure.png"), "PNG", optimize=True)
    print("Saved slide02_curriculum_structure.png")

# -------------------------------------------------------------
# SLIDE 07: NEGA ČULA: OČI, UŠI, NOS I NOKTIĆI
# -------------------------------------------------------------
def make_slide07():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 1: HIGIJENA I NEGA NOVOROĐENČETA",
        "NEGA ČULA NOVOROĐENČETA",
        "Protokoli toalete očiju, ušiju, nosića i nege noktića"
    )
    
    cards = [
        ("1. TOALETA OČIJU (PREVENCIJA INFEKCIJA)", C_TERRA, [
            ("Fiziološki rastvor i sterilna gaza:", "Natopiti sterilnu kompresu fiziološkim rastvorom (0.9% NaCl)."),
            ("Potez od spolja ka unutra:", "Brisati od spoljašnjeg ugla oka ka korenu nosa jednim potezom."),
            ("Zasebna gaza za svako oko:", "Nikada ne koristiti istu gazu za oba oka (prevencija unakrsne infekcije).")
        ]),
        ("2. TOALETA UŠIJU I NOSIĆA", C_SAGE, [
            ("Samo spoljašnja ušna školjka:", "Brisati samo pregibe i kožu iza uha; NIKADA štapiće u ušni kanal!"),
            ("Prohodnost nosnih hodnika:", "Pre podoja ukapati po 1-2 kapi fiziološkog rastvora u svaku nozdrvu."),
            ("Mekani nazalni aspirator:", "Usisavanje sekreta samo po potrebi ako beba otežano sisa ili diše.")
        ]),
        ("3. NEGA I SEČENJE NOKTIĆA", C_DARK, [
            ("Vreme prvog sečenja:", "Ne seći nokte prvih 3 do 4 nedelje dok se pločica ne odvoji od jagodice."),
            ("Zaobljene bebi makazice:", "Koristiti isključivo makazice sa tupim, zaobljenim vrhom (prethodno dezinfikovane)."),
            ("Pravolinijski rez:", "Seći ravno dok beba mirno spava ili sisa kako bi se izbegli nagli pokreti.")
        ])
    ]
    
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=52)
        
        item_y = y + 84
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, line_gap=34)
            item_y += 76
        y += 352
        
    # Warning
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_ALERT_BG, outline=C_RED, width=2)
    draw.text((W//2, 1262), "[KRITIČNO MEDICINSKO UPOZORENJE]", fill=C_RED, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1320, "NIKADA NE GURATI ŠTAPIĆE SA VATOM U UHO ILI NOS!", C_DARK)
    draw.text((W//2, 1386), "Štapići guraju cerumen i sekret dublje i mogu probušiti bubnu opnu.", fill=C_TERRA, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide07_sensory_care.png"), "PNG", optimize=True)
    print("Saved slide07_sensory_care.png")

# -------------------------------------------------------------
# SLIDE 11: PREDNOSTI DOJENJA I BIOLOŠKI ZNAČAJ MLEKA
# -------------------------------------------------------------
def make_slide11():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 2: DOJENJE I LAKTACIJA",
        "BIOLOŠKI I IMUNOLOŠKI ZNAČAJ DOJENJA",
        "Prednosti za bebu, majku i kreiranje emocionalne sigurnosti"
    )
    
    cards = [
        ("1. KOLOSTRUM: PRVA VAKCINA NOVOROĐENČETA", C_GOLD, [
            ("Zlatne kapi imuniteta:", "Gusto žuto mleko prvih 3-5 dana; bogato sekretornim IgA antitelima."),
            ("Zaštita crevne barijere:", "Laktoferin i lizozim štite novorođenče od patogena i kolonizuju mikrobiom."),
            ("Fiziološki laksativ:", "Olakšava izbacivanje mekonijuma i smanjuje rizik od novorođenačke žutice.")
        ]),
        ("2. DINAMIČKI NUTRITIVNI SASTAV ZRELOG MLEKA", C_TERRA, [
            ("Prilagođeno potrebama:", "Sastav se menja tokom jednog podoja, u toku dana i kako beba raste."),
            ("Optimalan odnos proteina:", "Surutka i kazein (60:40) pružaju maksimalnu svarljivost bez opterećenja bubrega."),
            ("Mozak i vid:", "DHA i esencijalne masne kiseline podstiču ubrzani razvoj sinapsi i kognicije.")
        ]),
        ("3. ZDRAVLJE MAJKE I EMOCIONALNA POVEZANOST", C_SAGE, [
            ("Involucija materice:", "Sisanje stimuliše oksitocin koji smanjuje postporođajno krvarenje."),
            ("Dugoročna prevencija:", "Dokazano smanjuje rizik od karcinoma dojke, jajnika i osteoporoze."),
            ("Koža-na-kožu kontakt:", "Stabilizuje puls, disanje i temperaturu bebe i podstiče osećaj sigurnosti.")
        ])
    ]
    
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=52)
        
        item_y = y + 84
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, line_gap=34)
            item_y += 76
        y += 352
        
    # Gold standard footer
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[PREPORUKA SZO I PEDIJATRIJSKIH UDRUŽENJA]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1320, "EKSKLUZIVNO DOJENJE PRVIH 6 MESECI ŽIVOTA", C_LINEN)
    draw.text((W//2, 1386), "Majčino mleko obezbeđuje sve nutrijente i tečnost bez potrebe za dodavanjem vode.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide11_breastfeeding_benefits.png"), "PNG", optimize=True)
    print("Saved slide11_breastfeeding_benefits.png")

# -------------------------------------------------------------
# SLIDE 12: HIGIJENA I NEGA DOJKI TOKOM LAKTACIJE
# -------------------------------------------------------------
def make_slide12():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 2: DOJENJE I LAKTACIJA",
        "HIGIJENA I NEGA DOJKI TOKOM LAKTACIJE",
        "Očuvanje hidrolipidnog sloja i zaštita bradavica od infekcija"
    )
    
    cards = [
        ("1. ZLATNA PRAVILA SVAKODNEVNE HIGIJENE", C_DARK, [
            ("Pranje samo toplom vodom:", "Dojke prati isključivo vodom pod tušem jednom dnevno."),
            ("Stroga zabrana sapuna i alkohola:", "Sapun, šamponi i alkohol uništavaju prirodnu zaštitu i isušuju kožu."),
            ("Montgomeryjeve žlezde:", "Kvržice na areoli luče prirodni uljani baktericidni film koji se ne sme spirati.")
        ]),
        ("2. NEGA NAKON PODOJA (LANOLIN I MLEKO)", C_TERRA, [
            ("Kapi majčinog mleka:", "Nakon podoja istisnuti kap mleka, razmazati po bradavici i ostaviti da se osuši."),
            ("100% medicinski čist lanolin:", "Naneti tanak sloj lanolina nakon podoja; štiti vlagu i ne mora se spirati."),
            ("Suvo i čisto okruženje:", "Izbegavati vlažnu sredinu koja pogoduje razvoju gljivica (kandida).")
        ]),
        ("3. TUFERI ZA DOJENJE I PROVETRAVANJE", C_SAGE, [
            ("Pamučni prozračni tuferi:", "Koristiti mekane pamučne tufere bez plastičnih nepropusnih folija."),
            ("Redovna zamena tufera:", "Menjati tufer čim postane vlažan kako bi bradavica uvek bila suva."),
            ("Vazdušne kupke:", "Ostaviti dojke izložene sobnom vazduhu 10 do 15 minuta nakon svakog podoja.")
        ])
    ]
    
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=52)
        
        item_y = y + 84
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, line_gap=34)
            item_y += 76
        y += 352
        
    # Bottom caution
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[PRAVILO PEDIJATRIJSKE NEGE]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1320, "NE BRISATI I NE RIBATI BRADAVICE PRE PODOJA!", C_LINEN)
    draw.text((W//2, 1386), "Prečesto pranje i brisanje uklanja prirodne lipide i stvara bolne mikropukotine.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide12_breast_hygiene.png"), "PNG", optimize=True)
    print("Saved slide12_breast_hygiene.png")

# -------------------------------------------------------------
# SLIDE 22: ŠETNJA I BORAVAK NA SVEŽEM VAZDUHU
# -------------------------------------------------------------
def make_slide22():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 3: NEGA I RAZVOJ ODOJČETA",
        "ŠETNJA I BORAVAK NA SVEŽEM VAZDUHU",
        "Klimatski uslovi, oprema kolica i adaptacija odojčeta"
    )
    
    cards = [
        ("1. VREMENSKI I TEMPERATURNI PRAG", C_TERRA, [
            ("Temperaturni raspon:", "Optimalno od 0°C do 28°C; Izbegavati izlazak ispod -5°C i preko 30°C."),
            ("Izbegavanje ekstremnih faktora:", "Ne šetati po jakom vetru, gustoj magli, jakom pljusku ili smogu."),
            ("Letnji i zimski tajming:", "Leti šetati rano ujutru ili predveče; zimi u najtoplijem delu dana (11h–14h).")
        ]),
        ("2. OPREMA KOLICA I POLOŽAJ ODOJČETA", C_SAGE, [
            ("Ravan položaj (Ravna korpa):", "Prvih 5-6 meseci beba boravi isključivo na ravnom dušeku korpe kolica."),
            ("Zaštita od sunca i UV zraka:", "Koristiti suncobran ili pokretnu tendu; beba do 6 meseci se ne izlaže suncu."),
            ("SMART upozorenje:", "Nikada ne prekrivati otvor kolica pelenom! To stvara opasan efekt staklene bašte.")
        ]),
        ("3. TRAJANJE I DINAMIKA ŠETNJI", C_DARK, [
            ("Prva šetnja:", "Nakon 2 do 3 nedelje po otpustu; početi sa 15-20 minuta na terasi ili dvorištu."),
            ("Postepeno produžavanje:", "Svakog dana produžavati za 10 minuta do standardnih 1 do 2 sata dnevno."),
            ("Slojevito oblačenje:", "Pravilo +1 sloj u odnosu na odraslu osobu; proveravati toplotu na potiljku.")
        ])
    ]
    
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=52)
        
        item_y = y + 84
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, line_gap=34)
            item_y += 76
        y += 352
        
    # Critical Safety Warning
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_ALERT_BG, outline=C_RED, width=2)
    draw.text((W//2, 1262), "[OPASNOST OD PREGREVANJA]", fill=C_RED, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1320, "NE PREKRIVATI KOLICA PELENOM ILI DEKOM!", C_DARK)
    draw.text((W//2, 1386), "Temperatura unutar pokrivenih kolica raste i do 15°C za samo 20 minuta.", fill=C_TERRA, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide22_outdoor_stroller.png"), "PNG", optimize=True)
    print("Saved slide22_outdoor_stroller.png")

# -------------------------------------------------------------
# SLIDE 23: NEMLEČNA DOHRANA (UVOĐENJE ČVRSTE HRANE)
# -------------------------------------------------------------
def make_slide23():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 3: NEGA I RAZVOJ ODOJČETA",
        "UVOĐENJE ČVRSTE HRANE (NEMLEČNA DOHRANA)",
        "Optimalni tajming, redosled namirnica i pravilo 3 dana"
    )
    
    cards = [
        ("1. ZNAKOVI ZRELOSTI ZA NEMLEČNU DOHRANU", C_TERRA, [
            ("Optimalni uzrast:", "Između navršenih 4 i 6 meseci (po preporuci pedijatra, ne pre 17. nedelje)."),
            ("Motorni preduslovi:", "Beba stabilno drži glavu, sedi uz blagu podršku i nestaje refleks guranja jezikom."),
            ("Ponašajni signali:", "Pokazuje izrazito interesovanje za hranu roditelja, otvara usta na kašičicu.")
        ]),
        ("2. PRAVILO 3 DANA ZA NOVE NAMIRNICE", C_SAGE, [
            ("Pojedinačno uvođenje:", "Uvek uvoditi samo jednu novu namirnicu u jutarnjim ili prepodnevnim satima."),
            ("Praćenje reakcija (3 dana):", "Ista namirnica se daje 3 uzastopna dana radi uočavanja osipa, grčeva ili proliva."),
            ("Postepena količina:", "Početi sa 1-2 kafene kašičice, pa postepeno povećavati do punog obroka.")
        ]),
        ("3. REDOSLED UVOĐENJA GRUPA NAMIRNICA", C_DARK, [
            ("1. Blago povrće:", "Tikvica, bundeva, šargarepa, krompir, paškanat (kuvano i pasirano)."),
            ("2. Žitarice bez glutena:", "Pirinač, proso, kukuruz (palenta) – mešano sa majčinim ili adaptiranim mlekom."),
            ("3. Voće i meso:", "Jabuka, kruška, banana; zatim mlado nemasno meso (ćuretina, piletina, teletina).")
        ])
    ]
    
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=52)
        
        item_y = y + 84
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, line_gap=34)
            item_y += 76
        y += 352
        
    # Strictly prohibited foods
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_ALERT_BG, outline=C_RED, width=2)
    draw.text((W//2, 1262), "[STROGE ZABRANE PRE NAVRŠENE 1. GODINE]", fill=C_RED, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1320, "BEZ SOLI, ŠEĆERA, MEDA I KRAVLJEG MLEKA!", C_DARK)
    draw.text((W//2, 1386), "Med nosi rizik od botulizma; so opterećuje bubrege; šećer stvara nezdrave navike.", fill=C_TERRA, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide23_solid_food_weaning.png"), "PNG", optimize=True)
    print("Saved slide23_solid_food_weaning.png")

# -------------------------------------------------------------
# SLIDE 28: PELENSKI OSIP I PROMENE NA KOŽI
# -------------------------------------------------------------
def make_slide28():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "PELENSKI OSIP I PROMENE NA KOŽI",
        "ABCDE protokol prevencije i nega dermatitisa kod odojčadi"
    )
    
    cards = [
        ("1. ZLATNI 'ABCDE' PROTOKOL ZA PELENSKU REGIJU", C_TERRA, [
            ("A - Air (Vazduh):", "Ostaviti bebu bez pelene što češće kako bi se koža prirodno sušila na vazduhu."),
            ("B - Barrier (Zaštita):", "Zaštitna krema na bazi cink-oksida pravi barijeru protiv amonijaka i stolice."),
            ("C - Cleansing (Čišćenje):", "Prati mlakom tekućom vodom; vlažne maramice svesti na minimum i bez mirisa."),
            ("D - Diaper (Pelena):", "Menjati pelenu odmah nakon defekacije, a mokru na svaka 2 do 3 sata."),
            ("E - Education (Edukacija):", "Ne trljati kožu frotirskim peškirom već je nežno tapkati.")
        ]),
        ("2. TEMENJAČA I TOPLOTNI OSIP (MILIARIA)", C_SAGE, [
            ("Temenjača (Seboreja):", "Umasirati toplo bademovo ulje 30 min pre kupanja, zatim nežno češljati mekom četkom."),
            ("Toplotni osip (Miliaria):", "Sitne crvene tačkice od pretopljavanja; rashladiti sobu i obući tanji pamuk.")
        ]),
        ("3. KADA JE POTREBAN PREGLED PEDIJATRA?", C_RED, [
            ("Sumnja na kandidijazu:", "Žarko crvenilo u pregibima sa sitnim tačkastim satelitima (zahteva antimikotik)."),
            ("Komplikacije:", "Pojava ranica, plikova, gnojnih bubuljica ili ako osip ne prolazi nakon 3 dana.")
        ])
    ]
    
    # First card is taller
    y = 155
    draw.rounded_rectangle([(35, y), (W-35, y + 430)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
    draw_badge(draw, 55, y + 16, cards[0][0], F_CARD_TITLE, cards[0][1], C_CARD, height=50)
    item_y = y + 78
    for lbl, desc in cards[0][2]:
        draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, line_gap=32)
        item_y += 70
    
    y = 605
    for title, col, items in cards[1:]:
        draw.rounded_rectangle([(35, y), (W-35, y + 295)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 16, title, F_CARD_TITLE, col, C_CARD, height=50)
        item_y = y + 78
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, line_gap=32)
            item_y += 70
        y += 315
        
    # Emergency notice
    draw.rounded_rectangle([(35, 1240), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1276), "[ZLATNO PRAVILO ZA NEGU KOŽE]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1332, "SUVA I ČISTA KOŽA JE NAJBOLJA PREVENCIJA OSIPA", C_LINEN)
    draw.text((W//2, 1395), "Kremu nanositi u tankom sloju samo na potpuno suvu kožu.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide28_skin_diaper_rash.png"), "PNG", optimize=True)
    print("Saved slide28_skin_diaper_rash.png")

# -------------------------------------------------------------
# SLIDE 40: DNEVNIK NEGE, DISKRECIJA I ETIČKI KODEKS
# -------------------------------------------------------------
def make_slide40():
    img, draw = create_base_canvas(
        "ROYAL NANNY AKADEMIJA • ZAVRŠNI STANDARDI",
        "DNEVNIK NEGE, DISKRECIJA I ETIČKI KODEKS",
        "Najviši standardi diskrecije, medicinske dokumentacije i poverenja"
    )
    
    cards = [
        ("1. STANDARDIZOVANI DNEVNIK DNEVNE NEGE", C_DARK, [
            ("Evidencija ishrane:", "Tačno vreme svakog podoja/obroka, trajanje po dojci ili uneta mililitraža formule."),
            ("Fiziološke funkcije:", "Broj i izgled mokrih pelena i stolice (boja, konzistencija, promena ritma)."),
            ("Ritmovi sna i temperatura:", "Dnevni i noćni intervali spavanja; beleženje izmerene telesne temperature.")
        ]),
        ("2. APSOLUTNA DISKRECIJA I POVERLJIVOST (NDA)", C_TERRA, [
            ("Zaštita privatnosti doma:", "Sve informacije o porodici, domu i navikama predstavljaju strogu poslovnu tajnu."),
            ("Zabrana fotografisanja:", "Apsolutno je zabranjeno fotografisanje deteta, doma i deljenje na društvenim mrežama."),
            ("Pravna odgovornost:", "Potpisani ugovor o poverljivosti (NDA) štiti integritet i bezbednost klijenta.")
        ]),
        ("3. PROTOKOL PREDAJE SMENE I HITNA KOMUNIKACIJA", C_SAGE, [
            ("Strukturirana predaja smene:", "Pismeni izveštaj i usmeni brifing roditeljima ili koleginici na kraju smene."),
            ("Evidencija lekova:", "Tačno uneta doza, naziv sirupa i minut kada je lek dat uz potpis nani."),
            ("Lista hitnih kontakata:", "Pedijatar, dežurna klinika i roditelji uvek na vrhu dnevnika nege.")
        ])
    ]
    
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=52)
        
        item_y = y + 84
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, line_gap=34)
            item_y += 76
        y += 352
        
    # Gold pledge
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[ZLATNI ZAVET ROYAL NANNY PROFESIONALACA]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1320, "POVERENJE, DISKRECIJA I BEZUSLOVNA SIGURNOST DETETA", C_LINEN)
    draw.text((W//2, 1386), "Vrhunska stručnost u kombinaciji sa tihim luksuzom i poštovanjem porodičnog doma.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide40_ethics_care_journal.png"), "PNG", optimize=True)
    print("Saved slide40_ethics_care_journal.png")

if __name__ == "__main__":
    make_slide02()
    make_slide07()
    make_slide11()
    make_slide12()
    make_slide22()
    make_slide23()
    make_slide28()
    make_slide40()
    print("ALL 8 NEW BESPOKE INFOGRAPHICS GENERATED SUCCESSFULLY!")
