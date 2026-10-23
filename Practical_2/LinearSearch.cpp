#include <iostream>
using namespace std;

int main() {
    int n, target;

    cout << "Enter the number of elements: ";
    cin >> n;

    int arr[n];

    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    cout << "Enter the element to search: ";
    cin >> target;
    int found = 0;

    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            cout << "Element found at position " << i + 1;
            cout <<" \n ";
            found = 1;
            break;
        }
    }
    if (!found)
        cout << "Element not found";
        cout <<" \n ";
    return 0;
    
}