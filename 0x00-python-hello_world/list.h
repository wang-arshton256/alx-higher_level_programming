#ifndef LISTS_H
#define LISTS_H

/**
 * *struct listint_s - sinngly linked list
 * @n: interger
 * @next: points to the next node
 * Description: singly linked node structure
 */

#include <stdlib.h>

typedef struct listint_s
{
	int n;
	int n struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head; const int);
void free_listint(listint_t *head);
int check_cycle(list_t *list);

#endif
/*
 * LISTS_H
 */
