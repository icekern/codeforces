#include <iostream>
#include <vector>
#include <numeric> // For std::accumulate
#include <algorithm> // For std::sort

// Function to read an integer
int I() {
    int n;
    std::cin >> n;
    return n;
}

// Function to read a line of space-separated integers into a vector
std::vector<int> LI() {
    int n_elements; // This will be the 'n' from the input, but we'll read it explicitly
    // In competitive programming, 'n' is usually given first, then 'n' elements.
    // Assuming 'n' is read by I() in solve(), and this function is for the elements.
    // If LI() needs to read 'n' elements without 'n' being passed, it's problematic.
    // For this translation, I'll assume it's used after 'n' is known.
    // Let's adjust LI to take 'n' as an argument, or assume it reads until EOF/newline.
    // Based on the Python code, LI() is used to read 'a' which has 'n' elements.
    // So, we'll read 'n' integers.
    int n = I(); // Read n first, then use it to read elements
    std::vector<int> vec(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> vec[i];
    }
    return vec;
}

// Global constant for MULTI test cases
const bool MULTI = true;

void solve() {
    // a vec size n
    // operations:
    // pay 1 coin to increase any element by 1
    // gain 1 coin decrease any element by 1

    // an array is ideal if
    // Vi a[i] >= 2  and  gcd(a[i],a[j]) = 1 for all i != j
    // you have no coins at the start

    // this means that u can modify the array as u want for a quantity of sum(a)
    // minumun namber of elements to remove to make it ideal

    // if i didn t have the conditions where i could remove elements it s easy
    // bcz i need to consider every array that respects this condition
    // sum(a) = sum(v)

    // if i do eratostene 4 * 10 ^ 5  we pick every possible nunber and we put them in a vector
    // we create a pfx of sum of the vector
    // we order the vector of the elements of the problem
    // and we remove elements until the sum is a[:i] >= era[i]

    int n = I(); // Read n
    std::vector<int> a(n); // Declare vector 'a' of size 'n'
    for (int i = 0; i < n; ++i) { // Read 'n' elements into 'a'
        std::cin >> a[i];
    }

    // eratostene (Sieve of Eratosthenes)
    // Max value for era based on 10**7 + 1
    const int MAX_ERA_VAL = 6000000 + 1;
    std::vector<int> is_composite(MAX_ERA_VAL, 0); // 0 means prime, 1 means composite

    for (int i = 2; i < MAX_ERA_VAL; ++i) {
        if (is_composite[i] == 0) { // If i is prime
            for (long long j = (long long)i * i; j < MAX_ERA_VAL; j += i) {
                is_composite[j] = 1; // Mark multiples as composite
            }
        }
    }

    std::vector<long long> era_primes; // Store actual prime numbers
    for (int i = 2; i < MAX_ERA_VAL; ++i) {
        if (is_composite[i] == 0) {
            era_primes.push_back(i);
        }
    }

    // Prefix sum of prime numbers
    std::vector<long long> pfx(era_primes.size() + 1, 0);
    for (int i = 0; i < era_primes.size(); ++i) {
        pfx[i + 1] = pfx[i] + era_primes[i];
    }

    std::sort(a.begin(), a.end()); // Sort the input array 'a'

    long long initial_sum = 0;
    for (int x : a) {
        initial_sum += x;
    }
    // Or using std::accumulate:
    // long long initial_sum = std::accumulate(a.begin(), a.end(), 0LL);

    int sol = 0;
    // Iterate from largest possible ideal array size down to 0
    // The Python loop `for i in range(len(a), 0, -1):` means i goes from len(a) down to 1 (inclusive)
    for (int i = a.size(); i >= 0; --i) {
        // pfx[i] is the sum of the first 'i' primes.
        // We need to ensure 'i' is a valid index for pfx and era_primes.
        // If i is 0, pfx[0] is 0.
        if (i == 0) { // If we consider an empty ideal array, sum is 0.
            sol = 0;
            break;
        }
        if (i <= era_primes.size() && pfx[i] <= initial_sum) {
            sol = i;
            break;
        } else {
            // This part of the logic is tricky in the original Python.
            // `initial_sum -= a[n - i]`
            // When `i` is `len(a)`, `n-i` is `0`. So it removes `a[0]`.
            // When `i` is `len(a)-1`, `n-i` is `1`. So it removes `a[1]`.
            // This means it's removing elements from the *start* of the sorted array `a`
            // as `i` decreases.
            // Let's re-evaluate the Python loop:
            // `for i in range(len(a), 0, -1):`
            //   `if pfx[i] <= initial_sum:`
            //     `sol = i`
            //     `break`
            //   `else:`
            //     `initial_sum -= a[n - i]`
            // This implies that `initial_sum` is the sum of the *remaining* elements in `a`
            // after 'removing' `len(a) - i` elements from the original array `a`.
            // The elements removed are `a[0], a[1], ..., a[len(a)-i-1]`.
            //
            // Let's trace it:
            // Initial: `initial_sum = sum(a)`
            // i = len(a): `pfx[len(a)] <= sum(a)`? If yes, `sol = len(a)`.
            // If no: `initial_sum -= a[n - len(a)]` which is `a[0]`.
            // Now `initial_sum` is `sum(a[1:])`.
            // i = len(a)-1: `pfx[len(a)-1] <= sum(a[1:])`? If yes, `sol = len(a)-1`.
            // If no: `initial_sum -= a[n - (len(a)-1)]` which is `a[1]`.
            // Now `initial_sum` is `sum(a[2:])`.
            //
            // So, `initial_sum` is always the sum of the `i` largest elements of the original `a`.
            // `a[n - i]` is the `i`-th element from the end, or `len(a) - i`-th element from the beginning (0-indexed).
            // Example: n=5, a=[1,2,3,4,5]
            // i=5: initial_sum = 15. pfx[5] <= 15? If not, initial_sum -= a[0] (1). initial_sum = 14.
            // i=4: pfx[4] <= 14? If not, initial_sum -= a[1] (2). initial_sum = 12.
            // i=3: pfx[3] <= 12? If not, initial_sum -= a[2] (3). initial_sum = 9.
            //
            // This means `initial_sum` should be the sum of the `i` largest elements of `a`.
            // A more direct way to implement this would be to calculate `current_sum` for the `i` largest elements.
            // The original logic is effectively trying to find the largest `i` such that the sum of the `i` largest elements of `a`
            // is greater than or equal to the sum of the first `i` primes.
            //
            // Let's re-think the loop for clarity in C++.
            // We want to find the maximum `k` (number of elements to keep) such that `sum(k_largest_elements_of_a) >= sum(first_k_primes)`.
            // The number of elements to remove would then be `n - k`.

            // The original Python logic is indeed removing elements from the *start* of the sorted array `a`
            // as `i` decreases. This means `initial_sum` is the sum of the `i` largest elements of `a`.
            // The index `n - i` refers to the element that is being "removed" from the consideration of `initial_sum`.
            // When `i` is `len(a)`, `n-i` is `0`, so `a[0]` is removed.
            // When `i` is `len(a)-1`, `n-i` is `1`, so `a[1]` is removed.
            // This means `initial_sum` always represents the sum of the *last `i` elements* of the sorted array `a`.
            // This is correct for finding the maximum `i` elements to keep.
            initial_sum -= a[n - i]; // This is the element that would be removed if we keep `i-1` elements
                                     // (i.e., we are now considering the sum of the `i-1` largest elements).
        }
    }

    std::cout << a.size() - sol << std::endl; // number of elements to remove to make it ideal
}

void main_func() {
    if (MULTI) {
        int t = I(); // Read number of test cases
        while (t--) {
            solve();
        }
    } else {
        solve();
    }
}

int main() {
    // Optimize C++ standard streams for competitive programming
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    main_func();

    return 0;
}
