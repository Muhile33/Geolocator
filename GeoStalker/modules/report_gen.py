from jinja2 import Environment, FileSystemLoader
import os
from color_utils.printx import print_success, print_error, print_info

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '../templates')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../reports')

def generate_report(data, filename="report.html"):
    try:
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        template = env.get_template("report_template.html")
        output = template.render(data=data)

        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        output_path = os.path.join(OUTPUT_DIR, filename)
        with open(output_path, "w") as f:
            f.write(output)

        print_success(f"Report generated: {output_path}")
        return output_path
    except Exception as e:
        print_error(f"Report generation failed: {e}")
        return None


if __name__ == "__main__":
    sample_data = {
        "title": "GeoStalker Recon Report",
        "entries": [
            {"name": "Instagram", "result": "User xyz found"},
            {"name": "IP Trace", "result": "Location: New York, USA"},
            {"name": "Email Breach", "result": "No breaches found"},
        ]
    }
    generate_report(sample_data)

