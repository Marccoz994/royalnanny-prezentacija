#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator za ROYAL_NANNY_Obuka_Predavaci.html
Kreira interaktivnu, modernu web prezentaciju sa navigacijom, modom za predavača,
pregledom slajdova i print-to-PDF stilovima.
"""

import os
import json
import base64
from slides_data import SLIDES_DATA

BASE_DIR = "/Users/markozivkovic/PREZENTACIJA ZA ROYAL NANNY"
ASSETS_DIR = os.path.join(BASE_DIR, "extracted_assets")
OUTPUT_HTML = os.path.join(BASE_DIR, "ROYAL_NANNY_Obuka_Predavaci.html")

def get_base64_img(filename):
    path = os.path.join(ASSETS_DIR, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            ext = filename.split(".")[-1].lower()
            mime = "image/png" if ext == "png" else "image/jpeg"
            return f"data:{mime};base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

def build_html():
    print(f"Pokrećem generisanje interaktivne HTML prezentacije: {OUTPUT_HTML}")
    
    logo_dark_b64 = get_base64_img("logo_horizontal_transparent.png")
    logo_light_b64 = get_base64_img("logo_horizontal_light.png")
    logo_mark_dark_b64 = get_base64_img("logo_mark_transparent.png")
    logo_mark_light_b64 = get_base64_img("logo_mark_light.png")
    logo_mark_cream_b64 = get_base64_img("logo_mark_cream.png")
    
    slides_json = json.dumps(SLIDES_DATA, ensure_ascii=False)
    
    template = """<!DOCTYPE html>
