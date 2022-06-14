#include <iostream>
#include <set>
#include <vector>

using namespace std;

// Checks how many trouble pairs are in both classes
int checkNumberOfPairs(set<int> &class1, set<int> &class2,
                       vector<pair<int, int>> &pairs) {
  int count = 0;

  for (auto &pair : pairs) {
    if (class1.find(pair.first) != class1.end() &&
        class1.find(pair.second) != class1.end())
      count += 1;
    else if (class2.find(pair.first) != class2.end() &&
             class2.find(pair.second) != class2.end())
      count += 1;
  }
  return count;
}

int main() {
  int N;
  cin >> N;
  for (int i = 0; i < N; i++) {
    int n, m;
    cin >> n >> m;
    vector<pair<int, int>> pairs;
    for (int j = 0; j < m; j++) {
      int u, v;
      cin >> u >> v;
      pairs.emplace_back(u, v);
    }
    set<int> class1;
    set<int> class2;

    for (int j = 1; j <= n; j++) {
      class1.insert(j);
    }

    for (int j = 1; j <= n; j++) {
      int beforeMoving = checkNumberOfPairs(class1, class2, pairs);
      class1.erase(j);
      class2.insert(j);
      int afterMoving = checkNumberOfPairs(class1, class2, pairs);
      if (afterMoving >= beforeMoving) {   // if the number of trouble pairs after moving the
                                            // student is less than before, then we keep the
                                            // student on the new classroom(best locally decision,
                                             // greedy)
        class2.erase(j);
        class1.insert(j);
      
      }

  
    }
    //  is not needed to check if min <= m/2 because we are
    // sure it will always happen, there are no impossible cases
    cout << "Case #" << i + 1 << ": " << class2.size() << endl;
    for (auto it = class2.begin(); it != class2.end(); it++) {
      if (it != class2.begin()) {
        cout << " ";
      }
      cout << *it;
    }
    cout << endl;
  }
  return 0;
}