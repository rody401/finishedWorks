#include <stdlib.h>
#include <iostream>
#include <string>
using namespace std;

void print_menu(void);
void print_balance(double);
double deposit_amount(double, double);
double withdraw_amount(double, double);

int main()
{
  // Setting up variables;  
  char choice;
  double deposit, withdraw;
  double balance = 5000.00;

  cout<<"Welcome!" << endl; //Startingto set up menu;
  print_balance(balance);  //Calling print_balance here;
  print_menu();
  cin >> choice;
  //Setting up print menu and choice;
  while(choice != 'Q' && choice != 'q') //If 'Q' || 'q' is entered, the program will exit;
  {
      if(choice == 'D' || choice == 'd') //Deposit part of the menu;
      {
          cout << "Please enter the amount you would like to deposit:" << endl;
          cin >> deposit;
          
          while(deposit < 0) //Setting up if the deposit entered is below 0;
          {
              cout << "Please enter a proper amount: " << endl;
              cin >> deposit;
          }
          
          balance = deposit_amount(deposit, balance);
          cout << "Your transaction is complete. Your current balance is " << balance << " dollars.\n";
      }
      else if(choice == 'W' || choice == 'w') //Withdraw part of the menu;
      {
          cout << "Please enter the amount you would like to withdraw:" << endl;
          cin >> withdraw;
          
          while(withdraw < 0) //Setting up if the withdraw entered is below 0;
          {
              cout << "Please enter a proper amount: " << endl;
              cin >> withdraw;
          }
          
          balance = withdraw_amount(withdraw, balance);
          cout << "Your tranaction is complete. Your current balance is " << balance << " dollars.\n";
      }
      else if (choice == 'B' || choice == 'b') //Balance part of the menu;
      {
          cout << "Your current balance is " << balance << " dollars.\n";
      }
      else
      {
          print_menu(); 
          cin >> choice;
          continue;
      }
      
      print_menu(); //The print menu repeats it's self like a counter;
      cin >> choice;
  }

 system("PAUSE");
 return 0;
}
//Defining the functions 
void print_balance(double balance)
{
    cout << "Your current balance is " << balance << " dollars.\n";
}

void print_menu()
{
    cout << "Here are your options: Enter (D) or (d) to make a deposit, (W) or (w) to make a withdrawl, (B) or (b) to view the current balance and (Q) or (q) to quit.\n";
}

double deposit_amount(double deposit, double balance)
{
	  return (balance + deposit);
}

double withdraw_amount(double withdraw, double balance)
{

      return (balance - withdraw);
}

