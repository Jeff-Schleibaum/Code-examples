/*
jeff schleibaum

paintEstimator.cpp

prompts user for price of paint,
number of rooms painted and square feet of wll space in each room

input:
user info on price of paint ,number of rooms,and suare feet .

processing:
1.prompt
2.create functions
 - getPrice()
 - getRooms(int,int,int)
 - getWallspace(int)
 - calcPaint(int,double,int&,double&)
3.display report

output:
report of paintEstimator.
*/

//header
#include<iostream>
#include<string>
#include<iomanip>
#include<cstdlib>
using namespace std;

//protypes
double getPrice();
int getRooms(int, int, int);
int getWallSpace(int);
void calcPaint(int, double, int&, double&);

int main() {

	int numroom,room1=0,room2=0,room3=0;
	double priceGallon;
	

	//intro
	cout << "\nPaint Job Estimator ... " << endl;

	 
	numroom = getRooms(room1,room2,room3);

	priceGallon = getPrice();







	return 0;
}

double getPrice()
{
	double pricegallon;

	cout << "\nPrice per gallon of paint (>=0): " << endl;
	cin >> pricegallon;
	if (pricegallon < 1)
		cout << "error must be 1 gallon or more..." << endl;
	return pricegallon;
}

int getRooms(int room1, int room2, int room3)
{
	int numroom,room=0;
	cout << "\nNumber of rooms to be painted (>=1): " << endl;
	cin >> numroom;
	if (numroom < 1)
		cout << "error must be one room or more..." << endl;
	if (numroom > 1) {
		room++;

		cout << " :" << room << endl;

	}
	return numroom;
}

int getWallSpace(int room)
{
	int wallspace;
	cout << "what is the square feet of walls in each room? " << endl;
	cin >> wallspace;
	return wallspace;
}

void calcPaint(int sqfeet, double pricepaint, int& gallons, double& cost)
{
	int totalPaintcost;
	totalPaintcost = sqfeet * pricepaint + gallons;
}


