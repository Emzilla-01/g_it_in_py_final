#!/usr/bin/env python3
import reports
import emails

if __name__ == "__main__":
  r_ = reports.generate_report()
  m_ = emails.generate_email()
  print(f"email m_ : {m_}")
  emails.send_email(m_)
  pass
