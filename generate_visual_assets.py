#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generiše visokokvalitetne pedijatrijske i kliničke infografike za Royal Nanny prezentaciju.
Svaka infografika koristi Royal Nanny paletu boja (Espresso, Sand, Cognac, Linen, Gold, Sage)
i sadrži precizne medicinske i edukativne protokole sa krupnim, jasnim i čitkim fontovima.
Optimizovano za maksimalnu veličinu i čitljivost segmenata.
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
        f_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", 46)
        f_serif = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 32)
        f_badge = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 23)
        f_card_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", 34)
        f_bold = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 31)
        f_body = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 27)
        f_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 23)
    except Exception:
        f_title = f_serif = f_badge = f_card_title = f_bold = f_body = f_small = ImageFont.load_default()
    return f_title, f_serif, f_badge, f_card_title, f_bold, f_body, f_small

F_TITLE, F_SERIF, F_BADGE, F_CARD_TITLE, F_BOLD, F_BODY, F_SMALL = get_fonts()

def create_base_canvas(badge_text, title_text, subtitle_text):
    img = Image.new("RGB", (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    
    # Header badge sa dinamičkom širinom - na samom vrhu
    bbox_b = draw.textbbox((0, 0), badge_text.upper(), font=F_BADGE)
    bw = (bbox_b[2] - bbox_b[0]) + 44
    draw.rounded_rectangle([(W//2 - bw//2, 16), (W//2 + bw//2, 64)], radius=8, fill=C_DARK)
    draw.text((W//2, 40), badge_text.upper(), fill=C_LINEN, font=F_BADGE, anchor="mm")
    
    # Main title with auto-fit width
    bbox = draw.textbbox((0, 0), title_text, font=F_TITLE)
    t_width = bbox[2] - bbox[0]
    if t_width > 1100:
        f_title_use = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", 35)
    else:
        f_title_use = F_TITLE
        
    draw.text((W//2, 92), title_text, fill=C_DARK, font=f_title_use, anchor="mm")
    
    # Subtitle with auto-fit width
    if subtitle_text:
        s_box = draw.textbbox((0, 0), subtitle_text, font=F_SERIF)
        s_w = s_box[2] - s_box[0]
        if s_w > 1080:
            f_sub_use = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 25)
        else:
            f_sub_use = F_SERIF
        draw.text((W//2, 132), subtitle_text, fill=C_TERRA, font=f_sub_use, anchor="mm")
        
    return img, draw

def draw_badge(draw, x, y, text, font, fill_color, text_color, radius=8, padding_x=34, height=54):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = (bbox[2] - bbox[0]) + padding_x
    draw.rounded_rectangle([(x, y), (x + w, y + height)], radius=radius, fill=fill_color)
    draw.text((x + padding_x // 2, y + height // 2), text, fill=text_color, font=font, anchor="lm")
    return x + w

def draw_item(draw, x, y, label, desc, font_lbl=F_BOLD, font_desc=F_BODY, col_lbl=C_DARK, col_desc=C_DARK, max_w=1040, line_gap=36):
    draw.text((x, y), label, fill=col_lbl, font=font_lbl)
    cur_y = y + line_gap
    draw.text((x, cur_y), desc, fill=col_desc, font=font_desc)
    return cur_y + 30

def draw_banner_title(draw, y, text, fill_color, max_width=1040, default_font=F_CARD_TITLE):
    bbox = draw.textbbox((0, 0), text, font=default_font)
    w = bbox[2] - bbox[0]
    if w > max_width:
        scale = max_width / w
        new_size = max(18, int(34 * scale))
        font_use = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", new_size)
    else:
        font_use = default_font
    draw.text((W//2, y), text, fill=fill_color, font=font_use, anchor="mm")

# -------------------------------------------------------------
# SLIDE 05: KUPANJE NOVOROĐENČETA - PRIPREMA STANICE
# -------------------------------------------------------------
def make_slide05():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 1: HIGIJENA I NEGA NOVOROĐENČETA",
        "STANICA ZA KUPANJE: PRIPREMA PRE SVLAČENJA",
        "Zlatni standard: Sve je na dohvat ruke pre nego što se beba svuče"
    )
    
    cards = [
        ("1. KADICA I VODA NA TAČNO 37°C", C_TERRA, [
            ("Optimalna temperatura vode:", "Tačno 36.5°C – 37°C (provereno vodenim termometrom)."),
            ("Visina vode u kadici:", "Za novorođenče samo 5 do 8 cm (do visine kukova)."),
            ("Test laktom/podlakticom:", "Uvek izvršiti dvostruku proveru pre spuštanja bebe.")
        ]),
        ("2. MIKROKLIMA PROSTORIJE (24°C – 26°C)", C_SAGE, [
            ("Temperatura kupatila/sobe:", "Zagrejati prostoriju na 24°C do 26°C."),
            ("Apsolutno bez promaje:", "Zatvoriti prozore i vrata minimum 15 minuta pre početka."),
            ("Topla podloga:", "Frotirski peškir i pelena položeni preko stola za prepovijanje.")
        ]),
        ("3. STERILNI I NEGUJUĆI MATERIJALI", C_DARK, [
            ("Medicinski sindet:", "pH neutralan (5.5), bez sapuna, alkohola i sulfata."),
            ("Sterilne komprese i fiziološki:", "Pripremljene za toaletu očiju i pupčanika."),
            ("Čista odeća i pelena:", "Bodi od organskog pamuka otkopčan i spreman za oblačenje.")
        ]),
    ]
    
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        
        item_y = y + 88
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            item_y += 76
        y += 352
        
    # Bottom warning
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[KRITIČNO PRAVILO BEZBEDNOSTI]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "BEBA SE NIKADA, NI NA SEKUND, NE OSTAVLJA SAMA!", C_LINEN)
    draw.text((W//2, 1386), "Ukoliko zazvoni telefon: beba se umotava u peškir i nosi sa sobom.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide05_bath_prep_station.png"), "PNG", optimize=True)
    print("Saved slide05_bath_prep_station.png")

# -------------------------------------------------------------
# SLIDE 08: OBRADA PUPČANIKA I PUPČANE RANE
# -------------------------------------------------------------
def make_slide08():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 1: NEGA PUPČANIKA I PUPČANE RANE",
        "OBRADA PUPČANIKA I PUPČANE RANE",
        "Zlatni standard suve nege pupka i rano uočavanje infekcije"
    )
    
    # Card 1: Protokol obrade
    draw.rounded_rectangle([(35, 160), (W-35, 790)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
    draw_badge(draw, 55, 180, "PROTOKOL DNEVNE SUVE OBRADE", F_CARD_TITLE, C_DARK, C_LINEN, height=54)
    
    steps = [
        ("1. Aseptična priprema:", "Pranje ruku toplom vodom i sapunom + dezinfekcija pre dodira rane."),
        ("2. Skidanje gaze i antiseptik:", "Pažljivo skidanje gaze bez cimanja štipaljke; prskanje Oktenisepta."),
        ("3. Čišćenje korena i sušenje:", "Bazu očistiti sterilnom gazom jednim potezom i ostaviti da se osuši."),
        ("4. Zaštita i rub pelene:", "Suva sterilna gaza i flaster; pelenu obavezno saviti ispod pupka.")
    ]
    
    sy = 270
    for s_title, s_desc in steps:
        draw_item(draw, 65, sy, s_title, s_desc, F_BOLD, F_BODY, C_TERRA, C_DARK, max_w=1040, line_gap=36)
        sy += 122
        
    # Card 2: Znakovi za uzbunu
    draw.rounded_rectangle([(35, 825), (W-35, 1465)], radius=14, fill=C_ALERT_BG, outline=C_RED, width=1)
    draw_badge(draw, 55, 845, "ZNAKOVI ZA UZBUNU (CRVENI ALARM)", F_CARD_TITLE, C_RED, C_CARD, height=54)
    
    alarms = [
        ("Crvenilo i otok kože oko pupka:", "Znak širenja infekcije na trbušni zid (omfalitis)."),
        ("Sekrecija i neprijatan miris:", "Gnojan, zamućen iscedak neprijatnog mirisa."),
        ("Aktivno krvarenje:", "Obilnije vlaženje ili pulsirajuće kapljanje krvi iz rane."),
        ("Opšte stanje i temperatura:", "Febrilnost, odbijanje hrane ili izražena letargija bebe.")
    ]
    
    ay = 935
    for a_title, a_desc in alarms:
        draw_item(draw, 65, ay, f"! {a_title}", f"  {a_desc}", F_BOLD, F_BODY, C_RED, C_DARK, max_w=1040, line_gap=36)
        ay += 126
        
    img.save(os.path.join(ASSETS_DIR, "slide08_umbilical_cord_care.png"), "PNG", optimize=True)
    print("Saved slide08_umbilical_cord_care.png")

# -------------------------------------------------------------
# SLIDE 11: BEZBEDNI POLOŽAJI NOŠENJA I PROTOKOL SPAVANJA (SIDS)
# -------------------------------------------------------------
def make_slide11():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 1: HIGIJENA I NEGA NOVOROĐENČETA",
        "BEZBEDNI POLOŽAJI I PROTOKOL SPAVANJA",
        "Biomehanika nošenja, prevencija aspiracije i zlatni standardi SIDS zaštite"
    )
    
    cards = [
        ("1. POLOŽAJI PRI NOŠENJU I HRANJENJU", C_TERRA, [
            ("Stabilna potpora za glavu i kičmu:", "Glava novorođenčeta ima čvrst oslonac na podlaktici; kičma prati 'C' luk."),
            ("Položaj 'tigar na drvetu':", "Beba leži potrbuške duž podlaktice sa glavom u lakatnom prevoju (olakšava gasove)."),
            ("Ugao od 30–45° pri hranjenju:", "Uspravnije uzglavlje sprečava ulazak tečnosti u Eustahijevu tubu i gušenje.")
        ]),
        ("2. ZLATNI STANDARD BEZBEDNOG SPAVANJA", C_SAGE, [
            ("Spavanje ISKLJUČIVO na leđima:", "Zlatno pravilo tokom cele prve godine života na ravnoj i čvrstoj podlozi."),
            ("Zabrana bočnog i potrbušnog položaja:", "Bočni položaj je nestabilan i nosi visok rizik od prevrtanja na stomak."),
            ("Prazan krevetac i namenska vreća:", "Strogo bez jastuka, debelih jorgana, pozicionera i plišanih ogradica!")
        ]),
        ("3. ROOM-SHARING I MIKROKLIMA", C_DARK, [
            ("Zaseban krevetac pored roditelja:", "Zajednička soba prvih 6 meseci bez deljenja kreveta (bed-sharing rizik)."),
            ("Optimalna temperatura sobe (20–22°C):", "Pretopljavanje bebe dokazano povećava rizik od sindroma iznenadne smrti."),
            ("Podrigivanje nakon svakog obroka:", "Vertikalno držanje 10–15 minuta pre spuštanja u krevetac na spavanje.")
        ]),
    ]
    
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        
        item_y = y + 88
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            item_y += 76
        y += 352
        
    # Bottom warning
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[ZLATNO PRAVILO BEZBEDNOG KREVETCA]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "ČIST, RAVAN I PRAZAN KREVETAC SPASAVA ŽIVOT BEBE!", C_LINEN)
    draw.text((W//2, 1386), "Dete uvek spava na leđima u svojoj namenskoj vreći bez igračaka i jastučića.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide11_safe_sleep_carrying.png"), "PNG", optimize=True)
    print("Saved slide11_safe_sleep_carrying.png")

# -------------------------------------------------------------
# SLIDE 12: POLOŽAJI PRI DOJENJU I ASIMETRIČNI HVAT
# -------------------------------------------------------------
def make_slide12():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 2: DOJENJE",
        "POLOŽAJI PRI DOJENJU I ASIMETRIČNI HVAT",
        "Biomehanika pravilnog podoja bez bola i ragada"
    )
    
    # Card 1: 3 Ključna položaja
    draw.rounded_rectangle([(35, 160), (W-35, 790)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
    draw_badge(draw, 55, 180, "3 ERGONOMSKA POLOŽAJA", F_CARD_TITLE, C_DARK, C_LINEN, height=54)
    
    pos = [
        ("1. Kolevka (Cradle / Cross-cradle):", "Beba leži na boku, stomak na stomak sa majkom. Glava u ravni sa kičmom."),
        ("2. Fudbalska lopta (Football Hold):", "Beba ispod pazuha majke. Idealno nakon carskog reza i za kontrolu glavice."),
        ("3. Bočni ležeći položaj (Side-lying):", "Majka i beba leže jedno naspram drugog. Savršeno za noćne podoje i odmor."),
        ("Ključno poravnanje:", "Uho, rame i kuk bebe MORAJU biti u istoj ravnoj liniji (beba ne sme okretati vrat)!")
    ]
    
    py = 270
    for p_title, p_desc in pos:
        draw_item(draw, 65, py, p_title, p_desc, F_BOLD, F_BODY, C_TERRA, C_DARK, max_w=1040, line_gap=36)
        py += 122
        
    # Card 2: Zlatni standard asimetričnog hvata
    draw.rounded_rectangle([(35, 825), (W-35, 1465)], radius=14, fill=C_CARD, outline=C_SAGE, width=1)
    draw_badge(draw, 55, 845, "ZLATNI STANDARD ASIMETRIČNOG HVATA", F_CARD_TITLE, C_SAGE, C_CARD, height=54)
    
    latch = [
        ("Širok ugao otvaranja usta:", "Usta otvorena preko 140° (kao pri zevanju) pre prinošenja dojci."),
        ("Brada duboko u tkivu dojke:", "Bebina brada prva dodiruje dojku, stimulišući refleks sisanja."),
        ("Nos potpuno slobodan:", "Zahvaljujući zabačenoj glavi, nosić je odvojen od dojke i beba nesmetano diše."),
        ("Izvrnute usne ('usne ribice'):", "I gornja i donja usna izvrnute upolje, pokrivajući veći deo donje areole."),
        ("Zvuk gutanja, bez coktanja:", "Čuje se ritmično gutanje (uh-uh). Coktanje znači gubitak vakuuma!")
    ]
    
    ly = 930
    for l_title, l_desc in latch:
        draw_item(draw, 65, ly, f"• {l_title}", f"   {l_desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
        ly += 102
        
    img.save(os.path.join(ASSETS_DIR, "slide12_breastfeeding_positions.png"), "PNG", optimize=True)
    print("Saved slide12_breastfeeding_positions.png")

# -------------------------------------------------------------
# SLIDE 13: IZAZOVI U LAKTACIJI (RAGADE, PREPUNJENOST, MASTITIS)
# -------------------------------------------------------------
def make_slide13():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 2: DOJENJE",
        "IZAZOVI U LAKTACIJI: PROTOKOL TRIJAŽE",
        "Efikasno olakšavanje tegoba i razlikovanje prepunjenosti od mastitisa"
    )
    
    challenges = [
        ("1. RAGADE (Bolne i ispucale bradavice)", C_TERRA, [
            ("Glavni uzrok:", "Nepravilan, plitak hvat bradavice (beba sisa samo vrh umesto areole)."),
            ("Tretman:", "100% prečišćeni medicinski lanolin (ne mora se ispirati pre podoja)."),
            ("Prirodni lek:", "Premazivanje bradavice kapljicom sopstvenog mleka i sušenje na vazduhu.")
        ]),
        ("2. PREPUNJENOST DOJKI (Engorgement)", C_SAGE, [
            ("Tople obloge PRE podoja:", "Zagrevanje 5-10 min i nežna masaža olakšavaju refleks otpuštanja mleka."),
            ("Iztiskivanje par kapi:", "Omekšati areolu pre podoja kako bi beba lakše uhvatila dojku."),
            ("Hladne obloge POSLE podoja:", "Hladan peškir ili obloge od kupusa 15 min za smanjenje otoka i bola.")
        ]),
        ("3. MASTITIS (Bakterijska infekcija dojke)", C_RED, [
            ("Simptomi:", "Ograničeni crveni trougao, vruća i tvrda dojka, jeza, T > 38.5°C."),
            ("Kritično pravilo:", "DOJENJE SE NE PREKIDA! Redovno pražnjenje dojke je ključ izlečenja."),
            ("Hitan korak:", "Obaveštavanje izabranog ginekologa/pedijatra radi propisivanja antibiotika.")
        ]),
    ]
    
    y = 160
    for title, col, items in challenges:
        draw.rounded_rectangle([(35, y), (W-35, y + 405)], radius=14, fill=C_CARD, outline=col, width=1)
        draw_badge(draw, 55, y + 20, title, F_CARD_TITLE, col, C_CARD, height=54)
        
        iy = y + 96
        for lbl, desc in items:
            draw_item(draw, 65, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            iy += 96
        y += 430
    
    img.save(os.path.join(ASSETS_DIR, "slide13_lactation_challenges.png"), "PNG", optimize=True)
    print("Saved slide13_lactation_challenges.png")

# -------------------------------------------------------------
# SLIDE 14: SKLADIŠTENJE MAJČINOG MLEKA
# -------------------------------------------------------------
def make_slide14():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 2: DOJENJE",
        "SKLADIŠTENJE MAJČINOG MLEKA: PRAVILO 4-4-6",
        "Očuvanje nutritivnih i imunoloških svojstava izmlazanog mleka"
    )
    
    rules = [
        ("SOBNA TEMPERATURA (do 25°C)", "DO 4 SATA", C_TERRA,
         "Držati na najhladnijem mestu u sobi, zaštićeno od direktnog sunčevog svetla i izvora toplote."),
        ("FRIŽIDER (na polici na 4°C)", "3 DO 5 DANA", C_SAGE,
         "Čuvati u dubini frižidera (nikada u vratima zbog temperaturnih oscilacija pri otvaranju)."),
        ("ZAMRZIVAČ (-18°C)", "3 DO 6 MESECI", C_DARK,
         "U namenskim sterilnim kesicama za mleko sa označenim datumom, satom i zapreminom.")
    ]
    
    y = 160
    for title, duration, col, desc in rules:
        draw.rounded_rectangle([(35, y), (W-35, y + 295)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        
        bbox_d = draw.textbbox((0, 0), duration, font=F_CARD_TITLE)
        dw = (bbox_d[2] - bbox_d[0]) + 34
        draw.rounded_rectangle([(W - 55 - dw, y + 18), (W - 55, y + 72)], radius=8, fill=C_GOLD)
        draw.text((W - 55 - dw//2, y + 45), duration, fill=C_DARK, font=F_CARD_TITLE, anchor="mm")
        
        draw.text((65, y + 98), desc, fill=C_DARK, font=F_BODY)
        draw.text((65, y + 160), "• Posude: Isključivo staklene flašice bez BPA ili sterilne kesice za zamrzivač.", fill=C_TERRA, font=F_BOLD)
        draw.text((65, y + 218), "• Obeležavanje: Uvek prvo trošiti najstarije izmlazano mleko (FIFO princip).", fill=C_DARK, font=F_BODY)
        y += 316
        
    # Bottom warning
    draw.rounded_rectangle([(35, 1125), (W-35, 1465)], radius=12, fill=C_ALERT_BG, outline=C_RED, width=1)
    draw_badge(draw, 55, 1145, "PRAVILA ODMRZAVANJA I ZABRANE", F_CARD_TITLE, C_RED, C_CARD, height=54)
    
    thaw = [
        ("Odmrzavanje:", "Polako u frižideru preko noći ili u posudi sa toplom vodom (do 37°C)."),
        ("STROGA ZABRANA MIKROTALASNE:", "Uništava antitela i vitamine i stvara 'vruće tačke' koje mogu opeći bebu!"),
        ("ZABRANA PONOVNOG ZAMRZAVANJA:", "Jednom odmrznuto mleko se mora iskoristiti u roku od 24h ili baciti.")
    ]
    ty = 1220
    for t_lbl, t_txt in thaw:
        draw_item(draw, 65, ty, f"• {t_lbl}", f"   {t_txt}", F_BOLD, F_BODY, C_RED, C_DARK, max_w=1040, line_gap=36)
        ty += 78
        
    img.save(os.path.join(ASSETS_DIR, "slide14_milk_storage_protocol.png"), "PNG", optimize=True)
    print("Saved slide14_milk_storage_protocol.png")

# -------------------------------------------------------------
# SLIDE 15: ADAPTIRANA FORMULA - PRIPREMA I HIGIJENA
# -------------------------------------------------------------
def make_slide15():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 2: DOJENJE",
        "ADAPTIRANA MLEČNA FORMULA: STERILNA PRIPREMA",
        "Sigurnost pripreme i prevencija bakterijskih infekcija"
    )
    
    steps = [
        ("1. STERILIZACIJA PRIBORA", C_DARK, [
            ("Parni sterilizator ili otkuvavanje:", "Flašice, cucle, zatvarači i merice moraju biti sterilni."),
            ("Sušenje na čistom stalku:", "Ne brisati pribor kuhinjskim krpama (izvor bakterija).")
        ]),
        ("2. PROKUVAVANJE VODE", C_TERRA, [
            ("Voda vri 3-5 minuta:", "Uništava potencijalne mikroorganizme."),
            ("Hlađenje na 40°C – 50°C:", "Prevruća voda uništava probiotike i vitamine u formuli, hladna se ne rastvara.")
        ]),
        ("3. TAČNA RAZMERA MERICA", C_SAGE, [
            ("Prvo voda, zatim prah:", "Sprečava zgrušavanje i omogućava tačno očitavanje mililitraže."),
            ("Isključivo RAVNE merice:", "Poravnati nožem bez sabijanja. Višak praha opterećuje bubrege bebe!")
        ]),
        ("4. PROVERA TEMPERATURE I VREME", C_RED, [
            ("Test na podlaktici:", "2-3 kapi na unutrašnju stranu ručnog zgloba (mora biti prijatno toplo, ne vrelo)."),
            ("Pravilo 1 sata:", "Preostalo mleko iz flašice se BACA nakon 60 minuta od početka hranjenja!")
        ]),
    ]
    
    y = 160
    for title, col, items in steps:
        draw.rounded_rectangle([(35, y), (W-35, y + 300)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=52)
        
        iy = y + 88
        for lbl, desc in items:
            draw_item(draw, 65, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            iy += 92
        y += 324
        
    img.save(os.path.join(ASSETS_DIR, "slide15_formula_prep_protocol.png"), "PNG", optimize=True)
    print("Saved slide15_formula_prep_protocol.png")

# -------------------------------------------------------------
# SLIDE 19: DENTICIJA, ORALNA HIGIJENA I HIDRACIJA
# -------------------------------------------------------------
def make_slide19():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 3: NEGA ODOJČETA",
        "DENTICIJA, ORALNA HIGIJENA I HIDRACIJA",
        "Nicanje zubića, nega desni i uvođenje vode uz nemlečnu dohranu"
    )
    
    cards = [
        ("1. SIMPTOMI NICANJA ZUBIĆA I OLAKŠAVANJE", C_TERRA, [
            ("Tipični znaci (4–8. mesec):", "Pojačana salivacija (balavljenje), otečene desni, griženje predmeta i nemir."),
            ("Hlađene silikonske glodalice:", "Držati isključivo u frižideru (NIKADA u zamrzivaču jer led oštećuje desni!)."),
            ("Masaža desni sterilnom gazom:", "Nežna masaža čistim prstom obmotanim vlažnom gazom ublažava pritisak.")
        ]),
        ("2. ORALNA HIGIJENA I PREVENCIJA KARIJESA", C_SAGE, [
            ("Toaleta pre nicanja zubića:", "Svakodnevno prebrisavanje desni i jezika vlažnom gazom nakon večere."),
            ("Pranje prvih zubića:", "Meka silikonska četkica i bebi pasta u količini zrna pirinča od prvog zubića."),
            ("Prevencija 'karijesa bočice':", "Stroga zabrana uspavljivanja sa flašicom soka, zaslađenog čaja ili mleka.")
        ]),
        ("3. ŠTA NIJE ZUBIĆ & PRAVILNA HIDRACIJA", C_DARK, [
            ("Povišena T >38.5°C i proliv NISU od zuba:", "Nicanje zuba ne izaziva visoku febrilnost – to je znak infekcije!"),
            ("Uvođenje vode tek sa dohranom:", "Do 6. meseca mleko potpuno hidrira bebu; voda se uvodi uz čvrste obroke."),
            ("Ponuđena voda u gutljajima:", "Uvek nuditi prokuvanu ili niskomineralnu negaziranu vodu nakon obroka.")
        ]),
    ]
    
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        
        item_y = y + 88
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            item_y += 76
        y += 352
        
    # Bottom warning
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[STROGA PEDIJATRIJSKA ZABRANA]", fill=C_RED, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "NIKADA NE KORISTITI ANESTEZIJSKE GELEVE SA LIDOKAINOM!", C_LINEN)
    draw.text((W//2, 1386), "Lidokain se apsorbuje kroz sluzokožu i može izazvati poremećaj rada srca i gutanja.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide19_dentition_oral_care.png"), "PNG", optimize=True)
    print("Saved slide19_dentition_oral_care.png")

# -------------------------------------------------------------
# SLIDE 20: KALENDAR IMUNIZACIJE I PRIPREMA ODOJČETA
# -------------------------------------------------------------
def make_slide20():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 3: NEGA ODOJČETA",
        "KALENDAR IMUNIZACIJE I PRIPREMA ODOJČETA",
        "Zvanični pedijatrijski kalendar vakcina i uloga dadilje u pripremi deteta"
    )
    
    cards = [
        ("1. VAKCINE NA ROĐENJU (PORODILIŠTE)", C_TERRA, [
            ("BCG vakcina (protiv tuberkuloze):", "Aplikuje se u levo rame; nakon 4–6 nedelja stvara se čvorić i krastica."),
            ("Hepatitis B (prva doza):", "Daje se intramuskularno u butinu unutar prva 24 sata po rođenju deteta."),
            ("Evidencija u knjižici:", "Provera unetih podataka o primljenim vakcinama pri otpustu iz porodilišta.")
        ]),
        ("2. PRIMARNA VAKCINACIJA (2, 3.5 I 5. MESEC)", C_SAGE, [
            ("Kombinovana (DTaP-IPV-Hib-HepB):", "Šestovalentna vakcina protiv 5–6 teških zaraznih bolesti u jednoj dozi."),
            ("Pneumokokna konjugovana vakcina:", "Štiti od bakterijskih pneumonija, meningitisa, sepse i gnojne upale uva."),
            ("MMR vakcina (12–15. mesec):", "Zaštita od malih boginja (morbili), zaušaka (mumps) i crvenke (rubeola).")
        ]),
        ("3. ULOGA DADILJE U DANU VAKCINACIJE", C_DARK, [
            ("Potpuno zdravstveno stanje:", "Dete mora biti pregledano od strane pedijatra; odlaže se ako postoji infekcija."),
            ("Udobna pamučna odeća:", "Bodići koji se lako raskopčavaju u predelu butine radi bezbednog davanja."),
            ("Smirivanje i evidencija:", "Podoj ili flašica nakon uboda umiruju bebu; podaci se unose u Dnevnik nege.")
        ]),
    ]
    
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        
        item_y = y + 88
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            item_y += 76
        y += 352
        
    # Bottom warning
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[ZLATNO PRAVILO PEDIJATRIJE]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "NIKADA NE DAVATI SIRUP PRE VAKCINE 'ZA SVAKI SLUČAJ'!", C_LINEN)
    draw.text((W//2, 1386), "Preventivno davanje antipiretika pre uboda dokazano smanjuje stvaranje antitela.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide20_vaccination_schedule.png"), "PNG", optimize=True)
    print("Saved slide20_vaccination_schedule.png")

# -------------------------------------------------------------
# SLIDE 21: VISOKA TEMPERATURA I PROTOKOL OBARANJA
# -------------------------------------------------------------
def make_slide21():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "VISOKA TEMPERATURA: MERENJE I HLAĐENJE",
        "Egzaktni pragovi febrilnosti i bezbedne mere fizikalnog rashlađivanja"
    )
    
    sections = [
        ("1. PEDIJATRIJSKI PRAGOVI MERENJA", C_TERRA, [
            ("Aksilarno merenje (pazuh):", "Granica povišene temperature je 38.0°C (očitavanje standardnim toplomerom)."),
            ("Rektalno merenje (čmar):", "Očitavanje je za 0.5°C više; febrilnost počinje od 38.5°C (zlatni standard do 1. god)."),
            ("Kada davati lekove:", "Antipiretici se daju iznad 38.5°C aksilarno (39.0°C rektalno) ili pri lošem stanju.")
        ]),
        ("2. FIZIKALNE MERE RASHLAĐIVANJA", C_SAGE, [
            ("Raskomoćivanje & mikroklima:", "Lagan pamučni bodi u provetrenoj sobi na 20–22°C (nikada ne pretopljavati!)."),
            ("Hidratacija & elektroliti:", "Češći podoji, gutljaji vode ili ORS rastvora sprečavaju dehidrataciju."),
            ("Tuširanje mlakom vodom (36–37°C):", "Lagano kvasiti trup i noge 5–10 minuta; strogo bez hladne vode i šoka!")
        ]),
        ("3. STROGO ZABRANJENE OPASNE METODE", C_RED, [
            ("Zabrana alkohola i sirćeta:", "Apsolutno zabranjeno utrljavanje – rizik od teškog trovanja kroz dečju kožu!"),
            ("Zabrana preznojavanja:", "Uvijanje u jorgane podiže unutrašnju temperaturu i vodi u toplotni udar.")
        ]),
    ]
    
    y = 160
    for title, col, items in sections:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        
        iy = y + 88
        for lbl, desc in items:
            draw_item(draw, 65, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            iy += 76
        y += 352
        
    # Bottom warning
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[HITAN ALARM ZA PEDIJATRA / 194]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1318, "Beba <3 meseca sa T >38°C, febrilne konvulzije ili letargija!", C_LINEN)
    draw.text((W//2, 1378), "Ponašanje deteta i kontakt očima važniji su od same cifre na toplomeru.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide21_fever_check_hd.png"), "PNG", optimize=True)
    print("Saved slide21_fever_check_hd.png")

# -------------------------------------------------------------
# SLIDE 22: PEDIJATRIJSKO DOZIRANJE ANTIPIRETIKA
# -------------------------------------------------------------
def make_slide22():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "DOZIRANJE ANTIPIRETIKA: PARACETAMOL VS IBUPROFEN",
        "Zlatno pravilo pedijatrije: Lek se dozira STROGO PO KILOGRAMIMA, nikada po uzrastu!"
    )
    
    # Paracetamol Card
    draw.rounded_rectangle([(35, 160), (W-35, 680)], radius=14, fill=C_CARD, outline=C_TERRA, width=1)
    draw_badge(draw, 55, 180, "PARACETAMOL (Sirup / Čepići)", F_CARD_TITLE, C_TERRA, C_CARD, height=54)
    
    bbox_d1 = draw.textbbox((0, 0), "10 – 15 mg / kg", font=F_CARD_TITLE)
    dw1 = (bbox_d1[2] - bbox_d1[0]) + 34
    draw.rounded_rectangle([(W - 55 - dw1, 180), (W - 55, 234)], radius=8, fill=C_GOLD)
    draw.text((W - 55 - dw1//2, 207), "10 – 15 mg / kg", fill=C_DARK, font=F_CARD_TITLE, anchor="mm")
    
    p_info = [
        ("Uzrast primene:", "Dozvoljen od prvih dana života (prema savetu pedijatra)."),
        ("Vremenski razmak:", "Daje se na svakih 4 do 6 sati po potrebi (maksimalno 4 doze u toku 24 sata)."),
        ("Maksimalan broj doza:", "Maksimalno 4 doze u toku 24 sata – nikada ne skraćivati razmak!"),
        ("Kada koristiti čepiće:", "Ukoliko beba povraća ili odbija špric, rektalni čepić deluje za 15-20 min.")
    ]
    py = 265
    for p_lbl, p_desc in p_info:
        draw_item(draw, 65, py, f"• {p_lbl}", f"   {p_desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
        py += 100
        
    # Ibuprofen Card
    draw.rounded_rectangle([(35, 710), (W-35, 1225)], radius=14, fill=C_CARD, outline=C_SAGE, width=1)
    draw_badge(draw, 55, 730, "IBUPROFEN (Brufen sirup)", F_CARD_TITLE, C_SAGE, C_CARD, height=54)
    
    bbox_d2 = draw.textbbox((0, 0), "5 – 10 mg / kg", font=F_CARD_TITLE)
    dw2 = (bbox_d2[2] - bbox_d2[0]) + 34
    draw.rounded_rectangle([(W - 55 - dw2, 730), (W - 55, 784)], radius=8, fill=C_GOLD)
    draw.text((W - 55 - dw2//2, 757), "5 – 10 mg / kg", fill=C_DARK, font=F_CARD_TITLE, anchor="mm")
    
    i_info = [
        ("STROGO OGRANIČENJE UZRASTA:", "ISKLJUČIVO za decu stariju od 3 meseca i preko 5 kg težine!"),
        ("Vremenski razmak:", "Daje se na svakih 6 do 8 sati po potrebi (maksimalno 3 doze u toku 24 sata)."),
        ("Preporuka za želudac:", "Davanje uz ili neposredno nakon obroka ili mleka radi zaštite sluznice."),
        ("Kombinovanje lekova:", "Samo po izričitom nalogu pedijatra; voditi strogi vremenski dnevnik!")
    ]
    iy = 815
    for i_lbl, i_desc in i_info:
        draw_item(draw, 65, iy, f"• {i_lbl}", f"   {i_desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
        iy += 100
        
    # Safety Banner
    draw.rounded_rectangle([(35, 1255), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1288), "[PROTOKOL BEZBEDNOSTI DADILJE]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw.text((W//2, 1336), "Uvek koristiti BAŽDARENI ORALNI ŠPRIC koji dolazi uz lek.", fill=C_LINEN, font=F_CARD_TITLE, anchor="mm")
    draw.text((W//2, 1386), "Kombinovanje Paracetamola i Ibuprofena dozvoljeno je ISKLJUČIVO po nalogu lekara.", fill=C_SAND, font=F_BODY, anchor="mm")
    draw.text((W//2, 1432), "Svaka data doza se u minut unosi u Dnevnik nege sa izmerenom temperaturom.", fill=C_LINEN, font=F_SMALL, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide22_pediatric_dosage_card.png"), "PNG", optimize=True)
    print("Saved slide22_pediatric_dosage_card.png")

# -------------------------------------------------------------
# SLIDE 23: DIGESTIVNE SMETNJE I ORALNA REHIDRACIJA
# -------------------------------------------------------------
def make_slide23():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "POVRAĆANJE, DIJAREJA I ORALNA REHIDRACIJA",
        "Klinička trijaža, sprečavanje dehidratacije i primena O.R.S."
    )
    
    # Card 1: Diferencijalna dijagnoza
    draw.rounded_rectangle([(35, 160), (W-35, 680)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
    draw_badge(draw, 55, 180, "BLJUCKANJE VS POVRAĆANJE U MLAZU", F_CARD_TITLE, C_DARK, C_LINEN, height=54)
    
    diffs = [
        ("Fiziološko bljuckanje (Refluks):", "Mala količina neusirenog mleka curi iz ugla usana; beba je mirna i lepo napreduje."),
        ("Povraćanje u mlazu (Projektilno):", "Sadržaj pod pritiskom na daljinu. Sumnja na stenozu pilorusa ili infekciju."),
        ("Prisustvo žuči ili krvi:", "Zeleni sadržaj (žuč) ili tragovi krvi zahtevaju HITAN transport na kliniku!"),
        ("Procena stolice:", "Vodena, eksplozivna stolica neprijatnog mirisa nosi visok rizik od dehidratacije.")
    ]
    dy = 265
    for d_title, d_desc in diffs:
        draw_item(draw, 65, dy, d_title, d_desc, F_BOLD, F_BODY, C_TERRA, C_DARK, max_w=1040, line_gap=36)
        dy += 100
        
    # Card 2: Protokol oralne rehidracije (O.R.S.)
    draw.rounded_rectangle([(35, 710), (W-35, 1225)], radius=14, fill=C_CARD, outline=C_SAGE, width=1)
    draw_badge(draw, 55, 730, "PROTOKOL DAVANJA O.R.S. RASTVORA", F_CARD_TITLE, C_SAGE, C_CARD, height=54)
    
    ors = [
        ("Rastvaranje praha:", "Kesica se rastvara u tačno propisanoj količini prokuvane vode (npr. 200 ml)."),
        ("Tehnika 'kašičica po kašičica':", "Davanje 1 kafene kašičice na svakih 5 do 10 minuta (nikada puna flašica odjednom!)."),
        ("Nakon epizode povraćanja:", "Pauzirati 15-20 minuta da se želudac smiri, pa nastaviti kašičicom."),
        ("Nastavak dojenja:", "Dojenje se NE PREKIDA – majčino mleko pruža optimalnu zaštitu crevne sluznice.")
    ]
    oy = 815
    for o_title, o_desc in ors:
        draw_item(draw, 65, oy, f"• {o_title}", f"   {o_desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
        oy += 100
        
    # 4 Znaka dehidratacije
    draw.rounded_rectangle([(35, 1255), (W-35, 1465)], radius=12, fill=C_ALERT_BG, outline=C_RED, width=1)
    draw.text((W//2, 1288), "[4 ZNAKA DEHIDRATACIJE ZA HITAN ODLAZAK KOD LEKARA]", fill=C_RED, font=F_BOLD, anchor="mm")
    
    draw.text((65, 1324), "1. Upala velika fontanela (udubljenje na temenu glave)", fill=C_DARK, font=F_BODY)
    draw.text((65, 1362), "2. Suve pelene duže od 6 sati (nedostatak mokrenja)", fill=C_DARK, font=F_BODY)
    draw.text((65, 1400), "3. Plač bez suza i suve, ispucale usne i jezik", fill=C_DARK, font=F_BODY)
    draw.text((65, 1436), "4. Izrazita pospanost, letargija ili upale očne jabučice", fill=C_DARK, font=F_BODY)
    
    img.save(os.path.join(ASSETS_DIR, "slide23_digestive_dehydration.png"), "PNG", optimize=True)
    print("Saved slide23_digestive_dehydration.png")

# -------------------------------------------------------------
# SLIDE 24: RESPIRATORNE I OČNE INFEKCIJE
# -------------------------------------------------------------
def make_slide24():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "RESPIRATORNE INFEKCIJE I TOALETA OČIJU",
        "Tehnika aspiracije nosa i nega zapušenih suznih kanala"
    )
    
    cards = [
        ("1. TOALETA NOSA I ISPIRANJE", C_DARK, [
            ("Fiziološki rastvor 0.9%:", "Ukapati po 1-2 ml u svaku nozdrvu dok beba leži na boku."),
            ("Nazalni aspirator:", "Izvlačenje sekreta laganim kontinuiranim podpritiskom pre obroka i spavanja."),
            ("Kritično pravilo:", "Beba diše samo na nos – zapušen nos sprečava sisanje i remeti miran san.")
        ]),
        ("2. NEGA OČIJU I KONJUNKTIVITIS", C_TERRA, [
            ("Pokret brisanja:", "Gaza sa fiziološkim od SPOLJAŠNJEG ka UNUTRAŠNJEM uglu bebinog oka."),
            ("Zasebna gaza za svako oko:", "NIKADA ne koristiti istu gazu za oba oka (sprečavanje prenosa infekcije)."),
            ("Masaža suznog kanala:", "Nežan pritisak prstom od korena nosa nadole, 3-4 puta dnevno.")
        ]),
        ("3. MERE OPREZA I ALARMI KOD INFEKCIJA", C_RED, [
            ("Stroga zabrana kamilice:", "Čaj od kamilice NIKADA ne stavljati u oko – nesterilan je i nosi alergene polena!"),
            ("Zabrana kapi za odrasle:", "Dekongestivi za odrasle u nosu odojčeta mogu izazvati kolaps disanja i spazam."),
            ("Kada se HITNO javiti lekaru:", "Zatvoreno oko, obilan gnoj, visoka temperatura ili otežano disanje bebe.")
        ]),
    ]
    
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 405)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 20, title, F_CARD_TITLE, col, C_CARD, height=54)
        
        iy = y + 96
        for lbl, desc in items:
            draw_item(draw, 65, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            iy += 96
        y += 430
        
    img.save(os.path.join(ASSETS_DIR, "slide24_respiratory_care.png"), "PNG", optimize=True)
    print("Saved slide24_respiratory_care.png")

# -------------------------------------------------------------
# SLIDE 25: POSTVAKCINALNE REAKCIJE I PROTOKOL NEGE
# -------------------------------------------------------------
def make_slide25():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "POSTVAKCINALNE REAKCIJE I PROTOKOL NEGE",
        "Diferencijacija normalnog imunog odgovora i upozoravajućih simptoma"
    )
    
    cards = [
        ("1. UOBIČAJENE I PROLAZNE REAKCIJE (24–48h)", C_TERRA, [
            ("Lokalna reakcija na butini:", "Blag otok, crvenilo i bolnost; stavljati suve hladne obloge preko gaze (bez leda)."),
            ("Fiziološka febrilnost:", "Umereno povišena temperatura je normalan znak imunološkog odgovora."),
            ("BCG reakcija (4–6 nedelja):", "Crveni čvorić, gnojnica i krastica na ramenu; NIKADA ne istiskivati i ne mazati.")
        ]),
        ("2. PROTOKOL PRAĆENJA I NEGE DADILJE", C_SAGE, [
            ("Zabrana preventivnih lekova:", "Paracetamol se NE DAJE unapred jer umanjuje efikasnost imunog odgovora."),
            ("Kada primeniti lek:", "Isključivo ako temperatura pređe 38.5°C rektalno ili ako beba trpi jake bolove."),
            ("Komfor i pojačana hidratacija:", "Lagana pamučna garderoba, češći podoji/tečnost i smirujući nežan zagrljaj.")
        ]),
        ("3. CRVENI ALARM – KADA HITNO POZVATI LEKARA", C_RED, [
            ("Neutešan vrišteći plač:", "Plač koji traje duže od 3 sata u kontinuitetu bez mogućnosti smirivanja."),
            ("Febrilne konvulzije i letargija:", "Ukočenost, grčevi, izrazita klonulost, odbijanje tečnosti ili otežano buđenje."),
            ("Veliki otok mesta uboda:", "Crvenilo i tvrd otok prečnika većeg od 5 cm ili uvećani limfni čvorovi.")
        ]),
    ]
    
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        
        item_y = y + 88
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            item_y += 76
        y += 352
        
    # Bottom warning
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[ZLATNO MEDICINSKO PRAVILO]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "REAKCIJA NA VAKCINU JE DOKAZ DA IMUNI SISTEM RADI!", C_LINEN)
    draw.text((W//2, 1386), "Pružite bebi mir, hidrataciju i bliskost, a sve parametre zabeležite u Dnevnik nege.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide25_vaccine_reactions.png"), "PNG", optimize=True)
    print("Saved slide25_vaccine_reactions.png")

# -------------------------------------------------------------
# SLIDE 26: PADOVI I POVREDE GLAVE - 48H PROTOKOL
# -------------------------------------------------------------
def make_slide26():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "PADOVI I POVREDE GLAVE: 48-ČASOVNI PROTOKOL",
        "Smiren pristup, prva pomoć na licu mesta i praćenje znakova potresa mozga"
    )
    
    # Card 1: Prva pomoć na licu mesta
    draw.rounded_rectangle([(35, 160), (W-35, 710)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
    draw_badge(draw, 55, 180, "PRVA POMOĆ NA LICU MESTA", F_CARD_TITLE, C_DARK, C_LINEN, height=54)
    
    aid = [
        ("1. Smiriti bebu i ne pomerati naglo:", "Ostaviti bebu u ležećem položaju ukoliko se sumnja na povredu vrata."),
        ("2. Primena hladne obloge:", "Kockice leda umotane u pamučnu pelenu držati na hematomu 10-15 minuta."),
        ("3. Zaustavljanje krvarenja:", "Direktan pritisak sterilnom gazom na ranu tokom 5 minuta bez podizanja gaze."),
        ("4. Provera svesti i refleksa:", "Da li je beba zaplakala odmah, da li reaguje na glas i prati pogledom?")
    ]
    ay = 270
    for a_title, a_desc in aid:
        draw_item(draw, 65, ay, a_title, a_desc, F_BOLD, F_BODY, C_TERRA, C_DARK, max_w=1040, line_gap=36)
        ay += 104
        
    # Card 2: 48h Neurološki monitoring
    draw.rounded_rectangle([(35, 740), (W-35, 1465)], radius=14, fill=C_ALERT_BG, outline=C_RED, width=1)
    draw_badge(draw, 55, 760, "5 ZNAKOVA ZA HITNU POMOĆ (194)", F_CARD_TITLE, C_RED, C_CARD, height=54)
    
    signs = [
        ("Gubitak svesti (makar i na par sekundi):", "Apsolutna indikacija za hitan pedijatrijski pregled i snimanje."),
        ("Povraćanje u mlazu više od dva puta:", "Klasičan znak povećanog intrakranijalnog pritiska nakon potresa mozga."),
        ("Asimetrične zenice ili ukočen pogled:", "Jedna zenica šira od druge, beba ne fokusira predmete."),
        ("Izrazita pospanost i otežano buđenje:", "Beba ne može da se razbudi radi hranjenja, mlitava je i nezainteresovana."),
        ("Curenje bistre tečnosti iz nosa ili uha:", "Sumnja na likvoreju (povredu baze lobanje) – NE DIRATI, HITNO 194!")
    ]
    sy = 850
    for s_title, s_desc in signs:
        draw_item(draw, 65, sy, f"! {s_title}", f"   {s_desc}", F_BOLD, F_BODY, C_RED, C_DARK, max_w=1040, line_gap=36)
        sy += 118
        
    img.save(os.path.join(ASSETS_DIR, "slide26_head_injury_first_aid.png"), "PNG", optimize=True)
    print("Saved slide26_head_injury_first_aid.png")

# -------------------------------------------------------------
# SLIDE 27: GUŠENJE ODOJČETA (< 1 GODINA) - HITAN PROTOKOL
# -------------------------------------------------------------
def make_slide27():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "GUŠENJE ODOJČETA (< 1 GODINA): HITAN PROTOKOL",
        "Postupak odgušenja disajnih puteva u 2 koraka"
    )
    
    # Card 1: Korak 1 - 5 Udaraca u leđa
    draw.rounded_rectangle([(35, 160), (W-35, 680)], radius=14, fill=C_CARD, outline=C_TERRA, width=1)
    draw_badge(draw, 55, 180, "KORAK 1: 5 UDARACA KORENOM DLANA U LEĐA", F_CARD_TITLE, C_TERRA, C_CARD, height=54)
    
    k1 = [
        ("Položaj deteta duž podlaktice:", "Položite bebu potrbuške duž svoje podlaktice, sa glavom NIŽE od grudnog koša."),
        ("Fiksacija donje vilice prstima:", "Šakom pažljivo fiksirajte donju vilicu (strogo paziti da se NE pritiskaju meka tkiva vrata!)."),
        ("Tehnika zadavanja udaraca:", "Izvedite 5 odmerenih, oštrih udaraca korenom dlana između lopatica usmerenih ka spolja.")
    ]
    y1 = 265
    for lbl, desc in k1:
        draw_item(draw, 65, y1, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
        y1 += 100
        
    # Card 2: Korak 2 - 5 Pritisaka na grudnu kost
    draw.rounded_rectangle([(35, 710), (W-35, 1225)], radius=14, fill=C_CARD, outline=C_SAGE, width=1)
    draw_badge(draw, 55, 730, "KORAK 2: 5 PRITISAKA NA SREDINU GRUDNOG KOŠA", F_CARD_TITLE, C_SAGE, C_CARD, height=54)
    
    k2 = [
        ("Okretanje bebe na leđa:", "Okrenite bebu na leđa na drugu podlakticu (glava ostaje nadole pod uglom od 30°)."),
        ("Pozicija dva prsta na sternumu:", "Postavite jagodice dva prsta na sredinu grudne kosti, jedan prst ispod linije bradavica."),
        ("Dubina i ritam kompresija:", "Izvedite 5 brzih, odsečnih pritisaka dubine oko 1.5 cm dok se disajni put ne oslobodi.")
    ]
    y2 = 815
    for lbl, desc in k2:
        draw_item(draw, 65, y2, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
        y2 += 100
        
    # Bottom warning
    draw.rounded_rectangle([(35, 1255), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1288), "[ZLATNO MEDICINSKO PRAVILO ROYAL NANNY]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1338, "NIKADA NE STAVLJATI PRSTE 'NA SLEPO' U USTA BEBE!", C_LINEN)
    draw.text((W//2, 1388), "Slepo vađenje gura strano telo još dublje i uzrokuje totalnu opstrukciju dušnika.", fill=C_SAND, font=F_BODY, anchor="mm")
    draw.text((W//2, 1432), "Ako beba izgubi svest: ODMAH POZVATI 194 i započeti KPR (kardiopulmonalnu reanimaciju).", fill=C_LINEN, font=F_SMALL, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide27_infant_choking_protocol.png"), "PNG", optimize=True)
    print("Saved slide27_infant_choking_protocol.png")

# -------------------------------------------------------------
# SLIDE 28: UJEDI INSEKATA, ZARAZNE BOLESTI I ALERGIJE
# -------------------------------------------------------------
def make_slide28():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "UJEDI INSEKATA, DEČJI OSIPI I ALERGIJE",
        "Pravilno uklanjanje krpelja, prepoznavanje osipa i anafilaksa"
    )
    
    topics = [
        ("1. PROTOKOL VAĐENJA KRPELJA", C_DARK, [
            ("Medicinska pinceta:", "Uhvatiti krpelja što bliže koži i povući RAVNO nagore umerenim pritiskom."),
            ("STROGA ZABRANA HEMIKALIJA:", "NIKADA ne stavljati ulje, alkohol ili aceton (gušenje krpelja luči toksine u krv!)."),
            ("Monitoring mesta uboda (30 dana):", "Pojava crvenog prstena koji se širi (Erythema migrans) ukazuje na Lajmsku bolest.")
        ]),
        ("2. PREPOZNAVANJE DEČJIH OSIPA", C_TERRA, [
            ("Varičela (Ovčije boginje):", "Vezikule ispunjene bistrom tečnošću ('kapi rose'), intenzivan svrab."),
            ("Šarlah (Streptokok):", "Sitnozrnast osip ('šmirgl papir'), izrazito crveno ždrelo i 'malinast jezik'."),
            ("Roseola infantum:", "Iznenadna visoka T 3 dana; po padu temperature izbija blag osip po telu.")
        ]),
        ("3. ANAFILAKTIČKI ŠOK (CRVENI ALARM 194)", C_RED, [
            ("Simptomi gušenja:", "Oticanje usana, jezika, otežano čujno disanje (stridor), bledilo i hladan znoj."),
            ("Hitan postupak:", "ODMAH pozvati 194, polusedeći položaj, pripremiti EpiPen ako je propisan.")
        ]),
    ]
    
    y = 160
    for title, col, items in topics:
        draw.rounded_rectangle([(35, y), (W-35, y + 405)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 20, title, F_CARD_TITLE, col, C_CARD, height=54)
        
        iy = y + 96
        for lbl, desc in items:
            draw_item(draw, 65, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            iy += 96
        y += 430
        
    img.save(os.path.join(ASSETS_DIR, "slide28_insect_bites_allergies.png"), "PNG", optimize=True)
    print("Saved slide28_insect_bites_allergies.png")

# -------------------------------------------------------------
# SLIDE 30: ZLATNI STANDARD PUTNE I KUĆNE APOTEKE
# -------------------------------------------------------------
def make_slide30():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "ZLATNI STANDARD KUĆNE I PUTNE APOTEKE",
        "4 obavezna segmenta profesionalne torbe za pedijatrijsku negu"
    )
    
    sections = [
        ("I. ANTIPIRETIČKI I ANALGETIČKI SEGMENT", C_TERRA, [
            ("Paracetamol sirup + rektalni čepići:", "Osnovni lek prvog izbora za temperaturu i bolove."),
            ("Ibuprofen sirup:", "Antiinflamatorno dejstvo (samo za bebe starije od 3 meseca)."),
            ("Originalni baždareni špricevi:", "Označeni mililitrima za svaku bočicu.")
        ]),
        ("II. GASTROENTEROLOŠKI SEGMENT", C_SAGE, [
            ("Oralni rehidracioni rastvor (O.R.S.):", "3 kesice sa balansiranim elektrolitima i glukozom."),
            ("Probiotik u kapima:", "Za regulaciju crevne flore i ublažavanje dijareje."),
            ("Kapi protiv grčeva (Simetikon / Laktaza):", "Za smanjenje gasova u crevima.")
        ]),
        ("III. ANTISEPTICI I OBRADA RANA", C_DARK, [
            ("Octenisept sprej:", "Bezbolan antiseptik za sluzokožu i kožu (ne peče!)."),
            ("Sterilne komprese i mikropor flaster:", "Različitih dimenzija za previjanje."),
            ("3% hidrogen i fiziološki rastvor:", "Ampule od 5 i 10 ml za toaletu očiju i nosa.")
        ]),
        ("IV. DIJAGNOSTIČKI PRIBOR I ALATI", C_GOLD, [
            ("Digitalni aksilarni / beskontaktni toplomer:", "Sa rezervnim baterijama."),
            ("Anatomska pinceta za krpelje:", "Sa tankim ravnim vrhom."),
            ("Makazice za nokte sa zaobljenim vrhom:", "Nerđajući medicinski čelik.")
        ]),
    ]
    
    y = 160
    for title, col, items in sections:
        draw.rounded_rectangle([(35, y), (W-35, y + 300)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD if col != C_GOLD else C_DARK, height=52)
        
        iy = y + 88
        for lbl, desc in items:
            draw_item(draw, 65, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=34)
            iy += 68
        y += 324
        
    img.save(os.path.join(ASSETS_DIR, "slide30_apoteka_kit.png"), "PNG", optimize=True)
    print("Saved slide30_apoteka_kit.png")

# -------------------------------------------------------------
# SLIDE 31: TEHNIKE BEZBEDNE ADMINISTRACIJE LEKOVA
# -------------------------------------------------------------
def make_slide31():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "TEHNIKE BEZBEDNE ADMINISTRACIJE LEKOVA",
        "Sprečavanje aspiracije, gušenja i stresa kod deteta"
    )
    
    techniques = [
        ("1. ORALNI ŠPRIC – SMER KA UNUTRAŠNJOJ STRANI OBRAZA", C_TERRA, [
            ("Položaj deteta:", "Dete je u polusedećem položaju u naručju dadilje (NIKADA u ležećem!)."),
            ("Smer šprica:", "Vrh šprica se uvodi uz unutrašnju stranu obraza (prema kutnjacima)."),
            ("STROGA ZABRANA:", "NIKADA ne špricati lek pravo u grlo ili jezik (izaziva laringospazam i gušenje!)."),
            ("Doziranje u mlazevima:", "Pritiskati klip u malim porcijama (po 0.5 ml) sinhronizovano sa gutanjem.")
        ]),
        ("2. UKAPAVANJE KAPI U OČI", C_SAGE, [
            ("Ukapavanje u donji kapak:", "Nežno povući donji očni kapak nadole i kapnuti u stvoreni džep (forniks)."),
            ("Bez dodirivanja oka:", "Vrh bočice ne sme dodirnuti trepavice ili oko radi očuvanja sterilnosti."),
            ("Zatvaranje oka:", "Zadržati oko zatvoreno par sekundi i obrisati višak sterilnom gazom.")
        ]),
        ("3. UKAPAVANJE KAPI U UŠI", C_DARK, [
            ("Zagrevanje bočice dlanovima:", "Bočicu protrljati dlanovima 2-3 minuta (hladne kapi izazivaju jaku vrtoglavicu)."),
            ("Položaj uva:", "Kod beba školjku povući nežno NAZAD i NADOLE radi ispravljanja slušnog kanala."),
            ("Mirovanje:", "Dete ostaje na boku 2-3 minuta nakon ukapavanja.")
        ]),
    ]
    
    y = 160
    for idx, (title, col, items) in enumerate(techniques):
        draw.rounded_rectangle([(35, y), (W-35, y + 405)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 20, title, F_CARD_TITLE, col, C_CARD, height=54)
        
        step_val = 74 if idx == 0 else 96
        iy = y + 86 if idx == 0 else y + 96
        for lbl, desc in items:
            draw_item(draw, 65, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=34 if idx == 0 else 36)
            iy += step_val
        y += 430
        
    img.save(os.path.join(ASSETS_DIR, "slide31_safe_medicine_admin.png"), "PNG", optimize=True)
    print("Saved slide31_safe_medicine_admin.png")

# -------------------------------------------------------------
# SLIDE 10: HIGIJENA GARDEROBE I BEBINOG PRIBORA
# -------------------------------------------------------------
def make_slide10_wardrobe_hygiene():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 1: HIGIJENA I NEGA NOVOROĐENČETA",
        "HIGIJENA GARDEROBE I BEBINOG PRIBORA",
        "Standardi pranja, sterilizacije i održavanja higijene enterijera"
    )
    cards = [
        ("1. PRANJE I ISPIRANJE ODEĆE (60°C – 90°C)", C_TERRA, [
            ("Pranje na visokim temperaturama:", "Bodići, benkice i pelene peru se na minimum 60°C radi eliminacije bakterija."),
            ("Tečni hipoalergeni deterdžent:", "Isključivo formulacije bez parfema i agresivnih tenzida (ne iritira kožu)."),
            ("STROGA ZABRANA OMEKŠIVAČA:", "Omekšivači ostavljaju hemijski film na pamuku koji izaziva kontaktni dermatitis!"),
            ("Dvostruko ispiranje (Double Rinse):", "Obavezno dodatno ispiranje čistom vodom radi uklanjanja svih tragova praška.")
        ]),
        ("2. PEGLANJE PAROM I SKLADIŠTENJE", C_SAGE, [
            ("Peglanje vrelom parom:", "Dezinfikuje pamuk, omekšava vlakna i eliminiše potrebu za hemijskim omekšivačima."),
            ("Peglanje sa unutrašnje strane:", "Naročito duž šavova i etiketa koji direktno dodiruju bebinu osetljivu kožu."),
            ("Čisto pamučno platno:", "Složene stvari se odlažu u zatvorene fioke zaštićene od kućne prašine.")
        ]),
        ("3. HIGIJENA PRIBORA I PULTA ZA PREPOVIJANJE", C_DARK, [
            ("Dezinfekcija pulta pre i posle:", "Medicinski antiseptik i čista pamučna tetra pelena kao podloga."),
            ("Igračke i glodalice:", "Redovno pranje toplom vodom i sodom bikarbonom pre stavljanja u usta."),
            ("Kanta za prljave pelene:", "Namenski antibakterijski koš sa poklopcem koji hermetički dihtuje.")
        ]),
    ]
    y = 160
    for idx, (title, col, items) in enumerate(cards):
        h = 330 if idx != 0 else 350
        draw.rounded_rectangle([(35, y), (W-35, y + h)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        item_y = y + 84
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=32)
            item_y += 66 if idx == 0 else 76
        y += h + 22
        
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[ZLATNO PRAVILO PEDIJATRIJSKE DERMATOLOGIJE]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "OMEKŠIVAČI ZA VEŠ SU STROGO ZABRANJENI ZA BEBE!", C_LINEN)
    draw.text((W//2, 1386), "Čista topla voda, parno peglanje i dvostruko ispiranje čuvaju hidrolipidnu barijeru kože.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide10_wardrobe_hygiene.png"), "PNG", optimize=True)
    print("Saved slide10_wardrobe_hygiene.png")

# -------------------------------------------------------------
# SLIDE 13: PRIPREMA DOJKI ZA PODOJ
# -------------------------------------------------------------
def make_slide13_breast_prep():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 2: DOJENJE",
        "PRIPREMA DOJKI ZA PODOJ: LET-DOWN PROTOKOL",
        "Podsticanje refleksa otpuštanja mleka i opuštanje mlečnih kanala"
    )
    cards = [
        ("1. TOPLE OBLOGE PRE PODOJA (5–10 MIN)", C_TERRA, [
            ("Vlažna topla tetra pelena:", "Zagreva tkivo dojke, širi mlečne kanaliće i olakšava kretanje mleka."),
            ("Topao tuš pred podoj:", "Mlaz tople vode usmeren preko ramena i leđa stimuliše lučenje oksitocina."),
            ("Zabrana prevrućih obloga:", "Temperatura obloge mora biti prijatno topla (ne preko 38°C) radi zaštite kože.")
        ]),
        ("2. NEŽNA MASAŽA I OMEKŠAVANJE AREOLE", C_SAGE, [
            ("Tehnika kružne masaže:", "Jagodicama prstiju praviti nežne spiralne pokrete od baze dojke ka bradavici."),
            ("Iztiskivanje nekoliko kapi mleka:", "Omekšava napetu areolu kako bi beba mogla duboko da zahvati tkivo."),
            ("Oslobađanje venske staze:", "Smanjuje otok areole i omogućava formiranje pravilnog vakuuma.")
        ]),
        ("3. PSIHOEMOCIONALNA RELAKSACIJA MAJKE", C_DARK, [
            ("Čaša vode pored fotelje:", "Dojenje pokreće intenzivnu žeđ – hidratacija je ključ kontinuirane laktacije."),
            ("Miran ambijent bez stresa:", "Prigušeno svetlo, udobna fotelja sa osloncem za leđa i noge."),
            ("Uloga dadilje:", "Dadilja priprema jastuk za dojenje, dodaje bebu i pruža tihu, nenametljivu podršku.")
        ]),
    ]
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        item_y = y + 88
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            item_y += 76
        y += 352
        
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[KLINIČKI PRINCIP LAKTACIJE]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "OKSITOCIN JE HORMON LJUBAVI, MIRA I SIGURNOSTI!", C_LINEN)
    draw.text((W//2, 1386), "Stres i napetost blokiraju otpuštanje mleka; toplina i podrška dadilje otvaraju kanale.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide13_breast_prep.png"), "PNG", optimize=True)
    print("Saved slide13_breast_prep.png")

# -------------------------------------------------------------
# SLIDE 15: ASIMETRIČNI HVAT I POSTAVLJANJE NA DOJKU
# -------------------------------------------------------------
def make_slide15_latch_technique():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 2: DOJENJE",
        "ASIMETRIČNI HVAT: ZLATNI STANDARD PODOJA",
        "Biomehanika postavljanja bebe na dojku bez bola i oštećenja bradavica"
    )
    cards = [
        ("1. PRINOŠENJE I ŠIROKO OTVARANJE USTA", C_TERRA, [
            ("Beba se prinosi dojci:", "Majka sedi uspravno i stabilno; beba se prinosi u visini bradavice (ne dojka bebi!)."),
            ("Bradavica u visini nosića:", "Dodirivanje gornje usne stimuliše refleks zevanja i otvaranje usta preko 140°."),
            ("Brada prva dodiruje dojku:", "Bebina brada utone duboko u donji pol areole pre prihvatanja bradavice.")
        ]),
        ("2. OSOBINE PRAVILNOG ASIMETRIČNOG HVATA", C_SAGE, [
            ("Donji deo areole pokriven:", "U ustima bebe nalazi se znatno veći deo areole odozdo nego odozgo."),
            ("Izvrnute usne ('usne ribice'):", "I gornja i donja usna su potpuno izvrnute upolje (nisu uvučene)."),
            ("Nos potpuno slobodan:", "Zahvaljujući zabačenoj glavici, nosić ne dodiruje dojku i beba nesmetano diše."),
            ("Zvuk ritmičnog gutanja:", "Čuje se duboko ritmično gutanje ('uh-uh'), bez coktanja i gubitka vakuuma.")
        ]),
    ]
    y = 160
    for idx, (title, col, items) in enumerate(cards):
        h = 420 if idx == 0 else 510
        draw.rounded_rectangle([(35, y), (W-35, y + h)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 20, title, F_CARD_TITLE, col, C_CARD, height=54)
        item_y = y + 96
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            item_y += 98 if idx == 0 else 92
        y += h + 24
        
    draw.rounded_rectangle([(35, 1140), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1180), "[ZLATNO PRAVILO BEZBOLNOG DOJENJA]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1240, "DOJENJE NE SME DA BOLI – BOL JE ZNAK PLITKOG HVATA!", C_LINEN)
    draw.text((W//2, 1310), "Ako se javi bol: nežno staviti vrh malog prsta u ugao bebinih usana radi prekida vakuuma,", fill=C_SAND, font=F_BODY, anchor="mm")
    draw.text((W//2, 1360), "odvojiti bebu i ponoviti prinušenje pod širokim uglom otvaranja.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide15_latch_technique.png"), "PNG", optimize=True)
    print("Saved slide15_latch_technique.png")

# -------------------------------------------------------------
# SLIDE 17: UPALA DOJKI (PREPUNJENOST I MASTITIS)
# -------------------------------------------------------------
def make_slide17_mastitis_protocol():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 2: DOJENJE",
        "TRIJAŽA I PROTOKOL: PREPUNJENOST VS MASTITIS",
        "Diferencijacija zastoja mleka i bakterijske infekcije dojke"
    )
    cards = [
        ("1. PREPUNJENOST DOJKI (FIZIOLOŠKI ZASTOJ)", C_TERRA, [
            ("Simptomi (obostrano):", "Obe dojke teške, otečene, tople i tvrde poput kamena; javlja se 3–5. dana."),
            ("Protokol nege:", "Tople obloge 5 min pre podoja, masaža, potpuno pražnjenje, hladne obloge posle podoja."),
            ("Temperatura:", "Telesna temperatura je normalna ili prolazno blago povišena (< 38°C).")
        ]),
        ("2. MASTITIS (BAKTERIJSKA UPALA DOJKE)", C_RED, [
            ("Simptomi (jednostrano):", "Crveni trougao, vreo i bolan čvor, malaksalost, jeza, drhtavica i T > 38.5°C."),
            ("Uzročnik:", "Bakterija (Staphylococcus) prodire kroz naprslu ragadu na bradavici."),
            ("Medicinska terapija:", "Hitno javljanje lekaru radi propisivanja antibiotika bezbednog za dojenje.")
        ]),
        ("3. NAJVAŽNIJE MEDICINSKO PRAVILO", C_DARK, [
            ("DOJENJE SE NE PREKIDA!:", "Prekid pražnjenja vodi u stvaranje apscesa i hiruršku intervenciju!"),
            ("Redovno pražnjenje obolele dojke:", "Beba je najefikasnija pumpica; mleko je potpuno bezbedno za dete.")
        ]),
    ]
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        item_y = y + 88
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            item_y += 76
        y += 352
        
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[KRITIČNO PRAVILO LAKTACIJSKE NEGE]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "PREKID DOJENJA KOD MASTITISA JE OPASNA GREŠKA!", C_LINEN)
    draw.text((W//2, 1386), "Redovno i potpuno pražnjenje obolele dojke je ključni uslov brzog izlečenja.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide17_mastitis_protocol.png"), "PNG", optimize=True)
    print("Saved slide17_mastitis_protocol.png")

# -------------------------------------------------------------
# SLIDE 18: IZMAZANJE MAJČINOG MLEKA
# -------------------------------------------------------------
def make_slide18_milk_expression():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 2: DOJENJE",
        "TEHNIKE IZMAZANJA MAJČINOG MLEKA",
        "Ručna tehnika po Marmet-ovoj i bezbedno korišćenje pumpica"
    )
    cards = [
        ("1. RUČNA TEHNIKA IZMAZANJA (METODA MARMET)", C_TERRA, [
            ("Pozicija prstiju ('C' hvat):", "Palac iznad, a kažiprst ispod areole (oko 2.5–3 cm iza baze bradavice)."),
            ("Pritisak ka grudnom košu:", "Pritisnuti prste ravno unazad (prema rebrima) bez razdvajanja prstiju."),
            ("Kotrljanje ka napred:", "Kružnim pokretom prstiju lagano pritiskati mlečne sinuse ka bradavici."),
            ("STROGA ZABRANA ŠTIPALJKE:", "Nikada ne stiskati i ne vući bradavicu – to oštećuje tkivo i stvara podlive!")
        ]),
        ("2. MEHANIČKE I ELEKTRIČNE PUMPICE", C_SAGE, [
            ("Odgovarajući levak (flange):", "Prečnik levka mora tačno odgovarati bradavici bez uvlačenja areole."),
            ("Postepeno podešavanje vakuuma:", "Započeti brzim plitkim ritmom stimulacije, zatim preći na dublji ritam."),
            ("Higijena i sterilizacija:", "Pranje svih delova toplom vodom i sterilizacija jednom dnevno.")
        ]),
        ("3. PODSTICAJ REFLEKSA PRE IZMAZANJA", C_DARK, [
            ("Topla obloga i masaža:", "5 minuta toplote pre početka udvostručuje količinu mleka."),
            ("Fotografija ili odeća bebe:", "Vizuelni i mirisni stimulans podstiče nagli skok oksitocina.")
        ]),
    ]
    y = 160
    for idx, (title, col, items) in enumerate(cards):
        h = 350 if idx == 0 else 320
        draw.rounded_rectangle([(35, y), (W-35, y + h)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        item_y = y + 84
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=34)
            item_y += 66 if idx == 0 else 76
        y += h + 22
        
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[PRAVILO ZA EFIKASNO IZMAZANJE]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "IZMAZANJE NE SME DA IZAZIVA BOL ILI POVREDE!", C_LINEN)
    draw.text((W//2, 1386), "Pravilna tehnika i relaksacija omogućavaju brzo pražnjenje bez nelagodnosti.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide18_milk_expression.png"), "PNG", optimize=True)
    print("Saved slide18_milk_expression.png")

# -------------------------------------------------------------
# SLIDE 24: ZDRAVE ŽIVOTNE NAVIKE I MOTORNI RAZVOJ
# -------------------------------------------------------------
def make_slide24_healthy_habits():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 3: NEGA ODOJČETA",
        "ZDRAVE ŽIVOTNE NAVIKE I MOTORNI RAZVOJ",
        "Cirkadijalni ritam, higijena ruku, tummy time i okruženje bez ekrana"
    )
    cards = [
        ("1. CIRKADIJALNI RITAM I HIGIJENA SNA", C_TERRA, [
            ("Razlikovanje dana i noći:", "Dnevne dremke uz svetlost i normalne zvuke doma; noć u potpunom mraku i tišini."),
            ("Večernja rutina u 4 koraka:", "Kupanje -> nežna masaža -> hranjenje -> spavanje uvek u isto vreme."),
            ("Doslednost rasporeda:", "Usklađen ritam odmora smanjuje kortizol i jača imunitet odojčeta.")
        ]),
        ("2. TUMMY TIME (VEŽBE NA STOMAKU)", C_SAGE, [
            ("Zlatni standard razvoja:", "3 do 5 puta dnevno po 3–5 minuta na čvrstoj podlozi dok je beba budna."),
            ("Jačanje posturalnih mišića:", "Razvija mišiće vrata, ramena i leđa neophodne za puzanje i sedenje."),
            ("Prevencija zaležavanja glave:", "Smanjuje rizik od položajne plagiocefalije (zaravnjenja potiljka).")
        ]),
        ("3. HIGIJENA RUKU I ZABRANA EKRANA", C_DARK, [
            ("Pranje ruku kao ritual:", "Pranje ruku detetu pre svakog obroka, nakon šetnje i presvlačenja pelena."),
            ("NULTA TOLERANCIJA NA EKRANE:", "Prema SZO smernicama, do 2. godine ekrani su STROGO zabranjeni!"),
            ("Dom bez duvanskog dima:", "Pasivno pušenje dramatično uvećava rizik od astme, bronhitisa i SIDS-a.")
        ]),
    ]
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        item_y = y + 88
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            item_y += 76
        y += 352
        
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[STANDARD ROYAL NANNY ZA RAZVOJ]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "AKTIVAN POKRET NA PODU JE NAJBOLJA IGRAČKA!", C_LINEN)
    draw.text((W//2, 1386), "Pasivno sedenje u ležaljkama i nosiljkama usporava motorni i senzorni razvoj deteta.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide24_healthy_habits.png"), "PNG", optimize=True)
    print("Saved slide24_healthy_habits.png")

# -------------------------------------------------------------
# SLIDE 29: INFEKCIJA OKA KOD ODOJČETA (KONJUNKTIVITIS)
# -------------------------------------------------------------
def make_slide29_eye_infection():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "INFEKCIJA OKA KOD ODOJČETA (KONJUNKTIVITIS)",
        "Sterilna toaleta, prohodnost suznog kanala i stroga zabrana kamilice"
    )
    cards = [
        ("1. PREPOZNAVANJE SIMPTOMA INFEKCIJE", C_TERRA, [
            ("Crvenilo vežnjače i otok kapaka:", "Odojče se budi sa slepljenim trepavicama i obilnim sekretom."),
            ("Žućkasto-zelenkast gnojan sekret:", "Znak bakterijske superinfekcije ili zastoja u suznom kanalu."),
            ("Suzno oko koje stalno vlaži:", "Često posledica urođenog suženja nazolakrimalnog kanalića.")
        ]),
        ("2. TEHNIKA STERILNE TOALETE OKA", C_SAGE, [
            ("Pokret od spolja ka unutra:", "Sterilna gaza natopljena fiziološkim povlači se od spoljašnjeg ugla ka nosu."),
            ("Zasebna gaza za svako oko:", "NIKADA ne brisati oba oka istom gazom (sprečavanje prenosa infekcije!)."),
            ("Masaža suznog kanala:", "Blag pritisak jagodicom čistog malog prsta od korena nosa nadole 3-4x dnevno.")
        ]),
        ("3. MEDICINSKA UPOZORENJA I ZABRANE", C_RED, [
            ("STROGA ZABRANA KAMILICE:", "Čaj od kamilice NIKADA ne stavljati u oko – nesterilan je i nosi alergene polena!"),
            ("Kapi isključivo po receptu:", "Antibiotske kapi propisuje isključivo pedijatar nakon pregleda."),
            ("Kada se HITNO javiti lekaru:", "Zatvoreno oko, obilan gnoj, visoka temperatura ili beba ne otvara oko.")
        ]),
    ]
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        item_y = y + 88
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            item_y += 76
        y += 352
        
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[ZLATNO PRAVILO PEDIJATRIJSKE OFTALMOLOGIJE]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "ČAJ OD KAMILICE JE STROGO ZABRANJEN ZA OČI BEBE!", C_LINEN)
    draw.text((W//2, 1386), "Samo sterilan fiziološki rastvor i sterilne komprese su bezbedni za negu očiju odojčeta.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide29_eye_infection.png"), "PNG", optimize=True)
    print("Saved slide29_eye_infection.png")

# -------------------------------------------------------------
# SLIDE 30: ZAPUŠEN NOS KOD ODOJČETA (RINITIS)
# -------------------------------------------------------------
def make_slide30_nasal_care():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "ZAPUŠEN NOS KOD ODOJČETA (RINITIS)",
        "Zašto je prohodnost nosa kritična i tehnika nazalne toalete"
    )
    cards = [
        ("1. ZAŠTO JE ZAPUŠEN NOS URGENTAN PROBLEM?", C_TERRA, [
            ("Odojčad dišu isključivo na nos:", "Beba anatomski ne ume spontano da diše na usta tokom sisanja."),
            ("Nemogućnost hranjenja i dehidracija:", "Zapušen nos onemogućava vakuum, beba odbija obrok i gubi na težini."),
            ("Rizik od upale uva (otitisa):", "Sekret lako prelazi u kratku i široku Eustahijevu tubu odojčeta.")
        ]),
        ("2. PROTOKOL ISPIRANJA I ASPIRACIJE", C_SAGE, [
            ("Položaj na boku:", "Beba leži bočno; rastvor se ukapava u gornju nozdrvu (1–2 ml fiziološkog 0.9% NaCl)."),
            ("Razmekšavanje sekreta:", "Sačekati 30–60 sekundi da rastvor razredi gust mukus pre aspiracije."),
            ("Nežna aspiracija:", "Aspirator koristiti u kratkim impulsima pre obroka i spavanja."),
            ("Podizanje uzglavlja za 30°:", "Postaviti peškir pod dušek radi sprečavanja slivanja sekreta u pluća.")
        ]),
        ("3. STROGO ZABRANJENE OPASNE METODE", C_RED, [
            ("Zabrana kapi za odrasle:", "Dekongestivi za odrasle u nosu odojčeta mogu izazvati kolaps i zastoj disanja!"),
            ("Zabrana agresivnih štapića:", "Nikada ne gurati štapiće sa vatom duboko u bebin nos.")
        ]),
    ]
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        item_y = y + 88
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            item_y += 76
        y += 352
        
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[KRITIČNO PRAVILO ZA RESPIRATORNU NEGU]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "NOS MORA BITI PROHODAN PRE SVAKOG PODOJA I SNA!", C_LINEN)
    draw.text((W//2, 1386), "Fiziološki rastvor, aspiracija i ovlažen vazduh (50–60%) su jedini bezbedni lekovi za nos.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide30_nasal_care.png"), "PNG", optimize=True)
    print("Saved slide30_nasal_care.png")

# -------------------------------------------------------------
# SLIDE 35: ZARAZNE BOLESTI DEČJEG UZRASTA
# -------------------------------------------------------------
def make_slide35_infectious_diseases():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "ZARAZNE BOLESTI DEČJEG UZRASTA",
        "Prepoznavanje kliničke slike, mere izolacije i nega obolelog deteta"
    )
    cards = [
        ("1. TIPICNE DEČJE OSIPNE GROZNICE", C_TERRA, [
            ("Varičela (Ovčije boginje):", "Vezikule ispunjene bistrom tečnošću ('kapi rose'), intenzivan svrab."),
            ("Šarlah (Streptokok):", "Sitnozrnast osip ('šmirgl papir'), zažareno ždrelo i 'malinast jezik' (antibiotik)."),
            ("Šesta bolest (Roseola):", "3 dana visoke T; po padu temperature izbija ružičasti osip po trupu."),
            ("BRNU sindrom (Ruke, noge, usta):", "Bolne afte u ustima i vezikule na dlanovima i tabanima.")
        ]),
        ("2. MERE IZOLACIJE I NEGA DADILJE", C_SAGE, [
            ("Stroga kućna izolacija:", "Dete ne dolazi u kontakt sa drugom decom i trudnicama (varičela je opasna!)."),
            ("Higijena noktiju i kože:", "Podseći noktiće ravno radi sprečavanja bakterijske infekcije češanjem."),
            ("Tretman svraba:", "Medicinske pene i gelovi sa polidokanolom (hlađenje bez talk pudera)."),
            ("Hidratacija i meka hrana:", "Hladni čajevi, jogurt i pasirana hrana bez kiselina i soli.")
        ]),
    ]
    y = 160
    for idx, (title, col, items) in enumerate(cards):
        h = 490 if idx == 0 else 510
        draw.rounded_rectangle([(35, y), (W-35, y + h)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 20, title, F_CARD_TITLE, col, C_CARD, height=54)
        item_y = y + 96
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            item_y += 94
        y += h + 24
        
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[ZLATNO PRAVILO ZA ZARAZNE BOLESTI]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "SVAKI OSIP PRAĆEN VISOKOM TEMPERATUROM ZAHTEVA LEKARA!", C_LINEN)
    draw.text((W//2, 1386), "Izolacija, odmor, hidracija i ublažavanje svraba su osnovni zadaci profesionalne dadilje.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide35_infectious_diseases.png"), "PNG", optimize=True)
    print("Saved slide35_infectious_diseases.png")

# -------------------------------------------------------------
# SLIDE 36: UJEDI INSEKATA: PROTOKOL ZA KRPELJE
# -------------------------------------------------------------
def make_slide36_insect_bites():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "UJEDI INSEKATA: PROTOKOL VAĐENJA KRPELJA",
        "Pravilno postupanje kod krpelja, osa, pčela i komaraca"
    )
    cards = [
        ("1. PROTOKOL PRAVILNOG VAĐENJA KRPELJA", C_DARK, [
            ("Medicinska anatomska pinceta:", "Uhvatiti krpelja što bliže koži (za sam usni aparat)."),
            ("Potez ravno nagore:", "Povući lagano, ravnomernim pritiskom nagore bez uvrtanja ili cimanja."),
            ("Dezinfekcija mesta uboda:", "Očistiti Okteniseptom ili 70% alkoholom NAKON što je krpelj izvađen."),
            ("STROGA ZABRANA HEMIKALIJA:", "NIKADA ne mazati uljem, alkoholom ili acetonom pre vađenja!")
        ]),
        ("2. MONITORING LAJMSKE BOLESTI (30 DANA)", C_TERRA, [
            ("Evidencija datuma uboda:", "Zapisati datum vađenja u Dnevnik nege i pratiti kožu mesec dana."),
            ("Crveni prsten koji se širi (Erythema migrans):", "Crvenilo sa bledim centrom (meta) – HITNO lekaru radi antibiotika.")
        ]),
        ("3. UJEDI OSA, PČELA I KOMARACA", C_SAGE, [
            ("Žaoka pčele:", "Sastrugati tupom stranom kartice (nikada ne stiskati pincetom mešak sa otrovom!)."),
            ("Hladan oblog:", "Kockica leda u pamučnoj peleni ublažava bol i sprečava širenje otoka.")
        ]),
    ]
    y = 160
    for idx, (title, col, items) in enumerate(cards):
        h = 350 if idx == 0 else 320
        draw.rounded_rectangle([(35, y), (W-35, y + h)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        item_y = y + 84
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=34)
            item_y += 66 if idx == 0 else 76
        y += h + 22
        
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[STROGA ZABRANA KOD KRPELJA]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "NIKADA NE PREMAZIVATI KRPELJA ULJEM ILI ALKOHOLOM!", C_LINEN)
    draw.text((W//2, 1386), "Gušenje tera krpelja da povrati toksine u krvotok i drastično uvećava rizik od infekcije.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide36_insect_bites.png"), "PNG", optimize=True)
    print("Saved slide36_insect_bites.png")

# -------------------------------------------------------------
# SLIDE 37: ALERGIJE I ANAFILAKTIČKI ŠOK
# -------------------------------------------------------------
def make_slide37_allergies_anaphylaxis():
    img, draw = create_base_canvas(
        "ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA",
        "ALERGIJE I ANAFILAKTIČKI ŠOK KOD DECE",
        "Diferencijacija blagih alergija i prepoznavanje urgentnog gušenja (194)"
    )
    cards = [
        ("1. BLAGE I UMERENE ALERGIJSKE REAKCIJE", C_TERRA, [
            ("Urtikarija (Koprivnjača):", "Izdignuti crveni pečati koji intenzivno svrbe i menjaju mesto po telu."),
            ("Digestivni simptomi:", "Nagli grčevi u stomaku, povraćanje ili proliv ubrzo nakon obroka."),
            ("Oticanje očnih kapaka:", "Otok bez otežanog disanja; prekinuti unos alergena i pozvati pedijatra.")
        ]),
        ("2. CRVENI ALARM: ANAFILAKTIČKI ŠOK (HITNO 194)", C_RED, [
            ("Oticanje usana, jezika i ždrela:", "Dete ne može da guta pljuvačku, oseća gušenje u grlu."),
            ("Otežano čujno disanje (Stridor):", "Zviždanje u grudima, promukao kašalj poput laveža, uvlačenje grudnog koša."),
            ("Cirkulatorni kolaps:", "Izrazito bledilo, pomodrele usne (cijanoza), hladan znoj i gubitak svesti.")
        ]),
        ("3. HITAN PROTOKOL DADILJE DO DOLASKA HITNE POMOĆI", C_DARK, [
            ("ODMAH POZVATI 194:", "Jasno reći: 'Dete se guši usled sumnje na anafilaktički šok!'"),
            ("Polusedeći položaj:", "Održavati dete u polusedećem položaju radi lakšeg disanja (ne na leđa!)."),
            ("Primena EpiPen-a:", "Ukoliko dete ima propisan autoinjektor, ubrizgati u spoljašnji deo butine pod 90°.")
        ]),
    ]
    y = 160
    for title, col, items in cards:
        draw.rounded_rectangle([(35, y), (W-35, y + 330)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 55, y + 18, title, F_CARD_TITLE, col, C_CARD, height=54)
        item_y = y + 88
        for lbl, desc in items:
            draw_item(draw, 65, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=1040, line_gap=36)
            item_y += 76
        y += 352
        
    draw.rounded_rectangle([(35, 1225), (W-35, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1262), "[URGENTNI PEDIJATRIJSKI PROTOKOL]", fill=C_GOLD, font=F_BOLD, anchor="mm")
    draw_banner_title(draw, 1322, "KOD ANAFILAKTIČKOG ŠOKA SEKUNDE SPASAVAJU ŽIVOT!", C_LINEN)
    draw.text((W//2, 1386), "Odmah pozvati 194, obezbediti prolaznost disajnih puteva i primeniti autoinjektor ako je propisan.", fill=C_SAND, font=F_BODY, anchor="mm")
    
    img.save(os.path.join(ASSETS_DIR, "slide37_allergies_anaphylaxis.png"), "PNG", optimize=True)
    print("Saved slide37_allergies_anaphylaxis.png")

if __name__ == "__main__":
    print("Generišem sve pedijatrijske i kliničke infografike za Royal Nanny V2...")
    make_slide05()
    make_slide08()
    make_slide10_wardrobe_hygiene()
    make_slide11()
    make_slide12()
    make_slide13()
    make_slide13_breast_prep()
    make_slide14()
    make_slide15()
    make_slide15_latch_technique()
    make_slide17_mastitis_protocol()
    make_slide18_milk_expression()
    make_slide19()
    make_slide20()
    make_slide21()
    make_slide22()
    make_slide23()
    make_slide24()
    make_slide24_healthy_habits()
    make_slide25()
    make_slide26()
    make_slide27()
    make_slide28()
    make_slide29_eye_infection()
    make_slide30()
    make_slide30_nasal_care()
    make_slide31()
    make_slide35_infectious_diseases()
    make_slide36_insect_bites()
    make_slide37_allergies_anaphylaxis()
    print("Sve infografike za V2 uspešno generisane sa uveličanim segmentima i optimizacijom!")
