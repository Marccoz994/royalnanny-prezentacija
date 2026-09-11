#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROYAL NANNY - Master skripta za generisanje prezentacije za predavače i kompletnih edukativnih materijala.
Pokreće:
1. generate_visual_assets.py -> kreira sve visokorezolutivne kliničke i pedijatrijske infografike
2. generate_pptx.py          -> generiše ROYAL_NANNY_Obuka_Predavaci.pptx sa 32 slajda, slikama i speaker notes
3. generate_html.py          -> generiše ROYAL_NANNY_Obuka_Predavaci.html interaktivnu prezentaciju sa navigacijom
"""

import subprocess
import sys
import os

BASE_DIR = "/Users/markozivkovic/PREZENTACIJA ZA ROYAL NANNY"

def run_step(script_name, description):
    print(f"\n==========================================")
    print(f"▶ {description} ({script_name})")
    print(f"==========================================")
    script_path = os.path.join(BASE_DIR, script_name)
    res = subprocess.run([sys.executable, script_path], cwd=BASE_DIR)
    if res.returncode != 0:
        print(f"❌ Greška pri izvršavanju {script_name}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    print("🚀 POKREĆEM KOMPLETAN MASTER BUILD ROYAL NANNY PREZENTACIJE...")
    run_step("generate_visual_assets.py", "Generisanje pedijatrijskih infografika i dijagrama")
    run_step("generate_pptx.py", "Generisanje PowerPoint prezentacije (.pptx)")
    run_step("generate_html.py", "Generisanje interaktivne HTML prezentacije (.html)")
    print("\n🎉 SVI FAJLOVI SU USPEŠNO GENERISANI I SPREMNI ZA RAD!")
