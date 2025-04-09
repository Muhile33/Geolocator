from fpdf import FPDF

def generate_report(data, output_format='pdf'):
    if output_format == 'pdf':
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"GeoStalker Recon Report", ln=True)
        pdf.ln(10)
        pdf.multi_cell(0, 10, txt=data)
        pdf.output("report.pdf")
        print("[+] Report generated: report.pdf")
    elif output_format == 'html':
        html = f"<html><body><h1>GeoStalker Recon Report</h1><p>{data}</p></body></html>"
        with open("report.html", "w") as f:
            f.write(html)
        print("[+] Report generated: report.html")
