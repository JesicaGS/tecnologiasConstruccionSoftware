import kotlin.nonsrp.Employee
import kotlin.srp.srp.*

fun main() {
    val employee1 = Employee(
        ID = 1,
        name = "Pedro Alonso",
        hoursWorked = 40,
        salary = 40.5
    )

    val employee2 = Employee(
        ID = 2,
        name = "Brr patapim",
        hoursWorked = 40,
        salary = 40.5
    )


    val employeeFacade = EmployeeFacade()


}