#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * check_cycle - check for a cycle lined list
 * @list: pointer to head node
 *
 * Return: integer
 */
int check_cycle(listint_t *list)
{
	listint_t *address;

	if (!list)
		return (0);

	address = list;

	while (list->next != NULL)
	{
		if (address == list->next)
		{
			return (1);
		}
		list = list->next;
	}

	return (0);
}
