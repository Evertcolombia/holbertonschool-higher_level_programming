#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

void print_phyton_list_info(PyObject *p)
{
	int len = 0, idx;
	PyObject *item;
	PyListObject *clone = (PyListObject *) p;

	len = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", (int) clone->allocated);

	for (idx = 0; idx < len; idx++)
	{
		item = PyList_GET_ITEM(p, idx);
		printf("Element %d: %s\n", idx, item->ob_type->tp_name);
	}

	return;
}
