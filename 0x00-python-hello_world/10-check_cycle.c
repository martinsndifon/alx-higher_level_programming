#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	do
	{
		if (temp->next == NULL)
			return (0);
		temp = temp->next;
	}while (temp != list);

	return (1);
}	
