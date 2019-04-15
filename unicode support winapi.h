/*
Returns 1 if unicode is supported
0 otherwise
*/

#include <windows.h>

#ifndef UNICODE
    #define SUPPORT 1
#else
    #define SUPPORT 0
#endif