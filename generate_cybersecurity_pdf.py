import os
import hashlib
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

TEAL = colors.HexColor("#00695C")
TEAL_DARK = colors.HexColor("#004D40")
TEAL_LIGHT = colors.HexColor("#E0F2F1")
ORANGE = colors.HexColor("#E65100")
BODY_TEXT = colors.HexColor("#212121")
SUBTLE = colors.HexColor("#757575")
LIGHT_BG = colors.HexColor("#FAFAFA")
WHITE = colors.white
BORDER = colors.HexColor("#BDBDBD")
ROW_ALT = colors.HexColor("#F5F5F5")

STUDENT_NAME = "Garvit Sharma"
ROLL_NUMBER = "2301730190"
STUDENT_EMAIL = "garvitsharma8909@gmail.com"

PAGE_W, PAGE_H = A4
MARGIN = 48
CONTENT_W = PAGE_W - 2 * MARGIN


def generate_cyber_uid():
    seed = f"CYBERSECURITY-AI-CAPSTONE-{ROLL_NUMBER}-ENTERPRISE-2026"
    digest = hashlib.sha256(seed.encode()).hexdigest().upper()
    return f"CYBER-AI-{digest[:4]}-{digest[4:8]}-{digest[8:12]}"


def S():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "T", parent=base["Heading1"], fontName="Helvetica-Bold",
            fontSize=15, leading=19, textColor=TEAL_DARK, spaceAfter=1),
        "subtitle": ParagraphStyle(
            "Sub", parent=base["Normal"], fontName="Helvetica-Oblique",
            fontSize=8, leading=11, textColor=SUBTLE, spaceAfter=6),
        "ml": ParagraphStyle(
            "ML", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=6.5, leading=8.5, textColor=SUBTLE),
        "mv": ParagraphStyle(
            "MV", parent=base["Normal"], fontName="Helvetica",
            fontSize=7, leading=9.5, textColor=BODY_TEXT),
        "h1": ParagraphStyle(
            "H1", parent=base["Heading2"], fontName="Helvetica-Bold",
            fontSize=9.5, leading=12, textColor=WHITE, spaceBefore=0, spaceAfter=0),
        "body": ParagraphStyle(
            "B", parent=base["Normal"], fontName="Helvetica",
            fontSize=7, leading=10, textColor=BODY_TEXT, spaceAfter=2),
        "code": ParagraphStyle(
            "C", parent=base["Normal"], fontName="Courier",
            fontSize=6, leading=8.5, textColor=BODY_TEXT),
        "th": ParagraphStyle(
            "TH", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=6, leading=8, textColor=WHITE),
        "td": ParagraphStyle(
            "TD", parent=base["Normal"], fontName="Helvetica",
            fontSize=6, leading=8, textColor=BODY_TEXT),
        "tdb": ParagraphStyle(
            "TDB", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=6, leading=8, textColor=TEAL_DARK),
    }


def draw_hf(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 6)
    canvas.setFillColor(SUBTLE)
    canvas.drawString(MARGIN, PAGE_H - 24, "AI in Cybersecurity Capstone  |  Threat Detection & Prevention System")
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 24, f"{STUDENT_NAME}  |  {ROLL_NUMBER}")
    canvas.setStrokeColor(TEAL)
    canvas.setLineWidth(0.75)
    canvas.line(MARGIN, PAGE_H - 28, PAGE_W - MARGIN, PAGE_H - 28)

    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, 30, PAGE_W - MARGIN, 30)
    canvas.setFont("Helvetica", 5.5)
    canvas.drawString(MARGIN, 20, "Confidential  ·  Enterprise Cybersecurity Architecture Report")
    canvas.drawRightString(PAGE_W - MARGIN, 20, f"Page {canvas.getPageNumber()}")
    canvas.restoreState()


def heading_banner(text, s):
    t = Table([[Paragraph(text, s["h1"])]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TEAL),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("ROUNDEDCORNERS", [3, 3, 0, 0]),
    ]))
    return t


def make_table(headers, rows, col_widths, s, header_color=TEAL_DARK):
    h = [[Paragraph(c, s["th"]) for c in headers]]
    d = []
    for row in rows:
        cells = []
        for i, c in enumerate(row):
            cells.append(Paragraph(c, s["tdb"] if i == 0 else s["td"]))
        d.append(cells)
    t = Table(h + d, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), header_color),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTSIZE", (0, 0), (-1, -1), 6),
        ("GRID", (0, 0), (-1, -1), 0.4, BORDER),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, ROW_ALT]),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return t


