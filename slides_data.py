#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Strukturirani podaci za 32 slajda prezentacije Royal Nanny Akademije.
Zvanični kurikulum: 4 modula nege i pedijatrije po materijalu Jelene Aleksić.
Saradnik: Spec. strukovna med-sestra Jelena Aleksić
"""

SLIDES_DATA = [   {   'badge': 'ROYAL NANNY AKADEMIJA',
        'bg_theme': 'dark',
        'category': 'ROYAL NANNY AKADEMIJA',
        'content_blocks': [   {   'bullets': [   '<strong>4 sveobuhvatna modula:</strong> Higijena i nega '
                                                 'novorođenčeta, dojenje, nega odojčeta i nega bolesnog deteta.',
                                                 '<strong>Medicinski utemeljeni protokoli:</strong> Zlatni standardi '
                                                 'pedijatrijske nege po programu Jelene Aleksić.',
                                                 '<strong>Vrhunski bonton & diskrecija:</strong> Diplomatska '
                                                 'komunikacija, etika i poštovanje privatnosti doma.',
                                                 '<strong>Praktične demonstracije:</strong> Usvajanje veština kroz '
                                                 'realne kliničke i životne situacije.'],
                                  'text': 'Sveobuhvatni pedijatrijsko-medicinski program kreiran za prenošenje '
                                          'najviših standarda nege, bezbednosti, emocionalne topline i profesionalne '
                                          'diskrecije u porodicama visokih zahteva.',
                                  'title': 'Ekskluzivna obuka za elitne dadilje'}],
        'id': 1,
        'image': 'p1_img2_736x946.png',
        'layout': 'cover',
        'lecturer_notes': {   'cilj': 'Postaviti autoritet predavača, predstaviti saradnika Spec. strukovnu med-sestru '
                                      'Jelenu Aleksić i definisati standarde izvrsnosti.',
                              'greske': "Polaznice često misle da je 'ljubav prema deci' dovoljna. Jasno podvući da je "
                                        'stručnost bez improvizacije temelj rada.',
                              'pitanje': 'Šta po vašem mišljenju razlikuje prosečnu dadilju od sertifikovane Royal '
                                         'Nanny profesionalne negovateljice?',
                              'teze': 'Naglasite da Royal Nanny obuka nije samo kurs čuvanja dece, već akademija '
                                      'elitne nege. Polaznice moraju shvatiti da je spoj medicinske obučenosti, '
                                      'preventivnog razmišljanja i bontona ono što stvara poverenje roditelja.'},
        'logo': 'logo_horizontal_light.png',
        'metrics': [   {'lbl': 'Stručna modula', 'val': '4'},
                       {'lbl': 'Kliničkih protokola', 'val': '30+'},
                       {'lbl': 'Fokus na bezbednost', 'val': '100%'}],
        'module': 'Uvod',
        'subtitle': 'Edukativni program za predavače • Saradnik: Spec. strukovna med-sestra Jelena Aleksić',
        'title': 'Standardi profesionalne nege i razvoja deteta',
        'title_styled': 'Standardi <em>profesionalne nege</em> i razvoja deteta'},
    {   'badge': 'FILOZOFIJA BRENDA',
        'bg_theme': 'light',
        'category': 'MISIJA I IDENTITET',
        'content_blocks': [   {   'bullets': [   '<strong>Ekskluzivna sinergija:</strong> Pažljivo građen most između '
                                                 'visokih zahteva luksuznog doma i iskrene brige o deci.',
                                                 '<strong>Dvostruka kompetencija:</strong> Spoj medicinske i '
                                                 'pedijatrijske obučenosti sa besprekornim manirima i etikom.',
                                                 '<strong>Individualni pristup:</strong> Prilagođavanje specifičnim '
                                                 'pravilima, navikama i vrednostima svake porodice.',
                                                 '<strong>Sigurnost i mir doma:</strong> Dadilja kao pouzdan oslonac '
                                                 'koji roditeljima pruža potpuno rasterećenje.'],
                                  'title': 'Retko i lično iskustvo'},
                              {   'bullets': [   '<strong>1. Poverenje & Sigurnost:</strong> Apsolutna pouzdanost i '
                                                 'pedijatrijska sigurnost deteta u svakom trenutku.',
                                                 '<strong>2. Elegancija & Diskretnost:</strong> Tih, nenametljiv rad, '
                                                 'poštovanje privatnosti doma i vrhunski bonton.',
                                                 '<strong>3. Medicinska svrha:</strong> Svaki postupak i rutina imaju '
                                                 'stručno pedijatrijsko i razvojno opravdanje.',
                                                 '<strong>4. Fluidnost & Toplota:</strong> Meki pristup koji poštuje '
                                                 'dečju individualnost i prirodni ritam.'],
                                  'title': 'Stubovi profesionalne izvrsnosti'}],
        'id': 2,
        'image': 'p11_img1_1080x1349.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Uskladiti stav polaznica sa očekivanjima klijenata visoke platežne moći i '
                                      'specifičnostima rada u luksuznim domaćinstvima.',
                              'greske': 'Dadilje ponekad pređu granicu profesionalne distance (previše se mešaju u '
                                        'privatne odnose) ili, nasuprot tome, nastupaju prestrogo i rigidno.',
                              'pitanje': 'Kako biste reagovali u situaciji kada roditelj ima neuobičajen ili suprotan '
                                         'zahtev u odnosu na ono što ste učili na obuci?',
                              'teze': 'Diskrecija je neprikosnovena: ništa što se vidi ili čuje u domu klijenta ne '
                                      'izlazi van ta četiri zida. Istovremeno, porodice traže toplinu – ne '
                                      'distanciranu figuru, već nekoga ko uliva mir i sigurnost.'},
        'module': 'Uvod',
        'subtitle': 'Filozofija i vrednosti brenda Royal Nanny',
        'title': 'Most između luksuznog doma i tople nege',
        'title_styled': 'Most između <em>luksuznog doma</em> i tople nege'},
    {   'badge': 'NASTAVNI PLAN',
        'bg_theme': 'light',
        'category': 'KURIKULUM I SATNICA',
        'content_blocks': [   {   'bullets': [   '<strong>Modul 1 – Higijena i nega novorođenčeta:</strong> Priprema '
                                                 'sobe i opreme, kupanje, nega kože, obrada pupčanika, nega čula, '
                                                 'oblačenje, položaji i higijena pribora.',
                                                 '<strong>Modul 2 – Dojenje:</strong> Prednosti dojenja, higijena i '
                                                 'priprema dojki, položaji i pravilan hvat, ragade, mastitis, '
                                                 'izmazanje, čuvanje mleka i adaptirana formula.'],
                                  'title': 'Moduli 1 & 2: Nega novorođenčeta i dojenje'},
                              {   'bullets': [   '<strong>Modul 3 – Nega odojčeta:</strong> Vakcinacija, prve šetnje, '
                                                 'uvođenje čvrste hrane, zdrave životne navike, denticija i priprema '
                                                 'za putovanja.',
                                                 '<strong>Modul 4 – Nega bolesnog deteta:</strong> Grčevi, osip i '
                                                 'pelenski ojed, infekcije oka i zapušen nos, febrilnost, dijareja, '
                                                 'povrede i nezgode, zarazne bolesti, alergije, apoteka i lekovi.',
                                                 '<strong>Saradnik programa:</strong> Spec. strukovna med-sestra '
                                                 'Jelena Aleksić • Zlatni standard pedijatrijske prakse.'],
                                  'title': 'Moduli 3 & 4: Nega odojčeta i bolesnog deteta'}],
        'id': 3,
        'image': 'p10_img1_3000x1999.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Dati polaznicama jasan roadmap današnjeg predavanja kroz 4 zvanična modula '
                                      'kurikuluma Jelene Aleksić.',
                              'greske': 'Predavač predugo ostaje na uvodnim slajdovima. Pređite na Modul 1 u roku od '
                                        'prvih 10-15 minuta obuke.',
                              'pitanje': 'Koji od ova 4 modula vam deluje kao oblast u kojoj imate najviše pitanja ili '
                                         'nedoumica?',
                              'teze': 'Objasnite dinamiku: program je podeljen u 4 logičke celine – od nege '
                                      'novorođenčeta, preko ishrane i odojčeta, do nege bolesnog deteta i hitnih '
                                      'intervencija. Predavanja su interaktivna uz demonstracije.'},
        'module': 'Uvod',
        'subtitle': '4 zvanična modula obuke • Saradnik: Spec. strukovna med-sestra Jelena Aleksić',
        'title': 'Struktura edukativnog programa',
        'title_styled': 'Struktura <em>edukativnog programa</em>'},
    {   'badge': 'MODUL 1: HIGIJENA I NEGA NOVOROĐENČETA',
        'bg_theme': 'light',
        'category': 'SOBA, NAMEŠTAJ I OPREMA',
        'content_blocks': [   {   'bullets': [   '<strong>Temperatura sobe (20–22°C):</strong> Idealna temperatura za '
                                                 'boravak i san bebe; pretopljavanje prostorije dokazano povećava '
                                                 'rizik od SIDS-a.',
                                                 '<strong>Vlažnost vazduha (45–60%):</strong> Očuvanje vlažnosti '
                                                 'sluzokože gornjih disajnih puteva pomoću hladnog ultrazvučnog '
                                                 'ovlaživača vazduha.',
                                                 '<strong>Poprečno provetravanje:</strong> Kratkotrajno i intenzivno '
                                                 'provetravanje 3–4 puta dnevno dok beba privremeno boravi u drugoj '
                                                 'sobi.',
                                                 '<strong>Izbacivanje sakupljača prašine:</strong> Soba bez teških '
                                                 'tepiha, zavesa, plišanih igračaka i osveživača vazduha koji '
                                                 'iritiraju bronhije.'],
                                  'title': 'Optimalna mikroklima i higijena prostora'},
                              {   'bullets': [   '<strong>Standard kreveca i dušeka:</strong> Čvrst antialergijski '
                                                 'dušek koji tačno naleže na ram kreveca (razmak između dušeka i '
                                                 'ograde manji od 2 prsta).',
                                                 '<strong>Pravilo praznog kreveca:</strong> Stroga zabrana jastuka, '
                                                 'debelih pokrivača, pozicionera i plišanih ogradica; beba spava u '
                                                 'namenskoj vreći.',
                                                 '<strong>Pult za prepovijanje:</strong> Ergonomski pult u visini '
                                                 "struka sa zaštitnim bočnim stranicama; pravilo: 'Jedna ruka je uvek "
                                                 "na bebi!'.",
                                                 '<strong>Pozicioniranje nameštaja:</strong> Krevetac mora biti '
                                                 'udaljen od grejnih tela, klima uređaja, direktnog sunčevog zračenja '
                                                 'i traka za roletne.'],
                                  'title': 'Izbor kreveca, nameštaja i bezbednost'}],
        'id': 4,
        'image': 'slide04_nursery_cot.jpg',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Naučiti polaznice kako da pripreme i održe idealan, siguran i čist prostor za '
                                      'novorođenče pre njegovog dolaska iz porodilišta.',
                              'greske': "Ostavljanje bebe na pultu za prepovijanje 'samo na sekund' dok se dohvati "
                                        'pelena – najčešći uzrok teških padova.',
                              'pitanje': 'Šta biste uradili ako zateknete krevetac pun plišanih jastučića i debelih '
                                         'ogradica koje su roditelji kupili iz estetskih razloga?',
                              'teze': 'Pretopljavanje je najveća greška roditelja. Dadilja mora autoritativno ali '
                                      'taktično objasniti zašto 20-22°C čuva bebin san i disanje. Insistirati na '
                                      'praznom krevecu.'},
        'module': 'Modul 1',
        'subtitle': 'Optimalna mikroklima, bezbedan krevetac i organizacija prostora',
        'title': 'Priprema sobe za bebu, nameštaja i opreme',
        'title_styled': 'Priprema sobe za bebu, <em>nameštaja i opreme</em>'},
    {   'badge': 'MODUL 1: HIGIJENA I NEGA NOVOROĐENČETA',
        'bg_theme': 'light',
        'category': 'KUPANJE BEBE',
        'content_blocks': [   {   'bullets': [   '<strong>Zagrejanost prostorije (24–26°C):</strong> Prostorija u '
                                                 'kojoj se beba kupa mora biti prethodno ugrejana, bez promaje i '
                                                 'hladnih strujanja vazduha.',
                                                 '<strong>Temperatura vode (36.5–37°C):</strong> Precizno merenje '
                                                 'vodenim termometrom uz obaveznu potvrdu unutrašnjom stranom '
                                                 'podlaktice/lakta.',
                                                 '<strong>Količina vode u kadici:</strong> Za novorođenče sipa se samo '
                                                 '5 do 8 cm vode (do nivoa bebinih kukova pri spuštanju).',
                                                 '<strong>Sigurnosni raspored pribora:</strong> Frotirski peškir sa '
                                                 'kapuljačom, tetra pelene, čista odeća i pribor složeni po redosledu '
                                                 'upotrebe.'],
                                  'title': 'Priprema ambijenta i opreme'},
                              {   'bullets': [   '<strong>Bokal sa čistom toplom vodom:</strong> Uvek pripremiti bokal '
                                                 'tople vode (37°C) za završno ispiranje tela i glavice.',
                                                 '<strong>Medicinski sindet:</strong> Dermatološko sredstvo bez sapuna '
                                                 '(pH 5.5) koje ne narušava prirodnu hidrolipidnu barijeru bebine '
                                                 'kože.',
                                                 '<strong>Pribor za pupčanik i čula:</strong> Sterilne komprese, '
                                                 'fiziološki rastvor i antiseptik za pupčanu ranu otvoreni pre početka '
                                                 'toalete.',
                                                 '<strong>Apsolutni fokus pažnje:</strong> Beba se NIKADA ne ostavlja '
                                                 'sama u kadici ili na stolu za prepovijanje, čak ni na delić '
                                                 'sekunde.'],
                                  'title': 'Sterilni i negujući pribor'}],
        'id': 5,
        'image': 'slide05_bath_prep_station.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Usvojiti protokol pripreme kupanja koji garantuje bezbednost, sprečava '
                                      'hipotermiju i eliminiše stres kod novorođenčeta.',
                              'greske': 'Zaboravljanje bokala za ispiranje pa korišćenje sapunjave vode iz kadice za '
                                        'pranje lica i očiju.',
                              'pitanje': 'Zašto je testiranje vode laktom obavezno čak i kada imamo digitalni '
                                         'termometar za vodu?',
                              'teze': 'Beba gubi toplotu četiri puta brže od odrasle osobe. Zato sve mora biti '
                                      'pripremljeno unapred: peškir raširen, odeća otkopčana, voda tačno 37°C. Kada se '
                                      'beba jednom svuče, nema traženja stvari po kući.'},
        'module': 'Modul 1',
        'subtitle': 'Zlatni standard: Sve neophodno pripremljeno na dohvat ruke pre svlačenja bebe',
        'title': 'Kupanje bebe: Priprema, stanica i mikroklima',
        'title_styled': 'Kupanje bebe: <em>Priprema, stanica i mikroklima</em>'},
    {   'badge': 'MODUL 1: HIGIJENA I NEGA NOVOROĐENČETA',
        'bg_theme': 'light',
        'category': 'TEHNIKA KUPANJA',
        'content_blocks': [   {   'bullets': [   '<strong>Stabilan hvat podlakticom:</strong> Beba leži potiljkom na '
                                                 'levoj podlaktici dadilje, dok šaka čvrsto obuhvata bebinu dalju '
                                                 'nadlakticu ispod pazuha.',
                                                 '<strong>Postepeno uranjanje:</strong> Beba se unosi polako, prvo '
                                                 'nožicama i karlicom, uz topao glas i kontakt očima koji pruža osećaj '
                                                 'sigurnosti.',
                                                 '<strong>Topla tetra pelena preko stomaka:</strong> Prekrivanje tela '
                                                 'mokrom toplom tetra pelenom sprečava Moroov refleks i strah od vode.',
                                                 '<strong>Trajanje kupanja (5–7 minuta):</strong> Kod novorođenčeta '
                                                 'kupanje je kratko kako bi se sprečilo rashlađivanje vode i '
                                                 'isušivanje epidermisa.'],
                                  'title': 'Pravilan hvat i spuštanje u vodu'},
                              {   'bullets': [   '<strong>Lice i glava pre tela:</strong> Lice se briše isključivo '
                                                 'čistom vodom; glavica se pere i ispira zabačena unazad (voda ne '
                                                 'ulazi u oči i uši).',
                                                 '<strong>Pregibi i nabori tela:</strong> Pažljivo pranje nabora '
                                                 'vrata, pazuha, prepona i međuprstnih prostora gde se zadržavaju '
                                                 'naslage.',
                                                 '<strong>Genitalna toaleta:</strong> Kod devojčica strogo od napred '
                                                 'ka nazad (ka anusu); kod dečaka nežno pranje bez nasilnog '
                                                 'prevlačenja prepucijuma.',
                                                 '<strong>Sušenje tapkanjem (bez trljanja):</strong> Umotavanje u '
                                                 'mekan frotir; svi pregibi se pažljivo osuše tapkanjem pamučnom tetra '
                                                 'pelenom.'],
                                  'title': 'Redosled pranja i sušenje tapkanjem'}],
        'id': 6,
        'image': 'slide06_baby_bath.jpg',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Praktično uvežbati hvat i redosled kupanja kako bi kupanje bilo sigurna, nežna '
                                      'i prijatna večernja rutina.',
                              'greske': 'Agresivno trljanje peškirom koje oštećuje nežni rožasti sloj kože i '
                                        'ostavljanje vlažnih nabora vrata i prepona što vodi u maceraciju i ojed.',
                              'pitanje': 'Kako smiriti bebu koja ima snažan Moroov refleks i histerično plače čim uđe '
                                         'u vodu?',
                              'teze': 'Demonstrirajte hvat na lutki: prsti obuhvataju nadlakticu, glava ima čvrst '
                                      'oslonac na podlaktici. Objasnite pravilo pranja od najčistijeg ka najprljavijem '
                                      'delu tela.'},
        'module': 'Modul 1',
        'subtitle': 'Siguran hvat, precizan redosled toalete i nežno sušenje tapkanjem',
        'title': 'Tehnika kupanja bebe u kadici i rutina nege',
        'title_styled': 'Tehnika kupanja bebe u <em>kadici i rutina nege</em>'},
    {   'badge': 'MODUL 1: HIGIJENA I NEGA NOVOROĐENČETA',
        'bg_theme': 'light',
        'category': 'NEGA KOŽE',
        'content_blocks': [   {   'bullets': [   '<strong>3 do 5 puta tanji epidermis:</strong> Koža novorođenčeta je '
                                                 'izrazito propustljiva za hemijske supstance, toksine i alergene iz '
                                                 'spoljašnje sredine.',
                                                 '<strong>Nezrela funkcija znojnih žlezda:</strong> Otežana '
                                                 'termoregulacija i sklonost brzom gubitku vlage čine kožu podložnom '
                                                 'perutanju i suvoći.',
                                                 '<strong>Formiranje kiselog omotača (pH 5.5):</strong> U prvim '
                                                 'nedeljama koža prelazi sa neutralnog na blago kiseli pH koji štiti '
                                                 'od patogenih bakterija.',
                                                 '<strong>Fiziološko perutanje (deskvamacija):</strong> Prirodna '
                                                 'pojava zamene rožastog sloja nakon rođenja; ne zahteva agresivno '
                                                 'skidanje već nežnu hidrataciju.'],
                                  'title': 'Specifičnosti kože novorođenčeta'},
                              {   'bullets': [   '<strong>Upotreba medicinskih sindeta:</strong> Pranje '
                                                 'dermokozmetičkim uljanim kupkama ili sindetima bez sapuna, parfema i '
                                                 'sulfata.',
                                                 '<strong>Pravilo 3 minuta za emolijens:</strong> Medicinska krema ili '
                                                 'balzam nanosi se u tankom sloju unutar 3 minuta nakon kupanja dok je '
                                                 'koža još vlažna.',
                                                 '<strong>Izbegavanje teških ulja:</strong> Čista mineralna, '
                                                 'parafinska i maslinova ulja mogu zapušiti pore i narušiti prirodnu '
                                                 'lipidnu barijeru kože.',
                                                 '<strong>Princip dermatološkog minimalizma:</strong> Manje je više – '
                                                 'ne gomilati kozmetičke preparate; zdravoj koži potrebna je samo '
                                                 'čista voda i blagi sindet.'],
                                  'title': 'Dermatološki izbor i pravilo 3 minuta'}],
        'id': 7,
        'image': 'p6_img4_1080x1080.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Upoznati polaznice sa osetljivošću dečje kože i osposobiti ih za pravilan '
                                      'odabir dermokozmetike bez komercijalnih zabluda.',
                              'greske': 'Korišćenje bebi pudera (talka) koji beba može udahnuti i preterano mazanje '
                                        'debelih slojeva krema na zdrave delove tela.',
                              'pitanje': 'Zašto maslinovo ulje iz kuhinje nije preporučljivo za negu kože '
                                         'novorođenčeta?',
                              'teze': 'Koža novorođenčeta upija sve što se na nju stavi. Objasnite razliku između '
                                      'klasičnog sapuna koji podiže pH na alkalnih 8-9 i medicinskog sindeta koji čuva '
                                      "pH 5.5. Upozorite na štetnost 'prirodnih' ulja iz kuhinje."},
        'module': 'Modul 1',
        'subtitle': 'Anatomija neonatalne kože, barijerna funkcija i dermatološki izbor',
        'title': 'Nega kože: Sindeti, emolijensi i pH ravnoteža',
        'title_styled': 'Nega kože: <em>Sindeti, emolijensi i pH ravnoteža</em>'},
    {   'badge': 'MODUL 1: HIGIJENA I NEGA NOVOROĐENČETA',
        'bg_theme': 'light',
        'category': 'PUPČANIK I PUPČANA RANA',
        'content_blocks': [   {   'bullets': [   '<strong>Protokol suve nege po SZO:</strong> Pupčani bataljak se '
                                                 'održava čistim i suvim, izložen vazduhu radi prirodne mumifikacije.',
                                                 '<strong>Pravilno postavljanje pelene:</strong> Gornja ivica pelene '
                                                 'se presavija prema spolja nadole kako pupak ne bi bio u kontaktu sa '
                                                 'urinom.',
                                                 '<strong>Antiseptik po indikaciji (Octenisept):</strong> Prska se na '
                                                 'bazu pupčanika samo u slučaju kontakta sa nečistoćom ili urinom, uz '
                                                 'sušenje sterilnom gazom.',
                                                 '<strong>Stroga zabrana agresivnih sredstava:</strong> ZABRANJENA '
                                                 'upotreba povidon joda (apsorpcija joda oštećuje štitastu žlezdu), '
                                                 'alkohola i antibiotskih praškova.'],
                                  'title': 'Standard suve obrade pupčanika'},
                              {   'bullets': [   '<strong>Fiziološko otpadanje (7–15. dan):</strong> Bataljak otpada '
                                                 'samostalno kada se potpuno osuši; strogo je zabranjeno povlačenje '
                                                 'ili uvrtanje.',
                                                 '<strong>Nega pupčane rane:</strong> Nakon otpadanja, ranica se čisti '
                                                 'sterilnom gazom i Octeniseptom dok se dno rane potpuno ne '
                                                 'epitelizuje.',
                                                 '<strong>Crveni alarm: Omfalitis (infekcija):</strong> Crvenilo kože '
                                                 'oko pupka prečnika >1 cm, otok, vlaženje, gnojan miris i povišena '
                                                 'temperatura.',
                                                 '<strong>Pupčani granulom:</strong> Ružičasto zrnasto tkivo na dnu '
                                                 'pupka koje stalno vlaži; zahteva pedijatrijski pregled i lapiziranje '
                                                 'srebrn-nitratom.'],
                                  'title': 'Otpadanje bataljka i crvene zastavice'}],
        'id': 8,
        'image': 'slide08_umbilical_cord_care.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Ovladati procedurom asepse pri obradi pupčanika i pravovremenim prepoznavanjem '
                                      'znakova lokalne i sistemske infekcije.',
                              'greske': 'Kvašenje pupčanika u kadici pre nego što ranica epitelizuje i stavljanje '
                                        'običnog flastera koji stvara vlažnu komoru pogodnu za bakterije.',
                              'pitanje': 'Šta ćete uraditi ako primetite par kapi sasušene krvi na gazi prilikom '
                                         'otpadanja bataljka?',
                              'teze': 'Pupčana vena je direktan put mikroorganizama u krvotok novorođenčeta. Ruke se '
                                      'moraju dezinfikovati pre svakog dodira. Objasnite zašto je suva nega zlatni '
                                      'standard i zašto je povidon jod zabranjen.'},
        'module': 'Modul 1',
        'subtitle': 'Zlatni standard suve obrade, antiseptički protokol i prepoznavanje komplikacija',
        'title': 'Nega pupčanika i pupčane rane',
        'title_styled': 'Nega pupčanika i <em>pupčane rane</em>'},
    {   'badge': 'MODUL 1: HIGIJENA I NEGA NOVOROĐENČETA',
        'bg_theme': 'light',
        'category': 'NEGA ČULA',
        'content_blocks': [   {   'bullets': [   '<strong>Toaleta očiju sterilnom gazom:</strong> Briše se od '
                                                 'spoljašnjeg ugla oka ka unutrašnjem; za svako oko koristi se nova, '
                                                 'zasebna sterilna gaza sa fiziološkim rastvorom.',
                                                 '<strong>Nega nosa fiziološkim kapima:</strong> Po 2–3 kapi 0.9% NaCl '
                                                 'u svaku nozdrvu pre dojenja i spavanja radi razmekšavanja sekreta.',
                                                 '<strong>Nega ušiju bez štapića:</strong> Čisti se isključivo '
                                                 'spoljašnja ušna školjka i prostor iza uva; pamučni štapići se NIKADA '
                                                 'ne guraju u ušni kanal.',
                                                 '<strong>Masaža suznog kanala:</strong> Kod suženja kanala i '
                                                 'krmeljanja, nežna masaža unutrašnjeg ugla oka čistim prstom usmerena '
                                                 'nadole duž nosa.'],
                                  'title': 'Toaleta očiju, ušiju i nosnih hodnika'},
                              {   'bullets': [   '<strong>Prvo sečenje nakon 2. nedelje:</strong> Noktići se skraćuju '
                                                 'tek kada očvrsnu i odvoje se od kožice jagodice.',
                                                 '<strong>Medicinski pribor:</strong> Upotreba bebi makazica sa tupim, '
                                                 'zaobljenim vrhom ili staklene turpije, prethodno prebrisanih '
                                                 'alkoholom.',
                                                 '<strong>Tehnika sečenja:</strong> Na rukama se noktići seku blago '
                                                 'polukružno, a na nogama strogo ravno (prevencija urastanja nokta).',
                                                 '<strong>Optimalan tajming:</strong> Noktići se seku dok beba čvrsto '
                                                 'spava u fazi dubokog sna ili neposredno posle kupanja kada su meki.'],
                                  'title': 'Bezbedno skraćivanje i nega noktića'}],
        'id': 9,
        'image': 'p4_img1_736x976.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Obučiti polaznice za sterilno i bezbedno izvođenje svakodnevne toalete čula '
                                      'novorođenčeta.',
                              'greske': 'Guranje štapića sa vatom u nosne otvore i uši bebe umesto korišćenja urolane '
                                        'sterilne gaze ili fiziološkog rastvora.',
                              'pitanje': 'Zašto nikada ne koristimo istu sterilnu gazu za oba oka bebe?',
                              'teze': 'Pokažite pravilan smer brisanja oka: od spolja ka unutra, jednom gazom samo '
                                      'jedan potez. Naglasite opasnost od štapića za uši koji mogu probušiti bubnu '
                                      'opnu ili nabiti cerumen.'},
        'module': 'Modul 1',
        'subtitle': 'Precizna toaleta čulnih organa sterilnim tehnikama i bezbedno sečenje noktiju',
        'title': 'Nega čula novorođenčeta: Oči, uši, nos i noktići',
        'title_styled': 'Nega čula novorođenčeta: <em>Oči, uši, nos i noktići</em>'},
    {   'badge': 'MODUL 1: HIGIJENA I NEGA NOVOROĐENČETA',
        'bg_theme': 'light',
        'category': 'OBLAČENJE I PRIBOR',
        'content_blocks': [   {   'bullets': [   '<strong>Pravilo jednog sloja više:</strong> Beba se oblači u jedan '
                                                 'sloj više u odnosu na odraslu osobu u istoj prostoriji; izbegavati '
                                                 'pretopljavanje.',
                                                 '<strong>100% organski češljani pamuk:</strong> Isključivo prirodni, '
                                                 'meki materijali; bez sintetike, krutih traka, tvrdih etiketa i '
                                                 'metalnih drikera koji dodiruju kožu.',
                                                 '<strong>Provera temperature na potiljku:</strong> Temperatura se '
                                                 'proverava opipavanjem potiljka i grudnog koša (topli i suvi), a ne '
                                                 'šaka i stopala.',
                                                 '<strong>Praktičnost kroja:</strong> Bodići sa preklopom na grudima '
                                                 '(benkice) koji se ne navlače preko glave, idealni za novorođenčad.'],
                                  'title': 'Principi pravilnog oblačenja bebe'},
                              {   'bullets': [   '<strong>Odvojeno pranje na 60–90°C:</strong> Bebin veš se pere '
                                                 'zasebno, blagim tečnim hipoalergenim deterdžentom bez parfema i bez '
                                                 'omekšivača.',
                                                 '<strong>Dvostruko ispiranje i peglanje:</strong> Obavezno dodatno '
                                                 'ispiranje radi uklanjanja deterdženta; peglanje parom uništava '
                                                 'rezidualne mikrobe.',
                                                 '<strong>Sterilizacija hranilica i pribora:</strong> Flašice, cucle, '
                                                 'pumpice i glodalice sterilišu se parom ili otkuvavanjem pre prve '
                                                 'upotrebe i redovno održavaju.',
                                                 '<strong>Dezinfekcija površina:</strong> Podloga za presvlačenje, '
                                                 'kadica i igračke redovno se peru i dezinfikuju bezbednim netoksičnim '
                                                 'sredstvima.'],
                                  'title': 'Higijena garderobe i bebinog pribora'}],
        'id': 10,
        'image': 'p9_img1_736x920.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Standardizovati održavanje bebine garderobe, pribora i oblačenja po strogim '
                                      'pedijatrijskim i higijenskim normama.',
                              'greske': 'Pretopljavanje deteta vunenim kapicama i čarapama unutar ugrejane sobe što '
                                        'dovodi do dehidratacije i toplotnog osipa.',
                              'pitanje': 'Bebine šake su hladne na dodir, ali potiljak je vreo i vlažan. Da li ćete '
                                         'bebu dodatno obući ili raskomotiti?',
                              'teze': 'Omekšivači za veš su jedan od vodećih uzroka kontaktnog dermatitisa kod '
                                      'odojčadi. Oblačenje mora biti praktično i komforno, a kontrola temperature vrši '
                                      'se isključivo na vratu/grudima.'},
        'module': 'Modul 1',
        'subtitle': 'Pravilo slojevitog oblačenja, izbor tkanina i rigorozna higijena bebinog pribora',
        'title': 'Oblačenje bebe i higijena garderobe i pribora',
        'title_styled': 'Oblačenje bebe i <em>higijena garderobe i pribora</em>'},
    {   'badge': 'MODUL 1: HIGIJENA I NEGA NOVOROĐENČETA',
        'bg_theme': 'light',
        'category': 'POLOŽAJI I BEZBEDAN SAN',
        'content_blocks': [   {   'bullets': [   '<strong>Stabilna potpora za glavu i kičmu:</strong> Glava '
                                                 'novorođenčeta mora imati čvrst oslonac na podlaktici; kičma prati '
                                                 "prirodan fiziološki 'C' luk.",
                                                 "<strong>Položaj 'tigar na drvetu':</strong> Beba leži potrbuške duž "
                                                 'podlaktice dadilje sa glavom u lakatnom prevoju – odličan položaj za '
                                                 'eliminaciju gasova.',
                                                 '<strong>Položaj podignutog uzglavlja pri hranjenju:</strong> Ugao od '
                                                 '30–45° tokom podoja ili flašice; sprečava aspiraciju mleka i ulazak '
                                                 'tečnosti u Eustahijevu tubu.',
                                                 '<strong>Protokol podrigivanja nakon obroka:</strong> Vertikalno '
                                                 'držanje bebe naslonjene na rame ili na krilu uz lagano tapkanje po '
                                                 'leđima 10–15 minuta.'],
                                  'title': 'Položaji pri nošenju i hranjenju'},
                              {   'bullets': [   '<strong>Spavanje ISKLJUČIVO na leđima:</strong> Položaj na leđima na '
                                                 'ravnoj površini je najbezbedniji položaj za san tokom cele prve '
                                                 'godine života.',
                                                 '<strong>Zabrana bočnog i potrbušnog položaja:</strong> Bočni položaj '
                                                 'je nestabilan i nosi visok rizik od nekontrolisanog prevrtanja na '
                                                 'stomak.',
                                                 '<strong>Prazan krevetac i namenska vreća:</strong> Bez jastuka, '
                                                 'gnezda, plišanih igračaka i ogradica; dete spava u vreći za spavanje '
                                                 'prilagođenoj sobnoj temperaturi.',
                                                 '<strong>Zaseban krevetac pored roditelja:</strong> Zajednička soba '
                                                 '(room-sharing) u sopstvenom krevecu tokom prvih 6 meseci pruža '
                                                 'optimalnu bezbednost.'],
                                  'title': 'Zlatna pravila bezbednog spavanja (SIDS)'}],
        'id': 11,
        'image': 'p18_img1_736x1103.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Usvojiti ergonomske položaje nošenja i striktno primenjivati protokole '
                                      'prevencije sindroma iznenadne smrti odojčeta (SIDS).',
                              'greske': "Dozvoljavanje spavanja u auto-sedištu ('jajetu') van automobila duže od 30 "
                                        'minuta – opasnost od položajne asfiksije.',
                              'pitanje': 'Roditelji insistiraju da beba spava na boku uz jastučić jer se plaše da će '
                                         'se zagrcnuti ako bljucne na leđima. Kako ćete im objasniti anatomiju?',
                              'teze': "Podaci pokazuju da je kampanja 'Spavanje na leđima' smanjila stopu SIDS-a za "
                                      'više od 50%. Dadilja nikada ne sme dozvoliti spavanje bebe na stomaku bez '
                                      'stalnog medicinskog nadzora.'},
        'module': 'Modul 1',
        'subtitle': 'Biomehanika nošenja novorođenčeta, prevencija aspiracije i protokoli bezbednog sna',
        'title': 'Položaj pri hranjenju, nošenju i spavanju',
        'title_styled': 'Položaji pri <em>hranjenju, nošenju i spavanju</em>'},
    {   'badge': 'MODUL 2: DOJENJE',
        'bg_theme': 'light',
        'category': 'PREDNOSTI I PRIPREMA',
        'content_blocks': [   {   'bullets': [   '<strong>Jedinstven biološki sastav:</strong> Majčino mleko sadrži '
                                                 'specifična antitela (sekretorni IgA), žive leukocite, enzime i '
                                                 'prebiotike (HMO).',
                                                 "<strong>Kolostrum ('tečno zlato'):</strong> Prvo mleko bogato "
                                                 'proteinima i imunoglobulinima; oblaže sluzokožu creva i deluje kao '
                                                 'prva prirodna vakcina.',
                                                 '<strong>Dugoročne zdravstvene prednosti:</strong> Štiti od '
                                                 'respiratornih i digestivnih infekcija, alergija, dijabetesa i '
                                                 'smanjuje rizik od gojaznosti.',
                                                 '<strong>Psihološka bliskost i oksitocin:</strong> Kontakt koža na '
                                                 'kožu smanjuje nivo stresa kod majke i bebe i podstiče emocionalno '
                                                 'vezivanje.'],
                                  'title': 'Zlatni standard ishrane: Prednosti dojenja'},
                              {   'bullets': [   '<strong>Pranje isključivo čistom vodom:</strong> Dojke se peru samo '
                                                 'mlakom vodom tokom dnevnog tuširanja; sapuni isušuju prirodna ulja '
                                                 'Montgomeryjevih žlezda.',
                                                 '<strong>Priprema pre podoja:</strong> Tople obloge ili kratak topao '
                                                 'tuš 5 minuta pre podoja olakšavaju refleks otpuštanja mleka '
                                                 '(let-down refleks).',
                                                 '<strong>Udoban položaj i relaksacija:</strong> Majka mora sedeti '
                                                 'potpuno opuštenih ramena i leđa, uz potporu namenskim jastukom za '
                                                 'dojenje.',
                                                 '<strong>Uloga profesionalne dadilje:</strong> Dadilja priprema '
                                                 'prostor, donosi bebu, dodaje majci čašu vode za hidrataciju i stvara '
                                                 'tihu atmosferu.'],
                                  'title': 'Higijena i priprema dojki pre podoja'}],
        'id': 12,
        'image': 'p17_img1_736x1103.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Osnažiti predavače i dadilje da pruže maksimalnu podršku majci koja doji bez '
                                      'nametanja pritiska ili stresa.',
                              'greske': "Komentari dadilje poput: 'Beba plače, možda ti mleko nije dovoljno jako' – to "
                                        'uništava samopouzdanje majke i sabotira laktaciju.',
                              'pitanje': 'Zašto se bradavice ne smeju prati sapunom pre svakog podoja?',
                              'teze': 'Dojenje je prirodno, ali se uči. Uloga dadilje je da majci pruži komfor: '
                                      'dodavanje jastuka, čaša vode (dojenje izaziva intenzivnu žeđ usled oksitocina) '
                                      'i smirivanje okruženja.'},
        'module': 'Modul 2',
        'subtitle': 'Imunološki značaj majčinog mleka, nega bradavica i podrška majci',
        'title': 'Prednosti dojenja, higijena i priprema dojki za podoj',
        'title_styled': 'Prednosti dojenja, <em>higijena i priprema dojki za podoj</em>'},
    {   'badge': 'MODUL 2: DOJENJE',
        'bg_theme': 'light',
        'category': 'POLOŽAJI I TEHNIKA',
        'content_blocks': [   {   'bullets': [   '<strong>Klasična kolevka:</strong> Bebina glava u pregibu lakta, '
                                                 "telo okrenuto 'stomak na stomak' sa majkom; uho, rame i kuk u ravnoj "
                                                 'liniji.',
                                                 '<strong>Unakrsna kolevka (Cross-cradle):</strong> Suprotna ruka '
                                                 'pridržava bebin potiljak i rameni pojas; idealan položaj za '
                                                 'novorođenče i učenje hvata.',
                                                 '<strong>Fudbalski hvat (ispod pazuha):</strong> Beba leži bočno '
                                                 'ispod majčine ruke; odličan izbor nakon carskog reza, kod većih '
                                                 'dojki ili blizanaca.',
                                                 '<strong>Ležeći bočni položaj:</strong> Majka i beba leže okrenute '
                                                 'jedno ka drugom; omogućava odmor majke tokom noći uz budan nadzor '
                                                 'dadilje.'],
                                  'title': 'Glavni položaji pri dojenju'},
                              {   'bullets': [   '<strong>Široko otvorena usta (ugao >130°):</strong> Beba obuhvata ne '
                                                 'samo bradavicu već i veći deo donje areole (bradavica usmerena ka '
                                                 'nepcu).',
                                                 '<strong>Izvrnute usne i bradica:</strong> Donja usna potpuno '
                                                 'izvrnuta prema spolja, bradica duboko utisnuta u dojku, nosić '
                                                 'slobodan za disanje.',
                                                 '<strong>Čujno gutanje bez coktanja:</strong> Čuju se duboki gutljaji '
                                                 '(pauza u disanju pri gutanju); nema coktanja ili uvlačenja obraza.',
                                                 '<strong>Bezbolan podoj:</strong> Nakon prvih 10-20 sekundi podoj ne '
                                                 'sme biti bolan; bol je uvek znak plitkog i nepravilnog hvata.'],
                                  'title': 'Znakovi pravilnog asimetričnog hvata'}],
        'id': 13,
        'image': 'slide12_breastfeeding_positions.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Uvežbati prepoznavanje asimetričnog hvata i biomehanike sisanja kako bi se '
                                      'sprečila pojava bola i oštećenja bradavica.',
                              'greske': "Povlačenje bebe sa dojke 'na silu' dok drži vakuum – garantovan način za "
                                        'nastanak ragada.',
                              'pitanje': 'Kako pravilno prekinuti vakuum i odvojiti bebu sa dojke ako je hvat plitak i '
                                         'bolan?',
                              'teze': 'Ključna poruka: Beba se privlači dojci, a ne dojka bebi! Majka se ne naginje '
                                      "napred jer to izaziva bolove u leđima. Bradavica treba da 'gleda' u bebin nosić "
                                      'pre nego što beba zine.'},
        'module': 'Modul 2',
        'subtitle': 'Ključni položaji majke i bebe, anatomija pravilnog hvata i prevencija bola',
        'title': 'Položaji pri dojenju i pravilno postavljanje na dojku',
        'title_styled': 'Položaji pri dojenju i <em>pravilno postavljanje na dojku</em>'},
    {   'badge': 'MODUL 2: DOJENJE',
        'bg_theme': 'light',
        'category': 'IZAZOVI U LAKTACIJI',
        'content_blocks': [   {   'bullets': [   '<strong>Uzrok je isključivo plitak hvat:</strong> Ragade ne nastaju '
                                                 'od predugog sisanja već zato što beba desnima gnječi vrh bradavice '
                                                 'umesto areole.',
                                                 '<strong>Premazivanje sopstvenim mlekom:</strong> Nakon podoja '
                                                 'istisnuti kap svežeg mleka, premazati bradavicu i ostaviti da se '
                                                 'osuši na vazduhu.',
                                                 '<strong>100% prečišćeni lanolin:</strong> Medicinski lanolin stvara '
                                                 'vlažnu barijeru koja ubrzava zarastanje bez potrebe za ispiranjem '
                                                 'pre podoja.',
                                                 '<strong>Silikonske bradavice (privremeno):</strong> Koristiti '
                                                 'isključivo kao privremeno pomagalo dok ranice zacele, uz stručnu '
                                                 'korekciju hvata.'],
                                  'title': 'Ispucale bradavice (Ragade)'},
                              {   'bullets': [   '<strong>Prepunjenost (engorgement):</strong> Dojke su teške, '
                                                 'zategnute i tople; rešava se čestim podojima, masažom i hladnim '
                                                 'oblogama posle podoja.',
                                                 '<strong>Začepljen mlečni kanal:</strong> Bolan čvorić na dojci; '
                                                 'blaga masaža prema bradavici pod toplim tušem i podoj sa bebinom '
                                                 'bradicom ka čvoru.',
                                                 '<strong>Klinički mastitis:</strong> Crvenilo u obliku trougla, jaka '
                                                 'bolnost, temperatura >38.5°C, jeza i drhtavica – zahteva pregled '
                                                 'lekara i antibiotike.',
                                                 '<strong>DOJENJE SE NE PREKIDA:</strong> Kod mastitisa dojenje se '
                                                 'nastavlja; redovno pražnjenje obolele dojke je ključno za izlečenje '
                                                 '(mleko je bezbedno).'],
                                  'title': 'Prepunjenost dojki i mastitis'}],
        'id': 14,
        'image': 'slide13_lactation_challenges.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Osposobiti polaznice za prepoznavanje i trijažu komplikacija u laktaciji i '
                                      'pružanje stručne prve pomoći.',
                              'greske': 'Agresivno i bolno stiskanje dojke na silu – to izaziva traumu tkiva i '
                                        'pogoršava upalu.',
                              'pitanje': 'Koja je razlika između fiziološke prepunjenosti dojki i kliničkog mastitisa?',
                              'teze': 'Razbijte mit: majka sa temperaturom i mastitisom NE SME da prestane da doji. '
                                      'Zastoj mleka pogoršava infekciju i vodi u apsces. Antibiotik koji lekar propiše '
                                      'je kompatibilan sa dojenjem.'},
        'module': 'Modul 2',
        'subtitle': 'Uzroci oštećenja, diferencijacija prepunjenosti i klinički tretman mastitisa',
        'title': 'Ispucale bradavice (ragade) i upala dojki (mastitis)',
        'title_styled': 'Ispucale bradavice (ragade) i <em>upala dojki (mastitis)</em>'},
    {   'badge': 'MODUL 2: DOJENJE',
        'bg_theme': 'light',
        'category': 'IZMAZANJE I SKLADIŠTENJE',
        'content_blocks': [   {   'bullets': [   '<strong>Stroga higijena ruku:</strong> Temeljno pranje ruku sapunom '
                                                 'i toplom vodom pre svakog kontakta sa pumpicom i posudama za mleko.',
                                                 '<strong>Sterilizacija delova pumpice:</strong> Svi delovi koji '
                                                 'dolaze u kontakt sa mlekom sterilišu se jednom dnevno i peru nakon '
                                                 'svake upotrebe.',
                                                 '<strong>Tehnika manuelnog izmazanja:</strong> Prsti u obliku slova '
                                                 "'C' 3 cm iza areole; ritmičan pritisak ka grudnom košu pa spajanje "
                                                 'prstiju.',
                                                 '<strong>Električne pumpice:</strong> Korišćenje odgovarajućeg levka '
                                                 '(veličina flanđe) koji ne tare bradavicu i rad na umerenoj jačini '
                                                 'vakuma.'],
                                  'title': 'Tehnike i higijena izmazanja'},
                              {   'bullets': [   '<strong>Sobna temperatura (do 22°C):</strong> Sveže izmlazano mleko '
                                                 'bezbedno je do 4 sata na čistom, prohladnom mestu.',
                                                 '<strong>Frižider (4°C):</strong> U dubini police frižidera (nikada u '
                                                 'vratima zbog oscilacija temperature) čuva se do 3–4 dana (optimalno '
                                                 '72h).',
                                                 '<strong>Zamrzivač (-18°C):</strong> U namenskim sterilnim kesicama '
                                                 'sa upisanim datumom i mililitražom čuva se od 3 do 6 meseci.',
                                                 '<strong>Odmrzavanje i zabrana mikrotalasne:</strong> Odmrzavanje u '
                                                 'frižideru ili u posudi sa toplom vodom; mikrotalasna uništava '
                                                 'antitela i pravi vrele tačke!'],
                                  'title': 'Standardi skladištenja i odmrzavanja (4-4-6)'}],
        'id': 15,
        'image': 'slide14_milk_storage_protocol.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Usvojiti pravila asepse pri manipulaciji izmlazanim mlekom i striktno poštovati '
                                      'temperaturne standarde skladištenja.',
                              'greske': 'Grejanje majčinog mleka u mikrotalasnoj rerni ili na ringli – proteini i '
                                        'antitela denaturišu već na temperaturama preko 40°C.',
                              'pitanje': 'Zašto se flašica sa majčinim mlekom ne sme mućkati energično kao sok?',
                              'teze': 'Objasnite pravilo FIFO (First In, First Out) – uvek se troši najstarije '
                                      'zamrznuto mleko. Jednom odmrznuto mleko se nikada ponovo ne zamrzava.'},
        'module': 'Modul 2',
        'subtitle': 'Manuelno i pumpicom izmazanje, sterilne posude i temperaturni standardi',
        'title': 'Izmazanje i protokoli čuvanja majčinog mleka',
        'title_styled': 'Izmazanje i <em>protokoli čuvanja majčinog mleka</em>'},
    {   'badge': 'MODUL 2: DOJENJE',
        'bg_theme': 'light',
        'category': 'MLEČNA FORMULA',
        'content_blocks': [   {   'bullets': [   '<strong>Izbor formule po savetu pedijatra:</strong> Standardna '
                                                 'formula 1, hipoalergena (HA) ili anti-refluks (AR) – bez '
                                                 'samoinicijativnih promena.',
                                                 '<strong>Prokuvavanje i hlađenje vode:</strong> Sveža voda se '
                                                 'prokuvava i hladi na 40–50°C pre mešanja (prevruća voda uništava '
                                                 'vitamine, hladna se ne rastvara).',
                                                 '<strong>Isključivo RAVNE merice praha:</strong> Svaka merica se '
                                                 'poravnava nožem bez sabijanja; prva se sipa voda pa tek onda prah.',
                                                 '<strong>Tačna razmera (1 merica na 30 ml vode):</strong> Strogo '
                                                 'poštovanje proporcije; gušća formula opterećuje bubrege i izaziva '
                                                 'opstipaciju.'],
                                  'title': 'Protokol pripreme formule'},
                              {   'bullets': [   '<strong>Test temperature na podlaktici:</strong> Nekoliko kapi na '
                                                 'unutrašnju stranu ručnog zgloba pre davanja bebi (mora biti prijatno '
                                                 'mlaka).',
                                                 '<strong>Pravilo 1 sata:</strong> Započeta flašica mora se popiti u '
                                                 'roku od 60 minuta; sav preostali sadržaj se BACA zbog razmnožavanja '
                                                 'bakterija iz pljuvačke.',
                                                 '<strong>Paced bottle-feeding tehnika:</strong> Flašica se drži '
                                                 'horizontalno da mleko ispunjava vrh cucle; pravi se pauza na svakih '
                                                 'nekoliko gutljaja.',
                                                 '<strong>Zabrana ostavljanja bebe same sa flašicom:</strong> Nikada '
                                                 'ne podupirati flašicu jastukom – izuzetan rizik od zagrcnjavanja, '
                                                 'gušenja i upale uva.'],
                                  'title': 'Bezbednost i tehnika hranjenja flašicom'}],
        'id': 16,
        'image': 'slide15_formula_prep_protocol.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Standardizovati sterilnu pripremu i bezbednu administraciju adaptiranog mleka '
                                      'kada majka ne doji.',
                              'greske': "Podgrevanje već jednom popijene i ohlađene formule 'da se ne baci' – opasnost "
                                        'od teških crevnih infekcija.',
                              'pitanje': "Šta se dešava ako dadilja sipa 'malo puniju mericu da beba bolje napreduje'?",
                              'teze': 'Formula nije sterilna u kutiji, a bakterija Cronobacter sakazakii može biti '
                                      'smrtonosna za novorođenče. Voda i flašice moraju biti besprekorno čisti. '
                                      'Hranjenje na flašicu zahteva isti kontakt očima i toplinu kao i dojenje.'},
        'module': 'Modul 2',
        'subtitle': 'Precizno doziranje, mikrobiološka bezbednost i pravila hranjenja na flašicu',
        'title': 'Adaptirana formula: Priprema, higijena i bezbednost',
        'title_styled': 'Adaptirana formula: <em>Priprema, higijena i bezbednost</em>'},
    {   'badge': 'MODUL 3: NEGA ODOJČETA',
        'bg_theme': 'light',
        'category': 'ŠETNJA I NAVIKE',
        'content_blocks': [   {   'bullets': [   '<strong>Vreme za prvu šetnju:</strong> Zdravorođena beba može u prvu '
                                                 'šetnju već od 2–3. nedelje života u prolećnim i letnjim mesecima.',
                                                 '<strong>Vremenska ograničenja:</strong> Izbegavati izlazak pri '
                                                 'temperaturama ispod -5°C, iznad 32°C, pri magli, jakom vetru i '
                                                 'povišenom aerozagađenju.',
                                                 '<strong>Postepeno produžavanje boravka:</strong> Prvi dan 15–20 '
                                                 'minuta, zatim postepeno do 1–2 sata dnevno (podstiče apetit i '
                                                 'sintezu vitamina D).',
                                                 '<strong>Zabrana prekrivanja kolica pelenom:</strong> Prekrivanje '
                                                 'kolica pamučnom pelenom podiže temperaturu unutar kolica za 4–7°C '
                                                 '(rizik od toplotnog udara!).'],
                                  'title': 'Protokol za prve šetnje i boravak napolju'},
                              {   'bullets': [   '<strong>Tummy time (Vreme na stomaku):</strong> Od prvih nedelja, '
                                                 '2–3 puta dnevno po par minuta na čvrstoj podlozi dok je beba budna – '
                                                 'jača vrat i leđa.',
                                                 '<strong>Diferencijacija dana i noći:</strong> Dnevne aktivnosti uz '
                                                 'prirodno svetlo i uobičajeni šum; noćna hranjenja u polumraku bez '
                                                 'stimulacije.',
                                                 '<strong>Slobodan pokret bez dubka:</strong> Pedijatrijski zabranjena '
                                                 'upotreba hodalica (dubaka); beba razvija puzanje i hod na podnoj '
                                                 'podlozi (puzzle).',
                                                 '<strong>Senzorna stimulacija bez ekrana:</strong> Pričanje, pevanje, '
                                                 'masaža tela i kontakt očima; NULTA tolerancija na telefone i '
                                                 'televiziju do 2. godine.'],
                                  'title': 'Zdrave životne navike i motorni razvoj'}],
        'id': 17,
        'image': 'p14_img2_736x920.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Uspostaviti zdrave životne navike, pravilan motorni razvoj i bezbedan boravak '
                                      'na svežem vazduhu.',
                              'greske': "Davanje telefona ili puštanje crtaća odojčetu tokom hranjenja kako bi 'mirno "
                                        "jelo'.",
                              'pitanje': 'Zašto Svetska zdravstvena organizacija i pedijatrijska udruženja izričito '
                                         'zabranjuju upotrebu dubka (hodalice)?',
                              'teze': 'Naglasite opasnost prekrivanja kolica leti. Mnogi roditelji prekriju kolica '
                                      'tetra pelenom misleći da štite bebu od sunca, a zapravo stvaraju opasnu rernu. '
                                      'Tummy time je temelj motorike i sprečava zaležanu glavicu (plagiocefaliju).'},
        'module': 'Modul 3',
        'subtitle': 'Boravak na svežem vazduhu, motorni razvoj kroz igru i ritam dana i noći',
        'title': 'Šetnja i zdrave životne navike odojčeta',
        'title_styled': 'Šetnja i <em>zdrave životne navike odojčeta</em>'},
    {   'badge': 'MODUL 3: NEGA ODOJČETA',
        'bg_theme': 'light',
        'category': 'ČVRSTA HRANA',
        'content_blocks': [   {   'bullets': [   '<strong>Uzrast spremnosti (oko 6. meseca):</strong> Dete samostalno '
                                                 'sedi uz podršku, drži stabilno glavu i gubi refleks izbacivanja '
                                                 'hrane jezikom.',
                                                 '<strong>Pravilo 3 dana za novu namirnicu:</strong> Svaka nova '
                                                 'namirnica uvodi se pojedinačno, u prepodnevnim časovima, tokom 3 '
                                                 'uzastopna dana.',
                                                 '<strong>Postupnost u količini i teksturi:</strong> Počinje se sa 1–2 '
                                                 'kašičice finog pirea, postepeno povećavajući obrok; mleko ostaje '
                                                 'primarna ishrana.',
                                                 '<strong>Bez prisiljavanja:</strong> Dete uči da istražuje teksture i '
                                                 'ukuse; prihvatanje pojedinog povrća zahteva i do 10–15 ponuđenih '
                                                 'pokušaja.'],
                                  'title': 'Spremnost deteta i pravilo 3 dana'},
                              {   'bullets': [   '<strong>Redosled uvođenja:</strong> Prvo neutralno povrće (tikvica, '
                                                 'krompir, šargarepa), zatim žitarice bez glutena (pirinač, proso), '
                                                 'voće, pa meso.',
                                                 '<strong>STROGO ZABRANJENO pre 1. godine:</strong> So (opterećuje '
                                                 'bubrege), šećer, kravlje mleko kao napitak i med (smrtonosni '
                                                 'infantilni botulizam!).',
                                                 '<strong>Opasnost od gušenja čvrstom hranom:</strong> Cela zrna '
                                                 'grožđa, čeri paradajz, kokice, tvrde bombone i celi orasi/lešnici '
                                                 'strogo zabranjeni.',
                                                 '<strong>Rano uvođenje alergena:</strong> Gluten, jaje i riba uvode '
                                                 'se pre navršene 1. godine po savremenim smernicama radi smanjenja '
                                                 'rizika od alergija.'],
                                  'title': 'Redosled namirnica i zabranjene namirnice'}],
        'id': 18,
        'image': 'p14_img3_736x1296.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Obučiti polaznice za vođenje nemlečne dohrane po najnovijim pedijatrijskim '
                                      'smernicama uz strogu prevenciju gušenja i botulizma.',
                              'greske': 'Blendiranje hrane u potpuno tečnu kašu do 15. meseca – dete mora razviti '
                                        'žvakanje gnječene hrane do 9–10. meseca.',
                              'pitanje': 'Zašto se nova namirnica nikada ne uvodi uveče pre spavanja?',
                              'teze': 'Podvucite crvenom bojom: MED JE ZABRANJEN pre navršene prve godine života zbog '
                                      'spora Clostridium botulinum. So i šećer se nikada ne dodaju u bebinu hranu. '
                                      'Nova namirnica se daje pre podne kako bi se reakcija uočila tokom dana.'},
        'module': 'Modul 3',
        'subtitle': 'Znakovi spremnosti, redosled namirnica i prevencija nutritivnih rizika',
        'title': 'Uvođenje čvrste hrane (Nemlečna dohrana)',
        'title_styled': 'Uvođenje čvrste hrane <em>(Nemlečna dohrana)</em>'},
    {   'badge': 'MODUL 3: NEGA ODOJČETA',
        'bg_theme': 'light',
        'category': 'DENTICIJA I HIDRACIJA',
        'content_blocks': [   {   'bullets': [   '<strong>Tipični simptomi (4–8. mesec):</strong> Pojačano '
                                                 'balavljenje, otečene desni, grizenje tvrdih predmeta, razdražljivost '
                                                 'i blago nemiran san.',
                                                 '<strong>Šta NIJE simptom zubića:</strong> Temperatura preko 38.5°C, '
                                                 'učestali prolivi i povraćanje nisu izazvani zubićima već infekcijom!',
                                                 '<strong>Hlađene silikonske glodalice:</strong> Glodalice ohlađene u '
                                                 'frižideru (NIKADA u zamrzivaču jer previše hladan predmet oštećuje '
                                                 'desni).',
                                                 '<strong>Masaža desni i gelovi:</strong> Nežna masaža čistim prstom '
                                                 'obmotanim sterilnom gazom; biljni gelovi bez anestetika '
                                                 '(lidokaina).'],
                                  'title': 'Denticija: Simptomi i bezbedno olakšanje'},
                              {   'bullets': [   '<strong>Toaleta pre nicanja zuba:</strong> Svakodnevno brisanje '
                                                 'desni i jezika vlažnom sterilnom gazom nakon večernjeg obroka.',
                                                 '<strong>Pranje prvih zubića:</strong> Čim nikne prvi zubić, koristi '
                                                 'se meka silikonska četkica i pasta prilagođena uzrastu u veličini '
                                                 'zrna pirinča.',
                                                 '<strong>Prevencija karijesa bočice:</strong> Zabrana uspavljivanja '
                                                 'deteta sa flašicom mleka, soka ili zaslađenog čaja u ustima.',
                                                 '<strong>Pravilna hidracija vodom:</strong> Voda se uvodi tek sa '
                                                 'početkom čvrste hrane (oko 6. meseca); do tada isključivo dojenje '
                                                 'ili formula zadovoljavaju žeđ.'],
                                  'title': 'Oralna higijena i uvođenje vode'}],
        'id': 19,
        'image': 'p17_img2_736x1313.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Razjasniti zablude oko nicanja zubića, postaviti temelje oralne higijene i '
                                      'pravilne hidracije odojčeta.',
                              'greske': 'Upotreba gelova sa lidokainom za desni koji mogu utrnuti grlo odojčeta i '
                                        'izazvati zagrcnjavanje ili poremećaj gutanja.',
                              'pitanje': 'Da li je dojenoj bebi od 3 meseca tokom vrelih letnjih dana potrebno davati '
                                         'vodu na flašicu?',
                              'teze': 'Zubići ne izazivaju visoku temperaturu od 39°C. Često roditelji i neobučene '
                                      "dadilje propuste ozbiljnu urinarnu ili virusnu infekciju misleći da je to 'od "
                                      "zubića'. Četkica se uvodi sa prvim zubom."},
        'module': 'Modul 3',
        'subtitle': 'Prepoznavanje simptoma, bezbedno olakšavanje bola i uvođenje vode',
        'title': 'Denticija (Nicanje zubića), oralna higijena i hidracija',
        'title_styled': 'Denticija (Nicanje zubića), <em>oralna higijena i hidracija</em>'},
    {   'badge': 'MODUL 3: NEGA ODOJČETA',
        'bg_theme': 'light',
        'category': 'VAKCINACIJA ODOJČETA',
        'content_blocks': [   {   'bullets': [   '<strong>Vakcinacija u porodilištu:</strong> BCG vakcina (protiv '
                                                 'tuberkuloze) i prva doza vakcine protiv Hepatitisa B aplikuju se na '
                                                 'rođenju.',
                                                 '<strong>Kombinovane petovalentne/šestovalentne:</strong> '
                                                 'DTaP-IPV-Hib-HepB u 2, 3.5 i 5. mesecu štite od difterije, tetanusa, '
                                                 'velikog kašlja, poliomijelitisa i hemofilusa.',
                                                 '<strong>Pneumokokna vakcina:</strong> Štiti odojčad od teških '
                                                 'bakterijskih upala pluća, meningitisa, sepse i gnojne upale srednjeg '
                                                 'uva.',
                                                 '<strong>MMR vakcina (12–15. mesec):</strong> Štiti dete od malih '
                                                 'boginja (morbila), zaušaka (mumpsa) i rubeole.'],
                                  'title': 'Kalendar imunizacije u prvoj godini'},
                              {   'bullets': [   '<strong>Zdravstveni status deteta:</strong> Dete mora biti potpuno '
                                                 'zdravo na dan vakcinacije; obavezan detaljan pregled izabranog '
                                                 'pedijatra.',
                                                 '<strong>Udobna odeća:</strong> Oblačenje deteta u meku pamučnu odeću '
                                                 'koja se lako raskopčava u predelu butine gde se daje vakcina.',
                                                 '<strong>Smirivanje i podrška:</strong> Dojenje, flašica ili zagrljaj '
                                                 'neposredno nakon uboda deluju umirujuće i smanjuju bol.',
                                                 '<strong>Vođenje evidencije:</strong> Upisivanje datuma, serije '
                                                 'vakcine i planiranih revakcina u Dnevnik nege i koordinacija sa '
                                                 'roditeljima.'],
                                  'title': 'Uloga dadilje u pripremi za vakcinaciju'}],
        'id': 20,
        'image': 'p1_img1_2000x2000.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Upoznati polaznice sa obaveznim kalendarom vakcinacije i njihovom ulogom u '
                                      'pripremi deteta i asistenciji roditeljima.',
                              'greske': "Davanje sirupa za snižavanje temperature PRE odlaska na vakcinaciju 'da ne bi "
                                        "dobilo temperaturu' – dokazano smanjuje efikasnost vakcine.",
                              'pitanje': 'Koje preglede pedijatar mora obaviti pre nego što odobri davanje vakcine?',
                              'teze': 'Imunizacija je civilizacijsko dostignuće koje spasava živote dece. Dadilja mora '
                                      'imati pozitivan, profesionalan i smiren stav, bez prenošenja sopstvenih '
                                      'strahova na dete.'},
        'module': 'Modul 3',
        'subtitle': 'Redovni kalendar vakcina, pedijatrijski pregled i priprema deteta',
        'title': 'Vakcinacija odojčeta: Kalendar imunizacije i priprema',
        'title_styled': 'Vakcinacija odojčeta: <em>Kalendar imunizacije i priprema</em>'},
    {   'badge': 'MODUL 3: NEGA ODOJČETA',
        'bg_theme': 'light',
        'category': 'PUTOVANJA SA ODOJČETOM',
        'content_blocks': [   {   'bullets': [   "<strong>Auto-sedište ('jaje') u kontra-smeru:</strong> Postavljeno "
                                                 'isključivo suprotno od smera kretanja vozila (rear-facing) sa '
                                                 'isključenim prednjim vazdušnim jastukom.',
                                                 '<strong>Pravilo 2 sata na putu:</strong> Na dužim putovanjima '
                                                 'automobilom obavezne su pauze na svaka 2 sata (vađenje bebe iz '
                                                 'sedišta, prepovijanje i istezanje).',
                                                 '<strong>Kontrola klime u automobilu:</strong> Razlika između spoljne '
                                                 'i unutrašnje temperature ne sme prelaziti 5–6°C; ventilacija ne sme '
                                                 'duvati direktno u bebu.',
                                                 '<strong>Putovanje avionom:</strong> Dojenje ili hranjenje na flašicu '
                                                 'tokom poletanja i sletanja sprečava bol u ušima usled promene '
                                                 'kabinskog pritiska.'],
                                  'title': 'Bezbednost u prevozu i priprema za put'},
                              {   'bullets': [   '<strong>Zaštita od sunca na moru:</strong> Bebe do 6 meseci se '
                                                 'NIKADA ne izlažu direktnom suncu; posle 6 meseci mineralni UV 50+ '
                                                 'preparati bez hemijskih filtera.',
                                                 '<strong>Zabrana boravka na plaži (10h–17h):</strong> Strogo '
                                                 'izbegavanje jakog UV zračenja; obavezni pamučni šeširići sa širokim '
                                                 'obodom i naočare za sunce.',
                                                 '<strong>Zimski uslovi i planina:</strong> Slojevito oblačenje '
                                                 "(skafander); zaštita lica hranljivom 'cold' kremom bez vode 20 "
                                                 'minuta pre izlaska na mraz.',
                                                 '<strong>Period aklimatizacije:</strong> Ostaviti detetu 24–48 sati '
                                                 'za mirno navikavanje na novu sredinu, vodu, krevetac i nadmorsku '
                                                 'visinu.'],
                                  'title': 'Specifičnosti letovanja i zimovanja'}],
        'id': 21,
        'image': 'p7_img2_1080x1350.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Pripremiti dadilju za bezbedno praćenje porodice na putovanjima, letovanjima i '
                                      'zimovanjima po Royal Nanny standardu.',
                              'greske': "Vožnja deteta u naručju odraslog 'samo par minuta dok se ne smiri' – "
                                        'smrtonosan rizik i pri najmanjem kočenju.',
                              'pitanje': 'Šta ćete uraditi ako tokom vožnje na autoputu beba počne neutešno da plače '
                                         'zato što je gladna?',
                              'teze': 'Putovanja sa bebom zahtevaju vojničku organizaciju. Auto-sedište je obavezno u '
                                      'svakom trenutku kretanja vozila – NIKADA se dete ne vadi iz sedišta tokom '
                                      'vožnje da bi se nahranilo.'},
        'module': 'Modul 3',
        'subtitle': 'Bezbednost u vožnji, adaptacija na klimu, zaštita od sunca i zimskih uslova',
        'title': 'Putovanje sa odojčetom: Priprema, letovanje i zimovanje',
        'title_styled': 'Putovanje sa odojčetom: <em>Priprema, letovanje i zimovanje</em>'},
    {   'badge': 'MODUL 4: NEGA BOLESNOG DETETA',
        'bg_theme': 'light',
        'category': 'GRČEVI (KOLIKE)',
        'content_blocks': [   {   'bullets': [   '<strong>Pravilo trojke po Vesselu:</strong> Plač traje duže od 3 '
                                                 'sata dnevno, najmanje 3 dana u nedelji, tokom perioda od 3 uzastopne '
                                                 'nedelje.',
                                                 '<strong>Tipična klinička slika:</strong> Iznenadan neutešan plač u '
                                                 'kasno popodne, crveno lice, stisnute pesnice i nožice privučene ka '
                                                 'napetom stomaku.',
                                                 '<strong>Uzroci kolika:</strong> Nezrelost gastrointestinalnog i '
                                                 'nervnog sistema, aerofagija (gutanje vazduha) i senzorno '
                                                 'preopterećenje.',
                                                 '<strong>Umirujući stav dadilje:</strong> Dadilja mora zračiti '
                                                 'staloženošću; anksioznost i panika odraslih prenose se na bebu i '
                                                 'pojačavaju plač.'],
                                  'title': 'Dijagnostički kriterijumi i priroda kolika'},
                              {   'bullets': [   "<strong>Položaj 'tigar na drvetu':</strong> Beba leži potrbuške na "
                                                 'podlaktici dadilje; blag pritisak na trbušni zid pruža trenutno '
                                                 'olakšanje od gasova.',
                                                 "<strong>Masaža abdomena i 'bicikl':</strong> Nežni kružni pokreti u "
                                                 'smeru kazaljke na satu i savijanje kolena ka stomaku radi evakuacije '
                                                 'gasova.',
                                                 '<strong>Topli oblozi na stomačić:</strong> Zagrejana pamučna tetra '
                                                 'pelena ili termofor sa košticama višnje položen preko bebinog '
                                                 'bodića.',
                                                 '<strong>Beli šum i nošenje u marami:</strong> Zvuci materice (beli '
                                                 'šum, šum vode) i ritmično nošenje smiruju nervni sistem '
                                                 'novorođenčeta.'],
                                  'title': 'Nefarmakološke mere i tehnike olakšanja'}],
        'id': 22,
        'image': 'slide20_baby_colic_care.jpg',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Obučiti polaznice za smireno, stručno i efikasno zbrinjavanje beba sa '
                                      'infantilnim kolikama bez panike i nepotrebnih lekova.',
                              'greske': 'Nervozno i grubo trešenje bebe (Shaken Baby Syndrome) u trenucima frustracije '
                                        'plačem – fatalne posledice za mozak novorođenčeta!',
                              'pitanje': 'Koja je razlika između plača izazvanog grčevima i plača koji ukazuje na '
                                         'akutni abdomen ili upalu uva?',
                              'teze': "Kolike nisu bolest već prolazna razvojna faza. Najvažniji 'lek' je mirna, "
                                      'staložena dadilja koja roditeljima uliva sigurnost dok beba prolazi kroz '
                                      'napad.'},
        'module': 'Modul 4',
        'subtitle': 'Definicija po Vesselu, biomehaničke tehnike smirivanja i podrška roditeljima',
        'title': 'Grčevi kod beba (Infantilne kolike): Smiren pristup i nega',
        'title_styled': 'Grčevi kod beba (Infantilne kolike): <em>Smiren pristup i nega</em>'},
    {   'badge': 'MODUL 4: NEGA BOLESNOG DETETA',
        'bg_theme': 'light',
        'category': 'OSIPI I KOŽNE PROMENE',
        'content_blocks': [   {   'bullets': [   '<strong>Uzroci nastanka:</strong> Vlaga, trenje, amonijak iz urina i '
                                                 'enzimi stolice narušavaju kožnu barijeru pelenske regije.',
                                                 '<strong>Higijena čistom mlakom vodom:</strong> Čim se pojavi '
                                                 'crvenilo, potpuno obustaviti vlažne maramice; prati bebu isključivo '
                                                 'mlakom vodom i tapkati suvim peškirom.',
                                                 '<strong>Kreme sa cink-oksidom:</strong> Nanosi se tanak zaštitni '
                                                 'film paste sa cinkom koja odbija vlagu i pomaže epitelizaciju '
                                                 'oštećene kože.',
                                                 "<strong>'Vazdušno kupanje':</strong> Ostaviti bebu razgolićenu bez "
                                                 'pelene što duže na nepropusnoj podlozi; vazduh je najmoćniji '
                                                 'prirodni lek za ojed.'],
                                  'title': 'Pelenski dermatitis (Ojed)'},
                              {   'bullets': [   '<strong>Toplotni osip (Miliarija):</strong> Sitne crvene tačkice na '
                                                 'vratu, grudima i pregibima usled pretopljavanja; prolazi '
                                                 'rashlađivanjem.',
                                                 '<strong>Atopijski ekcem:</strong> Suva, zadebljala crvena polja koja '
                                                 'svrbe; zahteva intenzivnu negu medicinskim emolijensima bez parfema.',
                                                 '<strong>Kandida u pelenskoj regiji:</strong> Jarko crvenilo sa '
                                                 'satelitskim tačkicama na rubovima; zahteva antimikotičnu mast po '
                                                 'nalogu pedijatra.',
                                                 '<strong>CRVENA ZASTAVICA: Petehije:</strong> Tačkasta krvarenja koja '
                                                 'NE BLEDE pod pritiskom staklene čaše – HITAN TRANSPORT U BOLNICU '
                                                 '(sumnja na sepsu/meningitis)!'],
                                  'title': 'Osipi po telu i crvene zastavice'}],
        'id': 23,
        'image': 'p16_img1_735x919.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Osposobiti dadilje za diferencijaciju bezazlenih kožnih promena od ozbiljnih '
                                      'pedijatrijskih stanja i test staklene čaše.',
                              'greske': 'Nanošenje kortikosteroidnih masti na svoju ruku bez izričitog pregleda i '
                                        'recepta pedijatra.',
                              'pitanje': 'Zašto vlažne maramice pogoršavaju pelenski osip čim se pojavi oštećenje '
                                         'kože?',
                              'teze': "Demonstrirajte 'test staklene čaše' (tumbler test): ako se pritisne dno čaše na "
                                      'osip i crvenilo ne izbledi, u pitanju je krvarenje u koži (petehije) – minut je '
                                      'važan, odmah se zove 194.'},
        'module': 'Modul 4',
        'subtitle': 'Diferencijacija osipa, prevencija ojeda i hitne crvene zastavice',
        'title': 'Osip po telu, pelenski osip i promene na koži',
        'title_styled': 'Osip po telu, pelenski osip i <em>promene na koži</em>'},
    {   'badge': 'MODUL 4: NEGA BOLESNOG DETETA',
        'bg_theme': 'light',
        'category': 'RESPIRATORNE I OČNE INFEKCIJE',
        'content_blocks': [   {   'bullets': [   '<strong>Zašto je zapušen nos kritičan:</strong> Odojčad dišu '
                                                 'isključivo na nos; zapušenost onemogućava sisanje, hranjenje i '
                                                 'dovodi do nemirnog sna i gubitka težine.',
                                                 '<strong>Ispiranje fiziološkim rastvorom (0.9% NaCl):</strong> Beba '
                                                 'leži na boku; ukapava se ili lagano ubrizgava 1–2 ml fiziološkog u '
                                                 'gornju nozdrvu radi razređivanja sekreta.',
                                                 '<strong>Nazalna aspiracija:</strong> Upotreba aspiratora (manuelnog '
                                                 'ili priključenog na usisivač) nežno i kratko, isključivo nakon '
                                                 'razmekšavanja sekreta rastvorom.',
                                                 '<strong>Ovlaživanje vazduha:</strong> Ultrazvučni ovlaživač u sobi i '
                                                 'podizanje uzglavlja kreveca za 30° olakšavaju disanje i sprečavaju '
                                                 'slivanje sekreta.'],
                                  'title': 'Zapušen nos kod odojčeta (Rinitis)'},
                              {   'bullets': [   '<strong>Simptomi infekcije:</strong> Crvenilo vežnjače, otok kapaka, '
                                                 'gust žućkast ili zelenkast sekret koji slepljuje trepavice nakon '
                                                 'buđenja.',
                                                 '<strong>Toaleta sterilnom gazom:</strong> Briše se od spoljašnjeg '
                                                 'ugla oka ka nosu; za svako oko koristi se nova sterilna gaza '
                                                 'natopljena fiziološkim rastvorom.',
                                                 '<strong>Stroga zabrana čaja od kamilice:</strong> Kamilica se NIKADA '
                                                 'ne stavlja na bebino oko – nije sterilna, sadrži alergene polena i '
                                                 'pogoduje razvoju bakterija.',
                                                 '<strong>Aplikacija antibiotskih kapi/masti:</strong> Isključivo po '
                                                 'nalogu lekara; vrh kapaljke ne sme dodirnuti oko kako se bočica ne '
                                                 'bi kontaminirala.'],
                                  'title': 'Infekcija oka (Konjunktivitis)'}],
        'id': 24,
        'image': 'slide24_respiratory_care.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Usvojiti pravilnu tehniku toalete nosa i sterilnu negu oka uz eliminaciju '
                                      'opasnih narodnih metoda poput kamilice.',
                              'greske': 'Ukapavanje kapi za nos za odrasle (dekongestiva) u bebin nos – rizik od '
                                        'kolapsa i zastoja disanja!',
                              'pitanje': 'U kom položaju beba mora da leži prilikom obilnog ispiranja nosnih hodnika '
                                         'fiziološkim rastvorom?',
                              'teze': 'Zapušen nos kod odojčeta je urgentan problem jer beba ne može istovremeno da '
                                      'diše na usta i sisa. Nos mora biti prohodan pre svakog podoja i spavanja. Čaj '
                                      'od kamilice je zabranjen u modernoj pedijatriji.'},
        'module': 'Modul 4',
        'subtitle': 'Toaleta disajnih puteva, aspiracija sekreta i higijenski protokol konjunktivitisa',
        'title': 'Zapušen nos i infekcija oka kod odojčadi',
        'title_styled': 'Zapušen nos i <em>infekcija oka kod odojčadi</em>'},
    {   'badge': 'MODUL 4: NEGA BOLESNOG DETETA',
        'bg_theme': 'light',
        'category': 'VAKCINALNE REAKCIJE',
        'content_blocks': [   {   'bullets': [   '<strong>Lokalna reakcija na mestu uboda:</strong> Blag otok, '
                                                 'crvenilo i bolnost na butini; stavljaju se suve hladne obloge preko '
                                                 'tkanine (nikada led ili alkohol na ubod).',
                                                 '<strong>Fiziološka febrilnost (24–48h):</strong> Umereno povišena '
                                                 'temperatura je normalan znak imunološkog odgovora i stvaranja '
                                                 'antitela; pojačati unos tečnosti.',
                                                 '<strong>Prolazna pospanost i razdražljivost:</strong> Dete može biti '
                                                 'pospanije ili plačljivije tokom prvog dana; pružiti dodatnu nežnost, '
                                                 'mir i komfor.',
                                                 '<strong>BCG reakcija (nakon 4–6 nedelja):</strong> Pojava crvenog '
                                                 'čvorića, gnojnice i krastice na ramenu; NIKADA ne istiskivati i ne '
                                                 'mazati (prirodan proces).'],
                                  'title': 'Uobičajene postvakcinalne reakcije'},
                              {   'bullets': [   '<strong>Praćenje temperature:</strong> Redovno merenje digitalnim '
                                                 'toplomerom; paracetamol dati samo ako temperatura pređe 38.5°C '
                                                 'rektalno.',
                                                 '<strong>Zabrana preventivnog davanja lekova:</strong> Paracetamol se '
                                                 'NE DAJE preventivno pre ili odmah posle vakcine jer umanjuje '
                                                 'stvaranje antitela.',
                                                 '<strong>Upozoravajući znaci za pedijatra:</strong> Neutešan vrišteći '
                                                 'plač duži od 3 sata, febrilne konvulzije, otok mesta uboda veći od 5 '
                                                 'cm ili izrazita klonulost.',
                                                 '<strong>Zapisivanje u Dnevnik nege:</strong> Tačno vreme '
                                                 'vakcinacije, izmerene temperature i sve primećene promene precizno '
                                                 'se evidentiraju.'],
                                  'title': 'Protokol nege i upozoravajući znaci'}],
        'id': 25,
        'image': 'slide21_fever_check_hd.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Obučiti polaznice za pravilno postvakcinalno praćenje odojčeta i smirivanje '
                                      'roditeljske zabrinutosti.',
                              'greske': 'Istiskivanje gnojnog čvorića na mestu BCG vakcine na ramenu bebe – to može '
                                        'dovesti do duboke infekcije kosti i limfnih čvorova.',
                              'pitanje': 'Koliko dugo je normalno da traje povišena temperatura nakon primljene '
                                         'petovalentne vakcine?',
                              'teze': 'Reakcija na vakcinu u vidu blage temperature do 38.5°C nije komplikacija već '
                                      'dokaz da imuni sistem radi. Objasnite zašto se na mesto uboda ne stavlja oblog '
                                      'od alkohola (isušuje i peče ranu).'},
        'module': 'Modul 4',
        'subtitle': 'Očekivane lokalne i opšte reakcije, nega mesta uboda i kada kontaktirati lekara',
        'title': 'Vakcinacija: Postvakcinalne reakcije i nega deteta',
        'title_styled': 'Vakcinacija: <em>Postvakcinalne reakcije i nega deteta</em>'},
    {   'badge': 'MODUL 4: NEGA BOLESNOG DETETA',
        'bg_theme': 'light',
        'category': 'DIGESTIVNE SMETNJE',
        'content_blocks': [   {   'bullets': [   '<strong>Rizik od brze dehidracije:</strong> Učestale vodenaste '
                                                 'stolice kod odojčeta mogu dovesti do teške dehidracije unutar svega '
                                                 'nekoliko sati.',
                                                 '<strong>Oralna rehidracija (O.R.S.):</strong> Zlatni standard – '
                                                 'kesica ORS rastvorena u prokuvanoj vodi daje se kašičicom na svakih '
                                                 '5 minuta u malim gutljajima.',
                                                 '<strong>Nastavak dojenja bez prekida:</strong> Dojenje se NIKADA ne '
                                                 'prekida tokom dijareje; majčino mleko obnavlja crevnu sluzokožu i '
                                                 'hidrira.',
                                                 '<strong>Znaci teške dehidracije (HITNO 194):</strong> Upala '
                                                 'fontanela, suva usta i jezik, plač bez suza, pelena suva duže od 6 '
                                                 'sati i letargija.'],
                                  'title': 'Dijareja (Proliv) i prevencija dehidracije'},
                              {   'bullets': [   '<strong>Fiziologija stolice dojene bebe:</strong> Dojena beba može '
                                                 'imati stolicu posle svakog podoja, ali i jednom u 7–10 dana ako je '
                                                 'meka i beba napreduje.',
                                                 '<strong>Kada je u pitanju zatvor:</strong> Tvrda, suva, brabonjasta '
                                                 'stolica uz bolan plač, napinjanje i tragove krvi usled analnih '
                                                 'fisura.',
                                                 '<strong>Korekcija ishrane i navika:</strong> Kod dece na dohrani '
                                                 'povećati unos vode, pasiranih šljiva, tikvica i krušaka; smanjiti '
                                                 'pirinač i bananu.',
                                                 '<strong>Stroga zabrana invazivnih metoda:</strong> NIKADA ne gurati '
                                                 'toplomer, sapun ili štapiće u čmar radi izazivanja stolice (opasnost '
                                                 'od traume i spazma)!'],
                                  'title': 'Opstipacija (Zatvor) kod odojčadi'}],
        'id': 26,
        'image': 'slide23_digestive_dehydration.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Osposobiti polaznice za brzu procenu dehidracije, primenu ORS rastvora i '
                                      'eliminaciju opasnih metoda kod opstipacije.',
                              'greske': 'Davanje lekova protiv proliva za odrasle (poput loperamida) deci – to '
                                        'parališe creva i može biti smrtonosno.',
                              'pitanje': 'Zašto se detetu koje povraća i ima proliv ne sme dati puna flašica vode ili '
                                         'čaja odjednom?',
                              'teze': 'Dehidracija je najveći neprijatelj odojčeta sa dijarejom. Pokažite znake: '
                                      'uvučena fontanela, suve usne, nedostatak suza. Objasnite tehniku davanja ORS '
                                      'rastvora kap po kap ili kašičicu po kašičicu.'},
        'module': 'Modul 4',
        'subtitle': 'Prevencija dehidracije, oralni rehidracioni rastvori (ORS) i regulacija stolice',
        'title': 'Digestivni poremećaji: Opstipacija i dijareja',
        'title_styled': 'Digestivni poremećaji: <em>Opstipacija i dijareja</em>'},
    {   'badge': 'MODUL 4: NEGA BOLESNOG DETETA',
        'bg_theme': 'light',
        'category': 'FEBRILNA STANJA',
        'content_blocks': [   {   'bullets': [   '<strong>Rektalno merenje (zlatni standard do 1. god):</strong> '
                                                 'Digitalni toplomer sa elastičnim vrhom; febrilnost je vrednost preko '
                                                 '38.5°C.',
                                                 '<strong>Aksilarno merenje (pazuh):</strong> Vrednost je za oko 0.5°C '
                                                 'niža nego rektalno; temperatura preko 38.0°C smatra se febrilnošću.',
                                                 '<strong>Beba mlađa od 3 meseca:</strong> Svaka temperatura iznad '
                                                 '38.0°C kod bebe u prva 3 meseca zahteva HITAN pregled pedijatra!',
                                                 '<strong>Opšte stanje važnije od broja:</strong> Ne leči se cifra na '
                                                 'toplomeru već dete; da li dete uspostavlja kontakt očima, pije '
                                                 'tečnost i mokri.'],
                                  'title': 'Definicija febrilnosti i merenje'},
                              {   'bullets': [   '<strong>Raskomoćivanje deteta:</strong> Skinuti suvišne slojeve '
                                                 'odeće; ostaviti dete u laganom pamučnom bodiću na sobnoj temperaturi '
                                                 'od 20–22°C.',
                                                 '<strong>Tuširanje mlakom vodom (36–37°C):</strong> Kupanje ili '
                                                 'tuširanje mlakom vodom tokom 10–15 minuta; NIKADA hladnom vodom '
                                                 '(izaziva drhtavicu i skok T!).',
                                                 '<strong>Pojačana hidratacija:</strong> Češći podoji, gutljaji vode '
                                                 'ili rastvora elektrolita sprečavaju dehidraciju usled ubrzanog '
                                                 'disanja i znojenja.',
                                                 '<strong>STROGA ZABRANA ALKOHOLA I SIRĆETA:</strong> Utrljavanje '
                                                 'alkohola ili sirćeta je opasno po život – alkohol se upija kroz kožu '
                                                 'i izaziva trovanje i komu!'],
                                  'title': 'Fizikalne mere obaranja temperature'}],
        'id': 27,
        'image': 'slide22_pediatric_dosage_card.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Usvojiti pravilne protokole merenja temperature i efikasne mere fizikalnog '
                                      'rashlađivanja bez narodnih zabluda.',
                              'greske': "Uvijanje febrilnog deteta u jorgane i ćebad 'da se preznoji' – to vodi pravo "
                                        'u toplotni udar i febrilne konvulzije.',
                              'pitanje': 'Zašto hladna voda i ledene obloge zapravo podižu unutrašnju temperaturu '
                                         'tela?',
                              'teze': 'Podvucite: alkohol i sirće su strogo zabranjeni u pedijatriji! Koža bebe je '
                                      'tanak sunđer koji apsorbuje alkohol direktno u krvotok. Tuširanje se radi '
                                      'isključivo mlakom vodom (36-37°C).'},
        'module': 'Modul 4',
        'subtitle': 'Metode merenja, aksilarna vs rektalna temperatura i fizikalno hlađenje',
        'title': 'Visoka temperatura: Granične vrednosti i fizikalne mere',
        'title_styled': 'Visoka temperatura: <em>Granične vrednosti i fizikalne mere</em>'},
    {   'badge': 'MODUL 4: NEGA BOLESNOG DETETA',
        'bg_theme': 'light',
        'category': 'POVREDE I NEZGODE',
        'content_blocks': [   {   'bullets': [   '<strong>Prva reakcija nakon pada:</strong> Ne pomerati naglo bebu '
                                                 'ako se sumnja na povredu vrata; proveriti svest, disanje i reakciju '
                                                 'zenica.',
                                                 '<strong>Hladan oblog na hematom:</strong> Led umotan u pamučnu '
                                                 'tkaninu držati 10–15 minuta radi sprečavanja širenja potkožnog '
                                                 'krvarenja.',
                                                 '<strong>5 znakova za HITNU POMOĆ (194):</strong> Gubitak svesti, '
                                                 'povraćanje u mlazu više od 2 puta, asimetrične zenice, letargija i '
                                                 'curenje bistre tečnosti iz nosa/uva.',
                                                 '<strong>Praćenje 48 sati:</strong> Buditi dete noću na svaka 3–4 '
                                                 'sata radi provere stanja svesti i koordinacije pokreta.'],
                                  'title': 'Padovi sa visine i povrede glave (48h protokol)'},
                              {   'bullets': [   '<strong>Opekotine (vrela voda, kafa):</strong> Odmah hladiti pod '
                                                 'tekućom hladnom vodom 10–15 minuta; pokriti sterilnom gazom '
                                                 '(zabranjeni ulje, mast i belance!).',
                                                 '<strong>Gušenje kod odojčeta (do 1. god):</strong> Beba se postavlja '
                                                 'potrbuške duž podlaktice sa glavom naniže; zadaje se 5 udaraca '
                                                 'dlanom u leđa.',
                                                 '<strong>5 pritisaka na grudnu kost:</strong> Ako strano telo nije '
                                                 'izbačeno, okrenuti bebu na leđa i pritisnuti sredinu grudne kosti sa '
                                                 'dva prsta 5 puta.',
                                                 '<strong>Hajmlihov zahvat (posle 1. god):</strong> Primenjuje se samo '
                                                 'kod starije dece koja stoje ili sede; nikada kod odojčadi zbog '
                                                 'rizika od povrede jetre.'],
                                  'title': 'Prva pomoć: Opekotine i gušenje stranim telom'}],
        'id': 28,
        'image': 'slide27_infant_choking_protocol.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Drilovati protokole prve pomoći kod najčešćih i najopasnijih trauma u dečjem '
                                      'uzrastu do nivoa automatske reakcije.',
                              'greske': 'Stavljanje masti, masti od jazavca ili belanca na opekotinu – to zadržava '
                                        'toplotu u dubini tkiva i dovodi do sepse.',
                              'pitanje': 'Koja je ključna razlika u prvoj pomoći kod gušenja odojčeta (do 1 godine) i '
                                         'todlera (posle 1 godine)?',
                              'teze': 'Demonstrirajte prvu pomoć kod gušenja odojčeta na lutki: 5 udaraca u leđa, 5 '
                                      'pritisaka na grudnu kost. Kod opekotina pravilo je: VODA, VODA, VODA – hladiti '
                                      '15 minuta pre bilo kakvog transporta.'},
        'module': 'Modul 4',
        'subtitle': 'Protokoli prve pomoći kod hitnih pedijatrijskih stanja u kućnim uslovima',
        'title': 'Povrede i nezgode: Padovi, povrede glave, opekotine i gušenje',
        'title_styled': 'Povrede i nezgode: <em>Padovi, povrede glave, opekotine i gušenje</em>'},
    {   'badge': 'MODUL 4: NEGA BOLESNOG DETETA',
        'bg_theme': 'light',
        'category': 'ZARAZNE BOLESTI I ALERGIJE',
        'content_blocks': [   {   'bullets': [   '<strong>Varičela (Ovčije boginje):</strong> Vezikule ispunjene '
                                                 "bistrom tečnošću ('kapi rose') koje svrbe; higijena ruku, kratki "
                                                 'noktići i antiseptički gel za svrab.',
                                                 '<strong>Šesta bolest (Roseola infantum):</strong> Iznenadna visoka '
                                                 'temperatura 3 dana; po padu temperature izbija sitan ružičasti osip '
                                                 'po trupu koji brzo prolazi.',
                                                 '<strong>BRNU sindrom (Ruke, noge, usta):</strong> Bolne ranice u '
                                                 'usnoj duplji i vezikule na dlanovima i tabanima; meka prohladna '
                                                 'hrana i hidratacija.',
                                                 '<strong>Izolacija i mere opreza:</strong> Zaraženo dete ne dolazi u '
                                                 'kontakt sa drugom decom i trudnicama; redovno provetravanje i '
                                                 'dezinfekcija igračaka.'],
                                  'title': 'Uobičajene zarazne bolesti kod dece'},
                              {   'bullets': [   '<strong>Ujed krpelja:</strong> Pincetom uhvatiti što bliže koži i '
                                                 'povući ravno nagore; NIKADA ne mazati alkoholom ili uljem (gušenje '
                                                 'tera krpelja da povrati toksine!).',
                                                 '<strong>Ujed ose ili pčele:</strong> Žaoku sastrugati tupom stranom '
                                                 'kartice ili noža (ne stiskati pincetom); hladan oblog lokalno radi '
                                                 'smanjenja otoka.',
                                                 '<strong>Urtikarija (Koprivnjača):</strong> Crveni izdignuti pečati '
                                                 'koji svrbe i migriraju po telu; znak alergijske reakcije na hranu '
                                                 'ili lekove.',
                                                 '<strong>CRVENI ALARM: Anafilaksa (HITNO 194):</strong> Otok usana, '
                                                 'jezika, otežano čujno disanje (stridor), gušenje i bledo-siva koža – '
                                                 'ODMAH 194 i EpiPen ako je propisan!'],
                                  'title': 'Ujedi insekata i anafilaktički šok'}],
        'id': 29,
        'image': 'slide28_insect_bites_allergies.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Osposobiti polaznice za prepoznavanje tipičnih dečjih osipnih groznica i hitno '
                                      'delovanje kod teških alergijskih reakcija.',
                              'greske': "Čekanje da 'alergija sama prođe' kada dete počne da otječe u licu ili otežano "
                                        'diše.',
                              'pitanje': 'Zašto se krpelj pre vađenja nikada ne sme premazivati acetonom, uljem ili '
                                         'alkoholom?',
                              'teze': 'Kod anafilakse sekunde odlučuju. Polaznice moraju prepoznati rane znake: '
                                      'oticanje očnih kapaka i usana, promuklost i kašalj poput laveža psa (stridor). '
                                      'Pokažite pravilno vađenje krpelja.'},
        'module': 'Modul 4',
        'subtitle': 'Prepoznavanje dečjih osipnih groznica, lokalne reakcije i anafilaksa',
        'title': 'Zarazne bolesti, ujedi insekata i alergije',
        'title_styled': 'Zarazne bolesti, <em>ujedi insekata i alergije</em>'},
    {   'badge': 'MODUL 4: NEGA BOLESNOG DETETA',
        'bg_theme': 'light',
        'category': 'PUTNA I KUĆNA APOTEKA',
        'content_blocks': [   {   'bullets': [   '<strong>Antipiretički segment:</strong> Paracetamol (sirup i čepići) '
                                                 'i Ibuprofen sirup sa originalnim baždarenim špricevima za doziranje '
                                                 'po kilogramu.',
                                                 '<strong>Gastroenterološki segment:</strong> Kesice oralnog '
                                                 'rehidracionog rastvora (O.R.S.) i pedijatrijski probiotik u kapima '
                                                 'za regulaciju crevne flore.',
                                                 '<strong>Respiratorni segment:</strong> Fiziološki rastvor u ampulama '
                                                 '(0.9% NaCl), nosni aspirator i sterilni špricevi za toaletu disajnih '
                                                 'puteva.',
                                                 '<strong>Sanitetski i antiseptički pribor:</strong> Octenisept sprej '
                                                 '(ne peče), sterilne gaze, flasteri, digitalni toplomer i anatomska '
                                                 'pinceta za krpelje.'],
                                  'title': '4 obavezna segmenta dečje apoteke'},
                              {   'bullets': [   '<strong>Bezbedno čuvanje van domašaja:</strong> Apoteka mora biti '
                                                 'zaključana na visini preko 1.5 m, van vidokruga i domašaja radoznale '
                                                 'dece.',
                                                 '<strong>Temperaturni režim:</strong> Čuvanje na suvom i tamnom mestu '
                                                 'do 25°C; lekovi koji zahtevaju hladan lanac (određeni '
                                                 'antibiotici/probiotici) u frižideru.',
                                                 '<strong>Revizija rokova upotrebe:</strong> Provera rokova trajanja '
                                                 'na svakih 6 meseci; obavezno upisivanje datuma otvaranja na bočicama '
                                                 'sirupa i kapi.',
                                                 '<strong>Zapis brojeva hitnih službi:</strong> U kutiji apoteke uvek '
                                                 'se nalazi cedulja sa brojem izabranog pedijatra, dežurne dečje '
                                                 'bolnice i Hitne pomoći (194).'],
                                  'title': 'Skladištenje, revizija i odgovornost'}],
        'id': 30,
        'image': 'slide30_apoteka_kit.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Standardizovati sadržaj i bezbedno rukovanje kućnom i putnom pedijatrijskom '
                                      'apotekom.',
                              'greske': 'Držanje lekova u noćnom ormariću ili na stolu gde ih dete može dohvatiti i '
                                        'progutati.',
                              'pitanje': 'Koliko dugo sirup paracetamola ili antibiotska suspenzija smeju da se '
                                         'koriste nakon prvog otvaranja bočice?',
                              'teze': 'Kada nastupi hitna situacija, nema vremena za odlazak u dežurnu apoteku. Sve '
                                      'mora biti u kući, sa važećim rokom i baždarenim špricem. Apoteka mora biti '
                                      'strogo zaključana.'},
        'module': 'Modul 4',
        'subtitle': 'Obavezni set lekova, sanitetski materijal, uslovi čuvanja i provera rokova',
        'title': 'Zlatni standard putne i kućne apoteke za decu',
        'title_styled': 'Zlatni standard <em>putne i kućne apoteke za decu</em>'},
    {   'badge': 'MODUL 4: NEGA BOLESNOG DETETA',
        'bg_theme': 'light',
        'category': 'ADMINISTRACIJA LEKOVA',
        'content_blocks': [   {   'bullets': [   '<strong>1. Pravi pacijent:</strong> Proveriti ime deteta pre '
                                                 'aplikacije, posebno u domovima sa više dece različitog uzrasta.',
                                                 '<strong>2. Pravi lek:</strong> Trostruka provera naziva na ambalaži '
                                                 '(pri uzimanju, pre merenja i pre vraćanja u apoteku).',
                                                 '<strong>3. Prava doza (PO KILOGRAMIMA):</strong> Doziranje se računa '
                                                 'ISKLJUČIVO prema težini deteta u kilogramima, nikada prema uzrastu '
                                                 'sa kutije!',
                                                 '<strong>4. Pravo vreme:</strong> Strogo poštovanje vremenskih '
                                                 'intervala (npr. antibiotik na 8h ili 12h, antipiretik na 4–6h).',
                                                 '<strong>5. Pravi način:</strong> Oralno, rektalno, nazalno ili '
                                                 'okularno – striktno poštovanje propisanog puta aplikacije.'],
                                  'title': "Protokol '5 PRAVILA BEZBEDNOSTI'"},
                              {   'bullets': [   '<strong>Oralni špric (NIKADA kašičicom):</strong> Špric se uvodi uz '
                                                 'unutrašnju stranu obraza (ka kutnjacima); lek se istiskuje lagano u '
                                                 'ritmu gutanja (ne u grlo!).',
                                                 '<strong>Položaj deteta:</strong> Dete mora biti u polusedećem '
                                                 'položaju u naručju (stroga zabrana davanja sirupa u ležećem položaju '
                                                 'zbog aspiracije).',
                                                 '<strong>Aplikacija čepića (supozitorija):</strong> Dete leži na boku '
                                                 'sa savijenim nožicama; nakon umetanja stisnuti gluteuse tokom 60 '
                                                 'sekundi da čepić ne ispadne.',
                                                 '<strong>Evidencija u Dnevnik nege:</strong> Svaki dati lek (tačan '
                                                 'naziv, doza u ml/mg, vreme davanja i potpis dadilje) unosi se u '
                                                 'Dnevnik nege.'],
                                  'title': 'Tehnike aplikacije sirupa, čepića i kapi'}],
        'id': 31,
        'image': 'slide31_safe_medicine_admin.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Usvojiti farmakološku bezbednost i savladati tehnike aplikacije lekova bez '
                                      'rizika od aspiracije i traumatskog iskustva za dete.',
                              'greske': 'Špricanje celokupne doze leka direktno u grlo deteta – to izaziva '
                                        'laringospazam, gušenje i povraćanje.',
                              'pitanje': 'Šta ćete uraditi ako dete povrati lek 5 minuta nakon što ste mu dali sirup '
                                         'paracetamola?',
                              'teze': 'Lek se dozira po KILOGRAMIMA. Dete od 2 godine može imati 10 kg ili 16 kg – '
                                      'doza ne može biti ista. Kašičice iz kuhinje su zabranjene (zapremine variraju '
                                      'od 2.5 do 7 ml). Uvek se koristi originalni dozirni špric.'},
        'module': 'Modul 4',
        'subtitle': 'Protokol 5 pravila, doziranje po kilogramu i tehnika aplikacije bez stresa',
        'title': 'Davanje lekova: Tehnike bezbedne administracije',
        'title_styled': 'Davanje lekova: <em>Tehnike bezbedne administracije</em>'},
    {   'badge': 'ZAVRŠNI MODUL: STANDARDI IZVRSNOSTI',
        'bg_theme': 'dark',
        'category': 'ETIKA I PROTOKOL',
        'content_blocks': [   {   'bullets': [   '<strong>Precizna dnevna evidencija:</strong> Svaki obrok (vreme, '
                                                 'količina), intervali sna, broj i izgled pelena, temperatura i '
                                                 'raspoloženje evidentiraju se u Dnevnik nege.',
                                                 '<strong>Primopredaja dužnosti roditeljima:</strong> Strukturiran '
                                                 'usmeni i pismeni brifing na kraju smene pruža roditeljima apsolutan '
                                                 'mir i uvid u ritam deteta.',
                                                 '<strong>Diplomatska i topla komunikacija:</strong> Asertivan, smiren '
                                                 'i profesionalan ton; poštovanje roditeljskog stila vaspitanja i '
                                                 'pravila luksuznog doma.',
                                                 '<strong>Profesionalni bonton u kući:</strong> Uredna uniforma, '
                                                 'besprekorna lična higijena, nenametljivo prisustvo i tačnost u '
                                                 'minut.'],
                                  'title': 'Vođenje Dnevnika nege i komunikacija'},
                              {   'bullets': [   '<strong>Apsolutna diskrecija (Ugovor o poverljivosti - '
                                                 'NDA):</strong> Stroga zabrana deljenja informacija o porodici, deci, '
                                                 'adresi i navikama doma na društvenim mrežama ili trećim licima.',
                                                 '<strong>Zabrana fotografisanja:</strong> Fotografisanje dece i '
                                                 'enterijera privatnim telefonom najstrože je zabranjeno bez izričite '
                                                 'pismene saglasnosti roditelja.',
                                                 '<strong>Stručni saradnik programa:</strong> Spec. strukovna '
                                                 'med-sestra Jelena Aleksić • Garant najviših pedijatrijskih i '
                                                 'kliničkih standarda.',
                                                 '<strong>Završna evaluacija i licenca:</strong> Polaganje praktičnih '
                                                 'simulacija na lutkama, provera znanja iz urgentne pedijatrije i '
                                                 'dodela Royal Nanny sertifikata.'],
                                  'title': 'Diskrecija, etika i sertifikacija'}],
        'id': 32,
        'image': 'p12_img1_736x1104.png',
        'layout': 'split_right_image',
        'lecturer_notes': {   'cilj': 'Zaključiti obuku, definisati profesionalni i etički kodeks i pripremiti '
                                      'polaznice za uspešan rad u klijentskim porodicama.',
                              'greske': 'Objavljivanje bilo kakve fotografije deteta ili enterijera na Instagramu ili '
                                        'TikToku – to povlači trenutni otkaz i gubitak licence.',
                              'pitanje': 'Kako ćete odgovoriti prijateljima ili poznanicima koji vas pitaju kod koga '
                                         'radite i kako izgleda kuća poznatog klijenta?',
                              'teze': 'Izvrsnost je navika, a ne jednokratan čin. Dnevnik nege je ogledalo '
                                      'profesionalnosti, a diskrecija je sveta. Zahvalite se polaznicama u ime '
                                      'saradnika Spec. strukovne med-sestre Jelene Aleksić i brenda Royal Nanny.'},
        'module': 'Završni modul',
        'subtitle': 'Partnerstvo sa roditeljima, standardi elitne nege i sertifikacija predavača',
        'title': 'Dnevnik nege, diskrecija i etički kodeks Royal Nanny',
        'title_styled': 'Dnevnik nege, <em>diskrecija i etički kodeks Royal Nanny</em>'}]
