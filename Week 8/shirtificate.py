from fpdf import FPDF
class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("Helvetica", size=50)
        self.text(0,0,text="CS50 Shirtificate")
        self._pdf.ln(h=20)
        self._pdf.image("shirtificate.png",x =0, y = 70)
        self.text(-250,255,text=f'{name} took CS50')

    def text(self,heights,colour,text):
        self._pdf.set_text_color(r=int(colour))
        self._pdf.cell(w=0,h=heights,txt=text,align='C')

    def produce(self,shirtificate):
        self._pdf.output(shirtificate)

intial_prod = input("Name: ")
final_prod = PDF(intial_prod)
final_prod.produce("shirtificate.pdf")
