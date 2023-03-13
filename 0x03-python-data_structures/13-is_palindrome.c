#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to singly linked list
 *
 * Return: 0 if not a palindrome or 1 if it is a palindrome
 */
int is_palindrome(listint_t **head) {
  listint_t *current = *head;
  int i = 0, j = 0, len = 0, *arr;

  if (!head || !*head)
    return (1); /* An empty list is a palindrome */
  while (current != NULL) {
    current = current->next;
    len++;
  }
  arr = malloc(sizeof(int) * len);
  if (!arr)
    return (0);
  current = *head;
  while (current != NULL) {
    arr[i] = current->n;
    current = current->next;
    i++;
  }
  i--;
  while (i > j) {
    if (arr[i] != arr[j]) {
      free(arr);
      return (0);
    }
    i--;
    j++;
  }
  free(arr);
  return (1);
}
