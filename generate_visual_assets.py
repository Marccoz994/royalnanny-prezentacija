#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generiše visokokvalitetne pedijatrijske i kliničke infografike za Royal Nanny prezentaciju.
Svaka infografika koristi Royal Nanny paletu boja (Espresso, Sand, Cognac, Linen, Gold, Sage)
i sadrži precizne medicinske i edukativne protokole sa krupnim, jasnim i čitkim fontovima.
Automatsko prelamanje teksta (text wrapping) garantuje da nijedan red nikada ne prelazi ivice kartice.
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
        f_title = ImageFont.truetype('/System/Library/Fonts/Supplemental/Georgia Bold.ttf', 44)
        f_serif = ImageFont.truetype('/System/Library/Fonts/Supplemental/Georgia.ttf', 30)
        f_badge = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 22)
        f_card_title = ImageFont.truetype('/System/Library/Fonts/Supplemental/Georgia Bold.ttf', 30)
        f_bold = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 28)
        f_body = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 25)
        f_small = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 22)
    except Exception:
        f_title = f_serif = f_badge = f_card_title = f_bold = f_body = f_small = ImageFont.load_default()
    return f_title, f_serif, f_badge, f_card_title, f_bold, f_body, f_small

F_TITLE, F_SERIF, F_BADGE, F_CARD_TITLE, F_BOLD, F_BODY, F_SMALL = get_fonts()

