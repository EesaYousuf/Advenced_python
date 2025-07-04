#pip install reportlab

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_invoice(customer_name, items, filename="invoice.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
