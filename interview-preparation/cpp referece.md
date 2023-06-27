# cpp referece

### **NOTES**

- By default things are passed by value in cpp not reference, use pointer of object to pass by reference

### **`new`**

returns **`pointer`** to newly created object. 

```cpp
class Node {
	public:
		int startTime;
		int endTime;

	public:
		Node(int start, int end) {
			startTime = start;
			endTime = end;
		}
};

Node n1 = new Node(1,2); // compilation error as ***new*** return ***Node **** not ***Node***
Node *n2 = new Node; // compilation error as default contructor (***Node()***) is not defined.
Node n3 = *(new Node(1,2)); // this will work fine

Node *nArray[] = { new Node(1,2), new Node(2,3) }; // initialize array of 2 Node
cout<<nArray[0]->startTime<<endl;
cout<<nArray[1]->startTime<<endl;

```

### **`array`**

```cpp
// creates an array of five int values, each initialized with a value of zero
int freqMap [5] = {};
int foo [5] = { 16, 2, 77, 40, 12071 };

// array length
sizeof(freqMap) / sizeof(int)
```

### [#include \<cstdlib\>](https://cplusplus.com/reference/cstdlib/)

This header defines several general purpose functions, including dynamic memory management, random number generation, communication with the environment, integer arithmetics, searching, sorting and converting.

- `int abs (int n);`

### [#include \<algorithm\>](https://cplusplus.com/reference/algorithm/)

- `fill_n`
    
    ```cpp
    void fill_n (OutputIterator first, Size n, const T& val);
    vector<int> myvector (8,10);        // myvector: 10 10 10 10 10 10 10 10
    fill_n (myvector.begin(),4,20);     // myvector: 20 20 20 20 10 10 10 10
    fill_n (myvector.begin()+3,3,33);   // myvector: 20 20 20 33 33 33 10 10
    ```
    
- `max`
    
    ```cpp
    template <class T> const T& max (const T& a, const T& b);
    template <class T, class Compare>
      const T& max (const T& a, const T& b, Compare comp);
    
    template <class T> const T& max (const T& a, const T& b) {
      return (a<b)?b:a;     // or: return comp(a,b)?b:a; for version (2)
    }
    ```
    
    a, b
        Values to compare.
    comp
        Binary function that accepts two values of type T as arguments, and returns a value convertible to bool. The value returned indicates whether the element passed as first argument is considered less than the second.
        The function shall not modify any of its arguments.
        This can either be a function pointer or a function object.
    
- `sort`
    
    ```cpp
    void sort (RandomAccessIterator first, RandomAccessIterator last);
    void sort (RandomAccessIterator first, RandomAccessIterator last, Compare comp);
    
    first, last
        Random-access iterators to the initial and final positions of the 
    		sequence to be sorted. The range used is [first,last), which contains 
    		all the elements between first and last, including the element pointed 
    		by first but not the element pointed by last.
    
    comp
    		The value returned indicates whether the element passed as first 
    		argument is considered to go before the second
    
    bool myfunction (int i,int j) { return (i<j); }
    
    int myints[] = {32,71,12,45,26,80,53,33};
    vector<int> myvector (myints, myints+8);               // 32 71 12 45 26 80 53 33
    
    // using default comparison (operator <):
    sort (myvector.begin(), myvector.begin()+4);           //(12 32 45 71)26 80 53 33
    
    // using function as comp
    sort (myvector.begin()+4, myvector.end(), myfunction); // 12 32 45 71(26 33 53 80)
    
    // using object as comp
    sort (myvector.begin(), myvector.end(), myobject);     //(12 26 32 33 45 53 71 80)
    ```
    
- `min`
    
    ```cpp
    template <class T> const T& min (const T& a, const T& b);
    template <class T, class Compare>
      const T& min (const T& a, const T& b, Compare comp);
    ```
    
    a, b
        Values to compare.
    comp
        Binary function that accepts two values of type T as arguments, and returns a value convertible to bool. The value returned indicates whether the element passed as first argument is considered less than the second.
        The function shall not modify any of its arguments.
        This can either be a function pointer or a function object.
    
- `reverse`
    
    ```cpp
    template <class BidirectionalIterator>
      void reverse (BidirectionalIterator first, BidirectionalIterator last);
    ```
    
    Reverses the order of the elements in the range `[first,last)`
    

