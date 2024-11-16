#include <stdio.h>

void removeDuplicates(int arr[], int n, int result[], int *size) {
    int isDuplicate;
    *size = 0; // Initialize size of the result array

    for (int i = 0; i < n; i++) {
        isDuplicate = 0;
        // Check if the current element exists in the result array
        for (int j = 0; j < *size; j++) {
            if (arr[i] == result[j]) {
                isDuplicate = 1;
                break;
            }
        }
        // If no duplicate is found, add to the result array
        if (!isDuplicate) {
            result[*size] = arr[i];
            (*size)++;
        }
    }
}

int main() {
    int arr[] = {5, 3, 8, 3, 7, 2, 8, 5, 1, 9, 3};
    int n = sizeof(arr) / sizeof(arr[0]);

    int result[n]; // Array to store unique elements
    int size;      // Size of the result array

    removeDuplicates(arr, n, result, &size);

    printf("Original Array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    printf("\nArray without Duplicates: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", result[i]);
    }

    return 0;
}
