public class ExportadorXlsxSimple implements XlsxExportable {
    @Override
    public void exportXlsx(String data){
        System.out.println("Xlsx -> " + data);
    }
}
