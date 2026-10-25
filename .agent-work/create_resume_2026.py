from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import BaseDocTemplate, Frame, Image, KeepTogether, PageTemplate, Paragraph, Spacer, Table, TableStyle

OUTPUT = "assets/Romy-Mondello-Resume-2026-10.pdf"

INK = colors.HexColor("#10110f")
MUTED = colors.HexColor("#4c514d")
LIME = colors.HexColor("#6b7e13")
LINE = colors.HexColor("#cfd4c7")


def make_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="Name", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=22,
        leading=24, textColor=INK, spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name="Kicker", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=8.2,
        leading=10, textColor=LIME, tracking=0.8, spaceAfter=5,
    ))
    styles.add(ParagraphStyle(
        name="Contact", parent=styles["Normal"], fontName="Helvetica", fontSize=7.4,
        leading=9.5, textColor=MUTED, spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="Summary", parent=styles["Normal"], fontName="Helvetica", fontSize=8.6,
        leading=11.4, textColor=INK, spaceAfter=9,
    ))
    styles.add(ParagraphStyle(
        name="Section", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.2,
        leading=11, textColor=INK, borderBottomWidth=0.6, borderBottomColor=LINE,
        spaceBefore=5, spaceAfter=5, keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name="Role", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=8.2,
        leading=9.7, textColor=INK, spaceAfter=1, keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name="RoleDate", parent=styles["Normal"], fontName="Helvetica", fontSize=7.3,
        leading=9, textColor=MUTED, alignment=2, keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name="Body", parent=styles["Normal"], fontName="Helvetica", fontSize=7.55,
        leading=9.7, textColor=INK, spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        name="ResumeBullet", parent=styles["Normal"], fontName="Helvetica", fontSize=7.35,
        leading=9.25, leftIndent=8, firstLineIndent=-6, textColor=INK, spaceAfter=1.3,
    ))
    styles.add(ParagraphStyle(
        name="Small", parent=styles["Normal"], fontName="Helvetica", fontSize=7.15,
        leading=9.1, textColor=INK, spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name="SmallMuted", parent=styles["Normal"], fontName="Helvetica", fontSize=6.9,
        leading=8.7, textColor=MUTED, spaceAfter=2,
    ))
    return styles


def p(text, style):
    return Paragraph(text, style)


def role(styles, title, date, bullets):
    header = Table([[p(title, styles["Role"]), p(date, styles["RoleDate"])]], colWidths=[4.55 * inch, 1.45 * inch])
    header.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    body = [header]
    body.extend(p(f"- {bullet}", styles["ResumeBullet"]) for bullet in bullets)
    return KeepTogether(body)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(0.62 * inch, 0.42 * inch, 7.88 * inch, 0.42 * inch)
    canvas.setFont("Helvetica", 6.8)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.62 * inch, 0.25 * inch, "Romy Mondello | AI and full-stack engineer | Public resume | October 2026")
    canvas.drawRightString(7.88 * inch, 0.25 * inch, "1")
    canvas.restoreState()


