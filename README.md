# Royal Nanny Akademija – Prezentacija za obuku predavača

Ekskluzivna, profesionalna edukativna prezentacija i prateći materijali za obuku predavača **Royal Nanny Akademije**.

---

## 🌟 Ključne karakteristike

- **32 detaljno razrađena slajda**: Od nege novorođenčeta, dojenja i bezbednosti, do hitnih stanja, komunikacije sa roditeljima i pravnog okvira.
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
