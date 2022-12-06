#include "lists.h"
#include <stdlib.h>

/**
 * reverse - reverses a linked list
 * @head: head of the linked list
 * Return: the head of the reversed linked list
 */

listint_t *reverse(listint_t *head)
{
	listint_t *temp, *prev, *next;

	temp = head;
	prev = NULL;
	while (temp != NULL)
	{
		next = temp->next;
		temp->next = prev;
		prev = temp;
		temp = next;
	}
	temp = prev;

	return (prev);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to a pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome
 * 	1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *fast, *slow, *nhead;

	if (!head)
		return (-1);

	if (!(*head))
		return (1);

	slow = *head;
	fast = *head;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	nhead = reverse(slow);
	temp = *head;

	while (nhead != NULL)
	{
		if (nhead->n != temp->n)
			return (0);
		temp = temp->next;
		nhead = nhead->next;
	}

	return (1);
}
