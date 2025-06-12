import json
import csv
from datetime import datetime

# Exportar resultados de varredura de portas para JSON ou CSV
def export_results(results, target, output_format="json", filename=None):
    """Exportar os dados para os formatos JSON ou CSV."""
    if not results:
        print("[x] No results to export.")
        return

    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"scan_{target.replace('.', '_')}_{timestamp}.{output_format}"

    try:
        if output_format == "json":
            data = [{"port": port, "banner": banner} for port, banner in results]
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        elif output_format == "csv":
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Port", "Banner"])
                for port, banner in results:
                    writer.writerow([port, banner])
        else:
            print(f"[x] Unsupported format: {output_format}. Use 'json' or 'csv'.")
            return
        print(f"[+] Results exported to {filename} in {output_format.upper()} format.")

    except Exception as e:
        print(f"[x] Error exporting results: {e}")
        return
