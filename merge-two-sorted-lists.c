// LC 21 - Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/
// Merges two sorted linked lists into one sorted list (in-place).
// Time: O(n + m) | Space: O(1)

#include <stdio.h>
#include <stdlib.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    // Dummy node to help build the new list
    struct ListNode dummy;
    dummy.next = NULL;
    struct ListNode* tail = &dummy;

    // Merge both lists
    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }

    // Attach the remaining elements
    tail->next = (list1 != NULL) ? list1 : list2;

    return dummy.next;
}
