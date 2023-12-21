#include "lists.h"
/**
 * check_cycle - checks for a cycle in the singly linked list
 * @list: list to check
 * Return: 1 if cycle and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp, *s2; /* s2: step twice */

	if (list == NULL)
		return (0);

	tmp = list->next;
	if (tmp == NULL || tmp->next == NULL)
		return (0);
	s2 = tmp->next->next;
	while (s2 != NULL || tmp != NULL)
	{
		if (tmp == list || s2 == tmp)
			return (1);
		tmp = tmp->next;
		if (s2->next == NULL || s2->next->next == NULL)
			break;
		s2 = s2->next->next;
	}
	return (0);
}
