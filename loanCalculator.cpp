/*
jeff schleibaum
loanCalculator.cpp
a program that prompts the user for the loan amount, 
annual interest rate, and term of the loan (in years) 
and displays the expected monthly payment, total amount to be paid,
and total interest to be paid.

input :
prompts auser for loan amount and than displays calculation 

processing:
prompt user
borrower name
loaning institution
loan amount
annual interest rate
term of loan
date of report

variables
double Mir;
int loanYears,loanMonths;

calculate
annual interest rate 
const double Air = 0.0375;
monthly interest rate 
Mir = Air /12;
number of payments
loanMonths = loanYears * 12;
monthly payment 



output: 
loan payment calculator display 
*/

// header
#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>
using namespace std;


int main() {

	// variables
	const double Air = 0.0375;
	double Mir,Totalamount;
	int loanYears, loanMonths,LoanAmount,numpayment,monthpayment;
	string BorrowerName,LoanInst, Datereport;

	//title
	cout << "Loan Payment Calculator ... " << endl << endl;

	//prompt
	cout << "Please enter the following information: " << endl << endl;

	
	cout << "Borrower's Name: \t";
	getline(cin, BorrowerName);
	cout << "Loaning Institution: \t";
	getline(cin, LoanInst);


	cout << "\nLoan Amount ($): \t\t";
	cin >> LoanAmount;
	cout << "Annual Interest Rate (%): \t3.75";
	cout << "\nTerm of Loan (years): \t\t";
	cin >> loanYears;
	cin.ignore();
	cout << "\nDate of Report: \t\t";
	getline(cin, Datereport);

	//output report
	cout << "\n--------------------------" << endl;
	cout << "Loan Payment Summary Report " << endl << endl;

	cout  << BorrowerName << endl;

	//calculate
	Mir = Air / 12;
	loanMonths = loanYears * 12;
	monthpayment = Mir * pow(1 + Mir, 360) / pow(1 + Mir, 360) - 1;
	Totalamount = monthpayment * Mir * loanMonths;

	cout << "Annual Interest Rate: 3.75%" << endl;
	cout << "Date: " << Datereport << endl << endl;
	cout << setw(8) << right << "LoanAmount: " << LoanAmount <<left << endl
		<< setw(8) << right << "Monthly Interest Rate: " << Mir <<left<<endl
		<< setw(8) << right << "Number of payments: " << loanMonths<<left << endl
		<< setw(8) << right << "Monthly payment: " << monthpayment << left
		<< endl;

	cout << setw(8) << right << "Total Amount to pay: \t" << Totalamount <<left << endl
		<< setw(8) << right << "Total interest: \t";











	return 0;
}
























