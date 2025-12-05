public class ExportadorCsv implements Exportador {
    @Override
    public void exportCsv(String data){
        System.out.println("CSV -> " + data);
    }

    @Override
    public void exportPdf(String data){
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    public void exportXlsx(String data){
        throw new UnsupportedOperationException("Not supported yet.");
    }
}
