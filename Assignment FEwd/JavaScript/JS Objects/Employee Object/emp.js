function submitdet(){

    let empId = document.getElementById("empId").value;
    let empName = document.getElementById("empName").value;
    let empSal = document.getElementById("empSal").value;
    empSal = parseInt(empSal);
    let empExp = document.getElementById("empExp").value;

   class Employee {

        constructor(empId, empName, empSal, empExp){
            this.empId = empId;
            this.empName = empName;
            this.empSal = empSal;
            this.empExp = empSal
        }
       totalSalary(empSal){
            return this.empSal * 12;
       }

       totalBonus(empSal){
           return (this.empSal * 8.33) / 100;
       }
   } 
 //--------creation objects n functions-----
   let empDetail = new Employee(empId, empName, empSal, empExp)

   let Annualsalary = empDetail.totalSalary();
   
   let totalBonus = empDetail.totalBonus()
   console.log(totalBonus);

   //---------displaying result---------
   document.getElementById("ResId").innerHTML = "Employee ID :- "+ empId;
   document.getElementById("ResName").innerHTML = "Employee Name :- "+ empName;
   document.getElementById("ResSal").innerHTML = "Employee Salary :- " +" Rs. "+ empSal;
   document.getElementById("ResWorkExp").innerHTML = "Employee Work Experience :- "+ empExp + " Year";
   document.getElementById("TotalResultSal").innerHTML = "Employee Annual Salary :- "+ "Rs. "+ Annualsalary ;
   document.getElementById("TotalBonus").innerHTML = "Employee Bonus :- "+ "Rs. "+ totalBonus ;
}