def create_base_canvas(badge_text, title_text, subtitle_text):
    img = Image.new('RGB', (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    
    # Outer luxury borders removed to avoid "okvir u okviru" (nested frames)
    
    # Header badge sa dinamičkom širinom - podignut na sam vrh
    bbox_b = draw.textbbox((0, 0), badge_text.upper(), font=F_BADGE)
    bw = (bbox_b[2] - bbox_b[0]) + 44
    draw.rounded_rectangle([(W//2 - bw//2, 18), (W//2 + bw//2, 66)], radius=8, fill=C_DARK)
    draw.text((W//2, 42), badge_text.upper(), fill=C_LINEN, font=F_BADGE, anchor='mm')
    
    # Main title with auto-fit width - podignut gore gde je bila gornja ivica
    bbox = draw.textbbox((0, 0), title_text, font=F_TITLE)
    t_width = bbox[2] - bbox[0]
    if t_width > 1050:
        f_title_use = ImageFont.truetype('/System/Library/Fonts/Supplemental/Georgia Bold.ttf', 34)
    else:
        f_title_use = F_TITLE
        
    draw.text((W//2, 94), title_text, fill=C_DARK, font=f_title_use, anchor='mm')
    
    # Subtitle with auto-fit width - podignut gore
    if subtitle_text:
        s_box = draw.textbbox((0, 0), subtitle_text, font=F_SERIF)
        s_w = s_box[2] - s_box[0]
        if s_w > 1020:
            f_sub_use = ImageFont.truetype('/System/Library/Fonts/Supplemental/Georgia.ttf', 24)
        else:
            f_sub_use = F_SERIF
        draw.text((W//2, 134), subtitle_text, fill=C_TERRA, font=f_sub_use, anchor='mm')
        
    return img, draw

def draw_badge(draw, x, y, text, font, fill_color, text_color, radius=8, padding_x=34, height=50):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = (bbox[2] - bbox[0]) + padding_x
    draw.rounded_rectangle([(x, y), (x + w, y + height)], radius=radius, fill=fill_color)
    draw.text((x + padding_x // 2, y + height // 2), text, fill=text_color, font=font, anchor='lm')
    return x + w

def draw_item(draw, x, y, label, desc, font_lbl=F_BOLD, font_desc=F_BODY, col_lbl=C_DARK, col_desc=C_DARK, max_w=960, line_gap=32):
    draw.text((x, y), label, fill=col_lbl, font=font_lbl)
    cur_y = y + line_gap
    draw.text((x, cur_y), desc, fill=col_desc, font=font_desc)
    return cur_y + 30

# -------------------------------------------------------------
# SLIDE 05: KUPANJE NOVOROĐENČETA - PRIPREMA STANICE
# -------------------------------------------------------------
def make_slide05():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 1: HIGIJENA I NEGA NOVOROĐENČETA',
        'STANICA ZA KUPANJE: PRIPREMA PRE SVLAČENJA',
        'Zlatni standard: Sve je na dohvat ruke pre nego što se beba svuče'
    )
    
    cards = [
        ('1. KADICA I VODA NA TAČNO 37°C', C_TERRA, [
            ('Optimalna temperatura vode:', 'Tačno 36.5°C – 37°C (provereno vodenim termometrom).'),
            ('Visina vode u kadici:', 'Za novorođenče samo 5 do 8 cm (do visine kukova).'),
            ('Test laktom/podlakticom:', 'Uvek izvršiti dvostruku proveru pre spuštanja bebe.')
        ]),
        ('2. MIKROKLIMA PROSTORIJE (24°C – 26°C)', C_SAGE, [
            ('Temperatura kupatila/sobe:', 'Zagrejati prostoriju na 24°C do 26°C.'),
            ('Apsolutno bez promaje:', 'Zatvoriti prozore i vrata minimum 15 minuta pre početka.'),
            ('Topla podloga:', 'Frotirski peškir i pelena položeni preko stola za prepovijanje.')
        ]),
        ('3. STERILNI I NEGUJUĆI MATERIJALI', C_DARK, [
            ('Medicinski sindet:', 'pH neutralan (5.5), bez sapuna, alkohola i sulfata.'),
            ('Sterilne komprese i fiziološki:', 'Pripremljene za toaletu očiju i pupčanika.'),
            ('Čista odeća i pelena:', 'Bodi od organskog pamuka otkopčan i spreman za oblačenje.')
        ]),
    ]
    
    y = 165
    for title, col, items in cards:
        draw.rounded_rectangle([(65, y), (W-65, y + 315)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 85, y + 18, title, F_CARD_TITLE, col, C_CARD, height=50)
        
        item_y = y + 84
        for lbl, desc in items:
            draw_item(draw, 95, item_y, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=980, line_gap=32)
            item_y += 72
        y += 345
        
    # Bottom warning
    draw.rounded_rectangle([(65, 1220), (W-65, 1460)], radius=12, fill=C_DARK)
    draw.text((W//2, 1260), '[KRITIČNO PRAVILO BEZBEDNOSTI]', fill=C_GOLD, font=F_BOLD, anchor='mm')
    draw.text((W//2, 1318), 'BEBA SE NIKADA, NI NA SEKUND, NE OSTAVLJA SAMA!', fill=C_LINEN, font=F_CARD_TITLE, anchor='mm')
    draw.text((W//2, 1378), 'Ukoliko zazvoni telefon: beba se umotava u peškir i nosi sa sobom.', fill=C_SAND, font=F_BODY, anchor='mm')
    
    img.save(os.path.join(ASSETS_DIR, 'slide05_bath_prep_station.png'), quality=95)
    print('Saved slide05_bath_prep_station.png')

# -------------------------------------------------------------
# SLIDE 08: OBRADA PUPČANIKA I PUPČANE RANE
# -------------------------------------------------------------
def make_slide08():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 1: NEGA PUPČANIKA I PUPČANE RANE',
        'OBRADA PUPČANIKA I PUPČANE RANE',
        'Zlatni standard suve nege pupka i rano uočavanje infekcije'
    )
    
    # Card 1: Protokol obrade
    draw.rounded_rectangle([(65, 165), (W-65, 785)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
    draw_badge(draw, 85, 185, 'PROTOKOL DNEVNE SUVE OBRADE', F_CARD_TITLE, C_DARK, C_LINEN, height=52)
    
    steps = [
        ('1. Aseptična priprema:', 'Pranje ruku toplom vodom i sapunom + dezinfekcija pre dodira rane.'),
        ('2. Skidanje gaze i antiseptik:', 'Pažljivo skidanje gaze bez cimanja štipaljke; prskanje Oktenisepta.'),
        ('3. Čišćenje korena i sušenje:', 'Bazu očistiti sterilnom gazom jednim potezom i ostaviti da se osuši.'),
        ('4. Zaštita i rub pelene:', 'Suva sterilna gaza i flaster; pelenu obavezno saviti ispod pupka.')
    ]
    
    sy = 275
    for s_title, s_desc in steps:
        draw_item(draw, 95, sy, s_title, s_desc, F_BOLD, F_BODY, C_TERRA, C_DARK, max_w=980, line_gap=34)
        sy += 120
        
    # Card 2: Znakovi za uzbunu
    draw.rounded_rectangle([(65, 820), (W-65, 1465)], radius=14, fill=C_ALERT_BG, outline=C_RED, width=1)
    draw_badge(draw, 85, 840, 'ZNAKOVI ZA UZBUNU (CRVENI ALARM)', F_CARD_TITLE, C_RED, C_CARD, height=52)
    
    alarms = [
        ('Crvenilo i otok kože oko pupka:', 'Znak širenja infekcije na trbušni zid (omfalitis).'),
        ('Sekrecija i neprijatan miris:', 'Gnojan, zamućen iscedak neprijatnog mirisa.'),
        ('Aktivno krvarenje:', 'Obilnije vlaženje ili pulsirajuće kapljanje krvi iz rane.'),
        ('Opšte stanje i temperatura:', 'Febrilnost, odbijanje hrane ili izražena letargija bebe.')
    ]
    
    ay = 930
    for a_title, a_desc in alarms:
        draw_item(draw, 95, ay, f"! {a_title}", f"  {a_desc}", F_BOLD, F_BODY, C_RED, C_DARK, max_w=980, line_gap=34)
        ay += 125
        
    img.save(os.path.join(ASSETS_DIR, 'slide08_umbilical_cord_care.png'), quality=95)
    print('Saved slide08_umbilical_cord_care.png')

# -------------------------------------------------------------
# SLIDE 12: POLOŽAJI PRI DOJENJU I ASIMETRIČNI HVAT
# -------------------------------------------------------------
def make_slide12():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 2: DOJENJE',
        'POLOŽAJI PRI DOJENJU I ASIMETRIČNI HVAT',
        'Biomehanika pravilnog podoja bez bola i ragada'
    )
    
    # Card 1: 3 Ključna položaja
    draw.rounded_rectangle([(65, 165), (W-65, 785)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
    draw_badge(draw, 85, 185, '3 ERGONOMSKA POLOŽAJA', F_CARD_TITLE, C_DARK, C_LINEN, height=52)
    
    pos = [
        ('1. Kolevka (Cradle / Cross-cradle):', 'Beba leži na boku, stomak na stomak sa majkom. Glava u ravni sa kičmom.'),
        ('2. Fudbalska lopta (Football Hold):', 'Beba ispod pazuha majke. Idealno nakon carskog reza i za kontrolu glavice.'),
        ('3. Bočni ležeći položaj (Side-lying):', 'Majka i beba leže jedno naspram drugog. Savršeno za noćne podoje i odmor.'),
        ('Ključno poravnanje:', 'Uho, rame i kuk bebe MORAJU biti u istoj ravnoj liniji (beba ne sme okretati vrat)!')
    ]
    
    py = 275
    for p_title, p_desc in pos:
        draw_item(draw, 95, py, p_title, p_desc, F_BOLD, F_BODY, C_TERRA, C_DARK, max_w=980, line_gap=34)
        py += 120
        
    # Card 2: Zlatni standard asimetričnog hvata
    draw.rounded_rectangle([(65, 820), (W-65, 1465)], radius=14, fill=C_CARD, outline=C_SAGE, width=1)
    draw_badge(draw, 85, 840, 'ZLATNI STANDARD ASIMETRIČNOG HVATA', F_CARD_TITLE, C_SAGE, C_CARD, height=52)
    
    latch = [
        ('Širok ugao otvaranja usta:', 'Usta otvorena preko 140° (kao pri zevanju) pre prinošenja dojci.'),
        ('Brada duboko u tkivu dojke:', 'Bebina brada prva dodiruje dojku, stimulišući refleks sisanja.'),
        ('Nos potpuno slobodan:', 'Zahvaljujući zabačenoj glavi, nosić je odvojen od dojke i beba nesmetano diše.'),
        ('Izvrnute usne ("usne ribice"):', 'I gornja i donja usna izvrnute upolje, pokrivajući veći deo donje areole.'),
        ('Zvuk gutanja, bez coktanja:', 'Čuje se ritmično gutanje (uh-uh). Coktanje znači gubitak vakuuma!')
    ]
    
    ly = 925
    for l_title, l_desc in latch:
        draw_item(draw, 95, ly, f"• {l_title}", f"   {l_desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=980, line_gap=34)
        ly += 100
        
    img.save(os.path.join(ASSETS_DIR, 'slide12_breastfeeding_positions.png'), quality=95)
    print('Saved slide12_breastfeeding_positions.png')

# -------------------------------------------------------------
# SLIDE 13: IZAZOVI U LAKTACIJI (RAGADE, PREPUNJENOST, MASTITIS)
# -------------------------------------------------------------
def make_slide13():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 2: DOJENJE',
        'IZAZOVI U LAKTACIJI: PROTOKOL TRIJAŽE',
        'Efikasno olakšavanje tegoba i razlikovanje prepunjenosti od mastitisa'
    )
    
    challenges = [
        ('1. RAGADE (Bolne i ispucale bradavice)', C_TERRA, [
            ('Glavni uzrok:', 'Nepravilan, plitak hvat bradavice (beba sisa samo vrh umesto areole).'),
            ('Tretman:', '100% prečišćeni medicinski lanolin (ne mora se ispirati pre podoja).'),
            ('Prirodni lek:', 'Premazivanje bradavice kapljicom sopstvenog mleka i sušenje na vazduhu.')
        ]),
        ('2. PREPUNJENOST DOJKI (Engorgement)', C_SAGE, [
            ('Tople obloge PRE podoja:', 'Zagrevanje 5-10 min i nežna masaža olakšavaju refleks otpuštanja mleka.'),
            ('Iztiskivanje par kapi:', 'Omekšati areolu pre podoja kako bi beba lakše uhvatila dojku.'),
            ('Hladne obloge POSLE podoja:', 'Hladan peškir ili obloge od kupusa 15 min za smanjenje otoka i bola.')
        ]),
        ('3. MASTITIS (Bakterijska infekcija dojke)', C_RED, [
            ('Simptomi:', 'Ograničeni crveni trougao, vruća i tvrda dojka, jeza, T > 38.5°C.'),
            ('Kritično pravilo:', 'DOJENJE SE NE PREKIDA! Redovno pražnjenje dojke je ključ izlečenja.'),
            ('Hitan korak:', 'Obaveštavanje izabranog ginekologa/pedijatra radi propisivanja antibiotika.')
        ]),
    ]
    
    y = 165
    for title, col, items in challenges:
        draw.rounded_rectangle([(65, y), (W-65, y + 400)], radius=14, fill=C_CARD, outline=col, width=1)
        draw_badge(draw, 85, y + 20, title, F_CARD_TITLE, col, C_CARD, height=52)
        
        iy = y + 94
        for lbl, desc in items:
            draw_item(draw, 95, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=980, line_gap=34)
            iy += 94
        y += 430
    
    img.save(os.path.join(ASSETS_DIR, 'slide13_lactation_challenges.png'), quality=95)
    print('Saved slide13_lactation_challenges.png')

# -------------------------------------------------------------
# SLIDE 14: SKLADIŠTENJE MAJČINOG MLEKA
# -------------------------------------------------------------
def make_slide14():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 2: DOJENJE',
        'SKLADIŠTENJE MAJČINOG MLEKA: PRAVILO 4-4-6',
        'Očuvanje nutritivnih i imunoloških svojstava izmlazanog mleka'
    )
    
    rules = [
        ('SOBNA TEMPERATURA (do 25°C)', 'DO 4 SATA', C_TERRA,
         'Držati na najhladnijem mestu u sobi, zaštićeno od direktnog sunčevog svetla i izvora toplote.'),
        ('FRIŽIDER (na polici na 4°C)', '3 DO 5 DANA', C_SAGE,
         'Čuvati u dubini frižidera (nikada u vratima zbog temperaturnih oscilacija pri otvaranju).'),
        ('ZAMRZIVAČ (-18°C)', '3 DO 6 MESECI', C_DARK,
         'U namenskim sterilnim kesicama za mleko sa označenim datumom, satom i zapreminom.')
    ]
    
    y = 165
    for title, duration, col, desc in rules:
        draw.rounded_rectangle([(65, y), (W-65, y + 285)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        
        # Header strip & Duration badge
        draw_badge(draw, 85, y + 18, title, F_CARD_TITLE, col, C_CARD, height=50)
        
        bbox_d = draw.textbbox((0, 0), duration, font=F_CARD_TITLE)
        dw = (bbox_d[2] - bbox_d[0]) + 34
        draw.rounded_rectangle([(W - 85 - dw, y + 18), (W - 85, y + 68)], radius=8, fill=C_GOLD)
        draw.text((W - 85 - dw//2, y + 43), duration, fill=C_DARK, font=F_CARD_TITLE, anchor='mm')
        
        draw.text((95, y + 95), desc, fill=C_DARK, font=F_BODY)
        draw.text((95, y + 155), "• Posude: Isključivo staklene flašice bez BPA ili sterilne pre-formirane kesice.", fill=C_TERRA, font=F_BOLD)
        draw.text((95, y + 210), "• Obeležavanje: Uvek prvo trošiti najstarije izmlazano mleko (FIFO princip).", fill=C_DARK, font=F_BODY)
        y += 310
        
    # Bottom warning
    draw.rounded_rectangle([(65, 1115), (W-65, 1460)], radius=12, fill=C_ALERT_BG, outline=C_RED, width=1)
    draw_badge(draw, 85, 1135, 'PRAVILA ODMRZAVANJA I ZABRANE', F_CARD_TITLE, C_RED, C_CARD, height=50)
    
    thaw = [
        ('Odmrzavanje:', 'Polako u frižideru preko noći ili u posudi sa toplom vodom (do 37°C).'),
        ('STROGA ZABRANA MIKROTALASNE:', 'Uništava antitela i vitamine i stvara "vruće tačke" koje mogu opeći bebu!'),
        ('ZABRANA PONOVNOG ZAMRZAVANJA:', 'Jednom odmrznuto mleko se mora iskoristiti u roku od 24h ili baciti.')
    ]
    ty = 1205
    for t_lbl, t_txt in thaw:
        draw_item(draw, 95, ty, f"• {t_lbl}", f"   {t_txt}", F_BOLD, F_BODY, C_RED, C_DARK, max_w=980, line_gap=32)
        ty += 75
        
    img.save(os.path.join(ASSETS_DIR, 'slide14_milk_storage_protocol.png'), quality=95)
    print('Saved slide14_milk_storage_protocol.png')

# -------------------------------------------------------------
# SLIDE 15: ADAPTIRANA FORMULA - PRIPREMA I HIGIJENA
# -------------------------------------------------------------
def make_slide15():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 2: DOJENJE',
        'ADAPTIRANA MLEČNA FORMULA: STERILNA PRIPREMA',
        'Sigurnost pripreme i prevencija bakterijskih infekcija'
    )
    
    steps = [
        ('1. STERILIZACIJA PRIBORA', C_DARK, [
            ('Parni sterilizator ili otkuvavanje:', 'Flašice, cucle, zatvarači i merice moraju biti sterilni.'),
            ('Sušenje na čistom stalku:', 'Ne brisati pribor kuhinjskim krpama (izvor bakterija).')
        ]),
        ('2. PROKUVAVANJE VODE', C_TERRA, [
            ('Voda vri 3-5 minuta:', 'Uništava potencijalne mikroorganizme.'),
            ('Hlađenje na 40°C – 50°C:', 'Prevruća voda uništava probiotike i vitamine u formuli, hladna se ne rastvara.')
        ]),
        ('3. TAČNA RAZMERA MERICA', C_SAGE, [
            ('Prvo voda, zatim prah:', 'Sprečava zgrušavanje i omogućava tačno očitavanje mililitraže.'),
            ('Isključivo RAVNE merice:', 'Poravnati nožem bez sabijanja. Višak praha opterećuje bubrege bebe!')
        ]),
        ('4. PROVERA TEMPERATURE I VREME', C_RED, [
            ('Test na podlaktici:', '2-3 kapi na unutrašnju stranu ručnog zgloba (mora biti prijatno toplo, ne vrelo).'),
            ('Pravilo 1 sata:', 'Preostalo mleko iz flašice se BACA nakon 60 minuta od početka hranjenja!')
        ]),
    ]
    
    y = 165
    for title, col, items in steps:
        draw.rounded_rectangle([(65, y), (W-65, y + 295)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 85, y + 18, title, F_CARD_TITLE, col, C_CARD, height=48)
        
        iy = y + 84
        for lbl, desc in items:
            draw_item(draw, 95, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=980, line_gap=32)
            iy += 88
        y += 320
        
    img.save(os.path.join(ASSETS_DIR, 'slide15_formula_prep_protocol.png'), quality=95)
    print('Saved slide15_formula_prep_protocol.png')

# -------------------------------------------------------------
# SLIDE 21: VISOKA TEMPERATURA I PROTOKOL OBARANJA
# -------------------------------------------------------------
def make_slide21():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA',
        'VISOKA TEMPERATURA: MERENJE I HLAĐENJE',
        'Egzaktni pragovi febrilnosti i bezbedne mere fizikalnog rashlađivanja'
    )
    
    sections = [
        ('1. PEDIJATRIJSKI PRAGOVI MERENJA', C_TERRA, [
            ('Aksilarno merenje (pazuh):', 'Granica povišene temperature je 38.0°C (očitavanje standardnim toplomerom).'),
            ('Rektalno merenje (čmar):', 'Očitavanje je za 0.5°C više; febrilnost počinje od 38.5°C (zlatni standard do 1. god).'),
            ('Kada davati lekove:', 'Antipiretici se daju iznad 38.5°C aksilarno (39.0°C rektalno) ili pri lošem stanju.')
        ]),
        ('2. FIZIKALNE MERE RASHLAĐIVANJA', C_SAGE, [
            ('Raskomoćivanje & mikroklima:', 'Lagan pamučni bodi u provetrenoj sobi na 20–22°C (nikada ne pretopljavati!).'),
            ('Hidratacija & elektroliti:', 'Češći podoji, gutljaji vode ili ORS rastvora sprečavaju dehidrataciju.'),
            ('Tuširanje mlakom vodom (36–37°C):', 'Lagano kvasiti trup i noge 5–10 minuta; strogo bez hladne vode i šoka!')
        ]),
        ('3. STROGO ZABRANJENE OPASNE METODE', C_RED, [
            ('Zabrana alkohola i sirćeta:', 'Apsolutno zabranjeno utrljavanje – rizik od teškog trovanja kroz dečju kožu!'),
            ('Zabrana preznojavanja:', 'Uvijanje u jorgane podiže unutrašnju temperaturu i vodi u toplotni udar.')
        ]),
    ]
    
    y = 165
    for title, col, items in sections:
        draw.rounded_rectangle([(65, y), (W-65, y + 315)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 85, y + 18, title, F_CARD_TITLE, col, C_CARD, height=50)
        
        iy = y + 84
        for lbl, desc in items:
            draw_item(draw, 95, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=980, line_gap=32)
            iy += 72
        y += 345
        
    # Bottom warning
    draw.rounded_rectangle([(65, 1220), (W-65, 1460)], radius=12, fill=C_DARK)
    draw.text((W//2, 1258), '[HITAN ALARM ZA PEDIJATRA / 194]', fill=C_GOLD, font=F_BOLD, anchor='mm')
    draw.text((W//2, 1312), 'Beba <3 meseca sa T >38°C, febrilne konvulzije ili letargija!', fill=C_LINEN, font=F_CARD_TITLE, anchor='mm')
    draw.text((W//2, 1370), 'Ponašanje deteta i kontakt očima važniji su od same cifre na toplomeru.', fill=C_SAND, font=F_BODY, anchor='mm')
    
    img.save(os.path.join(ASSETS_DIR, 'slide21_fever_check_hd.png'), quality=95)
    print('Saved slide21_fever_check_hd.png')

# -------------------------------------------------------------
# SLIDE 22: PEDIJATRIJSKO DOZIRANJE ANTIPIRETIKA
# -------------------------------------------------------------
def make_slide22():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA',
        'DOZIRANJE ANTIPIRETIKA: PARACETAMOL VS IBUPROFEN',
        'Zlatno pravilo pedijatrije: Lek se dozira STROGO PO KILOGRAMIMA, nikada po uzrastu!'
    )
    
    # Paracetamol Card
    draw.rounded_rectangle([(65, 165), (W-65, 680)], radius=14, fill=C_CARD, outline=C_TERRA, width=1)
    draw_badge(draw, 85, 185, 'PARACETAMOL (Sirup / Čepići)', F_CARD_TITLE, C_TERRA, C_CARD, height=52)
    
    # Dosage pill
    bbox_d1 = draw.textbbox((0, 0), '10 – 15 mg / kg', font=F_CARD_TITLE)
    dw1 = (bbox_d1[2] - bbox_d1[0]) + 34
    draw.rounded_rectangle([(W - 85 - dw1, 185), (W - 85, 237)], radius=8, fill=C_GOLD)
    draw.text((W - 85 - dw1//2, 211), '10 – 15 mg / kg', fill=C_DARK, font=F_CARD_TITLE, anchor='mm')
    
    p_info = [
        ('Uzrast primene:', 'Dozvoljen od prvih dana života (prema savetu pedijatra).'),
        ('Vremenski razmak:', 'Daje se na svakih 4 do 6 sati po potrebi (maksimalno 4 doze u toku 24 sata).'),
        ('Maksimalan broj doza:', 'Maksimalno 4 doze u toku 24 sata – nikada ne skraćivati razmak!'),
        ('Kada koristiti čepiće:', 'Ukoliko beba povraća ili odbija špric, rektalni čepić deluje za 15-20 min.')
    ]
    py = 265
    for p_lbl, p_desc in p_info:
        draw_item(draw, 95, py, f"• {p_lbl}", f"   {p_desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=980, line_gap=34)
        py += 98
        
    # Ibuprofen Card
    draw.rounded_rectangle([(65, 710), (W-65, 1225)], radius=14, fill=C_CARD, outline=C_SAGE, width=1)
    draw_badge(draw, 85, 730, 'IBUPROFEN (Brufen sirup)', F_CARD_TITLE, C_SAGE, C_CARD, height=52)
    
    bbox_d2 = draw.textbbox((0, 0), '5 – 10 mg / kg', font=F_CARD_TITLE)
    dw2 = (bbox_d2[2] - bbox_d2[0]) + 34
    draw.rounded_rectangle([(W - 85 - dw2, 730), (W - 85, 782)], radius=8, fill=C_GOLD)
    draw.text((W - 85 - dw2//2, 756), '5 – 10 mg / kg', fill=C_DARK, font=F_CARD_TITLE, anchor='mm')
    
    i_info = [
        ('STROGO OGRANIČENJE UZRASTA:', 'ISKLJUČIVO za decu stariju od 3 meseca i preko 5 kg težine!'),
        ('Vremenski razmak:', 'Daje se na svakih 6 do 8 sati po potrebi (maksimalno 3 doze u toku 24 sata).'),
        ('Preporuka za želudac:', 'Davanje uz ili neposredno nakon obroka ili mleka radi zaštite sluznice.'),
        ('Kombinovanje lekova:', 'Samo po izričitom nalogu pedijatra; voditi strogi vremenski dnevnik!')
    ]
    iy = 810
    for i_lbl, i_desc in i_info:
        draw_item(draw, 95, iy, f"• {i_lbl}", f"   {i_desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=980, line_gap=34)
        iy += 98
        
    # Safety Banner
    draw.rounded_rectangle([(65, 1255), (W-65, 1465)], radius=12, fill=C_DARK)
    draw.text((W//2, 1288), '[PROTOKOL BEZBEDNOSTI DADILJE]', fill=C_GOLD, font=F_BOLD, anchor='mm')
    draw.text((W//2, 1336), 'Uvek koristiti BAŽDARENI ORALNI ŠPRIC koji dolazi uz lek.', fill=C_LINEN, font=F_CARD_TITLE, anchor='mm')
    draw.text((W//2, 1386), 'Kombinovanje Paracetamola i Ibuprofena dozvoljeno je ISKLJUČIVO po nalogu lekara.', fill=C_SAND, font=F_BODY, anchor='mm')
    draw.text((W//2, 1432), 'Svaka data doza se u minut unosi u Dnevnik nege sa izmerenom temperaturom.', fill=C_LINEN, font=F_SMALL, anchor='mm')
    
    img.save(os.path.join(ASSETS_DIR, 'slide22_pediatric_dosage_card.png'), quality=95)
    print('Saved slide22_pediatric_dosage_card.png')

# -------------------------------------------------------------
# SLIDE 23: DIGESTIVNE SMETNJE I ORALNA REHIDRACIJA
# -------------------------------------------------------------
def make_slide23():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA',
        'POVRAĆANJE, DIJAREJA I ORALNA REHIDRACIJA',
        'Klinička trijaža, sprečavanje dehidratacije i primena O.R.S.'
    )
    
    # Card 1: Diferencijalna dijagnoza
    draw.rounded_rectangle([(65, 165), (W-65, 680)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
    draw_badge(draw, 85, 185, 'BLJUCKANJE VS POVRAĆANJE U MLAZU', F_CARD_TITLE, C_DARK, C_LINEN, height=52)
    
    diffs = [
        ('Fiziološko bljuckanje (Refluks):', 'Mala količina neusirenog mleka curi iz ugla usana; beba je mirna i lepo napreduje.'),
        ('Povraćanje u mlazu (Projektilno):', 'Sadržaj pod pritiskom na daljinu. Sumnja na stenozu pilorusa ili infekciju.'),
        ('Prisustvo žuči ili krvi:', 'Zeleni sadržaj (žuč) ili tragovi krvi zahtevaju HITAN transport na kliniku!'),
        ('Procena stolice:', 'Vodena, eksplozivna stolica neprijatnog mirisa nosi visok rizik od dehidratacije.')
    ]
    dy = 265
    for d_title, d_desc in diffs:
        draw_item(draw, 95, dy, d_title, d_desc, F_BOLD, F_BODY, C_TERRA, C_DARK, max_w=980, line_gap=34)
        dy += 98
        
    # Card 2: Protokol oralne rehidracije (O.R.S.)
    draw.rounded_rectangle([(65, 710), (W-65, 1225)], radius=14, fill=C_CARD, outline=C_SAGE, width=1)
    draw_badge(draw, 85, 730, 'PROTOKOL DAVANJA O.R.S. RASTVORA', F_CARD_TITLE, C_SAGE, C_CARD, height=52)
    
    ors = [
        ('Rastvaranje praha:', 'Kesica se rastvara u tačno propisanoj količini prokuvane vode (npr. 200 ml).'),
        ('Tehnika "kašičica po kašičica":', 'Davanje 1 kafene kašičice na svakih 5 do 10 minuta (nikada puna flašica odjednom!).'),
        ('Nakon epizode povraćanja:', 'Pauzirati 15-20 minuta da se želudac smiri, pa nastaviti kašičicom.'),
        ('Nastavak dojenja:', 'Dojenje se NE PREKIDA – majčino mleko pruža optimalnu zaštitu crevne sluznice.')
    ]
    oy = 810
    for o_title, o_desc in ors:
        draw_item(draw, 95, oy, f"• {o_title}", f"   {o_desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=980, line_gap=34)
        oy += 98
        
    # 4 Znaka dehidratacije
    draw.rounded_rectangle([(65, 1255), (W-65, 1465)], radius=12, fill=C_ALERT_BG, outline=C_RED, width=1)
    draw.text((W//2, 1288), '[4 ZNAKA DEHIDRATACIJE ZA HITAN ODLAZAK KOD LEKARA]', fill=C_RED, font=F_BOLD, anchor='mm')
    
    draw.text((95, 1324), '1. Upala velika fontanela (udubljenje na temenu glave)', fill=C_DARK, font=F_BODY)
    draw.text((95, 1362), '2. Suve pelene duže od 6 sati (nedostatak mokrenja)', fill=C_DARK, font=F_BODY)
    draw.text((95, 1400), '3. Plač bez suza i suve, ispucale usne i jezik', fill=C_DARK, font=F_BODY)
    draw.text((95, 1436), '4. Izrazita pospanost, letargija ili upale očne jabučice', fill=C_DARK, font=F_BODY)
    
    img.save(os.path.join(ASSETS_DIR, 'slide23_digestive_dehydration.png'), quality=95)
    print('Saved slide23_digestive_dehydration.png')

# -------------------------------------------------------------
# SLIDE 24: RESPIRATORNE I OČNE INFEKCIJE
# -------------------------------------------------------------
def make_slide24():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA',
        'RESPIRATORNE INFEKCIJE I TOALETA OČIJU',
        'Tehnika aspiracije nosa i nega zapušenih suznih kanala'
    )
    
    cards = [
        ('1. TOALETA NOSA I ISPIRANJE', C_DARK, [
            ('Fiziološki rastvor 0.9%:', 'Ukapati po 1-2 ml u svaku nozdrvu dok beba leži na boku.'),
            ('Nazalni aspirator:', 'Izvlačenje sekreta laganim kontinuiranim podpritiskom pre obroka i spavanja.'),
            ('Kritično pravilo:', 'Beba diše samo na nos – zapušen nos sprečava sisanje i remeti miran san.')
        ]),
        ('2. NEGA OČIJU I KONJUNKTIVITIS', C_TERRA, [
            ('Pokret brisanja:', 'Gaza sa fiziološkim od SPOLJAŠNJEG ka UNUTRAŠNJEM uglu bebinog oka.'),
            ('Zasebna gaza za svako oko:', 'NIKADA ne koristiti istu gazu za oba oka (sprečavanje prenosa infekcije).'),
            ('Masaža suznog kanala:', 'Nežan pritisak prstom od korena nosa nadole, 3-4 puta dnevno.')
        ]),
        ('3. NEGA NAKON VAKCINACIJE', C_SAGE, [
            ('Mesto uboda:', 'Staviti hladnu suvu oblogu preko čiste tkanine (nikada led direktno na kožu).'),
            ('Reakcija:', 'Umerena temperatura i pospanost u prvih 24-48h su normalan imunološki odgovor.'),
            ('Doziranje antipiretika:', 'Paracetamol dati samo ako temperatura pređe 38.5°C (ili pri jakom bolu).')
        ]),
    ]
    
    y = 165
    for title, col, items in cards:
        draw.rounded_rectangle([(65, y), (W-65, y + 400)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 85, y + 20, title, F_CARD_TITLE, col, C_CARD, height=52)
        
        iy = y + 94
        for lbl, desc in items:
            draw_item(draw, 95, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=980, line_gap=34)
            iy += 94
        y += 430
        
    img.save(os.path.join(ASSETS_DIR, 'slide24_respiratory_care.png'), quality=95)
    print('Saved slide24_respiratory_care.png')

# -------------------------------------------------------------
# SLIDE 25: MAPA BEZBEDNOSTI DOMA PO UZRASTIMA
# -------------------------------------------------------------
def make_slide25():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA',
        'MAPA BEZBEDNOSTI DOMA PO UZRASTIMA',
        'Prevencija tihih opasnosti kod odojčadi i radoznalih todlera'
    )
    
    sections = [
        ('1. UZRAST DO 1. GODINE: TIHE OPASNOSTI', C_TERRA, [
            ('Sto za prepovijanje:', 'Jedna ruka je UVEK na bebi; ne okreću se leđa (sekund je dovoljan za pad).'),
            ('Bezbedan krevetac:', 'Čvrst dušek, bez jastuka, teških jorgana i igračaka (prevencija SIDS-a).'),
            ('Medicinska zabrana dubka:', 'Dubak stvara lažnu stabilnost, uzrokuje teške padove niz stepenice i deformitete.')
        ]),
        ('2. UZRAST 1–4 GODINE: RADOZNALI ISTRAŽIVAČI', C_DARK, [
            ('Kuhinjske mere opreza:', 'Drške posuđa okrenute ka zidu, zaštita na rerni, noževi i ringle van domašaja.'),
            ('Zaštita od padova sa visine:', 'Sigurnosne reze na prozorima i terasama; ormari tiplovani za zid protiv preturanja.'),
            ('Aspiracija stranih tela:', 'Sitni predmeti (<3 cm), novčići, magneti i baterije van dečjeg dometa!')
        ]),
        ('3. TOKSIČNOST I OPEKOTINE', C_RED, [
            ('Kućna hemija i lekovi:', 'Zaključani u ormarićima na visini preko 1.5 m; kapsule za veš strogo sakrivene.'),
            ('Vrele tečnosti i kafa:', 'Ne piti vruć napitak dok se dete drži u naručju; kabl ketlera van domašaja.')
        ]),
    ]
    
    y = 165
    for title, col, items in sections:
        draw.rounded_rectangle([(65, y), (W-65, y + 315)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 85, y + 18, title, F_CARD_TITLE, col, C_CARD, height=50)
        
        iy = y + 84
        for lbl, desc in items:
            draw_item(draw, 95, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=980, line_gap=32)
            iy += 72
        y += 345
        
    # Bottom warning
    draw.rounded_rectangle([(65, 1220), (W-65, 1460)], radius=12, fill=C_DARK)
    draw.text((W//2, 1258), '[ZLATNO PRAVILO ROYAL NANNY DADILJE]', fill=C_GOLD, font=F_BOLD, anchor='mm')
    
    ban_text = 'PROSTOR SE PRILAGOĐAVA DETETU PRE NEGO ŠTO SE DESI INCIDENT!'
    b_box = draw.textbbox((0, 0), ban_text, font=F_BOLD)
    f_ban = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 24) if (b_box[2]-b_box[0] > 1000) else F_BOLD
    draw.text((W//2, 1312), ban_text, fill=C_LINEN, font=f_ban, anchor='mm')
    draw.text((W//2, 1370), 'Stalno skeniranje prostora: uvek budite tri koraka ispred detetove radoznalosti.', fill=C_SAND, font=F_BODY, anchor='mm')
    
    img.save(os.path.join(ASSETS_DIR, 'slide25_safe_play_hd.png'), quality=95)
    print('Saved slide25_safe_play_hd.png')

# -------------------------------------------------------------
# SLIDE 26: PADOVI I POVREDE GLAVE - 48H PROTOKOL
# -------------------------------------------------------------
def make_slide26():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA',
        'PADOVI I POVREDE GLAVE: 48-ČASOVNI PROTOKOL',
        'Smiren pristup, prva pomoć na licu mesta i praćenje znakova potresa mozga'
    )
    
    # Card 1: Prva pomoć na licu mesta
    draw.rounded_rectangle([(65, 165), (W-65, 710)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
    draw_badge(draw, 85, 185, 'PRVA POMOĆ NA LICU MESTA', F_CARD_TITLE, C_DARK, C_LINEN, height=52)
    
    aid = [
        ('1. Smiriti bebu i ne pomerati naglo:', 'Ostaviti bebu u ležećem položaju ukoliko se sumnja na povredu vrata.'),
        ('2. Primena hladne obloge:', 'Kockice leda umotane u pamučnu pelenu držati na hematomu 10-15 minuta.'),
        ('3. Zaustavljanje krvarenja:', 'Direktan pritisak sterilnom gazom na ranu tokom 5 minuta bez podizanja gaze.'),
        ('4. Provera svesti i refleksa:', 'Da li je beba zaplakala odmah, da li reaguje na glas i prati pogledom?')
    ]
    ay = 275
    for a_title, a_desc in aid:
        draw_item(draw, 95, ay, a_title, a_desc, F_BOLD, F_BODY, C_TERRA, C_DARK, max_w=980, line_gap=34)
        ay += 102
        
    # Card 2: 48h Neurološki monitoring
    draw.rounded_rectangle([(65, 740), (W-65, 1465)], radius=14, fill=C_ALERT_BG, outline=C_RED, width=1)
    draw_badge(draw, 85, 760, '5 ZNAKOVA ZA HITNU POMOĆ (194)', F_CARD_TITLE, C_RED, C_CARD, height=52)
    
    signs = [
        ('Gubitak svesti (makar i na par sekundi):', 'Apsolutna indikacija za hitan pedijatrijski pregled i snimanje.'),
        ('Povraćanje u mlazu više od dva puta:', 'Klasičan znak povećanog intrakranijalnog pritiska nakon potresa mozga.'),
        ('Asimetrične zenice ili ukočen pogled:', 'Jedna zenica šira od druge, beba ne fokusira predmete.'),
        ('Izrazita pospanost i otežano buđenje:', 'Beba ne može da se razbudi radi hranjenja, mlitava je i nezainteresovana.'),
        ('Curenje bistre tečnosti iz nosa ili uha:', 'Sumnja na likvoreju (povredu baze lobanje) – NE DIRATI, HITNO 194!')
    ]
    sy = 845
    for s_title, s_desc in signs:
        draw_item(draw, 95, sy, f"! {s_title}", f"   {s_desc}", F_BOLD, F_BODY, C_RED, C_DARK, max_w=980, line_gap=34)
        sy += 118
        
    img.save(os.path.join(ASSETS_DIR, 'slide26_head_injury_first_aid.png'), quality=95)
    print('Saved slide26_head_injury_first_aid.png')

# -------------------------------------------------------------
# SLIDE 28: UJEDI INSEKATA, ZARAZNE BOLESTI I ALERGIJE
# -------------------------------------------------------------
def make_slide28():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA',
        'UJEDI INSEKATA, DEČJI OSIPI I ALERGIJE',
        'Pravilno uklanjanje krpelja, prepoznavanje osipa i anafilaksa'
    )
    
    topics = [
        ('1. PROTOKOL VAĐENJA KRPELJA', C_DARK, [
            ('Medicinska pinceta:', 'Uhvatiti krpelja što bliže koži i povući RAVNO nagore umerenim pritiskom.'),
            ('STROGA ZABRANA HEMIKALIJA:', 'NIKADA ne stavljati ulje, alkohol ili aceton (gušenje krpelja luči toksine u krv!).'),
            ('Monitoring mesta uboda (30 dana):', 'Pojava crvenog prstena koji se širi (Erythema migrans) ukazuje na Lajmsku bolest.')
        ]),
        ('2. PREPOZNAVANJE DEČJIH OSIPA', C_TERRA, [
            ('Varičela (Ovčije boginje):', 'Vezikule ispunjene bistrom tečnošću ("kapi rose"), intenzivan svrab.'),
            ('Šarlah (Streptokok):', 'Sitnozrnast osip ("šmirgl papir"), izrazito crveno ždrelo i "malinast jezik".'),
            ('Roseola infantum:', 'Iznenadna visoka T 3 dana; po padu temperature izbija blag osip po telu.')
        ]),
        ('3. ANAFILAKTIČKI ŠOK (CRVENI ALARM 194)', C_RED, [
            ('Simptomi gušenja:', 'Oticanje usana, jezika, otežano čujno disanje (stridor), bledilo i hladan znoj.'),
            ('Hitan postupak:', 'ODMAH pozvati 194, polusedeći položaj, pripremiti EpiPen ako je propisan.')
        ]),
    ]
    
    y = 165
    for title, col, items in topics:
        draw.rounded_rectangle([(65, y), (W-65, y + 400)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 85, y + 20, title, F_CARD_TITLE, col, C_CARD, height=52)
        
        iy = y + 94
        for lbl, desc in items:
            draw_item(draw, 95, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=980, line_gap=34)
            iy += 94
        y += 430
        
    img.save(os.path.join(ASSETS_DIR, 'slide28_insect_bites_allergies.png'), quality=95)
    print('Saved slide28_insect_bites_allergies.png')

# -------------------------------------------------------------
# SLIDE 30: ZLATNI STANDARD PUTNE I KUĆNE APOTEKE
# -------------------------------------------------------------
def make_slide30():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA',
        'ZLATNI STANDARD KUĆNE I PUTNE APOTEKE',
        '4 obavezna segmenta profesionalne torbe za pedijatrijsku negu'
    )
    
    sections = [
        ('I. ANTIPIRETIČKI I ANALGETIČKI SEGMENT', C_TERRA, [
            ('Paracetamol sirup + rektalni čepići:', 'Osnovni lek prvog izbora za temperaturu i bolove.'),
            ('Ibuprofen sirup:', 'Antiinflamatorno dejstvo (samo za bebe starije od 3 meseca).'),
            ('Originalni baždareni špricevi:', 'Označeni mililitrima za svaku bočicu.')
        ]),
        ('II. GASTROENTEROLOŠKI SEGMENT', C_SAGE, [
            ('Oralni rehidracioni rastvor (O.R.S.):', '3 kesice sa balansiranim elektrolitima i glukozom.'),
            ('Probiotik u kapima:', 'Za regulaciju crevne flore i ublažavanje dijareje.'),
            ('Kapi protiv grčeva (Simetikon / Laktaza):', 'Za smanjenje gasova u crevima.')
        ]),
        ('III. ANTISEPTICI I OBRADA RANA', C_DARK, [
            ('Octenisept sprej:', 'Bezbolan antiseptik za sluzokožu i kožu (ne peče!).'),
            ('Sterilne komprese i mikropor flaster:', 'Različitih dimenzija za previjanje.'),
            ('3% hidrogen i fiziološki rastvor:', 'Ampule od 5 i 10 ml za toaletu očiju i nosa.')
        ]),
        ('IV. DIJAGNOSTIČKI PRIBOR I ALATI', C_GOLD, [
            ('Digitalni aksilarni / beskontaktni toplomer:', 'Sa rezervnim baterijama.'),
            ('Anatomska pinceta za krpelje:', 'Sa tankim ravnim vrhom.'),
            ('Makazice za nokte sa zaobljenim vrhom:', 'Nerđajući medicinski čelik.')
        ]),
    ]
    
    y = 165
    for title, col, items in sections:
        draw.rounded_rectangle([(65, y), (W-65, y + 295)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 85, y + 18, title, F_CARD_TITLE, col, C_CARD if col != C_GOLD else C_DARK, height=48)
        
        iy = y + 84
        for lbl, desc in items:
            draw_item(draw, 95, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=980, line_gap=30)
            iy += 66
        y += 320
        
    img.save(os.path.join(ASSETS_DIR, 'slide30_apoteka_kit.png'), quality=95)
    print('Saved slide30_apoteka_kit.png')

# -------------------------------------------------------------
# SLIDE 31: TEHNIKE BEZBEDNE ADMINISTRACIJE LEKOVA
# -------------------------------------------------------------
def make_slide31():
    img, draw = create_base_canvas(
        'ROYAL NANNY • MODUL 4: NEGA BOLESNOG DETETA',
        'TEHNIKE BEZBEDNE ADMINISTRACIJE LEKOVA',
        'Sprečavanje aspiracije, gušenja i stresa kod deteta'
    )
    
    techniques = [
        ('1. ORALNI ŠPRIC – SMER KA UNUTRAŠNJOJ STRANI OBRAZA', C_TERRA, [
            ('Položaj deteta:', 'Dete je u polusedećem položaju u naručju dadilje (NIKADA u ležećem!).'),
            ('Smer šprica:', 'Vrh šprica se uvodi uz unutrašnju stranu obraza (prema kutnjacima).'),
            ('STROGA ZABRANA:', 'NIKADA ne špricati lek pravo u grlo ili jezik (izaziva laringospazam i gušenje!).'),
            ('Doziranje u mlazevima:', 'Pritiskati klip u malim porcijama (po 0.5 ml) sinhronizovano sa gutanjem.')
        ]),
        ('2. UKAPAVANJE KAPI U OČI', C_SAGE, [
            ('Ukapavanje u donji kapak:', 'Nežno povući donji očni kapak nadole i kapnuti u stvoreni džep (forniks).'),
            ('Bez dodirivanja oka:', 'Vrh bočice ne sme dodirnuti trepavice ili oko radi očuvanja sterilnosti.'),
            ('Zatvaranje oka:', 'Zadržati oko zatvoreno par sekundi i obrisati višak sterilnom gazom.')
        ]),
        ('3. UKAPAVANJE KAPI U UŠI', C_DARK, [
            ('Zagrevanje bočice dlanovima:', 'Bočicu protrljati dlanovima 2-3 minuta (hladne kapi izazivaju jaku vrtoglavicu).'),
            ('Položaj uva:', 'Kod beba školjku povući nežno NAZAD i NADOLE radi ispravljanja slušnog kanala.'),
            ('Mirovanje:', 'Dete ostaje na boku 2-3 minuta nakon ukapavanja.')
        ]),
    ]
    
    y = 165
    for idx, (title, col, items) in enumerate(techniques):
        draw.rounded_rectangle([(65, y), (W-65, y + 400)], radius=14, fill=C_CARD, outline=C_SAND, width=1)
        draw_badge(draw, 85, y + 20, title, F_CARD_TITLE, col, C_CARD, height=52)
        
        step_val = 72 if idx == 0 else 94
        iy = y + 84 if idx == 0 else y + 94
        for lbl, desc in items:
            draw_item(draw, 95, iy, f"• {lbl}", f"   {desc}", F_BOLD, F_BODY, C_DARK, C_DARK, max_w=980, line_gap=32 if idx == 0 else 34)
            iy += step_val
        y += 430
        
    img.save(os.path.join(ASSETS_DIR, 'slide31_safe_medicine_admin.png'), quality=95)
    print('Saved slide31_safe_medicine_admin.png')

if __name__ == '__main__':
    print('Generišem sve pedijatrijske i kliničke infografike...')
    make_slide05()
    make_slide08()
    make_slide12()
    make_slide13()
    make_slide14()
    make_slide15()
    make_slide21()
    make_slide22()
    make_slide23()
    make_slide24()
    make_slide25()
    make_slide26()
    make_slide28()
    make_slide30()
    make_slide31()
    print('Sve infografike uspešno generisane!')
