#!/usr/bin/env python3
import psutil
#from pprint import pprint
import socket
import emails
from cfg import user

def check_cpu():
  c = psutil.cpu_percent(interval=0.2)
  if c > 80:
    #raise Exception("CPU usage over 80%!")
    m_ = emails.generate_email(from_="automation@example.com",
                    to = user+"@example.com",
                    subject="Error - CPU usage is over 80%",
                    body="Please check your system and resolve the issue as soon as possible.",
                    attachment=None)
    emails.send_email(m_)
  return(f"CPU usage: {c}%")

def check_disk():
  d = psutil.disk_usage("/")
  if d.percent < 20:
    #raise Exception("Available disk below 20%!")
    m_ = emails.generate_email(from_="automation@example.com",
                    to = user+"@example.com",
                    subject="Error - Available disk space is less than 20%",
                    body="Please check your system and resolve the issue as soon as possible.",
                    attachment=None)
    emails.send_email(m_)

  return(f"Disk usage: {d}%")

def check_mem():
  m = psutil.virtual_memory()
  av = m.available/1e+6
  if av < 500:
    #raise Exception("Available memory below 500MB!")
    m_ = emails.generate_email(from_="automation@example.com",
                    to = user+"@example.com",
                    subject="Error - Available memory is less than 500MB",
                    body="Please check your system and resolve the issue as soon as possible.",
                    attachment=None)
    emails.send_email(m_)

  return(f"Available memory: {av}MB")

def check_localhost():
  ip = socket.gethostbyname("localhost")
  if ip == None:
    #raise Exception("Cannot resolve localhost!")
    m_ = emails.generate_email(from_="automation@example.com",
                    to = user+"@example.com",
                    subject="Error - localhost cannot be resolved to 127.0.0.1",
                    body="Please check your system and resolve the issue as soon as possible.",
                    attachment=None)
    emails.send_email(m_)
  return(f"localhost resolves to {ip}")

def main():
  output=[]
  for f in [check_cpu, check_mem, check_disk, check_localhost]:
    output.append(str(f()))
  print(output)

if __name__ == "__main__":
  main()
