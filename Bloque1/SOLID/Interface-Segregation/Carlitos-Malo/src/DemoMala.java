public class DemoMala {
    public static void main(String[] args) {
        Exportador exportador = new ExportadorCsv();
        exportador.exportCsv("Ventas = 1000");

        try{
            exportador.exportPdf("Ventas = 1000");
        } catch(UnsupportedOperationException e){
            System.out.println(e.getMessage());
        }

        try {
            exportador.exportPdf("Ventas = 1000");
        } catch(UnsupportedOperationException e){
            System.out.println(e.getMessage());
        }
    }
}
