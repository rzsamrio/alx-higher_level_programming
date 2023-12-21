#include "lists.h"

int check_cycle(listint_t *list)
{
	int i, j, len;
	listint_t **addr, **tmp, *current = list;

	len = 10;
	addr = malloc(sizeof(listint_t *) * len);
	for (i = 0; current != NULL; i++)
	{
		if (i == len) /* Realloc? */
		{
			len += 10;
			tmp = malloc(sizeof(listint_t *) * len);
			for (j = 0; j < (len - 10); j++)
				tmp[j] = addr[j];
			free(addr);
			addr = tmp;
		}

		for (j = 0; j < i; j++) /* Check the saved address list for a match */
		{
			if (current == addr[j])
			{
				free(addr);
				return (1);
			}
		}
		addr[i] = current;
		current = current->next;
	}
	free(addr);
	return (0); /* Program is O(n^2) */
}
