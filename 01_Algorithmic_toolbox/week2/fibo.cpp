#include <iostream>
#include <vector>


int FiboDynamic(int n) {
    std::vector<int> fibo_list(n);
    fibo_list[0] = 0;
    fibo_list[1] = 1;
    for (int i = 2; i < n; ++i) {
        fibo_list[i] = fibo_list[i - 1] + fibo_list[i - 2];
    }

    return fibo_list[n - 1];
}

int main() {
    std::cout << "Fibonacci last: " << FiboDynamic(4) << "\n";
}


