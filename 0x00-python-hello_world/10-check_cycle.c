#include "lists.h"

/**
 * check_cycle - checks for a cycle in the singly linked list
 * @list: list to check
 * Return: 1 if cycle and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp, *head = list;

	if (list == NULL)
		return (0);

	tmp = head->next;
	while (tmp != NULL)
	{
		if (tmp == head)
			return (1);
		tmp = tmp->next;
	}
	return (0);
}