### **`#include <iostream> // std::cout`**

### **`#include <vector>`**

- `constructor`
    
    ```cpp
    vector<int> first;                                // empty vector of ints
    vector<int> second (4,100);                       // four ints with value 100
    vector<int> third (second.begin(),second.end());  // iterating through second
    vector<int> fourth (third);                       // a copy of third
    
    // the iterator constructor can also be used to construct from arrays:
    int myints[] = {16,2,77,29};
    vector<int> fifth (myints, myints + sizeof(myints) / sizeof(int) );
    ```
    
- `Iterators`
    
    ```cpp
    **begin** - Returns an iterator pointing to the first element in the vector.
    **end** - Returns an iterator pointing to the past-the-end element in the vector.
    **rbegin**
    **rend**
    
    // it **cannot be used to modify the contents** it points to, even if the vector object is not itself const.
    **cbegin**
    **cend** 
    **crbegin**
    **crend**
    
    //example
    for (auto it = myvector.cbegin(); it != myvector.cend(); ++it)
        std::cout << ' ' << ***it**;
    ```
    
- `push_back(element)`
- `pop_back(element)`
- `size()`
- `back()` - reference to last element
- `front()` - reference to front element
- `clear()`
- `empty()`

### **`#include <string> // std::string`**

- `a.compare(b)`
    - 0 => a and b are equal
    - <0 => Either the value of the first character that does not match is lower in the *`a`*, or all compared characters match but the *`a`* is shorter.
    - >0 => Either the value of the first character that does not match is greater in the *`a`*, or all compared characters match but the *`a`* is longer.
- `substr (size_t pos = 0, size_t len = npos) const;`
    
    If len is not provided then it indicates all characters until the end of the string.
    
- `size_t size() const;`

### `#include <utility> // std::pair`

