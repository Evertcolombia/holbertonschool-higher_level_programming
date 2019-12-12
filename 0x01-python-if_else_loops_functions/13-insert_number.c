#include "lists.h"
#include <stdio.h>
listint_t *insert_node(listint_t **head, __attribute((unused))int number)
{
	/*listint_t *tmp;*/
	listint_t *current;

	if (!head)
		return (0);
	current = *head;

	while(current->next)
	{
		current = current->next;
	}
	return (current);
}
