public class ExportadorPdfSimple implements PdfExportable {
    @Override
    public void exportPdf(String data){
        System.out.println("PDF -> " + data);
    }
}
