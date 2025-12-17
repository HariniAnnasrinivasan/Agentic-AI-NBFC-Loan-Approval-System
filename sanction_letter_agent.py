from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os


class SanctionLetterAgent:
    def generate(self, data):
        """
        Generates a professional loan sanction letter PDF
        """

        # Ensure output directory exists
        os.makedirs("sanction_letters", exist_ok=True)

        file_name = f"sanction_letters/Sanction_Letter_{data['phone']}.pdf"
        c = canvas.Canvas(file_name, pagesize=A4)

        width, height = A4
        y = height - 50

        # Header
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, y, "NBFC PRIVATE LIMITED")
        y -= 20

        c.setFont("Helvetica", 10)
        c.drawString(50, y, "Registered NBFC | RBI Compliant")
        y -= 40

        # Date
        c.setFont("Helvetica", 10)
        c.drawString(50, y, f"Date: {datetime.today().strftime('%d %B %Y')}")
        y -= 30

        # Customer Details
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "LOAN SANCTION LETTER")
        y -= 30

        c.setFont("Helvetica", 11)
        c.drawString(50, y, f"Dear Customer,")
        y -= 20

        c.drawString(
            50, y,
            "We are pleased to inform you that your personal loan application has been approved."
        )
        y -= 30

        # Loan Details Box
        c.setFont("Helvetica-Bold", 11)
        c.drawString(50, y, "Loan Details:")
        y -= 20

        c.setFont("Helvetica", 11)
        c.drawString(70, y, f"Loan Amount Approved : ₹{data['approved_amount']:,}")
        y -= 18

        c.drawString(70, y, f"Loan Purpose         : {data['purpose']}")
        y -= 18

        c.drawString(70, y, f"Loan Tenure          : {data['approved_tenure']} years")
        y -= 18

        c.drawString(70, y, f"Interest Rate        : 14% per annum")
        y -= 18

        c.drawString(70, y, f"Approx. EMI          : ₹{int(data['approved_amount'] / (data['approved_tenure']*12)):,}")
        y -= 30

        # Terms & Conditions
        c.setFont("Helvetica-Bold", 11)
        c.drawString(50, y, "Important Terms & Conditions:")
        y -= 20

        c.setFont("Helvetica", 10)
        terms = [
            "• The loan is subject to final documentation and verification.",
            "• EMI payments must be made on or before the due date every month.",
            "• Any delay in payment may attract penalties as per NBFC policy.",
            "• Prepayment and foreclosure are allowed as per applicable charges.",
            "• This sanction letter is valid for 30 days from the date of issue."
        ]

        for term in terms:
            c.drawString(60, y, term)
            y -= 15

        y -= 20

        # Closing
        c.setFont("Helvetica", 11)
        c.drawString(
            50, y,
            "If you have any questions or need further assistance, please feel free to contact us."
        )
        y -= 30

        c.drawString(50, y, "We look forward to serving you.")
        y -= 50

        # Signature
        c.setFont("Helvetica-Bold", 11)
        c.drawString(50, y, "For NBFC Private Limited")
        y -= 40

        c.setFont("Helvetica", 11)
        c.drawString(50, y, "Authorized Signatory")

        # Footer
        c.setFont("Helvetica", 8)
        c.drawString(
            50, 40,
            "This is a system-generated sanction letter and does not require a physical signature."
        )

        c.save()

        return file_name