- `**pair**`
    - `contructor`
        
        ```cpp
        // pair::pair example
        #include <utility>      // std::pair, std::make_pair
        #include <string>       // std::string
        #include <iostream>     // std::cout
        using namespace std
        
        int main () {
          std::pair <string,double> product1;                     // default constructor
          std::pair <string,double> product2 ("tomatoes",2.30);   // value init
          std::pair <string,double> product3 (product2);          // copy constructor
        
          product1 = make_pair<string,double>("lightbulbs",0.99);   // using make_pair (move)
        
          product2.first = "shoes";                  // the type of first is string
          product2.second = 39.90;                   // the type of second is double
        
          std::cout << "The price of " << product1.first << " is $" << product1.second << '\n';
          std::cout << "The price of " << product2.first << " is $" << product2.second << '\n';
          std::cout << "The price of " << product3.first << " is $" << product3.second << '\n';
          return 0;
        }
        ```
        
    - `swap(pair pr)` - Exchanges the contents of the [pair](https://www.cplusplus.com/pair) object with the contents of pr.
- `**make_pair(``T1 x, T2 y)`**
    
    A [pair](https://www.cplusplus.com/pair) object whose elements first and second are set to x and y respectively.
    

### [#include \<stack\>](https://cplusplus.com/reference/stack/stack/) // std::stack

- **[`constructor`](https://cplusplus.com/reference/stack/stack/stack/)** Construct stack (public member function)
    
    ```cpp
    // constructing stacks
    #include <iostream>       // std::cout
    #include <stack>          // std::stack
    #include <vector>         // std::vector
    #include <deque>          // std::deque
    
    int main ()
    {
      std::deque<int> mydeque (3,100);          // deque with 3 elements
      std::vector<int> myvector (2,200);        // vector with 2 elements
    
      std::stack<int> first;                    // empty stack
      std::stack<int> second (mydeque);         // stack initialized to copy of deque
    
      std::stack<int,std::vector<int> > third;  // empty stack using vector
      std::stack<int,std::vector<int> > fourth (myvector);
    
      std::cout << "size of first: " << first.size() << '\n';
      std::cout << "size of second: " << second.size() << '\n';
      std::cout << "size of third: " << third.size() << '\n';
      std::cout << "size of fourth: " << fourth.size() << '\n';
    
      return 0;
    }
    ```
    
- **[`empty`](https://cplusplus.com/reference/stack/stack/empty/)** Test whether container is empty (public member function)
- **[`size`](https://cplusplus.com/reference/stack/stack/size/)** Return size (public member function)
- **[`top`](https://cplusplus.com/reference/stack/stack/top/)** Access next element (public member function)
- **[`push`](https://cplusplus.com/reference/stack/stack/push/)** Insert element (public member function)
- **[`emplace`](https://cplusplus.com/reference/stack/stack/emplace/)** Construct and insert element (public member function)
- **[`pop`](https://cplusplus.com/reference/stack/stack/pop/)** Remove top element (public member function)
- **[`swap`](https://cplusplus.com/reference/stack/stack/swap/)** Swap contents (public member function)

### **`#include <queue> // std::queue`**

- `queue<int *> myqueue`
    
    ```cpp
    // constructing queues
    #include <iostream>       // std::cout
    #include <deque>          // std::deque
    #include <list>           // std::list
    #include <queue>          // std::queue
    
    int main ()
    {
      std::deque<int> mydeck (3,100);        // deque with 3 elements
      std::list<int> mylist (2,200);         // list with 2 elements
    
      std::queue<int> first;                 // empty queue
      std::queue<int> second (mydeck);       // queue initialized to copy of deque
    
      std::queue<int,std::list<int> > third; // empty queue with list as underlying container
      std::queue<int,std::list<int> > fourth (mylist);
    
      std::cout << "size of first: " << first.size() << '\n';
      std::cout << "size of second: " << second.size() << '\n';
      std::cout << "size of third: " << third.size() << '\n';
      std::cout << "size of fourth: " << fourth.size() << '\n';
    
      return 0;
    }
    ```
    
- `empty()`
- `push(Element e)`
- `pop()`
- `**front()**`
- `back()`
- `size()`

### `priority_queue`

- `constructor`
    
    By default priority_queue is **`maxHeap`**.
    
    ```cpp
    typedef mytype;
    
    class minHeapC*omparison* {
        public:
            bool operator()(mytype a, mytype b) {
                if(a.compare(b)>0)
                    return true;
                return false;
            }
    };
    
    // minHeapC*omparison(a,b)* -> if this return true meaning, b has more  priority than a
    priority_queue <mytype, vector<mytype>, minHeapC*omparison*> pq;
    ```
    
- `push(Element e)`
- **`top()`** - Returns a constant reference to the *top element* in the [priority_queue](https://www.cplusplus.com/priority_queue).
- `pop()`
- `size()`
- `empty()`

### **`#include <list> // std::list`**

- **[`(constructor)`](https://cplusplus.com/reference/list/list/list/)** Construct list (public member function)
    
    ```cpp
    // constructing lists
    #include <iostream>
    #include <list>
    
    int main ()
    {
      // constructors used in the same order as described above:
      std::list<int> first;                                // empty list of ints
      std::list<int> second (4,100);                       // four ints with value 100
      std::list<int> third (second.begin(),second.end());  // iterating through second
      std::list<int> fourth (third);                       // a copy of third
    
      // the iterator constructor can also be used to construct from arrays:
      int myints[] = {16,2,77,29};
      std::list<int> fifth (myints, myints + sizeof(myints) / sizeof(int) );
    
      std::cout << "The contents of fifth are: ";
      for (std::list<int>::iterator it = fifth.begin(); it != fifth.end(); it++)
        std::cout << *it << ' ';
    
      std::cout << '\n';
    
      return 0;
    }
    ```
    

### **`#include <deque> // std::deque`**

### `#include <climits>`

| name | expresses | possible value* |
| --- | --- | --- |
| CHAR_BIT | Number of bits in a char object (byte) | 8 or greater* |
| SCHAR_MIN | Minimum value for an object of type signed char | -127 (-27+1) or less* |
| SCHAR_MAX | Maximum value for an object of type signed char | 127 (27-1) or greater* |
| UCHAR_MAX | Maximum value for an object of type unsigned char | 255 (28-1) or greater* |
| CHAR_MIN | Minimum value for an object of type char | either SCHAR_MIN or 0 |
| CHAR_MAX | Maximum value for an object of type char | either SCHAR_MAX or UCHAR_MAX |
| MB_LEN_MAX | Maximum number of bytes in a multibyte character, for any locale | 1 or greater* |
| SHRT_MIN | Minimum value for an object of type short int | -32767 (-215+1) or less* |
| SHRT_MAX | Maximum value for an object of type short int | 32767 (215-1) or greater* |
| USHRT_MAX | Maximum value for an object of type unsigned short int | 65535 (216-1) or greater* |
| INT_MIN | Minimum value for an object of type int | -32767 (-215+1) or less* |
| INT_MAX | Maximum value for an object of type int | 32767 (215-1) or greater* |
| UINT_MAX | Maximum value for an object of type unsigned int | 65535 (216-1) or greater* |
| LONG_MIN | Minimum value for an object of type long int | -2147483647 (-231+1) or less* |
| LONG_MAX | Maximum value for an object of type long int | 2147483647 (231-1) or greater* |
| ULONG_MAX | Maximum value for an object of type unsigned long int | 4294967295 (232-1) or greater* |
| LLONG_MIN | Minimum value for an object of type long long int | -9223372036854775807 (-263+1) or less* |
| LLONG_MAX | Maximum value for an object of type long long int | 9223372036854775807 (263-1) or greater* |
| ULLONG_MAX | Maximum value for an object of type unsigned long long int | 18446744073709551615 (264-1) or greater* |

### `#include <unordered_map>`

- `constructor`
    
    ```cpp
    unordered_map<string,string> stringmap; // empty
    unordered_map<string,string> second ( {{"apple","red"},{"lemon","yellow"}} );       // init list
    unordered_map<string,string> third ( {{"orange","orange"},{"strawberry","red"}} );  // init list
    unordered_map<string,string> fourth (second);                    // copy
    unordered_map<string,string> sixth (fourth.begin(),fourth.end());  // range
    ```
    
- `**operator[]**`
    
    If *k* does not match the key of any element in the container, the function inserts a new element with that key and returns a reference to its mapped value. Notice that this always increases the [container size](https://www.cplusplus.com/unordered_map::size) by one, even if no mapped value is assigned to the element (the element is constructed using its default constructor).
    
- `insert ( const value_type& val );`
    
    Each element is inserted only if its key is not equivalent to the key of any other element already in the container
    
    ```cpp
    unordered_map<string,double> myrecipe;
    unordered_map<string,double> mypantry = {{"milk",2.0},{"flour",1.5}};
    pair<string,double> myshopping ("baking powder",0.3);
    
    myrecipe.insert (myshopping);                        // copy insertion
    myrecipe.insert (make_pair<string,double>("eggs",6.0)); // move insertion
    myrecipe.insert (mypantry.begin(), mypantry.end());  // range insertion
    myrecipe.insert ( {{"sugar",0.8},{"salt",0.1}} );    // initializer list insertion
    ```
    
- `end()`
- `find(key)` - return `iterator`
    
    An iterator to the element, if the specified key value is found, or [unordered_map::end](https://www.cplusplus.com/unordered_map::end) if the specified key is not found in the container.
    
    ```cpp
    int main ()
    {
      std::unordered_map<std::string,double> mymap = {
         {"mom",5.4},
         {"dad",6.1},
         {"bro",5.9} };
    
      std::string input;
      std::cout << "who? ";
      getline (std::cin,input);
    
      std::unordered_map<std::string,double>::const_iterator got = mymap.find (input);
    
      if ( got == mymap.end() )
        std::cout << "not found";
      else
        std::cout << got->first << " is " << got->second;
    
      std::cout << std::endl;
    
      return 0;
    }
    
    	
    Edit & Run
    
    // Possible output:
    // who? dad
    // dad is 6.1
    ```
    
- `size()`
- `erase()`
- **Unordered map with custom key (struct, class)**
    
    ```cpp
    // struct or class to be used as key
    struct Tuple {
        pair<string, string> key;
    
    		// custom comparator
        bool **operator==**(const Tuple& p) const
        {
            return key.first.compare(p.key.first)==0 && key.second.compare(p.key.second)==0;
        }
       
        Tuple(string a, string b) {
            key = make_pair(a,b);
        }
    };
    
    // Hasher function object. A hasher is a function that returns 
    // an integral value based on the container object key passed to 
    // it as argument.
    // Member type hasher is defined in unordered_map as an alias of 
    // its **third template parameter** (Hash).
    class MyHashFunction {
    public:
     
        size_t **operator()**(const Tuple& p) const
        {
            return p.key.first.size() + p.key.second.size();
        }
    };
    
    typedef unordered_map<Tuple, int, MyHashFunction> custom_map;
    ```
    

### `#include <unordered_set>`