#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

// Funzione per leggere un intero
// CONVERTED FROM GEMINI CUZ PYTHON DOESN T PASS

int I() {
    int n;
    std::cin >> n;
    return n;
}

// Funzione per risolvere il problema
void solve() {
    int n = I();
    std::map<int, int> cnt;
    std::map<int, int> sup;

    for (int i = 0; i < n; ++i) {
        int val;
        std::cin >> val;
        cnt[val]++;
    }

    std::string solution = "NO";
    
    // Otteniamo le chiavi ordinate da cnt
    std::vector<int> keys;
    for (auto const& [key, val] : cnt) {
        keys.push_back(key);
    }
    std::sort(keys.begin(), keys.end());

    for (int i : keys) {
        int temp = cnt[i];
        int temp_sup = sup[i];

        if (temp >= 4) {
            solution = "YES";
            break;
        } else if (temp >= 2) {
            if (temp_sup == 1) {
                solution = "YES";
                break;
            }
            sup[i + 1] = 1;
        } else if (temp == 1) {
            if (temp_sup == 1) {
                sup[i + 1] = 1;
            }
        }
    }
    std::cout << solution << std::endl;
}

int main() {
    // Ottimizzazione per I/O più veloci
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    bool MULTI = true; // Imposta a true per eseguire più casi di test

    if (MULTI) {
        int t = I(); // Legge il numero di casi di test
        while (t--) {
            solve();
        }
    } else {
        solve();
    }

    return 0;
}