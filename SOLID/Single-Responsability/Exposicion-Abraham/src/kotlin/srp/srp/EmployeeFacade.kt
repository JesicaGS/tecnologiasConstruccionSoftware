package kotlin.srp.srp

class EmployeeFacade {
    val payCalculator = PayCalculator()
    val hourReporter = HourReporter()
    val employeeSaver = EmployeeSaver()

    fun calculatePay(employee: Employee) {
        payCalculator.calculatePay(employee)
    }

    fun reportHours(employee: Employee) {
        hourReporter.reportHourse(employee)
    }

    fun employeeSaver(employee: Employee) {
        employeeSaver.saveEmployee(employee)
    }
}