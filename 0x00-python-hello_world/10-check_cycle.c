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
	listint_t *tmp;

	if (list == NULL)
		return (0);

	address = list;
	tmp = list;

	while (tmp->next != NULL)
	{
		if (address == tmp->next)
		{
			return (1);
		}
		tmp = tmp->next;
	}

	return (0);
}
