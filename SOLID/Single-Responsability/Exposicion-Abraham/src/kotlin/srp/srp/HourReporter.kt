package kotlin.srp.srp

class HourReporter {
    fun reportHourse(employee: Employee) : String {
        val ordinaryHours = regularHours(employee)
        val nonOrdinaryHours = employee.hoursWorked - ordinaryHours
        return "Employee ${employee.name} has worked ${ordinaryHours} ordinary hours and ${nonOrdinaryHours} extra hours"
    }

    private fun regularHours(employee: Employee) : Int {
        return if (employee.hoursWorked > 40) 40 else hoursWorked
    }
}