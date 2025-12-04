public class ExportadorCsvSimple implements CsvExportable {
    @Override
    public void exportCsv(String data){
        System.out.println("CSV -> " + data);
    }
}
