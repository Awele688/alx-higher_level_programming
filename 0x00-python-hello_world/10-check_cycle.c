#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *snail = list, *hare = list;

	if (list == NULL)
		return (0);

	while (snail && hare && hare->next)
	{
		snail = snail->next;
		hare = hare->next->next;
		if (snail == hare)
			return (1);
	}

	return (0);
}
