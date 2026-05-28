#include<iostream>
int Digits(int num){
    for(int i=10;;){
        double k=num/i;
        if(k>0 && k<1){
            return i;
        }
        else{
            
        }
    }
    }
    

int main(){
    int l=Digits(459);
    std::cout<< l;
    return 0;
}