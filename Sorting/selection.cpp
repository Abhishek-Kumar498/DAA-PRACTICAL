#include<iostream>
using namespace std;
int main(){
    int arr[] = {5, 2, 9, 1, 5,20,21,1};
    int n = sizeof(arr)/sizeof(arr[0]);
    for(int i=0; i<n-1; i++){
        int minindex = i;
        for (int j = i+1 ;j<n;j++){
            if(arr[j]<arr[minindex]){
                minindex = j;
            }
        }
        int temp = arr[i];
            arr[i] = arr[minindex];
            arr[minindex] = temp;
        
    }
    for(int i = 0 ;i<n ; i++){
        cout << arr[i] << "  ";
    }
    cout << "\n";
    return 0;
}
