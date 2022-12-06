#define PY_SSIZE_T_CLEAN
#include <python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - prints info about python list
 * @p: python list to be passed
 * Return: void
 */

void print_python_list_info(pyobject *p)
{
	int len = pyList_Size(p), i = 0;
	int allot = (((pyListobject *)p)->allocated);

	printf("[*] Size of the python List = %d\n", len);
	printf("[*] Allocated = %d\n", allot);

	while (i < len)
	{
		pyobject *ele = pyList_GetItem(p, i);
		const char *eleName = py_TYPE(ele)->tp_name;
		printf("Element %d: %s\n", i, eleName);
		i++;
	}
}
