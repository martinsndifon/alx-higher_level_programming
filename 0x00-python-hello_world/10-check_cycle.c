#include "lists.h"

/**
 * check_cycle - checks if a singly-linked list contains a cycle.
 * @list: a singly-linked list
 *
 * Return: 0 if no cycle and 1 if a cycle exist
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	if (list == NULL)
		return (0);

	do
	{
		if (temp->next == NULL)
			return (0);
		temp = temp->next;
	}while (temp != list);

	return (1);
}	
