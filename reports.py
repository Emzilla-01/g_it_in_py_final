#!/usr/bin/env python3
from reportlab.platypus import Paragraph, Spacer, Table, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
import os
import datetime

def get_paragraph(source_path="supplier-data/descriptions/"):
  nl="\n"
  r_text=""
  for fp in os.listdir(source_path):
    with open(os.path.join(source_path, fp), 'rt') as textfile:
      record_ = [l for l in textfile.readlines()]
      record_s = f"""name: {record_[0].replace(nl, '')}
weight: {record_[1].replace(nl,'')}

"""
    #print(record_s)
      r_text += record_s
  return(r_text)


def generate_report(attachment="/tmp/processed.pdf", title=f'Processed Update on {datetime.datetime.now().strftime("%B %d, %Y")}', paragraph=get_paragraph()):
  #source_path = "supplier-data/descriptions/"
  styles = getSampleStyleSheet()
  datestr=datetime.datetime.now().strftime("%B %d, %Y")

  #report = SimpleDocTemplate("/tmp/processed.pdf")
  report = SimpleDocTemplate(attachment)

  #report_title = Paragraph("Processed Update on "+datestr, styles["h1"])
  report_title = Paragraph(title, styles["h1"])

  report.build([report_title, Paragraph(paragraph)])

if __name__ == "__main__":
  generate_report()
