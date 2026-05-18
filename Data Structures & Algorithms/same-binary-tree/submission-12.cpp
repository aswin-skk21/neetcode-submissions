/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
            if (!p && !q) return true;
            if (!p || !q) return false;

            std::queue<TreeNode*> s;
            std::queue<TreeNode*> t;
            s.push(p);
            t.push(q);

            while (!s.empty() && !t.empty()) {
                TreeNode* curr1 = s.front();
                TreeNode* curr2 = t.front();
                if (curr1->val != curr2->val) return false;
                s.pop();
                t.pop();

                if (curr1->left != nullptr && curr2 ->left != nullptr) {
                    s.push(curr1->left);
                    t.push(curr2->left);
                } else if (curr1->left != nullptr || curr2 ->left != nullptr) return false;
                if (curr1->right != nullptr && curr2 ->right != nullptr) {
                    s.push(curr1->right);
                    t.push(curr2->right);
                } else if (curr1->right != nullptr || curr2 ->right != nullptr) return false;
            }
            return s.empty() && t.empty();
        }
};