def build():
    styles = make_styles()
    doc = BaseDocTemplate(
        OUTPUT, pagesize=letter, leftMargin=0.62 * inch, rightMargin=0.62 * inch,
        topMargin=0.52 * inch, bottomMargin=0.55 * inch, title="Romy Mondello - Resume 2026",
        author="Romy Mondello",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="one-page")
    doc.addPageTemplates([PageTemplate(id="resume", frames=[frame], onPage=footer)])

    story = []
    mark = Image("assets/portrait.png", width=0.38 * inch, height=0.38 * inch)
    header = Table([[mark, [p("Romy Mondello", styles["Name"]), p("AI AND FULL-STACK ENGINEER - AGENT INFRASTRUCTURE - DEVELOPER TOOLS", styles["Kicker"])]],], colWidths=[0.52 * inch, 6.0 * inch])
    header.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(header)
    story.append(p(
        "Somerville, MA | Remote US | Boston/Cambridge hybrid<br/>"
        "<a href='mailto:rmondello2629@gmail.com'>rmondello2629@gmail.com</a> | "
        "<a href='https://mondello.dev'>mondello.dev</a> | "
        "<a href='https://github.com/integrate-your-mind'>github.com/integrate-your-mind</a> | "
        "<a href='https://www.linkedin.com/in/romy-m-08621b168/'>LinkedIn</a>",
        styles["Contact"],
    ))
    story.append(p(
        "AI, full-stack, and systems engineer with six years of professional software-engineering experience since joining Knox Financial in 2020. "
        "I build agent systems and the infrastructure they run on, with public work spanning JEV workflows for Codex and Claude Code, QQ runtime contributions, Rust systems, and formal verification. "
        "Earlier independent AI work began with deep learning in 2017 and language models around 2019, including GPT-3 beta participation.",
        styles["Summary"],
    ))

    story.append(p("Independent product engineering and open source", styles["Section"]))
    story.append(role(styles, "Independent Product Engineering / Open Source", "May 2025 - present", [
        "Built <b>JEV Workflows</b>, a public open-source plugin for Codex and Claude Code that provides typed decision consultation, failure diagnosis, and evidence-based completion review. Model recommendations remain advisory and separate from permission to act.",
        "Contributed to the open-source Rust QQ coding-agent harness in merged PRs <a href='https://github.com/retsu-AI/qq/pull/333'>#333</a>, <a href='https://github.com/retsu-AI/qq/pull/319'>#319</a>, and <a href='https://github.com/retsu-AI/qq/pull/72'>#72</a>, covering session-history recovery after held-tool cancellation or restart, shared JEV protocol validation, review checkpoints, and provider-neutral reasoning-effort settings.",
        "Co-developing a bounded local agent-execution prototype with a cofounder. It explores Temporal coordination, PostgreSQL run state, isolated workers, explicit cancellation controls, persisted evidence, and guarded verification.",
        "Built Ferrite, a public Rust-first TypeScript application-framework prototype with server-side rendering, file-system routing, artifact serving, WASM and Node bindings, and browser hydration."
    ]))
    story.append(role(styles, "Formal research", "Independent", [
        "Authored a 10-page <a href='https://arxiv.org/abs/2608.02634'>arXiv preprint</a> giving a dimension-two counterexample to the separable Jacobian conjecture in characteristic two, with Jacobian determinant 1 and separable degree 3. Formalized the full theorem in Lean 4 and Mathlib with digest-locked sources and replay receipts.",
    ]))

    story.append(p("Professional experience", styles["Section"]))
    story.append(role(styles, "Further - Consultant, Research Engineer (contract)", "Feb 10 - Apr 14, 2025", [
        "Co-designed the LangGraph agent and data-pipeline architecture with the CTO, then built Zillow and mortgage API pipelines with typed state, tool orchestration, retrieval, and rule-based risk checks.",
        "Helped the team use Cursor and coding agents, and fixed LaTeX rendering and API timeouts in the AI Genius web app.",
    ]))
    story.append(role(styles, "Pillzumi - Machine Learning Engineer (contract)", "Dec 2024 - Feb 2025", [
        "Built long-running elizaOS social-agent integrations across WebRTC and X direct-message workflows, with persistent memory, action frameworks, and API-rate-limit handling.",
    ]))
    story.append(role(styles, "Verizon Business - Customer Solutions", "Apr - Dec 2024", [
        "Owned a CRM book of business in a technical-consultative B2B motion covering discovery, solution design, customer engineering conversations, and closing.",
    ]))
    story.append(role(styles, "Verus AI - Data Scientist", "2022 - 2023", [
        "Built Google Cloud pipelines into BigQuery and Vertex AI, trained recurrent models for spend, usage, and customer-growth forecasting, and monitored model and data quality.",
    ]))
    story.append(role(styles, "Knox Financial - Backend Software Engineer", "Jul 2020 - Mar 2021", [
        "Built real-estate search on data feeds and AWS and Google APIs, distributed ingestion, PostgreSQL forecasting services, REST APIs, funnel instrumentation, and forecast visuals.",
        "Hardened CI/CD, reduced flaky-test noise, introduced deploy gates, and reviewed backend code.",
    ]))

    bottom = Table([
        [p("<b>Education</b><br/>Associate of Science, Computer Science<br/>Bunker Hill Community College - Dean's List", styles["Small"]),
         p("<b>Technical</b><br/>TypeScript, JavaScript, Python, Rust, Lean 4, Swift, Go | React, Next.js, Node.js, FastAPI, Axum | PostgreSQL, Temporal, Redis, Docker, AWS, GCP, BigQuery | LangGraph, OpenClaw, elizaOS, RAG, MLX, PyTorch/MPS", styles["Small"])],
    ], colWidths=[2.15 * inch, 4.0 * inch])
    bottom.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEABOVE", (0, 0), (-1, 0), 0.6, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(bottom)
    doc.build(story)


if __name__ == "__main__":
    build()
