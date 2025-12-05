public class DemoBuena {
    public static void main(String[] args) {
        ExportadorCsvSimple exportador = new ExportadorCsvSimple();
        ReportService service = new ReportService(exportador);
        service.exportarVentas("Ventas de el mes: 1000");

        ExportadorPdfSimple exportador1 = new ExportadorPdfSimple();
        ReportService service1 = new ReportService(exportador1)
    }
}
