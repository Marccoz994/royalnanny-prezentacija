#!/usr/bin/env python3
"""
ROYAL NANNY - Skripta za generisanje prezentacije za predavače
Kreira:
1. ROYAL_NANNY_Obuka_Predavaci.pptx (PowerPoint sa beleskama predavaca)
2. ROYAL_NANNY_Obuka_Predavaci.html (Interaktivna web prezentacija)
"""

import os
import json
import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

print("Generating Royal Nanny lecture presentation...")
