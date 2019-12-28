#include "lists.h"

/**
 * is_palidrome - Return is a list s palindrome or not
 * @head:  double ponter to head
 *
 * Return: 1 on success
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int count, i, j;
	int nums [1024];

	current = *head;
	count = 0; i = 0;

	if (*head == NULL)
		return (1);
	j = 0;
	while (current->next != NULL)
	{
		nums[j] = current->n;
		current = current->next;
		count++;
	}

	if (count  % 2 == 0)
	{
		printf("pasa");
		return (0);
	}
	else
	{
		j = count;
		for (i = 0; i < count / 2; i++)
		{
			if (nums[i] == nums[j])
			{
				printf("hhappens");
				i++;
				j--;

			}
			else
			{
				printf("pasa en else");
				return (0);
			}
		}
		return (1);
	}
}
