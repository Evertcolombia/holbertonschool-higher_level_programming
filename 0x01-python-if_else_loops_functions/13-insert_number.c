#include "lists.h"
#include <stdlib.h>

/**
 * *insert_node - insert a node in sorted lned list
 * @head: header of list
 * @number: number to insert
 *
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new_node;

	current = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
		*head = new_node;

	if (current->n > number)
		new_node->next = *head, *head = new_node;
	else
	{
		while (current->next != NULL)
		{
			if ((current->n < number) && ((current->next)->n > number))
			{
				current->next = new_node;
				new_node->next = current->next;
			}
			current = current->next;
		}

		if (current->n < number)
		{

			current->next = new_node;
		}
	}
	return (new_node);
}
