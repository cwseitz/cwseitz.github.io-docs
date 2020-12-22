### Introduction

The C programming language was first developed in the 1970s by Dennis Ritchie a Bell Labs. The language was inspired by its predecessor B and eventually would be standardized by the American National Standards Institute (ANSI) in the 1980s. The C programming language is a relatively low-level programming language which means that, as the programmer, you are required to do most of the leg work that is done automatically by higher level languages like Python. Practically speaking, we have to take memory management into our own hands when programming in C. This makes it very easy to shoot yourself in the foot as the programmer, but it also allows you program just about anything. This is by no means a comprehensive guide; it is only meant to be a rough overview of the language. The C Programming Language textbook is a great resources if you want to learn the ins and outs of the language.

### Hello World

Let's start with the hello world program in C. First, we must import the header file stdio.h, which handles basic input and output from the keyboard and display, respectively. Then we define the function main() which is required in every C program. In C, we are given the option of including the return type of the program before the function name but if our function does not return anything we can omit this. Lastly, we make a function call to *printf()*, where the f stands for format. This is the standard function used for printing to the console and we will see of an example of formatting in the next section. 


```c
#include <stdio.h>

main() {

    printf("Hello World");
    
}
```

    Hello World

### Defining variables

 The first instance of this that we will encounter is in the definition of variables and their data types. This comes down to what is called *static typing* and *dynamic typing*  and there is a nice thread on this [here](https://stackoverflow.com/questions/1517582/what-is-the-difference-between-statically-typed-and-dynamically-typed-languages), but the tl;dr version is just that statically typed languages, like C, require the programmer to explicitly specify the data type of a particular variable when it is defined. Dynamically typed languages, like Python, have a system for inferring the type of a variable. Let's see this in action by creating a Farhenheit-Celsius table.

In the code above you can see that we defined five different variables: fahr, celsius, lower, upper, and step. Each of these is an integer so is preceded by *int*. The rest is just a standard while loop for incrementing the temperature in fahrenheit. 

### Data types in C

Of course, there are other data types available for use in C. You can even define your own custom data types but we won't discuss that here. Anyway, we can arrange some of the commonly used data types in a table:

| Type  | Storage | Value Range |
| ----  | ------- | ----------- |
| char  | 1 byte | -128 to 127 or 0 to 255 |
| unsigned char  | 1 byte | 0 to 255 |
| signed char | 1 byte | -128 to 127 |
| int  | 2 or 4 bytes | -32,768 to 32,767 or -2,147,483,648 to 2,147,483,647 |
| unsigned int  | 2 or 4 bytes | 0 to 65,535 or 0 to 4,294,967,295 |
| float  | 4 bytes | 1.2E-38 to 3.4E+38 |
| double  | 8 bytes | 2.3E-308 to 1.7E+308 |
| short | 2 bytes | -32,768 to 32,767 |
| unsigned short | 2 bytes | 0 to 65,535|
| long | 8 bytes | -9223372036854775808 to 9223372036854775807 |
| unsigned long | 8 bytes | 0 to 18446744073709551615 |


This is by no means a comprehensive list, but its a good start. Let's verify this table by writing a program that defines a variable of each of these types and prints number of bytes allocated for it by using the sizeof function():


```c
#include <stdio.h>

int main() {

    char a_char; 
    unsigned char a_uchar;
    signed char a_schar;
    int a_int; 
    unsigned int a_uint;
    float a_float;
    double a_double;
    short a_short;
    unsigned short a_ushort;
    long a_long;
    unsigned long a_ulong;
    
    
    printf("The size of char is %zu byte(s)\n", sizeof(a_char));
    printf("The size of unsigned char is %zu byte(s)\n", sizeof(a_uchar));
    printf("The size of signed char is %zu byte(s)\n", sizeof(a_schar));
    printf("The size of int is %zu byte(s)\n", sizeof(a_int));
    printf("The size of unsigned int is %zu byte(s)\n", sizeof(a_uint));
    printf("The size of a float is %zu byte(s)\n", sizeof(a_float));
    printf("The size of a double is %zu byte(s)\n", sizeof(a_double));
    printf("The size of short is %zu byte(s)\n", sizeof(a_short));
    printf("The size of unsigned short is %zu byte(s)\n", sizeof(a_ushort));
    printf("The size of long is %zu byte(s)\n", sizeof(a_long));
    printf("The size of unsigned long is %zu byte(s)\n", sizeof(a_ulong));
    
    
}
```

    The size of char is 1 byte(s)
    The size of unsigned char is 1 byte(s)
    The size of signed char is 1 byte(s)
    The size of int is 4 byte(s)
    The size of unsigned int is 4 byte(s)
    The size of a float is 4 byte(s)
    The size of a double is 8 byte(s)
    The size of short is 2 byte(s)
    The size of unsigned short is 2 byte(s)
    The size of long is 8 byte(s)
    The size of unsigned long is 8 byte(s)


### Looping

To learn the syntax for looping in C, we will write a Fahrenheit-Celsius conversion program which can also be found in the standard  C Programming Language textbook. 

#### While-Loops

The standard syntax for a while loop is while(condition){do something}. We can utilize our newfound knowledge of variable definitions to set some bounds on the while-loop.


```c
#include <stdio.h>

int main() {

    int fahr, celsius;
    int lower, upper, step;
    
    lower = 0; /* lower limit of temp table */
    upper = 300; /* upper limit of temp table */
    step = 20; /* step size */
    
    fahr = lower;
    
    while (fahr <= upper){
        
        celsius = 5 * (fahr - 32) / 9;
        printf("%d\t%d\n", fahr, celsius);
        fahr = fahr + step;
    
    }   
}
```

    0	-17
    20	-6
    40	4
    60	15
    80	26
    100	37
    120	48
    140	60
    160	71
    180	82
    200	93
    220	104
    240	115
    260	126
    280	137
    300	148


### For-Loops

Let's write the same program using a for-loop this time. The standard syntax for a for-loop is for(lower bound; upper bound; increment){do something}. In place of 'lower bound' we set some initial condition for the counter that will be modified in the body of the loop. Upper bound is of course the value the counter will take it the loops last iteration, and the increment determines how much the counter is incremented at each iteration. In this case, the counter is the temperature on a fahrenheit scale.


```c
#include <stdio.h>

int main() {

    int fahr, celsius;
    int lower, upper, step;
    
    lower = 0; /* lower limit of temp table */
    upper = 300; /* upper limit of temp table */
    step = 20; /* step size */
    
    fahr = lower;
    
    for (fahr = lower; fahr <= upper; fahr = fahr + step){
    
        celsius = 5 * (fahr - 32) / 9;
        printf("%d\t%d\n", fahr, celsius);
    }

}
```

    0	-17
    20	-6
    40	4
    60	15
    80	26
    100	37
    120	48
    140	60
    160	71
    180	82
    200	93
    220	104
    240	115
    260	126
    280	137
    300	148


### Arrays

#### Character Arrays

In this next section, we will focus on arrays and their implementation in C. This brings up an interesting topic: there is no such thing as a string at this level, rather, strings are implemented as arrays of characters. So we can defined a string by defining an array and assigning its elements as the characters of string like 'bananas'.


```c
#include <stdio.h>

int main() {

    char mystr[7] = "bananas";
    printf("The size of '%s' is %zu byte(s)\n", mystr, sizeof(mystr));

}
```

    The size of 'bananas' is 7 byte(s)


### Integer Arrays

Arrays of integers are defined in a similar way; however, you cannot print the entire array as we did with the character array above. You have to iterate through the array and call printf() for each element. 


```c
#include <stdio.h>

int main() {

    int ndigits = 5;
    int i;
    int digits[ndigits];
    
    for (i = 0; i <= ndigits; i++){

        digits[i] = i;
        printf("%d\n", digits[i]);
    
    }    
}
```

    0
    1
    2
    3
    4
    5


### Control Flow

Another indispensible tool in C programming is the use of control-flow that will determine the behavior of the program given certain inputs. One useful example of this involves using control flow to determine whether a variable is an integer or alphabetical character. This kind of control flow could be very useful when reading raw data from files and parsing the content. 


```c
#include <stdio.h>
#include <ctype.h>

int main(){

   int var1 = 'a';
   int var2 = '5';
    
    
   /* Check variable 1 */
   if(isdigit(var1)) {
      printf("var1 = |%c| is a digit\n", var1);
   } else if (isalpha(var1)){
      printf("var1 = |%c| is an alphabetical character\n", var1);
   }
   
   /* Check variable 2 */
   if(isdigit(var2)){
      printf("var2 = |%c| is a digit\n", var2);
   } else if (isalpha(var2)){
      printf("var2= |%c| is an alphabetical character\n", var2);
   }
}
```

    var1 = |a| is an alphabetical character
    var2 = |5| is a digit


### Functions & Arguments

I really like how the C Programming Language textbook describes the philosophy of a function. The author writes: "With properly defined functions, it is possible to ignore *how* a job is done; knowing *what* is done is sufficient. Thus far, we've utilized functions like printf(), isdigit(), etc.; now, we'd like to define some functions of our own. When defining user functions in C, we have to use a *function prototype* which is typically one line of code that includes three things: the function's return type, name, and arguments. For example if we want to define a function that performs multiplication, it's prototype would look like: float sqrt(float m, float n);. Then, we can write out the body of the function and invoke it in main.



```c
#include <stdio.h>

float mult(float m, float n);

int main(){

    float m, n, p;
    m = 5; 
    n = 2;
    p = mult(m,n);
    printf("The product is: %f", p);
    
}

float mult(float m, float n){

    float p; 
    p = m*n;
    return(p);
    

}
```

    The product is: 10.000000

### Pointers

A pointer in C is a variable that contains the address of another variable. To really understand pointers and why
they are useful, it is necessary to understand how RAM in a computer is organized. RAM is typically an array of memory cells which are numbered consecutively. That address is usually in hexadecimal format. To define a pointer, we precede the pointer name with an asterisk. If b is the variable containing the pointer and type is the data type of the variable that b will point to. For example, we can assign the address of a variable a to another variable b. Also, we can access and modify what is stored in a via the *indirection* or *dereferencing* operator This is best shown by example:


```c
#include <stdio.h>


int main(){

    int a, c, *b;
    
    a = 5;
    b = &a; 
    
    printf("The variable a is located at: %p\n", b); 
    printf("The contents of a is: %d\n", *b);
    
    c = *b;
    *b += 5;
    ++*b;

    printf("The contents of a is: %d\n", *b);
    printf("The contents of c is: %d", c);
    
}

```

    The variable a is located at: 0x7ffe7b87f988
    The contents of a is: 5
    The contents of a is: 11
    The contents of c is: 5

As you can see, we can assign the address of a to the pointer b. Then, we can copy what is contained in a to another variable c by using the indirection operator. After that, we modify a using the same operator, keeping c intact. Moving on, pointers become especially important when passing variables to a function you want to modify the original variables. In C, arguments are passed to functions *by value* meaning that when you pass, say, an integer to a function you pass only a *copy* of that integer to the function. Therefore, the function has no way of modifying the variable itself. There is a good example of how to reconcile this issue with pointers in the C Programming Language textbook. We will define a function swap(), which will take to variables and swap their values. First, we will try it the wrong way and then we will show how pointers make it work correctly. 



```c
#include <stdio.h>

void swap(int x, int y){

    int temp; 
    temp = x;
    x = y; 
    y = temp;

}


int main(){

    int x,y; 
    x = 1; 
    y = 2;
    
    swap(x, y);
    printf("The variable x contains: %d\n", x); 
    printf("The variable y contains: %d\n", y); 

}
```

    The variable x contains: 1
    The variable y contains: 2


As you can see, nothing happened. Now let's try it the correct way by using pointers to x and y.


```c
#include <stdio.h>

void swap(int *px, int *py){

    int temp; 
    temp = *px;
    *px = *py; 
    *py = temp;

}


int main(){

    int x,y; 
    x = 1; 
    y = 2;
    
    swap(&x, &y);
    printf("The variable x contains: %d\n", x); 
    printf("The variable y contains: %d\n", y); 

}
```

    The variable x contains: 2
    The variable y contains: 1


### Address Arithmetic

In its most basic form, address arithmetic allows you to define a pointer to a particular location in memory and then increment that pointer to arrive at neighboring memory locations. This is especially useful if you want to allocate a block of memory addresses for storage. In the code below, we will allocate a block of memory allocbuf that will fit ALLOCSIZE characters. The user can then call the function alloc() to allocate chunks of allocbuf for their storage needs.   


```c
#define ALLOCSIZE 10000

static char allocbuf[ALLOCSIZE]; /* array of characters */
static char *allocp = &allocbuf[0]; /* initialize pointer to start of allocbuf */

char *alloc(int n){
    
    if(allocbuf + ALLOCSIZE - allocp >= n){ /* check if n chars will fit */
        allocp += n;
        return allocp - n; 
        
    } else {
    
        return 0; /* signal that there is no space */
    }

}

void afree(char *p){
    
    if (p >= allocbuf && p < allocbuf + ALLOCSIZE){
        
        allocp = p;
    
    }

}
```

Notice the alloc() checks first to see if n characters will fit in allocbuf. If their request can be fulfilled, n is added to the pointer allocp and allocp - n is returned so the user has the starting point for their block of memory. Recall that allocp is a global variable so successive calls to alloc() will affect allocp permanently. Finally, afree() can be used to free memory beyond a memory location p. It does this by simply reassigning the pointer allocp to the memory location beyond which memory should be freed. These functions are implemented in the standard library (but more robustly) as malloc() and free().
