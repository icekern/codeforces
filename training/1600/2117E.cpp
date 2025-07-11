#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

// Created on: 11/07/2025 18:10:46
// Author: Porcelli
// GitHub: https://github.com/icekern/codeforces

void solve() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    std::vector<int> b(n);

    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
        std::cin >> b[i];
    }

    std::map<int, std::vector<int>> first_strip;
    std::map<int, std::vector<int>> second_strip;

    for (int i = n - 1; i >= 0; --i) {
        if (i % 2 == 1) { // Odd index
            first_strip[a[i]].push_back(i);
            second_strip[b[i]].push_back(i);
        } else { // Even index
            first_strip[b[i]].push_back(i);
            second_strip[a[i]].push_back(i);
        }
    }

    int sol = 0;
    for (int i = 1; i <= n; ++i) {
        if (first_strip.count(i) && !first_strip[i].empty() && second_strip.count(i) && !second_strip[i].empty()) {
            sol = std::max(sol, std::min(first_strip[i][0], second_strip[i][0]) + 1);
        }

        if (first_strip.count(i) && first_strip[i].size() > 1) {
            if (first_strip[i][0] == first_strip[i][1] + 1) {
                if (first_strip[i].size() > 2) {
                    sol = std::max(sol, first_strip[i][2] + 1);
                }
            } else {
                sol = std::max(sol, first_strip[i][1] + 1);
            }
        }

        if (second_strip.count(i) && second_strip[i].size() > 1) {
            if (second_strip[i][0] == second_strip[i][1] + 1) {
                if (second_strip[i].size() > 2) {
                    sol = std::max(sol, second_strip[i][2] + 1);
                }
            } else {
                sol = std::max(sol, second_strip[i][1] + 1);
            }
        }
    }
    std::cout << sol << std::endl;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int multi;
    std::cin >> multi;
    while (multi--) {
        solve();
    }

    return 0;
}