#include "lists.h"
/**
 * insert_node - inserts ode in an ascending list
 * @head: address of head node
 * @number: number to insert
 * Return: address of node, NULL if malloc fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *next, *new;

	curr = *head;
	new = malloc(sizeof(listint_t)); /* init node */
	if (new == NULL)
		return (NULL);
	if (*head == NULL || number < (*head)->n)	/* compare number with head */
	{
		new->n = number;
		new->next = curr;
		*head = new;
		return (new);
	}
	while (curr != NULL)	/* loop through */
	{
		next = curr->next;
		if (next != NULL)
		{
			if (number <= next->n && number >= curr->n)
			{
				new->n = number;
				curr->next = new;
				new->next = next;
				break;
			}
			else	/* Iterate current and next pointers */
			{
				curr = next;
				next = curr->next;
			}
		}
		else	/* Once iteration ends, number must be > max number in list */
		{
			new->n = number;
			curr->next = new;
			new->next = NULL;
			break;
		}
	}
	return (new);
}