def build_cybersecurity_pdf():
    pdf_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "docs", "deliverables", "AI_Cybersecurity_Threat_Detection_Report.pdf")
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    doc = SimpleDocTemplate(
        pdf_path, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=34, bottomMargin=38)

    s = S()
    story = []
    uid = generate_cyber_uid()

    # Title
    story.append(Spacer(1, 6))
    story.append(Paragraph("AI-Based Threat Detection &amp; Prevention System", s["title"]))
    story.append(Paragraph("Enterprise Infrastructure  ·  Hybrid ML/DL  ·  Explainable AI  ·  SOAR", s["subtitle"]))

    # Metadata
    cw = CONTENT_W / 6
    meta = [
        [Paragraph("<b>Candidate</b>", s["ml"]), Paragraph(STUDENT_NAME, s["mv"]),
         Paragraph("<b>Roll No.</b>", s["ml"]), Paragraph(ROLL_NUMBER, s["mv"]),
         Paragraph("<b>Verification</b>", s["ml"]), Paragraph(uid, s["mv"])],
        [Paragraph("<b>Email</b>", s["ml"]), Paragraph(STUDENT_EMAIL, s["mv"]),
         Paragraph("<b>Domain</b>", s["ml"]), Paragraph("AI in Cybersecurity", s["mv"]),
         Paragraph("<b>Scope</b>", s["ml"]), Paragraph("Mid-Sized Enterprise", s["mv"])],
    ]
    mt = Table(meta, colWidths=[cw * 0.7, cw * 1.3, cw * 0.7, cw * 1.3, cw * 0.7, cw * 1.3])
    mt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TEAL_LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.5, TEAL),
        ("LINEBELOW", (0, 0), (-1, 0), 0.3, TEAL),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(mt)
    story.append(Spacer(1, 12))

    # 1. Executive Summary
    story.append(heading_banner("1. Executive Summary: Scope, Objectives & Key Design Decisions", s))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<b>Operational Scope:</b> Mid-sized enterprises face polymorphic ransomware, credential stuffing, and "
        "advanced persistent threats (APTs) with constrained SOC headcount. Signature-based IDS fail against zero-day exploits.", s["body"]))
    story.append(Paragraph(
        "<b>Strategic Objectives:</b> Autonomous, real-time AI/ML threat detection achieving sub-second anomaly detection, "
        "&lt;0.5% false positives, and human-interpretable XAI narratives for business leaders.", s["body"]))
    story.append(Paragraph(
        "<b>Key Design Decisions:</b><br/>"
        "&#8226; <i>Hybrid AI Engine:</i> XGBoost/LightGBM for known patterns + Deep Autoencoders and Isolation Forests for zero-day discovery.<br/>"
        "&#8226; <i>SOAR Containment:</i> API integration into firewalls and identity providers to isolate endpoints in milliseconds.", s["body"]))
    story.append(Spacer(1, 10))

    # 2. Threat Model
    story.append(heading_banner("2. Threat Model: Top-5 Enterprise Threats", s))
    story.append(Spacer(1, 4))
    story.append(make_table(
        ["Threat Vector", "Target Surface", "Attack Mechanism", "Risk Profile"],
        [
            ["Ransomware & Exfiltration", "Storage, DBs, Endpoints", "Silent encryption & bulk egress via DNS/HTTPS", "Catastrophic financial and regulatory breach"],
            ["Credential Stuffing", "SSO, Active Directory, VPN", "Distributed automated authentication attacks", "Primary entry for 82% of enterprise compromises"],
            ["Insider Threats", "Laptops, S3 Buckets", "Off-hours high-volume file transfers", "Bypasses firewalls via legitimate credentials"],
            ["C2 Beacons", "Workstation Sockets", "Low-and-slow periodic heartbeat callbacks", "Active APT preparing lateral movement"],
            ["Phishing / Spear-Phishing", "Email Gateway", "LLM social engineering & spoofed links", "Zero-day attachments bypassing signatures"],
        ],
        [CONTENT_W * 0.20, CONTENT_W * 0.20, CONTENT_W * 0.30, CONTENT_W * 0.30], s))
    story.append(Spacer(1, 12))

    # 3. Architecture
    story.append(heading_banner("3. System Architecture: End-to-End Pipeline", s))
    story.append(Spacer(1, 4))
    story.append(make_table(
        ["Stage", "Component", "Description"],
        [
            ["1. Data Ingestion", "Apache Kafka", "NetFlow/IPFIX, Zeek metadata, Sysmon, CloudTrail at 50K events/sec"],
            ["2. Feature Engineering", "Apache Flink", "Sliding-window aggregation: inter-arrival time, byte ratios, DNS entropy"],
            ["3. ML/DL Detection", "XGBoost + VAE", "Supervised ensemble for known attacks; VAE reconstruction loss for zero-days"],
            ["4. XAI Alerting", "SHAP Engine", "Tensor weights converted to plain-English executive decision narratives"],
            ["5. SOAR Response", "Webhooks", "BGP blackholing, CrowdStrike quarantine, AD token revocation"],
        ],
        [CONTENT_W * 0.20, CONTENT_W * 0.17, CONTENT_W * 0.63], s, header_color=TEAL))
    story.append(Spacer(1, 12))

    # 4. Feature Engineering
    story.append(heading_banner("4. Feature Engineering & Justification", s))
    story.append(Spacer(1, 4))
    story.append(make_table(
        ["Feature", "Formulation", "Justification"],
        [
            ["Byte Transfer Velocity", "Bytes / Flow Duration", "Distinguishes browsing from rapid bulk exfiltration"],
            ["DNS Query Entropy", "-sum(p * log2(p))", "Detects DNS tunneling / C2 beaconing via random subdomains"],
            ["Auth Failure Concentration", "Failed Attempts in 60s Window", "Identifies brute-force and password spraying attacks"],
            ["Off-Hours Deviation", "|Access_Time - User_Mean|", "Flags stolen credentials used outside business hours"],
            ["Connection Fanout", "Unique Dest IPs / 5 min", "Exposes worm propagation and port-scanning movement"],
        ],
        [CONTENT_W * 0.22, CONTENT_W * 0.28, CONTENT_W * 0.50], s, header_color=ORANGE))
    story.append(Spacer(1, 12))

    # 5. Adversarial ML
    story.append(heading_banner("5. Adversarial ML Attacks & Defense Strategy", s))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<b>Adversarial Threat:</b> Evasion attacks (FGSM, Zeroth-Order Optimization) inject chaff packets, "
        "fragment payloads, or interleave benign bursts to dilute byte velocity and bypass ML thresholds.", s["body"]))
    story.append(Paragraph(
        "<b>Defense:</b><br/>"
        "&#8226; <i>Adversarial Hardening:</i> Retraining with PGD-perturbed network flows.<br/>"
        "&#8226; <i>Feature Squeezing:</i> Spatial smoothing and bit-depth reduction strip noise before inference.", s["body"]))
    story.append(Spacer(1, 10))

    # 6. XAI Demo
    story.append(heading_banner("6. Explainable AI (XAI) Demonstration", s))
    story.append(Spacer(1, 4))
    xai = (
        "=== AI SECURITY INCIDENT EXPLANATION (EXECUTIVE SUMMARY) ===<br/>"
        "ALERT LEVEL: HIGH RISK CRITICAL INCIDENT  |  Confidence: 99.8%<br/><br/>"
        "WHAT HAPPENED: Workstation 10.0.14.88 transferred 850 MB to external server 198.51.100.24.<br/><br/>"
        "WHY THE AI TRIGGERED THIS ALERT:<br/>"
        "  * Unusually Fast Data Transfer Speed: 90.0% of risk (Exfiltration Spike)<br/>"
        "  * Repeated Failed Logins: 5.3% of risk (7 brute-force attempts)<br/>"
        "  * Connection to Untrusted Domain: 3.5% of risk<br/><br/>"
        "ACTION: Endpoint quarantined; credentials suspended.")
    xt = Table([[Paragraph(xai, s["code"])]], colWidths=[CONTENT_W])
    xt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FFF3E0")),
        ("BOX", (0, 0), (-1, -1), 0.75, ORANGE),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(xt)
    story.append(Spacer(1, 12))

    # 7. Ethics
    story.append(heading_banner("7. Ethical & Privacy Governance", s))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<b>Privacy Concerns:</b> Deep packet inspection and telemetry tracking (keystroke rhythms, browser data, "
        "off-hours monitoring) risk violating GDPR Art. 88 and workplace privacy regulations.", s["body"]))
    story.append(Paragraph(
        "<b>Mitigation:</b> Differential Privacy and Zero-Knowledge Data Masking at ingestion. PII and credentials "
        "are pseudonymized (SHA-256 with rotating salt) before feature extraction. The ML model classifies strictly "
        "behavioral telemetry without processing personal identities.", s["body"]))

    doc.build(story, onFirstPage=draw_hf, onLaterPages=draw_hf)
    print(f"[SUCCESS] AI Cybersecurity PDF generated: {pdf_path}")


if __name__ == "__main__":
    build_cybersecurity_pdf()
