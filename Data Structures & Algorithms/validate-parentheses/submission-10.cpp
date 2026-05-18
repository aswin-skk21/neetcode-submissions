class Solution {
public:
    bool isValid(string s) {
        stack<char> p;
        unordered_map<char, char> f = {{']', '['}, {'}', '{'}, {')', '('}};
        int i = 0;
        if (s.size() % 2 != 0) return false;
        while (i != s.size()) {
            if (s[i] != ']' && s[i] != ')' && s[i] != '}') {
                p.push(s[i]);
            }
            else if (!p.empty() && f[s[i]] == p.top()) {
                   p.pop(); 
            } else {
                return false;
            }
            i++;
        }
        return p.empty();
    }
};
