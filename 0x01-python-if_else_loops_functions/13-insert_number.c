#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node into sorted linked-list
 * @head: a pointer to the linked list to work with
 * @number: the int to add into the linked list
 *
 * Return: the address of the new node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp;

	if (!head)
		return (NULL);

	node = malloc(sizeof(*node));
	if (node == NULL)
	{
		free(node);
		return (NULL);
	}

	node->n = number;
	node->next = NULL;
	
	if (!(*head))
	{
		*head = node;
		return (*head);
	}

	temp = *head;

	while (temp->next != NULL)
	{
		if (temp->next->n > node->n)
		{
			listint_t *temp1 = temp->next;
			temp->next = node;
			node->next = temp1;
			return (*head);
		}

		temp = temp->next;
	}

	temp->next = node;

	return (*head);
}

