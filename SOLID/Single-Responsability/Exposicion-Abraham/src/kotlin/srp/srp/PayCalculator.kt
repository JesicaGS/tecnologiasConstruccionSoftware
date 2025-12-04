package kotlin.srp.srp

class PayCalculator {
    fun calculatePay(employee: Employee) {
        val ordinaryHours = regularHours(employee)
        val nonOrdinaryHours = employee.hoursWorked - ordinaryHours
    }
}