<html lang="sr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Royal Nanny Akademija • Obuka za predavače</title>
    
    <!-- Google Fonts: Libre Baskerville & Poppins -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --c-dark: #47342E;
            --c-bg: #F7F5F0;
            --c-sand: #CDBBA0;
            --c-linen: #F0E9D7;
            --c-terra: #765535;
            --c-sage: #8B906D;
            --c-olive: #69614F;
            --c-gold: #D1AE66;
            --c-blush: #E7DBCE;
            --c-border: #E4DCCE;
            --c-card-bg: #FFFFFF;
            --c-text-muted: #7A7067;
            --font-title: 'Libre Baskerville', Georgia, serif;
            --font-body: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
            --shadow-sm: 0 4px 12px rgba(71, 52, 46, 0.05);
            --shadow-md: 0 10px 30px rgba(71, 52, 46, 0.08);
            --shadow-lg: 0 20px 40px rgba(71, 52, 46, 0.12);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: var(--font-body);
            background-color: #1E1715;
            color: var(--c-dark);
            height: 100vh;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            user-select: none;
        }

        /* Progress Bar */
        .progress-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: rgba(255, 255, 255, 0.1);
            z-index: 1000;
        }

        .progress-bar {
            height: 100%;
            width: 0%;
            background: linear-gradient(90deg, var(--c-sand), var(--c-gold));
            transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        /* App Header Controls */
        .top-navbar {
            height: 54px;
            background: #2D2320;
            color: var(--c-linen);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 24px;
            border-bottom: 1px solid rgba(205, 187, 160, 0.2);
            z-index: 100;
        }

        .brand-zone {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .brand-logo-img {
            height: 26px;
            filter: brightness(1.2);
        }

        .module-indicator {
            font-size: 11px;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: var(--c-sand);
            font-weight: 600;
            background: rgba(205, 187, 160, 0.15);
            padding: 4px 12px;
            border-radius: 20px;
            border: 1px solid rgba(205, 187, 160, 0.3);
        }

        .actions-zone {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .btn-nav {
            background: rgba(255, 255, 255, 0.08);
            color: var(--c-linen);
            border: 1px solid rgba(205, 187, 160, 0.3);
            border-radius: 6px;
            padding: 6px 14px;
            font-size: 12px;
            font-family: var(--font-body);
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 6px;
            text-decoration: none;
        }

        .btn-nav:hover {
            background: var(--c-sand);
            color: var(--c-dark);
            border-color: var(--c-sand);
        }

        .btn-nav.active {
            background: var(--c-sand);
            color: var(--c-dark);
            font-weight: 600;
        }

        .btn-download-pptx {
            background: rgba(209, 174, 102, 0.18);
            border-color: var(--c-gold);
            color: var(--c-gold);
            font-weight: 600;
        }

        .btn-download-pptx:hover {
            background: var(--c-gold);
            color: var(--c-dark);
            border-color: var(--c-gold);
        }

        .slide-counter-badge {
            font-size: 13px;
            font-weight: 600;
            letter-spacing: 1px;
            color: var(--c-gold);
            padding: 0 10px;
        }

        /* Main Stage */
        .stage-wrapper {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 12px;
            position: relative;
            overflow: hidden;
            width: 100%;
            height: calc(100vh - 52px - 34px);
            box-sizing: border-box;
        }

        .slide-deck-scaler {
            width: calc(1600px * var(--slide-scale, 1));
            height: calc(900px * var(--slide-scale, 1));
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            transition: width 0.15s ease, height 0.15s ease;
        }

        /* Slide Frame: Exactly 16:9 Aspect Ratio Base Canvas (1600x900) */
        .slide-deck-frame {
            width: 1600px;
            height: 900px;
            background-color: var(--c-bg);
            border-radius: 12px;
            box-shadow: var(--shadow-lg), 0 0 0 1px rgba(205, 187, 160, 0.25);
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(var(--slide-scale, 1));
            transform-origin: center center;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            flex-shrink: 0;
            box-sizing: border-box;
        }

        /* Slide Container */
        .slide-content {
            width: 1600px;
            height: 900px;
            padding: 30px 48px 22px 48px;
            display: flex;
            flex-direction: column;
            position: relative;
            box-sizing: border-box;
        }

        .slide-content.dark-theme {
            background-color: var(--c-dark);
            color: var(--c-linen);
        }

        /* Header inside slide */
        .slide-inner-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 14px;
        }

        .slide-titles-wrap {
            flex: 1;
        }

        .brand-eyebrow {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 6px;
        }

        .rn-monogram-mark {
            height: 28px;
            width: auto;
            object-fit: contain;
        }

        .category-pill {
            display: inline-block;
            font-size: 12.5px;
            letter-spacing: 2.5px;
            text-transform: uppercase;
            font-weight: 700;
            color: var(--c-terra);
        }

        .dark-theme .category-pill {
            color: var(--c-sand);
        }

        .slide-h1 {
            font-family: var(--font-title);
            font-size: 36px;
            font-weight: 700;
            line-height: 1.2;
            color: var(--c-dark);
            letter-spacing: -0.4px;
        }

        .dark-theme .slide-h1 {
            color: var(--c-linen);
        }

        .slide-h1 em {
            font-style: italic;
            font-family: var(--font-title);
            color: var(--c-terra);
            font-weight: 400;
        }

        .dark-theme .slide-h1 em {
            color: var(--c-gold);
            font-weight: 400;
        }

        .slide-sub {
            font-size: 17.5px;
            color: var(--c-olive);
            margin-top: 5px;
            font-weight: 400;
            line-height: 1.42;
        }

        .dark-theme .slide-sub {
            color: rgba(240, 233, 215, 0.75);
        }

        .slide-watermark-logo {
            height: 38px;
            opacity: 0.9;
        }

        /* Slide Body Layouts */
        .slide-body {
            flex: 1;
            display: flex;
            gap: 24px;
            min-height: 0;
        }

        /* Layout: Split Right Image */
        .layout-split-image {
            display: grid;
            grid-template-columns: 1.18fr 0.82fr;
            gap: 24px;
            height: 100%;
            min-height: 0;
            flex: 1;
        }

        .split-text-col {
            display: flex;
            flex-direction: column;
            gap: 14px;
            height: 100%;
            min-height: 0;
        }

        .split-image-col {
            height: 100%;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid var(--c-border);
            box-shadow: var(--shadow-sm);
            background: #EDE6D8;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
        }

        .split-image-col img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            display: block;
        }

        .photo-overlay-badge {
            position: absolute;
            top: 14px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(45, 35, 32, 0.55);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            padding: 5px 14px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.25);
            pointer-events: none;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.25);
        }

        .photo-overlay-badge img {
            height: 15px;
            width: auto;
            object-fit: contain;
            filter: brightness(1.25);
        }

        /* Layout: Two Column Cards */
        .layout-two-col,
        .layout-two-cards {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
            height: 100%;
            min-height: 0;
            flex: 1;
        }

        /* Layout: Three Cards */
        .layout-three-cards {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 20px;
            height: 100%;
            min-height: 0;
            flex: 1;
        }

        /* Layout: Matrix 4 Quadrants */
        .layout-matrix-4 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: 1fr 1fr;
            gap: 16px;
            height: 100%;
            min-height: 0;
            flex: 1;
        }

        /* Standard Cards - Title anchored at top, bullets centered in remainder */
        .proto-card {
            background: var(--c-card-bg);
            border: 1px solid var(--c-border);
            border-left: 5px solid var(--c-terra);
            border-radius: 12px;
            padding: 22px 28px;
            box-shadow: var(--shadow-sm);
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            flex: 1;
            min-height: 0;
            overflow: hidden;
            box-sizing: border-box;
        }

        .dark-theme .proto-card {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(205, 187, 160, 0.22);
            border-left: 5px solid var(--c-gold);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        }

        .proto-card-title {
            font-family: var(--font-title);
            font-size: 23px;
            font-weight: 700;
            color: var(--c-dark);
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 8px;
            line-height: 1.25;
            flex-shrink: 0;
        }

        .dark-theme .proto-card-title {
            color: var(--c-sand);
        }

        .proto-card-desc {
            font-size: 17px;
            line-height: 1.52;
            color: #382F2B;
            margin-bottom: 8px;
        }

        .dark-theme .proto-card-desc {
            color: var(--c-linen);
        }

        .proto-bullets {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 10px;
            flex: 1;
            justify-content: center;
        }

        .proto-bullets li {
            font-size: 17px;
            line-height: 1.48;
            color: #382F2B;
            position: relative;
            padding-left: 18px;
        }

        .dark-theme .proto-bullets li {
            color: var(--c-linen);
        }

        .proto-bullets li::before {
            content: "•";
            position: absolute;
            left: 2px;
            top: -1px;
            color: var(--c-terra);
            font-weight: bold;
            font-size: 18px;
        }

        .dark-theme .proto-bullets li::before {
            color: var(--c-gold);
        }

        .proto-bullets li strong {
            color: var(--c-dark);
            font-weight: 600;
        }

        .dark-theme .proto-bullets li strong {
            color: var(--c-sand);
        }

        /* Metrics Strip */
        .metrics-strip {
            display: flex;
            gap: 12px;
            margin-bottom: 8px;
            flex-shrink: 0;
        }

        .metric-badge {
            background: var(--c-linen);
            border: 1px solid var(--c-sand);
            border-radius: 9px;
            padding: 8px 16px;
            display: flex;
            flex-direction: column;
            flex: 1;
            box-sizing: border-box;
        }

        .dark-theme .metric-badge {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(205, 187, 160, 0.3);
        }

        .metric-val {
            font-family: var(--font-title);
            font-size: 30px;
            font-weight: 700;
            color: var(--c-terra);
            line-height: 1.1;
        }

        .dark-theme .metric-val {
            color: var(--c-gold);
        }

        .metric-lbl {
            font-size: 12.5px;
            color: var(--c-olive);
            text-transform: uppercase;
            letter-spacing: 0.6px;
            font-weight: 600;
            margin-top: 2px;
        }

        .dark-theme .metric-lbl {
            color: rgba(240, 233, 215, 0.8);
        }

        /* Layout specific adjustments */
        .layout-three-cards .proto-card {
            padding: 18px 22px;
        }
        .layout-three-cards .proto-card-title {
            font-size: 20.5px;
            margin-bottom: 8px;
        }
        .layout-three-cards .proto-bullets {
            gap: 8px;
        }
        .layout-three-cards .proto-bullets li {
            font-size: 16px;
            line-height: 1.44;
        }

        .layout-matrix-4 .proto-card {
            padding: 14px 18px;
        }
        .layout-matrix-4 .proto-card-title {
            font-size: 19.5px;
            margin-bottom: 6px;
        }
        .layout-matrix-4 .proto-bullets {
            gap: 6px;
        }
        .layout-matrix-4 .proto-bullets li {
            font-size: 15.2px;
            line-height: 1.42;
        }

        /* Density modifiers */
        .density-medium .split-text-col {
            gap: 12px;
        }
        .density-medium .proto-card {
            padding: 18px 24px;
        }
        .density-medium .proto-card-title {
            font-size: 19.5px;
            margin-bottom: 8px;
        }
        .density-medium .proto-bullets {
            gap: 8px;
        }
        .density-medium .proto-bullets li {
            font-size: 15px;
            line-height: 1.45;
        }

        .density-compact .split-text-col {
            gap: 10px;
        }
        .density-compact .metrics-strip {
            gap: 10px;
            margin-bottom: 6px;
        }
        .density-compact .metric-badge {
            padding: 6px 12px;
        }
        .density-compact .metric-val {
            font-size: 23px;
        }
        .density-compact .metric-lbl {
            font-size: 11px;
        }
        .density-compact .proto-card {
            padding: 15px 22px;
            border-left-width: 4px;
        }
        .density-compact .proto-card-title {
            font-size: 18.5px;
            margin-bottom: 6px;
        }
        .density-compact .proto-bullets {
            gap: 6px;
        }
        .density-compact .proto-bullets li {
            font-size: 14.5px;
            line-height: 1.42;
            padding-left: 16px;
        }

        /* Slide Footer */
        .slide-inner-footer {
            height: 32px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid rgba(71, 52, 46, 0.1);
            margin-top: 12px;
            padding-top: 8px;
        }

        .dark-theme .slide-inner-footer {
            border-top-color: rgba(205, 187, 160, 0.2);
        }

        .footer-values-strip {
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 2.5px;
            text-transform: uppercase;
            color: var(--c-sand);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .dark-theme .footer-values-strip {
            color: var(--c-sand);
        }

        .footer-values-strip .val-dot {
            color: var(--c-gold);
            font-size: 12px;
        }

        .footer-meta-strip {
            font-size: 11px;
            color: var(--c-text-muted);
            letter-spacing: 0.8px;
            display: flex;
            align-items: center;
            gap: 16px;
        }

        .dark-theme .footer-meta-strip {
            color: rgba(205, 187, 160, 0.7);
        }

        .footer-slide-num {
            font-weight: 700;
            color: var(--c-terra);
            font-size: 12px;
        }

        .dark-theme .footer-slide-num {
            color: var(--c-gold);
        }

        /* Presenter Drawer */
        .presenter-panel {
            position: fixed;
            bottom: 50px;
            right: 20px;
            width: 480px;
            max-height: 70vh;
            background: #2B211E;
            color: var(--c-linen);
            border: 1px solid var(--c-sand);
            border-radius: 12px;
            box-shadow: var(--shadow-lg);
            z-index: 500;
            display: none;
            flex-direction: column;
            overflow: hidden;
            animation: slideUp 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .presenter-panel.open {
            display: flex;
        }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .presenter-header {
            padding: 14px 18px;
            background: #211917;
            border-bottom: 1px solid rgba(205, 187, 160, 0.2);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .presenter-header h3 {
            font-family: var(--font-title);
            font-size: 14px;
            color: var(--c-gold);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .btn-close-notes {
            background: none;
            border: none;
            color: var(--c-sand);
            font-size: 18px;
            cursor: pointer;
        }

        .presenter-body {
            padding: 18px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 16px;
            font-size: 12.5px;
            line-height: 1.6;
        }

        .note-box {
            background: rgba(255, 255, 255, 0.04);
            border-left: 3px solid var(--c-sand);
            padding: 10px 14px;
            border-radius: 0 6px 6px 0;
        }

        .note-box.warning {
            border-left-color: #D96B43;
            background: rgba(217, 107, 67, 0.08);
        }

        .note-box.question {
            border-left-color: var(--c-gold);
            background: rgba(209, 174, 102, 0.08);
        }

        .note-box-title {
            font-weight: 600;
            color: var(--c-sand);
            margin-bottom: 4px;
            font-size: 11px;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .note-box.warning .note-box-title {
            color: #E28867;
        }

        .note-box.question .note-box-title {
            color: var(--c-gold);
        }

        /* Grid View */
        .grid-modal {
            position: fixed;
            top: 54px;
            left: 0;
            width: 100vw;
            height: calc(100vh - 54px);
            background: rgba(20, 15, 13, 0.95);
            backdrop-filter: blur(8px);
            z-index: 800;
            display: none;
            padding: 40px;
            overflow-y: auto;
        }

        .grid-modal.open {
            display: block;
        }

        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
            gap: 20px;
            max-width: 1400px;
            margin: 0 auto;
        }

        .thumb-card {
            background: var(--c-bg);
            border-radius: 8px;
            aspect-ratio: 16 / 9;
            padding: 14px;
            cursor: pointer;
            border: 2px solid transparent;
            transition: all 0.2s ease;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }

        .thumb-card:hover {
            border-color: var(--c-sand);
            transform: translateY(-4px);
        }

        .thumb-card.active {
            border-color: var(--c-gold);
            box-shadow: 0 0 15px rgba(209, 174, 102, 0.5);
        }

        .thumb-card.dark {
            background: var(--c-dark);
            color: var(--c-linen);
        }

        .thumb-num {
            font-size: 11px;
            font-weight: bold;
            color: var(--c-terra);
        }

        .thumb-card.dark .thumb-num {
            color: var(--c-sand);
        }

        .thumb-title {
            font-family: var(--font-title);
            font-size: 11.5px;
            font-weight: bold;
            line-height: 1.3;
        }

        .thumb-cat {
            font-size: 9px;
            text-transform: uppercase;
            color: var(--c-text-muted);
            letter-spacing: 0.5px;
        }

        .thumb-card.dark .thumb-cat {
            color: rgba(205, 187, 160, 0.7);
        }

        /* Bottom Floating Bar */
        .bottom-bar {
            height: 48px;
            background: #241C1A;
            color: var(--c-linen);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 24px;
            font-size: 11px;
            border-top: 1px solid rgba(205, 187, 160, 0.15);
        }

        .keyboard-shortcuts {
            display: flex;
            gap: 16px;
            color: var(--c-sand);
        }

        .kbd {
            background: rgba(255, 255, 255, 0.1);
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
            font-size: 10px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            margin-right: 4px;
            color: #FFF;
        }

        /* Print / PDF Styles */
        @media print {
            body {
                background: none !important;
                color: #000 !important;
                height: auto !important;
                overflow: visible !important;
            }

            .top-navbar, .bottom-bar, .presenter-panel, .grid-modal, .progress-container {
                display: none !important;
            }

            @page {
                size: 1600px 900px landscape;
                margin: 0;
            }

            .stage-wrapper {
                padding: 0 !important;
                display: block !important;
                height: 900px !important;
                width: 1600px !important;
            }

            .slide-deck-scaler {
                width: 1600px !important;
                height: 900px !important;
                --slide-scale: 1 !important;
            }

            .slide-deck-frame {
                position: relative !important;
                top: 0 !important;
                left: 0 !important;
                transform: none !important;
                width: 1600px !important;
                height: 900px !important;
                max-height: none !important;
                aspect-ratio: 16 / 9 !important;
                page-break-after: always !important;
                box-shadow: none !important;
                border: none !important;
                border-radius: 0 !important;
            }
        }
    </style>
</head>
<body>

    <div class="progress-container">
        <div class="progress-bar" id="progressBar"></div>
    </div>

    <header class="top-navbar">
        <div class="brand-zone">
            <img src="{{LOGO_LIGHT}}" alt="Royal Nanny" class="brand-logo-img">
            <span class="module-indicator" id="moduleBadge">Modul 0: Uvod</span>
        </div>
        <div class="actions-zone">
            <button class="btn-nav" id="btnPrev" title="Prethodni slajd (←)">‹ Prethodni</button>
            <span class="slide-counter-badge" id="slideCounter">01 / 32</span>
            <button class="btn-nav" id="btnNext" title="Sledeći slajd (→)">Sledeći ›</button>
            <button class="btn-nav" id="btnGrid" title="Pregled svih slajdova (G)">☷ Slajdovi</button>
            <button class="btn-nav" id="btnNotes" title="Beleške za predavača (N)">📝 Beleške</button>
            <button class="btn-nav" id="btnFullscreen" title="Puni ekran (F)">⛶ Fullscreen</button>
            <button class="btn-nav" id="btnPrint" title="Štampaj ili sačuvaj kao PDF">🖨️ PDF</button>
            <a href="ROYAL_NANNY_Obuka_Predavaci.pptx" download="ROYAL_NANNY_Obuka_Predavaci.pptx" class="btn-nav btn-download-pptx" id="btnDownloadPptx" title="Preuzmi PowerPoint prezentaciju (.pptx)">📥 Preuzmi PPTX</a>
        </div>
    </header>

    <main class="stage-wrapper" id="stageWrapper">
        <div class="slide-deck-scaler" id="slideScaler">
            <div class="slide-deck-frame" id="slideFrame">
                <div class="slide-content" id="slideContent"></div>
            </div>
        </div>
    </main>

    <footer class="bottom-bar">
        <div class="keyboard-shortcuts">
            <span><span class="kbd">←</span> <span class="kbd">→</span> Navigacija</span>
            <span><span class="kbd">Space</span> Sledeći</span>
            <span><span class="kbd">N</span> Beleške za predavača</span>
            <span><span class="kbd">G</span> Pregled svih slajdova</span>
            <span><span class="kbd">F</span> Puni ekran</span>
        </div>
        <div style="color: var(--c-sand);">
            Predavač: <strong>Jelena Aleksić</strong> • Royal Nanny 2026
        </div>
    </footer>

    <div class="presenter-panel" id="presenterPanel">
        <div class="presenter-header">
            <h3>📝 Beleške & Metodika za predavača</h3>
            <button class="btn-close-notes" id="btnCloseNotes">✕</button>
        </div>
        <div class="presenter-body" id="presenterBody"></div>
    </div>

    <div class="grid-modal" id="gridModal">
        <div class="grid-container" id="gridContainer"></div>
    </div>

    <script>
        const SLIDES = {{SLIDES_DATA_PLACEHOLDER}};
        const LOGO_DARK = "{{LOGO_DARK}}";
        const LOGO_LIGHT = "{{LOGO_LIGHT}}";
        const LOGO_MARK_DARK = "{{LOGO_MARK_DARK}}";
        const LOGO_MARK_LIGHT = "{{LOGO_MARK_LIGHT}}";
        const LOGO_MARK_CREAM = "{{LOGO_MARK_CREAM}}";
        
        let currentIndex = 0;
        let isNotesOpen = false;
        let isGridOpen = false;

        const slideFrame = document.getElementById("slideFrame");
        const slideContent = document.getElementById("slideContent");
        const slideCounter = document.getElementById("slideCounter");
        const moduleBadge = document.getElementById("moduleBadge");
        const progressBar = document.getElementById("progressBar");
        const presenterPanel = document.getElementById("presenterPanel");
        const presenterBody = document.getElementById("presenterBody");
        const btnNotes = document.getElementById("btnNotes");
        const gridModal = document.getElementById("gridModal");
        const gridContainer = document.getElementById("gridContainer");

        function renderSlide(index) {
            const s = SLIDES[index];
            const isDark = s.bg_theme === "dark";
            
            const blocks = s.content_blocks || [];
            const numCards = blocks.length || 1;
            const maxBullets = blocks.reduce((max, b) => Math.max(max, b.bullets ? b.bullets.length : 0), 0);
            const totalBullets = blocks.reduce((acc, b) => acc + (b.bullets ? b.bullets.length : 0), 0);
            const hasMetrics = Boolean(s.metrics && s.metrics.length > 0);
            let densityClass = "";
            if (numCards >= 3 || (hasMetrics && totalBullets >= 8) || maxBullets >= 5) {
                densityClass = " density-compact";
            } else if (hasMetrics || totalBullets >= 7) {
                densityClass = " density-medium";
            }
            
            slideContent.className = "slide-content" + (isDark ? " dark-theme" : "") + densityClass;
            
            const currentLogo = isDark ? LOGO_LIGHT : LOGO_DARK;
            const currentMonogram = isDark ? LOGO_MARK_CREAM : LOGO_MARK_DARK;
            
            let headerHtml = `
                <div class="slide-inner-header">
                    <div class="slide-titles-wrap">
                        <div class="brand-eyebrow">
                            <img src="${currentMonogram}" alt="RN" class="rn-monogram-mark">
                            <span class="category-pill">${s.category || "ROYAL NANNY"}</span>
                        </div>
                        <h1 class="slide-h1">${s.title_styled || s.title}</h1>
                        ${s.subtitle ? `<p class="slide-sub">${s.subtitle}</p>` : ""}
                    </div>
                    <img src="${currentLogo}" alt="Royal Nanny" class="slide-watermark-logo">
                </div>
            `;

            let bodyHtml = `<div class="slide-body">`;
            
            let metricsHtml = "";
            if (s.metrics && s.metrics.length > 0) {
                metricsHtml = `<div class="metrics-strip">` + s.metrics.map(m => `
                    <div class="metric-badge">
                        <span class="metric-val">${m.val}</span>
                        <span class="metric-lbl">${m.lbl}</span>
                    </div>
                `).join("") + `</div>`;
            }

            if (s.layout === "split_right_image" || s.layout === "cover") {
                bodyHtml += `
                    <div class="layout-split-image">
                        <div class="split-text-col">
                            ${metricsHtml}
                            ${s.content_blocks.map(b => `
                                <div class="proto-card">
                                    <h3 class="proto-card-title">${b.title}</h3>
                                    ${b.text ? `<p class="proto-card-desc">${b.text}</p>` : ""}
                                    ${b.bullets ? `
                                        <ul class="proto-bullets">
                                            ${b.bullets.map(item => `<li>${item}</li>`).join("")}
                                        </ul>
                                    ` : ""}
                                </div>
                            `).join("")}
                        </div>
                        ${(() => {
                            if (!s.image) return '<div class="split-image-col"></div>';
                            const isInfo = s.image.startsWith("slide") || s.image.includes("_protocol") || s.image.includes("_card") || s.image.includes("_station") || s.image.includes("_care") || s.image.includes("_admin") || s.image.includes("_kit") || s.image.includes("_allergies") || s.image.includes("_positions") || s.image.includes("_first_aid") || s.image.includes("_dehydration") || s.image.includes("_hd.png");
                            const colStyle = isInfo ? "background: transparent; border: none; box-shadow: none;" : "";
                            const fitStyle = isInfo ? "object-fit: contain; background: transparent; padding: 0;" : "object-fit: cover;";
                            return `
                                <div class="split-image-col" style="${colStyle}">
                                    <img src="extracted_assets/${s.image}" alt="${s.title}" style="${fitStyle}">
                                    ${!isInfo ? `
                                        <div class="photo-overlay-badge">
                                            <img src="${LOGO_LIGHT}" alt="Royal Nanny">
                                        </div>
                                    ` : ""}
                                </div>
                            `;
                        })()}
                    </div>
                `;
            } else if (s.layout === "two_col_cards") {
                bodyHtml += `
                    <div style="display: flex; flex-direction: column; width: 100%; height: 100%;">
                        ${metricsHtml}
                        <div class="layout-two-col">
                            ${s.content_blocks.map(b => `
                                <div class="proto-card">
                                    <h3 class="proto-card-title">${b.title}</h3>
                                    ${b.text ? `<p class="proto-card-desc">${b.text}</p>` : ""}
                                    ${b.bullets ? `
                                        <ul class="proto-bullets">
                                            ${b.bullets.map(item => `<li>${item}</li>`).join("")}
                                        </ul>
                                    ` : ""}
                                </div>
                            `).join("")}
                        </div>
                    </div>
                `;
            } else if (s.layout === "three_cards") {
                bodyHtml += `
                    <div style="display: flex; flex-direction: column; width: 100%; height: 100%;">
                        ${metricsHtml}
                        <div class="layout-three-cards">
                            ${s.content_blocks.map(b => `
                                <div class="proto-card">
                                    <h3 class="proto-card-title">${b.title}</h3>
                                    ${b.text ? `<p class="proto-card-desc">${b.text}</p>` : ""}
                                    ${b.bullets ? `
                                        <ul class="proto-bullets">
                                            ${b.bullets.map(item => `<li>${item}</li>`).join("")}
                                        </ul>
                                    ` : ""}
                                </div>
                            `).join("")}
                        </div>
                    </div>
                `;
            } else if (s.layout === "matrix_4") {
                bodyHtml += `
                    <div class="layout-matrix-4">
                        ${s.content_blocks.map(b => `
                            <div class="proto-card">
                                <h3 class="proto-card-title">${b.title}</h3>
                                <div class="proto-card-inner">
                                    ${b.text ? `<p class="proto-card-desc">${b.text}</p>` : ""}
                                    ${b.bullets ? `
                                        <ul class="proto-bullets">
                                            ${b.bullets.map(item => `<li>${item}</li>`).join("")}
                                        </ul>
                                    ` : ""}
                                </div>
                            </div>
                        `).join("")}
                    </div>
                `;
            }

            bodyHtml += `</div>`;

            let footerHtml = `
                <div class="slide-inner-footer">
                    <div class="footer-values-strip">
                        <span>PROVERENE</span>
                        <span class="val-dot">•</span>
                        <span>ELEGANTNE</span>
                        <span class="val-dot">•</span>
                        <span>POUZDANE</span>
                    </div>
                    <div class="footer-meta-strip">
                        <span>ROYAL NANNY AKADEMIJA • STANDARDI PROFESIONALNE NEGE</span>
                        <span class="footer-slide-num">${String(index + 1).padStart(2, '0')} / ${String(SLIDES.length).padStart(2, '0')}</span>
                    </div>
                </div>
            `;

            slideContent.innerHTML = headerHtml + bodyHtml + footerHtml;

            slideCounter.textContent = `${String(index + 1).padStart(2, '0')} / ${String(SLIDES.length).padStart(2, '0')}`;
            moduleBadge.textContent = s.module;
            progressBar.style.width = `${((index + 1) / SLIDES.length) * 100}%`;
            history.replaceState(null, null, '#' + (index + 1));

            updateNotes(s);
            updateSlideScale();
        }

        function updateNotes(s) {
            const n = s.lecturer_notes || {};
            presenterBody.innerHTML = `
                <div class="note-box">
                    <div class="note-box-title">🎯 Cilj teme & ishodi učenja</div>
                    <div>${n.cilj || "Usvajanje kliničkog protokola i bezbednosnih pravila."}</div>
                </div>
                <div class="note-box">
                    <div class="note-box-title">📌 Ključne teze & metodika predavanja</div>
                    <div>${n.teze || "Detaljno objasniti redosled koraka i obrazložiti fiziološku pozadinu."}</div>
                </div>
                <div class="note-box warning">
                    <div class="note-box-title">⚠️ Najčešće greške i zablude u praksi</div>
                    <div>${n.greske || "Rutinsko postupanje bez provere parametara."}</div>
                </div>
                <div class="note-box question">
                    <div class="note-box-title">❓ Pitanje za polaznice (Interakcija)</div>
                    <div><strong>${n.pitanje || "Kako biste reagovali u ovoj situaciji?"}</strong></div>
                </div>
            `;
        }

        function populateGrid() {
            gridContainer.innerHTML = SLIDES.map((s, i) => `
                <div class="thumb-card ${s.bg_theme === 'dark' ? 'dark' : ''} ${i === currentIndex ? 'active' : ''}" onclick="goToSlide(${i})">
                    <div style="display: flex; justify-content: space-between;">
                        <span class="thumb-cat">${s.module}</span>
                        <span class="thumb-num">${String(i+1).padStart(2, '0')}</span>
                    </div>
                    <div class="thumb-title">${s.title}</div>
                    <div class="thumb-cat">${s.category}</div>
                </div>
            `).join("");
        }

        function goToSlide(i) {
            if (i >= 0 && i < SLIDES.length) {
                currentIndex = i;
                renderSlide(currentIndex);
                if (isGridOpen) toggleGrid();
            }
        }

        function nextSlide() {
            if (currentIndex < SLIDES.length - 1) {
                currentIndex++;
                renderSlide(currentIndex);
            }
        }

        function prevSlide() {
            if (currentIndex > 0) {
                currentIndex--;
                renderSlide(currentIndex);
            }
        }

        function toggleNotes() {
            isNotesOpen = !isNotesOpen;
            presenterPanel.classList.toggle("open", isNotesOpen);
            btnNotes.classList.toggle("active", isNotesOpen);
        }

        function toggleGrid() {
            isGridOpen = !isGridOpen;
            gridModal.classList.toggle("open", isGridOpen);
            if (isGridOpen) populateGrid();
        }

        function toggleFullscreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(() => {});
            } else {
                document.exitFullscreen();
            }
        }

        document.getElementById("btnNext").addEventListener("click", nextSlide);
        document.getElementById("btnPrev").addEventListener("click", prevSlide);
        btnNotes.addEventListener("click", toggleNotes);
        document.getElementById("btnCloseNotes").addEventListener("click", toggleNotes);
        document.getElementById("btnGrid").addEventListener("click", toggleGrid);
        document.getElementById("btnFullscreen").addEventListener("click", toggleFullscreen);
        document.getElementById("btnPrint").addEventListener("click", () => window.print());

        window.addEventListener("keydown", (e) => {
            if (e.key === "ArrowRight" || e.key === " " || e.key === "PageDown") {
                nextSlide();
            } else if (e.key === "ArrowLeft" || e.key === "PageUp") {
                prevSlide();
            } else if (e.key.toLowerCase() === "n") {
                toggleNotes();
            } else if (e.key.toLowerCase() === "g") {
                toggleGrid();
            } else if (e.key.toLowerCase() === "f") {
                toggleFullscreen();
            } else if (e.key === "Escape") {
                if (isGridOpen) toggleGrid();
                if (isNotesOpen) toggleNotes();
            }
        });

        function initFromUrl() {
            const hash = window.location.hash.replace('#', '');
            if (hash) {
                const parsed = parseInt(hash, 10);
                if (!isNaN(parsed) && parsed >= 1 && parsed <= SLIDES.length) {
                    currentIndex = parsed - 1;
                }
            }
            renderSlide(currentIndex);
        }

        function updateSlideScale() {
            const stage = document.getElementById("stageWrapper");
            const scaler = document.getElementById("slideScaler");
            if (!stage || !scaler) return;

            const padX = 24;
            const padY = 16;
            const availW = Math.max(100, stage.clientWidth - padX);
            const availH = Math.max(100, stage.clientHeight - padY);

            const BASE_W = 1600;
            const BASE_H = 900;

            const scale = Math.min(availW / BASE_W, availH / BASE_H);
            scaler.style.setProperty("--slide-scale", scale);
        }

        window.addEventListener("resize", updateSlideScale);
        window.addEventListener("fullscreenchange", updateSlideScale);
        window.addEventListener("DOMContentLoaded", updateSlideScale);
        window.addEventListener("hashchange", initFromUrl);
        initFromUrl();
        updateSlideScale();
    </script>
</body>
</html>
"""
    
    html_content = template.replace("{{SLIDES_DATA_PLACEHOLDER}}", slides_json)
    html_content = html_content.replace("{{LOGO_DARK}}", logo_dark_b64)
    html_content = html_content.replace("{{LOGO_LIGHT}}", logo_light_b64)
    html_content = html_content.replace("{{LOGO_MARK_DARK}}", logo_mark_dark_b64)
    html_content = html_content.replace("{{LOGO_MARK_LIGHT}}", logo_mark_light_b64)
    html_content = html_content.replace("{{LOGO_MARK_CREAM}}", logo_mark_cream_b64)

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ Uspešno sačuvan interaktivni HTML fajl: {OUTPUT_HTML}")
    
    index_html = os.path.join(BASE_DIR, "index.html")
    with open(index_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ Uspešno sačuvan index.html fajl za GitHub Pages: {index_html}")

if __name__ == "__main__":
    build_html()
