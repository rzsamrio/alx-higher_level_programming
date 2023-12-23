#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: address of the head node
 * Return: 1 if true, 0 if false
 */


int is_palindrome(listint_t **head)
{
	int i, len, centre, stop, iter,  stat = 1;
	listint_t *curr;
	int *arr;

	if (*head == NULL)
		return (1);

	curr = *head;
	for (len = 0; curr != NULL; len++)
		curr = curr->next;
	if (len % 2 == 0)
		centre = len / 2;
	else
		centre =  (len / 2) + 1;

	iter = len % 2 == 0 ? centre - 1 : centre - 2;
	arr = malloc(sizeof(int) * (centre));

	curr = *head;
	for (i = 0, stop = centre; i < len; i++)
	{
		if (i < stop)
			arr[i] = curr->n;
		else
		{
			if (arr[iter] != curr->n)
			{
				stat = 0;
			}
			iter--;
		}
		curr = curr->next;
	}
	return (stat);
}
