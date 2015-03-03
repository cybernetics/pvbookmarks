

.. index::
   pair: endianness; ntohs


=================================
Endianness Code Project tutorial
=================================

.. seealso:: http://www.codeproject.com/Articles/4804/Basic-concepts-on-Endianness


.. contents::
   :depth: 3

How to switch from one format to the other ?
=============================================

It is very easy to reverse a multi-byte number if you need the other format, it
is simply a matter of swapping bytes and the conversion is the same in both
directions.

The following example shows how an Endian conversion function could be
implemented using simple C unions::


    unsigned long ByteSwap1 (unsigned long nLongNumber)
    {
       union u {unsigned long vi; unsigned char c[sizeof(unsigned long)];};
       union v {unsigned long ni; unsigned char d[sizeof(unsigned long)];};
       union u un;
       union v vn;
       un.vi = nLongNumber;
       vn.d[0]=un.c[3];
       vn.d[1]=un.c[2];
       vn.d[2]=un.c[1];
       vn.d[3]=un.c[0];
       return (vn.ni);
    }

Note that this function is intented to work with 32-bit integers.

A more efficient function can be implemented using bitwise operations as shown
below::


    unsigned long ByteSwap2 (unsigned long nLongNumber)
    {
       return (((nLongNumber&0x000000FF)<<24)
              +((nLongNumber&0x0000FF00)<<8)
              +((nLongNumber&0x00FF0000)>>8)
              +((nLongNumber&0xFF000000)>>24));
    }


And this is a version in assembly language::


    unsigned long ByteSwap3 (unsigned long nLongNumber)
    {
       unsigned long nRetNumber ;

       __asm
       {
          mov eax, nLongNumber
          xchg ah, al
          ror eax, 16
          xchg ah, al
          mov nRetNumber, eax
       }

       return nRetNumber;
    }

A 16-bit version of a byte swap function is really straightforward::

    unsigned short ByteSwap4 (unsigned short nValue)
    {
       return (((nValue>> 8)) | (nValue << 8));

    }


Finally, we can write a more general function that can deal with any atomic
data type (e.g. int, float, double, etc) with automatic size detection::


    #include <algorithm> //required for std::swap

    #define ByteSwap5(x) ByteSwap((unsigned char *) &x,sizeof(x))

    void ByteSwap(unsigned char * b, int n)
    {
       register int i = 0;
       register int j = n-1;
       while (i<j)
       {
          std::swap(b[i], b[j]);
          i++, j--;
       }
    }


For example, the next code snippet shows how to convert a data array of doubles
from one format (e.g. Big-Endian) to the other (e.g. Little-Endian)::

    double* dArray; //array in big-endian format
    int n; //Number of elements

    for (register int i = 0; i <n; i++)
       ByteSwap5(dArray[i]);


Actually, in most cases, you won't need to implement any of the above functions
since there are a set of socket functions (see Table I), declared in winsock2.h,
which are defined for TCP/IP, so all machines that support TCP/IP networking
have them available.

**They store the data in 'network byte order' which is standard and endianness
independent**.

=========  ===================================================================================================
Function   Explaination
=========  ===================================================================================================
ntohs      Convert a 16-bit quantity from network byte order to host byte order (Big-Endian to Little-Endian)
ntohl      Convert a 32-bit quantity from network byte order to host byte order (Big-Endian to Little-Endian)
htons      Convert a 16-bit quantity from host byte order to network byte order (Little-Endian to Big-Endian)
htonl      Convert a 32-bit quantity from host byte order to network byte order (Little-Endian to Big-Endian)
=========  ===================================================================================================


Suppose your machine uses Little Endian order. To transmit the 32-bit value
0x0a0b0c0d over a TCP/IP connection, you have to call htonl() and transmit the
result::

    TransmitNum(htonl(0x0a0b0c0d));



Likewise, to convert an incoming 32-bit value, use ntohl():
Collapse | Copy Code

int n = ntohl(GetNumberFromNetwork());

If the processor on which the TCP/IP stack is to be run is itself also Big-Endian,
each of the four macros (i.e. ntohs, ntohl, htons, htonl) will be defined to do
nothing and there will be no run-time performance impact.

If, however, the processor is Little-Endian, the macros will reorder the bytes
appropriately. These macros are routinely called when building and parsing
network packets and when socket connections are created.

Serious run-time performance penalties occur when using TCP/IP on a Little-Endian
processor. For that reason, it may be unwise to select a Little-Endian processor
for use in a device, such as a router or gateway, with an abundance of network
functionality..

One additional problem with the host-to-network APIs is that they are unable
to manipulate 64-bit data elements.

However, you can write your own ntohll() and htonll() corresponding functions::

- ntohll: converts a 64-bit integer to host byte order.
- ntonll: converts a 64-bit integer to network byte order.

The implementation is simple enough::


    #define ntohll(x) (((_int64)(ntohl((int)((x << 32) >> 32))) << 32) |
                         (unsigned int)ntohl(((int)(x >> 32)))) //By Runner
    #define htonll(x) ntohll(x)


How to dynamically test for the Endian type at run time ?
=========================================================

As explained in Computer Animation FAQ, you can use the following function to
see if your code is running on a Little- or Big-Endian system::


    #define BIG_ENDIAN      0
    #define LITTLE_ENDIAN   1

    int TestByteOrder()
    {
       short int word = 0x0001;
       char *byte = (char *) &word;
       return(byte[0] ? LITTLE_ENDIAN : BIG_ENDIAN);
    }

This code assigns the value 0001h to a 16-bit integer. A char pointer is then
assigned to point at the first (least-significant) byte of the integer value.

If the first byte of the integer is 0x01h, then the system is Little-Endian
(the 0x01h is in the lowest, or least-significant, address).

If it is 0x00h then the system is Big-Endian.

Similarly::

    bool IsBigEndian()
    {
       short word = 0x4321;
       if((*(char *)& word) != 0x21 )
         return true;
       else
         return false;
    }



which is just the reverse of the same coin.

You can also use the standard byte order API’s to determine the byte-order of a
system at run-time. For example::

    bool IsBigEndian() { return( htonl(1)==1 ); }



