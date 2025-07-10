#include <iostream>
#include <vector>
#include <numeric>
#include <deque>
#include <algorithm>

int I() {
    int n;
    std::cin >> n;
    return n;
}

std::vector<int> LI() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }
    return a;
}

bool DEBUG = true;

template <typename... Args>
void PRI(Args... args) {
    if (DEBUG) {
        std::cout << "\033[92m";
        ((std::cout << args << " "), ...);
        std::cout << "\033[0m\n";
    } else {
        ((std::cout << args << " "), ...);
        std::cout << "\n";
    }
}

void solve() {
    int n = I();
    std::vector<int> a(n);
    for(int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    int min_gcd_overall = 0;
    if (n > 0) {
        min_gcd_overall = a[0];
        for (int i = 1; i < n; ++i) {
            min_gcd_overall = std::gcd(min_gcd_overall, a[i]);
        }
    }

    int min_steps = 2e9;
    int idx_of_best_start = -1;

    for (int i = 0; i < n; ++i) {
        std::deque<std::pair<int, int>> queue;
        queue.push_back({a[i], 0});
        std::vector<bool> visited(5001, false); 

        while (!queue.empty()) {
            std::pair<int, int> current = queue.front();
            queue.pop_front();
            int x = current.first;
            int steps = current.second;

            if (visited[x]) {
                continue;
            }
            visited[x] = true;

            if (x == min_gcd_overall) {
                if (steps < min_steps) {
                    min_steps = steps;
                    idx_of_best_start = i;
                }
                break;
            }

            for (int j = i + 1; j < n; ++j) {
                int new_x = std::gcd(x, a[j]);
                if (new_x != x && !visited[new_x]) {
                    queue.push_back({new_x, steps + 1});
                }
            }
        }
    }
    
    for (int i = 0; i < n; ++i) {
        if (i == idx_of_best_start) {
            continue;
        }
        if (a[i] != min_gcd_overall) {
            min_steps += 1;
        }
    }
    
    PRI(min_steps);
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    bool MULTI = true;

    if (MULTI) {
        int t = I();
        while (t--) {
            solve();
        }
    } else {
        solve();
    }

    return 0;
}