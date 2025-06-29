#include <iostream>
#include <vector>
#include <algorithm> // For std::lower_bound and std::upper_bound

// Function to get integer input
int I() {
    int n;
    std::cin >> n;
    return n;
}

// Function to get a list of integers
std::vector<int> LI() {
    std::string line;
    std::getline(std::cin >> std::ws, line); // Read the rest of the line after int, skipping whitespace
    std::vector<int> v;
    std::string num_str;
    for (char c : line) {
        if (c == ' ') {
            if (!num_str.empty()) {
                v.push_back(std::stoi(num_str));
                num_str.clear();
            }
        } else {
            num_str += c;
        }
    }
    if (!num_str.empty()) {
        v.push_back(std::stoi(num_str));
    }
    return v;
}

void solve() {
    int n = I();
    std::vector<int> v = LI();
    long long sol = 0; // Use long long for sol to avoid potential overflow

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            // In C++, std::lower_bound is equivalent to bisect_left
            // std::upper_bound is equivalent to bisect_right
            auto upper_bound_it = std::lower_bound(v.begin(), v.end(), v[i] + v[j]);
            
            // This part of the logic seems to be about a lower bound related to v[n-1]
            // Let's re-evaluate the original Python: `v[n - 1] - v[i] - v[j] + 1`
            // This means we are looking for values `x` such that `x >= v[n-1] - v[i] - v[j] + 1`
            auto lower_bound_it = std::lower_bound(v.begin(), v.end(), v[n - 1] - v[i] - v[j] + 1);
            
            // Get indices from iterators
            int upper_bound_idx = std::distance(v.begin(), upper_bound_it);
            int lower_bound_idx = std::distance(v.begin(), lower_bound_it);

            if (std::max(lower_bound_idx, j + 1) < upper_bound_idx) {
                sol += upper_bound_idx - std::max(lower_bound_idx, j + 1);
            }
        }
    }
    std::cout << sol << std::endl;
}

int main() {
    // For faster input/output
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    bool MULTI = true; // Equivalent to your Python's MULTI = True
    if (MULTI) {
        int num_test_cases = I();
        while (num_test_cases--) {
            solve();
        }
    } else {
        solve();
    }

    return 0;
}