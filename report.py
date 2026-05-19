from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(filename, content):
    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("AI HR REPORT", styles["Title"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph(content.replace("\n", "<br/>"), styles["Normal"]))

    doc.build(story)