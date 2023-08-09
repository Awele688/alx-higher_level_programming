#include "lists.h"
/**
 * insert_node - Insert in sorted linked list
 * @head:  ptr to  head of the linked list.
 * @number:  number to be inserted.
 *
 * Return: If function fails - NULL.
 * Otherwise - ptr to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nod = *head, *novel;

	novel = malloc(sizeof(listint_t));
	if (novel == NULL)
		return (NULL);
	novel->n = number;

	if (nod == NULL || nod->n >= number)
	{
		novel->next = nod;
		*head = novel;
		return (novel);
	}

	while (nod && nod->next && nod->next->n < number)
		nod = nod->next;

	novel->next = nod->next;
	nod->next = novel;

	return (novel);
}
