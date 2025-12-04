public class ReportService {
    private final CsvExportable csv;
    private final PdfExportable pdf;

    public ReportService(CsvExportable csv, PdfExportable pdf) {
        this.csv = csv;
        this.pdf = pdf;
    }

    public void exportarVentas(String data){
        csv.exportCsv(data);
        pdf.exportPdf(data);
    }
}
