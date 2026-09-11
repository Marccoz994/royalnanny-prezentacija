# Royal Nanny Akademija – Prezentacija za obuku predavača

Ekskluzivna, profesionalna edukativna prezentacija i prateći materijali za obuku predavača **Royal Nanny Akademije**.  
**Saradnik i autor kurikuluma:** Spec. strukovna med-sestra Jelena Aleksić

---

## 🌟 4 Zvanična edukativna modula

1. **Modul 1 – Higijena i nega novorođenčeta**:
   - Priprema sobe za bebu, nameštaja i opreme za bebu
   - Kupanje bebe (priprema i tehnika)
   - Nega kože
   - Nega pupčanika i pupčane rane
   - Nega čula
   - Oblačenje bebe
   - Položaj pri hranjenju, nošenju i spavanju
   - Higijena bebine garderobe i bebinog pribora

2. **Modul 2 – Dojenje**:
   - Prednosti dojenja
   - Higijena i nega dojki
   - Priprema dojki za podoj
   - Položaji pri dojenju
   - Pravilno postavljanje bebe na dojku
   - Ispucale bradavice – ragade
   - Upala dojki
   - Izmazanje majčinog mleka
   - Čuvanje mleka
   - Adaptirana formula

3. **Modul 3 – Nega odojčeta**:
   - Vakcinacija
   - Šetnja
   - Uvođenje čvrste hrane
   - Zdrave životne navike
   - Denticija
   - Putovanje

4. **Modul 4 – Nega bolesnog deteta**:
   - Grčevi
   - Osip po telu, pelenski osip
   - Infekcija oka
   - Zapušen nos
   - Vakcinacija (postvakcinalne reakcije i nega)
   - Opstipacija – dijareja
   - Visoka temperatura
   - Povrede i nezgode
   - Zarazne bolesti
   - Ujed insekta
   - Alergije
   - Putna apoteka
   - Davanje lekova

---

## 🎛️ Mogućnosti prezentacije

- **Interaktivna HTML prezentacija (`index.html`)**:
  - 📥 **Dugme za preuzimanje PPTX-a**: Direktan download kompletne PowerPoint prezentacije sa svim slajdovima i beleškama.
  - 🎙️ **Režim za predavača (Speaker Notes)**: Pritisnite taster `N` ili kliknite na "Beleške" za detaljan vodič kroz predavanje i diskusije.
  - 🎛️ **Pregled svih slajdova (Overview mode)**: Pritisnite `O` ili "Pregled" za brzu navigaciju.
  - ⌨️ **Tastaturna navigacija**: Strelice levo/desno, razmaknica ili dugmad na ekranu.
  - 🎨 **Prilagođeni Royal Nanny dizajn**: Luksuzna paleta (Navy plava `#0B1B2B`, šampanj zlatna `#C5A880`, krem bela `#F7F5F0`), prilagođene infografike bez duplih okvira, jasna tipografija i optimalna čitljivost.
- **PowerPoint verzija (`ROYAL_NANNY_Obuka_Predavaci.pptx`)**:
  - Format 16:9, kompletno uređeni slajdovi, integrisane visoko-rezolutivne pedijatrijske infografike i speaker notes ugrađeni u svaki slajd.

---

## 📁 Struktura projekta

- `index.html` / `ROYAL_NANNY_Obuka_Predavaci.html` – Interaktivna web prezentacija (spremna za GitHub Pages ili lokalni pregled)
- `ROYAL_NANNY_Obuka_Predavaci.pptx` – PowerPoint prezentacija za predavače
- `extracted_assets/` – Sve optimizovane grafike, infografike, dijagrami i brend elementi
- `Vodic_Za_Predavace_Royal_Nanny.md` – Kompletan tekstualni vodič za predavače
- `slides_data.py` – Strukturirana baza svih 32 slajda sa tekstovima, tačkama i speaker notes
- `generate_visual_assets.py` – Skripta za generisanje pedijatrijskih i kliničkih infografika
- `generate_pptx.py` – Skripta za automatsko generisanje `.pptx` datoteke
- `generate_html.py` – Skripta za kreiranje `.html` interaktivne prezentacije
- `generate_all.py` – Master skripta za regenerisanje svih materijala u jednom koraku

---

## 🚀 Pokretanje i generisanje

### 1. Lokalni pregled prezentacije
Jednostavno otvorite `index.html` u bilo kom modernom web pregledaču (Chrome, Safari, Firefox, Edge).

### 2. Ponovno generisanje svih materijala
Ukoliko izmenite podatke u `slides_data.py`, pokrenite:
```bash
python3 generate_all.py
```
Ova skripta će automatski osvežiti sve vizuelne elemente, PowerPoint fajl i HTML interaktivnu prezentaciju.
