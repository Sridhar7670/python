const employeeID = document.querySelector("#employeeID");
const fname = document.querySelector("#fname");
const salary = document.querySelector("#salary");
const team = document.querySelector("#team");
const companyName = document.querySelector("#companyName");
const role = document.querySelector("#role");
const addButton = document.querySelector("#addEmployee");
const resetButton = document.querySelector("#reset");
const recordsColumn = document.querySelector("#records-column");
const updatebutton=document.querySelector('#updateEmployee');
const vip_column=document.querySelector(".vip_column")
let Index = null;

// Event Listeners
addButton.addEventListener("click", addEmployee);
resetButton.addEventListener("click", clearInputs);
updatebutton.addEventListener('click',update)

// Retrieve employees from localStorage
const getEmployees = () => JSON.parse(localStorage.getItem("employees")) || [];
const IMPEmployees=()=>JSON.parse(localStorage.getItem('IMPemp'))||[]


// Save employees,special employees to localStorage
const saveEmployees = (employees) => localStorage.setItem("employees", JSON.stringify(employees));
const importantEmplyees=(imp_employee)=>localStorage.setItem('IMPemp',JSON.stringify(imp_employee))

// Clear all input fields

function clearInputs() {
    employeeID.value = "";
    fname.value = "";
    salary.value = "";
    team.value = "";
    companyName.value = "";
    role.value = "SDE";
}

function addEmployee() {
    const employees = getEmployees();
    const imp=IMPEmployees();

    // Creating new employee object
    const newEmployee = {
        employeeID: employeeID.value,
        fname: fname.value,
        salary: salary.value,
        team: team.value,
        companyName: companyName.value,
        role: role.value
    };

    employees.push(newEmployee);
    saveEmployees(employees);
    clearInputs();
    displayEmployees();
}
function displayEmployees() {
    const employees = getEmployees();

    recordsColumn.innerHTML = '';  

    if (employees.length) {
        for (let index = 0; index < employees.length; index++) {
            const emp = employees[index];
            
            

            recordsColumn.innerHTML += `
                <tr>
                    <td>${emp.employeeID}</td>
                    <td>${emp.fname}</td>
                    <td>${emp.salary}</td>
                    <td>${emp.team}</td>
                    <td>${emp.companyName}</td>
                    <td>${emp.role}</td>
                    <td>
                        <i class="fa-solid fa-pencil" onclick="editEmployee(${index})"></i>
                        <i class="fa-solid fa-trash" onclick="deleteEmployee(${index})"></i>
                        <button class="vip" onclick="addVIP(${index})">Treat VIP</button>
                    </td>
                </tr>
            `;
        }
    } else {
        recordsColumn.innerHTML = `<tr><td colspan="7">No records found</td></tr>`;
    }
}

function editEmployee(index) {
    const employees = getEmployees();
    const emp = employees[index];

    employeeID.value = emp.employeeID;
    fname.value = emp.fname;
    salary.value = emp.salary;
    team.value = emp.team;
    companyName.value = emp.companyName;
    role.value = emp.role;

    updatebutton.style='display:block'
    addButton.style='display:none'
    // Set currentEditIndex to the current index when generating the HTML
    Index = index;
    
    
}
function update(){
    
    const employees = getEmployees();
    const emp = employees[Index];
   
    emp.employeeID=employeeID.value;
    emp.fname=fname.value;
    emp.salary=salary.value;
    emp.team=team.value;
    emp.companyName=companyName.value;
    emp.role=role.value

    updatebutton.style='display:none'
    addButton.style='display:block'
    saveEmployees(employees);
    displayEmployees();
}
function deleteEmployee(index) {
    if (confirm("Are you sure you want to delete this employee?")) {
        const employees = getEmployees();
        employees.splice(index, 1);
        saveEmployees(employees);
        displayEmployees();
    }
}
function addVIP(index){
    i=0
    if(confirm("are you sure you wanted to treat him as vip?")){
        

        //adding in vip table 
        const vip=IMPEmployees()
        const employees = getEmployees();
        const emp = employees[Index];

   
        


        //deleting in employee table 
        employees.splice(index, 1);
        saveEmployees(employees);
        displayEmployees();
        i=i+1
    }
}
// Load employees on page load
displayEmployees();
