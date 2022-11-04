#include <bits/stdc++.h>

using namespace std;

typedef long long ll;


// class Degree{
//     public:
//         string text;
//         Degree(){
//             text = "You have a degreee!";
//         }
//         void display(){
//             cout << text<<"\n";
//         }
// };

// class Department{
//     public :
//         string dpt;
//         Department(){
//             dpt = "Department ET";
//         }
// };

// class UG : public Degree, public Department{
//     private:
//         string UGtext = "You have a UG degree\t";
//     public:
//         UG(){
//             text = UGtext + dpt;
//         }
// };

// class PG: public Degree{
//     private:
//         string PGtext = "You have a PG Degree";
//     public:
//         PG(){
//             text = PGtext;
//         }
// };

// int main(){
//     Degree obj1;
//     UG obj2;
//     PG obj3;

//     obj1.display();
//     obj2.display();
//     obj3.display();
// }

// 1 Student info and printing

// class Reader{
//     protected :
//         string name;
//         int rno;
//         Reader(){
//             cin >> name >> rno;
//         }
// };

// class Printer : public Reader{
//     public :
//     void print(){
//         cout << "Name "<< name << "\n" << "Roll No. "<< rno << "\n";
//     }
// };

// 2 square and cube using hierarchial inheritance

// class Number{
//     public :
//         int n;
//         Number(){
//             cin >> n;
//         }
// };

// class Cube : public Number{

//     public:
//         Cube(){
//             cout << "Cube of " << n << " is " << n * n * n<< "\n";
//         }
// };

// class Square : public Number{
//     public :
//         Square(){
//             cout << "Square of " << n << " is " << n * n << "\n";
//         }
// };

// int main(){
//     Cube obj1;
//     Square obj2;
// }

// 3) Read emp info and print

// class getInfo{
//     public:
//         string name;
//         int empno;
        
//         void get(){
//             cin >> name >> empno;
//         }
// };

// class printInfo : public getInfo{
//     public:
//         void print(){
//             get();
//             cout << "Name : " << name<<"\nRoll no : " << empno;
//         }
// };

// class emp : public printInfo{
//     public : 
//         emp(){
//             printInfo ob1;
//             ob1.print();
//         }
// };

// int main(){
//     emp first;
// }

// 4) Access protected data member 


class Base{
    public:
    void print(){
        cout << "This is Base Class\n";
    }
};

class Derived : public Base{
    public:
        void print(){
            cout << "This is Derived sub class\n";
        }
};

int main(){
    Base ob1;
    Derived ob2;
    ob1.print();
    ob2.print();
}