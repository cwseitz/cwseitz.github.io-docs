### The Python/C API

This post will cover one method for improving the performance of native Python code. Python is an interpreted language and is therefore not compiled directly. Naturally, the solution is to make use of direclty compiled code rather than interpreted code to achieve performance gains. In the python world, that is commonly achieved by making use of the Python/C API. 

The Python/C API provides an interface between the Python interpreter and the C standard libarary as well as custom modules. The most common use of this API is to write extension C modules than can extend the python interpreter. This is particularly useful when execution speed is critical or an existing module(s) is written in C and needs to be invoked from Python.

We can get started by writing a module in C that provides an interface to the C library function fputs(). The declaration of fputs looks like this:


```c
int fputs(const char *str, FILE *stream)
```

We can see that fputs takes an array of characters as well a pointer to a FILE object that identifies the stream where the string is to be written. Now, let's create a module called magicpants that will serve as a wrapper to the fputs() standard library function. In a file magicpants.c we define the following functions.


```c
#include <Python.h>


static PyObject *magicpants_fputs(PyObject *self, PyObject *args) {
    char *str, *filename = NULL;
    int bytes_copied = -1;

    /* Parse arguments */
    if(!PyArg_ParseTuple(args, "ss", &str, &filename)) {
        return NULL;
    }

    FILE *fp = fopen(filename, "w");
    bytes_copied = fputs(str, fp);
    fclose(fp);

    return PyLong_FromLong(bytes_copied);
}

static PyMethodDef MagicpantsMethods[] = {
    {"fputs", magicpants_fputs, METH_VARARGS, "Python interface for fputs C library function"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef magicpantsmodule = {
    PyModuleDef_HEAD_INIT,
    "magicpants",
    "Python interface for the fputs C library function",
    -1,
    MagicpantsMethods
};

PyMODINIT_FUNC PyInit_magicpants(void) {
    return PyModule_Create(&magicpantsmodule);
}

```

There are a total of four functions that make up our Python extension module written in C. The first function *magicpants_fputs* is the function that will be invoked by the user. It calls the fputs() C function and allows the user to write a Python string object to a file. At this point, it is critical to address the declaration


```c
static PyObject *magicpants_fputs(PyObject *self, PyObject *args){}
```

Notice that the function is set to return the PyObject type. Everything you can touch in Python is a PyObject in C. That includes lists, dictionaries, sockets, files, integers, strings, functions, classes, you name it. If you can touch it in Python, it’s a PyObject in C. In addition, the function takes PyObjects as arguments which are parsed by the following chunk of code:


```c
/* Parse arguments */
if(!PyArg_ParseTuple(args, "ss", &str, &filename)) {
    return NULL;
}
```

After that, fputs() is invoked and we return the number of bytes written with *PyLong_FromLong* which of course is a Python object. 

The second function is called the method mapping table:


```c
static PyMethodDef MagicpantsMethods[] = {
    {"fputs", magicpants_fputs, METH_VARARGS, "Python interface for fputs C library function"},
    {NULL, NULL, 0, NULL}
};
```

It is a structure that contains the following information:

**ml_name** − This is the name of the function as the Python interpreter presents when it is used in Python programs.

**ml_meth** − This must be the address to a function that has any one of the signatures described in previous section.

**ml_flags** − This tells the interpreter which of the three signatures ml_meth is using.

**ml_doc** − This is the docstring for the function, which could be NULL if you do not feel like writing one.

The third function defines the module itself: 


```c
static struct PyModuleDef magicpantsmodule = {
    PyModuleDef_HEAD_INIT,
    "magicpants",
    "Python interface for the fputs C library function",
    -1,
    MagicpantsMethods
};
```


```c
The fourth simply initializes the C extension
```


```c
PyMODINIT_FUNC PyInit_magicpants(void) {
    return PyModule_Create(&magicpantsmodule);
}

```

Finally, to call our C functions, we can install our module to our current environment by creating the following setup.py file in the same directory as magicpants.c 


```c
from distutils.core import setup, Extension

def main():
    setup(name="magicpants",
          version="1.0.0",
          description="Python interface for the fputs C library function",
          author="Clayton Seitz",
          author_email="cwseitz@uchicago.edu",
          ext_modules=[Extension("magicpants", ["magicpants.c"])])

if __name__ == "__main__":
    main()

```


```c
python setup.py install
python
>>> import magicpants
>>> magicpants.fputs("You now have magical pants", "magicpants.txt")
```

If you are saving a python script to call this, be sure to name it something other than magicpants.py to avoid any conflicts
