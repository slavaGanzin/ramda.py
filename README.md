# ramda.py

[![PyPI version](https://badge.fury.io/py/ramda.svg)](https://badge.fury.io/py/ramda)
[![Build Status](https://travis-ci.com/slavaGanzin/ramda.py.svg?branch=master)](https://travis-ci.com/slavaGanzin/ramda.py) [![Coverage Status](https://coveralls.io/repos/github/slavaGanzin/ramda.py/badge.svg?branch=master)](https://coveralls.io/github/slavaGanzin/ramda.py?branch=master)

Python Clone of [Ramda.js](http://ramdajs.com)

Improved fork of [Jack Firth's original impementation](https://github.com/jackfirth/pyramda)

```sh
pip install ramda
```

```python
>>> from ramda import *
>>> inc(1)
2
>>> map(inc, [1, 2, 3])
[2, 3, 4]
>>> incEach = map(inc)
>>> incEach([1, 2, 3])
[2, 3, 4]
```


















#Docs
```python
T(*args)
    """A function that always returns true. Any passed in parameters are ignored"""

add(x, y)
    """Adds two values"""

adjust(f, i, xs)
    """Applies a function to the value at the given index of an array, returning a
new copy of the array with the element at the given index replaced with the
result of the function application"""

all(p, xs)
    """Returns true if all elements of the list match the predicate, false if
there are any that don't.
Dispatches to the all method of the second argument, if present.
Acts as a transducer if a transformer is given in list position"""

all_pass(ps, v)
    """Takes a list of predicates and returns a predicate that returns true for a
given list of arguments if every one of the provided predicates is satisfied
by those arguments.
The function returned is a curried function whose arity matches that of the
highest-arity predicate"""

always(x, y)
    """Returns a function that always returns the given value. Note that for
non-primitives the value returned is a reference to the original value.
This function is known as const, constant, or K (for K combinator) in
other languages and libraries"""

any(p, xs)
    """Returns true if at least one of elements of the list match the predicate,
false otherwise.
Dispatches to the any method of the second argument, if present.
Acts as a transducer if a transformer is given in list position"""

any_pass(ps, v)
    """Takes a list of predicates and returns a predicate that returns true for a
given list of arguments if at least one of the provided predicates is
satisfied by those arguments.
The function returned is a curried function whose arity matches that of the
highest-arity predicate"""

ap(fs, xs)
    """ap applies a list of functions to a list of values.
Dispatches to the ap method of the second argument, if present. Also
treats curried functions as applicatives"""

aperture(n, xs)
    """Returns a new list, composed of n-tuples of consecutive elements. If n is
greater than the length of the list, an empty list is returned.
Acts as a transducer if a transformer is given in list position"""

append(x, ys)
    """Returns a new list containing the contents of the given list, followed by
the given element"""

apply(f, xs)
    """Applies function fn to the argument list args. This is useful for
creating a fixed-arity function from a variadic function. fn should be a
bound function if context is significant"""

apply_spec(spec)
    """Given a spec object recursively mapping properties to functions, creates a
function producing an object of the same structure, by mapping each property
to the result of calling its associated function with the supplied arguments"""

apply_to(x, f)
    """Takes a value and applies a function to it.
This function is also known as the thrush combinator"""

ascend(predicate)
    """Makes an ascending comparator function out of a function that returns a value
that can be compared with < and >"""

assoc(key, value, object)
    """Makes a shallow clone of an object, setting or overriding the specified
property with the given value. Note that this copies and flattens prototype
properties onto the new object as well. All non-primitive properties are
copied by reference"""

assoc_path(path, value, object)
    """Makes a shallow clone of an object, setting or overriding the nodes required
to create the given path, and placing the specific value at the tail end of
that path. Note that this copies and flattens prototype properties onto the
new object as well. All non-primitive properties are copied by reference"""

binary(f)
    """Wraps a function of any arity (including nullary) in a function that accepts
exactly 2 parameters. Any extraneous parameters will not be passed to the
supplied function"""

bind(f, o)
    """Creates a function that is bound to a context.
Note: R.bind does not provide the additional argument-binding capabilities of
Function.prototype.bind"""

both(p1, p2, v)
    """A function which calls the two provided functions and returns the &&
of the results.
It returns the result of the first function if it is false-y and the result
of the second function otherwise. Note that this is short-circuited,
meaning that the second function will not be invoked if the first returns a
false-y value.
In addition to functions, R.both also accepts any fantasy-land compatible
applicative functor"""

call(f, *args)
    """Returns the result of calling its first argument with the remaining
arguments. This is occasionally useful as a converging function for
R.converge: the first branch can produce a function while the
remaining branches produce values to be passed to that function as its
arguments"""

chain(f, xs)
    """chain maps a function over a list and concatenates the results. chain
is also known as flatMap in some libraries
Dispatches to the chain method of the second argument, if present,
according to the FantasyLand Chain spec"""

clamp(min, max, value)
    """Restricts a number to be within a range.
Also works for other ordered types such as Strings and Dates"""

clone(v)
    """Creates a deep copy of the value which may contain (nested) Arrays and
Objects, Numbers, Strings, Booleans and Dates. Functions are
assigned by reference rather than copied
Dispatches to a clone method if present"""

comparator(predicate)
    """Makes a comparator function out of a function that reports whether the first
element is less than the second"""

complement(f)
    """Takes a function f and returns a function g such that if called with the same arguments
when f returns a "truthy" value, g returns false and when f returns a "falsy" value g returns true.
R.complement may be applied to any functor"""

compose(*funcs)
    """Performs right-to-left function composition. The rightmost function may have
any arity; the remaining functions must be unary.
Note: The result of compose is not automatically curried"""

concat(xs, ys)
    """Returns the result of concatenating the given lists or strings.
Note: R.concat expects both arguments to be of the same type,
unlike the native Array.prototype.concat method. It will throw
an error if you concat an Array with a non-Array value.
Dispatches to the concat method of the first argument, if present.
Can also concatenate two members of a fantasy-land
compatible semigroup"""

cond(conditions, value)
    """Returns a function, fn, which encapsulates if/else, if/else, ... logic.
R.cond takes a list of [predicate, transformer] pairs. All of the arguments
to fn are applied to each of the predicates in turn until one returns a
"truthy" value, at which point fn returns the result of applying its
arguments to the corresponding transformer. If none of the predicates
matches, fn returns undefined"""

contains(y, xs)
    """Returns true if the specified value is equal, in R.equals
terms, to at least one element of the given list; false otherwise"""

converge(converging, branches, args)
    """Accepts a converging function and a list of branching functions and returns
a new function. When invoked, this new function is applied to some
arguments, each branching function is applied to those same arguments. The
results of each branching function are passed as arguments to the converging
function to produce the return value"""

count_by(function, list)
    """Counts the elements of a list according to how many match each value of a
key generated by the supplied function. Returns an object mapping the keys
produced by fn to the number of occurrences in the list. Note that all
keys are coerced to strings because of how JavaScript objects work.
Acts as a transducer if a transformer is given in list position"""

curry_by_spec(curry_spec, f)
    """Returns a curried equivalent of the provided function. The curried function
has two unusual capabilities. First, its arguments needn't be provided one
at a time. If f is a ternary function and g is R.curry(f), the
following are equivalent:
g(1)(2)(3)
g(1)(2, 3)
g(1, 2)(3)
g(1, 2, 3)
Secondly, the special placeholder value R.__ may be used to specify
"gaps", allowing partial application of any combination of arguments,
regardless of their positions. If g is as above and _ is R.__,
the following are equivalent:
g(1, 2, 3)
g(_, 2, 3)(1)
g(_, _, 3)(1)(2)
g(_, _, 3)(1, 2)
g(_, 2)(1)(3)
g(_, 2)(1, 3)
g(_, 2)(_, 3)(1)"""

curry_n(n, f)
    """Returns a curried equivalent of the provided function, with the specified
arity. The curried function has two unusual capabilities. First, its
arguments needn't be provided one at a time. If g is R.curryN(3, f), the
following are equivalent:
g(1)(2)(3)
g(1)(2, 3)
g(1, 2)(3)
g(1, 2, 3)
Secondly, the special placeholder value R.__ may be used to specify
"gaps", allowing partial application of any combination of arguments,
regardless of their positions. If g is as above and _ is R.__,
the following are equivalent:
g(1, 2, 3)
g(_, 2, 3)(1)
g(_, _, 3)(1)(2)
g(_, _, 3)(1, 2)
g(_, 2)(1)(3)
g(_, 2)(1, 3)
g(_, 2)(_, 3)(1)"""

dec(x)
    """Decrements its argument"""

default_to(default, x)
    """Returns the second argument if it is not null, undefined or NaN;
otherwise the first argument is returned"""

descend(predicate)
    """Makes a descending comparator function out of a function that returns a value
that can be compared with < and >"""

difference(xs, ys)
    """Finds the set (i.e. no duplicates) of all elements in the first list not
contained in the second list. Objects and Arrays are compared in terms of
value equality, not reference equality"""

difference_with(f, xs, ys)
    """Finds the set (i.e. no duplicates) of all elements in the first list not
contained in the second list. Duplication is determined according to the
value returned by applying the supplied predicate to two list elements"""

dissoc(key, object)
    """Returns a new object that does not contain a prop property"""

dissoc_path(path, object)
    """Makes a shallow clone of an object, omitting the property at the given path.
Note that this copies and flattens prototype properties onto the new object
as well. All non-primitive properties are copied by reference"""

divide(x, y)
    """Divides two numbers. Equivalent to a / b"""

drop(n, xs)
    """Returns all but the first n elements of the given list, string, or
transducer/transformer (or object with a drop method).
Dispatches to the drop method of the second argument, if present"""

drop_last(n, xs)
    """Returns a list containing all but the last n elements of the given list"""

drop_last_while(predicate, xs)
    """Returns a new list excluding all the tailing elements of a given list which
satisfy the supplied predicate function. It passes each value from the right
to the supplied predicate function, skipping elements until the predicate
function returns a falsy value. The predicate function is applied to one argument:
(value)"""

None
    """Returns a new list without any consecutively repeating elements.
R.equals is used to determine equality.
Acts as a transducer if a transformer is given in list position"""

drop_repeats_with(f, xs)
    """Returns a new list without any consecutively repeating elements. Equality is
determined by applying the supplied predicate to each pair of consecutive elements. The
first element in a series of equal elements will be preserved.
Acts as a transducer if a transformer is given in list position"""

drop_while(predicate, xs)
    """Returns a new list excluding the leading elements of a given list which
satisfy the supplied predicate function. It passes each value to the supplied
predicate function, skipping elements while the predicate function returns
true. The predicate function is applied to one argument: (value).
Dispatches to the dropWhile method of the second argument, if present.
Acts as a transducer if a transformer is given in list position"""

either(predicate1, predicate2, value)
    """A function wrapping calls to the two functions in an || operation,
returning the result of the first function if it is truth-y and the result
of the second function otherwise. Note that this is short-circuited,
meaning that the second function will not be invoked if the first returns a
truth-y value.
In addition to functions, R.either also accepts any fantasy-land compatible
applicative functor"""

empty(x)
    """Returns the empty value of its argument's type. Ramda defines the empty
value of Array ([]), Object ({}), String (''), and Arguments. Other
types are supported if they define <Type>.empty,
<Type>.prototype.empty or implement the
FantasyLand Monoid spec.
Dispatches to the empty method of the first argument, if present"""

ends_with(needle, haystack)
    """Checks if a list ends with the provided values"""

eq_by(predicate, a, b)
    """Takes a function and two values in its domain and returns true if the
values map to the same value in the codomain; false otherwise"""

eq_props(prop, object1, object2)
    """Reports whether two objects have the same value, in R.equals
terms, for the specified property. Useful as a curried predicate"""

equals(x, y)
    """Returns true if its arguments are equivalent, false otherwise. Handles
cyclical data structures.
Dispatches symmetrically to the equals methods of both arguments, if
present"""

evolve(transformations, object)
    """Creates a new object by recursively evolving a shallow copy of object,
according to the transformation functions. All non-primitive properties
are copied by reference.
A transformation function will not be invoked if its corresponding key
does not exist in the evolved object"""

filter(p, xs)
    """Takes a predicate and a Filterable, and returns a new filterable of the
same type containing the members of the given filterable which satisfy the
given predicate. Filterable objects include plain objects or any object
that has a filter method such as Array.
Dispatches to the filter method of the second argument, if present.
Acts as a transducer if a transformer is given in list position"""

find(p, xs)
    """Returns the first element of the list which matches the predicate, or
undefined if no element matches.
Dispatches to the find method of the second argument, if present.
Acts as a transducer if a transformer is given in list position"""

find_index(p, xs)
    """Returns the index of the first element of the list which matches the
predicate, or -1 if no element matches.
Acts as a transducer if a transformer is given in list position"""

find_last(p, xs)
    """Returns the last element of the list which matches the predicate, or
undefined if no element matches.
Acts as a transducer if a transformer is given in list position"""

find_last_index(p, xs)
    """Returns the index of the last element of the list which matches the
predicate, or -1 if no element matches.
Acts as a transducer if a transformer is given in list position"""

flatten_until(is_leaf, xs)
    """Returns a new list by pulling every item out of it (and all its sub-arrays)
and putting them in a new array, depth-first"""

flip(f)
    """Returns a new function much like the supplied one, except that the first two
arguments' order is reversed"""

for_each(f, xs)
    """Iterate over an input list, calling a provided function fn for each
element in the list.
fn receives one argument: (value).
Note: R.forEach does not skip deleted or unassigned indices (sparse
arrays), unlike the native Array.prototype.forEach method. For more
details on this behavior, see:
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#Description
Also note that, unlike Array.prototype.forEach, Ramda's forEach returns
the original array. In some libraries this function is named each.
Dispatches to the forEach method of the second argument, if present"""

for_each_obj_indexed(f, xs)
    """Iterate over an input object, calling a provided function fn for each
key and value in the object.
fn receives three argument: (value, key, obj)"""

from_pairs(pairs)
    """Creates a new object from a list key-value pairs. If a key appears in
multiple pairs, the rightmost pair is included in the object"""

group_by(f, xs)
    """Splits a list into sub-lists stored in an object, based on the result of
calling a String-returning function on each element, and grouping the
results according to values returned.
Dispatches to the groupBy method of the second argument, if present.
Acts as a transducer if a transformer is given in list position"""

group_with(predicate, xs)
    """Takes a list and returns a list of lists where each sublist's elements are
all satisfied pairwise comparison according to the provided function.
Only adjacent elements are passed to the comparison function"""

gt(y, x)
    """Returns true if the first argument is greater than the second; false
otherwise"""

gte(y, x)
    """Returns true if the first argument is greater than or equal to the second;
false otherwise"""

has(name, o)
    """Returns whether or not an object has an own property with the specified name"""

head(list)
    """Returns the first element of the given list or string. In some libraries
this function is named first"""

identical(x, y)
    """Returns true if its arguments are identical, false otherwise. Values are
identical if they reference the same memory. NaN is identical to NaN;
0 and -0 are not identical"""

identity(x)
    """A function that does nothing but return the parameter supplied to it. Good
as a default or placeholder function"""

if_else(predicate, on_true_func, on_false_func, value)
    """Creates a function that will process either the onTrue or the onFalse
function depending upon the result of the condition predicate"""

inc(x)
    """Increments its argument"""

index_by(f, xs)
    """Given a function that generates a key, turns a list of objects into an
object indexing the objects by the given key. Note that if multiple
objects generate the same value for the indexing key only the last value
will be included in the generated object.
Acts as a transducer if a transformer is given in list position"""

index_of(y, xs)
    """Returns the position of the first occurrence of an item in an array, or -1
if the item is not included in the array. R.equals is used to
determine equality"""

init(list)
    """Returns all but the last element of the given list or string"""

inner_join(predicate, xs, ys)
    """Takes a predicate pred, a list xs, and a list ys, and returns a list
xs' comprising each of the elements of xs which is equal to one or more
elements of ys according to pred.
pred must be a binary function expecting an element from each list.
xs, ys, and xs' are treated as sets, semantically, so ordering should
not be significant, but since xs' is ordered the implementation guarantees
that its values are in the same order as they appear in xs. Duplicates are
not removed, so xs' may contain duplicates if xs contains duplicates"""

insert(position, element, list)
    """Inserts the supplied element into the list, at the specified index. Note that
this is not destructive: it returns a copy of the list with the changes.
No lists have been harmed in the application of this function"""

insert_all(position, elements, list)
    """Inserts the sub-list into the list, at the specified index. Note that this is not
destructive: it returns a copy of the list with the changes.
No lists have been harmed in the application of this function"""

intersection(list1, list2)
    """Combines two lists into a set (i.e. no duplicates) composed of those
elements common to both lists"""

intersperse(separator, xs)
    """Creates a new list with the separator interposed between elements.
Dispatches to the intersperse method of the second argument, if present"""

invert(object)
    """Same as R.invertObj, however this accounts for objects with
duplicate values by putting the values into an array"""

invert_obj(object)
    """Returns a new object with the keys of the given object as values, and the
values of the given object, which are coerced to strings, as keys. Note
that the last key found is preferred when handling the same value"""

invoker(arity, f)
    """Turns a named method with a specified arity into a function that can be
called directly supplied with arguments and a target object.
The returned function is curried and accepts arity + 1 parameters where
the final parameter is the target object"""

is_empty(xs)
    """Returns true if the given value is its type's empty value; false
otherwise"""

is_nil(xs)
    """Checks if the input value is null or undefined"""

join(sep, xs)
    """Returns a string made by inserting the separator between each element and
concatenating all the elements into a single string"""

juxt(functions, *args)
    """juxt applies a list of functions to a list of values"""

keys(dict)
    """Returns a list containing the names of all the enumerable own properties of
the supplied object.
Note that the order of the output array is not guaranteed to be consistent
across different JS platforms"""

last(list)
    """Returns the last element of the given list or string"""

last_index_of(y, xs)
    """Returns the position of the last occurrence of an item in an array, or -1 if
the item is not included in the array. R.equals is used to
determine equality"""

length(x)
    """Returns the number of elements in the array by returning list.length"""

lt(y, x)
    """Returns true if the first argument is less than the second; false
otherwise"""

lte(y, x)
    """Returns true if the first argument is less than or equal to the second;
false otherwise"""

map(f, xs)
    """Takes a function and
a functor,
applies the function to each of the functor's values, and returns
a functor of the same shape.
Ramda provides suitable map implementations for Array and Object,
so this function may be applied to [1, 2, 3] or {x: 1, y: 2, z: 3}.
Dispatches to the map method of the second argument, if present.
Acts as a transducer if a transformer is given in list position.
Also treats functions as functors and will compose them together"""

map_accum(function, accumulator, list)
    """The mapAccum function behaves like a combination of map and reduce; it
applies a function to each element of a list, passing an accumulating
parameter from left to right, and returning a final value of this
accumulator together with the new list.
The iterator function receives two arguments, acc and value, and should
return a tuple [acc, value]"""

map_accum_right(function, accumulator, list)
    """The mapAccumRight function behaves like a combination of map and reduce; it
applies a function to each element of a list, passing an accumulating
parameter from right to left, and returning a final value of this
accumulator together with the new list.
Similar to mapAccum, except moves through the input list from
the right to the left.
The iterator function receives two arguments, value and acc, and should
return a tuple [value, acc]"""

map_obj_indexed(f, xs)
    """An Object-specific version of map. The function is applied to three
arguments: (value, key, obj). If only the value is significant, use
map instead"""

None
    """Tests a regular expression against a String. Note that this function will
return an empty array when there are no matches. This differs from
String.prototype.match
which returns null when there are no matches"""

max(x, y)
    """Returns the larger of its two arguments"""

max_by(f, x, y)
    """Takes a function and two values, and returns whichever value produces the
larger result when passed to the provided function"""

mean(xs)
    """Returns the mean of the given list of numbers"""

median(xs)
    """Returns the median of the given list of numbers"""

memoize(f)
    """Creates a new function that, when invoked, caches the result of calling fn
for a given argument set and returns the result. Subsequent calls to the
memoized fn with the same argument set will not result in an additional
call to fn; instead, the cached result for that set of arguments will be
returned"""

memoize_with(key_generator, f)
    """A customisable version of R.memoize. memoizeWith takes an
additional function that will be applied to a given argument set and used to
create the cache key under which the results of the function to be memoized
will be stored. Care must be taken when implementing key generation to avoid
clashes that may overwrite previous entries erroneously"""

merge(object1, object2)
    """Create a new object with the own properties of the first object merged with
the own properties of the second object. If a key exists in both objects,
the value from the second object will be used"""

merge_all(objects)
    """Merges a list of objects together into one object"""

merge_with(function, object1, object2)
    """Creates a new object with the own properties of the two provided objects. If
a key exists in both objects, the provided function is applied to the values
associated with the key in each object, with the result being used as the
value associated with the key in the returned object"""

merge_with_key(function, object1, object2)
    """Creates a new object with the own properties of the two provided objects. If
a key exists in both objects, the provided function is applied to the key
and the values associated with the key in each object, with the result being
used as the value associated with the key in the returned object"""

min(x, y)
    """Returns the smaller of its two arguments"""

min_by(f, x, y)
    """Takes a function and two values, and returns whichever value produces the
smaller result when passed to the provided function"""

modulo(x, y)
    """Divides the first parameter by the second and returns the remainder. Note
that this function preserves the JavaScript-style behavior for modulo. For
mathematical modulo see mathMod"""

multiply(x, y)
    """Multiplies two numbers. Equivalent to a * b but curried"""

n_ary(n, f)
    """Wraps a function of any arity (including nullary) in a function that accepts
exactly n parameters. Any extraneous parameters will not be passed to the
supplied function"""

negate(x)
    """Negates its argument"""

none(predicate, X)
    """Returns true if no elements of the list match the predicate, false
otherwise.
Dispatches to the any method of the second argument, if present"""

nth(n, xs)
    """Returns the nth element of the given list or string. If n is negative the
element at index length + n is returned"""

nth_arg(n)
    """Returns a function which returns its nth argument"""

obj_of(k, v)
    """Creates an object containing a single key:value pair"""

of(x)
    """Returns a singleton array containing the value provided.
Note this of is different from the ES6 of; See
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/of"""

omit(keys, dict)
    """Returns a partial copy of an object omitting the keys specified"""

once(f)
    """Accepts a function fn and returns a function that guards invocation of
fn such that fn can only ever be called once, no matter how many times
the returned function is invoked. The first value calculated is returned in
subsequent invocations"""

pair(first, second)
    """Takes two arguments, fst and snd, and returns [fst, snd]"""

partial(f, args)
    """Takes a function f and a list of arguments, and returns a function g.
When applied, g returns the result of applying f to the arguments
provided initially followed by the arguments provided to g"""

None
    """Takes a predicate and a list or other Filterable object and returns the
pair of filterable objects of the same type of elements which do and do not
satisfy, the predicate, respectively. Filterable objects include plain objects or any object
that has a filter method such as Array"""

path(keys, dict)
    """Retrieve the value at a given path"""

path_eq(path, equals_to, value)
    """Determines whether a nested path on an object has a specific value, in
R.equals terms. Most likely used to filter a list"""

path_or(default, path, value)
    """If the given, non-null object has a value at the given path, returns the
value at that path. Otherwise returns the provided default value"""

path_satisfies(predicate, path, value)
    """Returns true if the specified object property at given path satisfies the
given predicate; false otherwise"""

pick(keys, dict)
    """Returns a partial copy of an object containing only the keys specified. If
the key does not exist, the property is ignored"""

pick_all(keys, dict)
    """Similar to pick except that this one includes a key: undefined pair for
properties that don't exist"""

pick_by(f, dict)
    """Returns a partial copy of an object containing only the keys that satisfy
the supplied predicate"""

pipe(*funcs)
    """Performs left-to-right function composition. The leftmost function may have
any arity; the remaining functions must be unary.
In some libraries this function is named sequence.
Note: The result of pipe is not automatically curried"""

pluck(key, xs)
    """Returns a new list by plucking the same named property off all objects in
the list supplied.
pluck will work on
any functor in
addition to arrays, as it is equivalent to R.map(R.prop(k), f)"""

prepend(value, list)
    """Returns a new list with the given element at the front, followed by the
contents of the list"""

product(xs)
    """Multiplies together all the elements of a list"""

project(selectors, list)
    """Reasonable analog to SQL select statement"""

prop(name, o)
    """Returns a function that when supplied an object returns the indicated
property of that object, if it exists"""

prop_eq(property, value, object)
    """Returns true if the specified object property is equal, in
R.equals terms, to the given value; false otherwise.
You can test multiple properties with R.where"""

prop_is(type, property, value)
    """Returns true if the specified object property is of the given type;
false otherwise"""

prop_or(default, property, object)
    """If the given, non-null object has an own property with the specified name,
returns the value of that property. Otherwise returns the provided default
value"""

prop_satisfies(predicate, property, object)
    """Returns true if the specified object property satisfies the given
predicate; false otherwise. You can test multiple properties with
R.where"""

props(properties, object)
    """Acts as multiple prop: array of keys in, array of values out. Preserves
order"""

range(from_, to)
    """Returns a list of numbers from from (inclusive) to to (exclusive)"""

reduce(iterator, accumulator, list)
    """Returns a single item by iterating through the list, successively calling
the iterator function and passing it an accumulator value and the current
value from the array, and then passing the result to the next call.
The iterator function receives two values: (acc, value). It may use
R.reduced to shortcut the iteration.
The arguments' order of reduceRight's iterator function
is (value, acc).
Note: R.reduce does not skip deleted or unassigned indices (sparse
arrays), unlike the native Array.prototype.reduce method. For more details
on this behavior, see:
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce#Description
Dispatches to the reduce method of the third argument, if present. When
doing so, it is up to the user to handle the R.reduced
shortcuting, as this is not implemented by reduce"""

reduce_while(predicate, iterator, accumulator, list)
    """Like reduce, reduceWhile returns a single item by iterating
through the list, successively calling the iterator function. reduceWhile
also takes a predicate that is evaluated before each step. If the predicate
returns false, it "short-circuits" the iteration and returns the current
value of the accumulator"""

__init__(self, value)
    """Returns a value wrapped to indicate that it is the final value of the reduce
and transduce functions. The returned value should be considered a black
box: the internal structure is not guaranteed to be stable.
Note: this optimization is unavailable to functions not explicitly listed
above. For instance, it is not currently supported by
reduceRight"""

reject(p, xs)
    """The complement of filter.
Acts as a transducer if a transformer is given in list position. Filterable
objects include plain objects or any object that has a filter method such
as Array"""

remove(index, length, list)
    """Removes the sub-list of list starting at index start and containing
count elements. Note that this is not destructive: it returns a copy of
the list with the changes.
No lists have been harmed in the application of this function"""

repeat(value, times)
    """Returns a fixed list of size n containing a specified identical value"""

replace(pattern, replacement, string)
    """Replace a substring or regex match in a string with a replacement"""

reverse(list)
    """Returns a new list or string with the elements or characters in reverse
order"""

scan(function, accumulator, list)
    """Scan is similar to reduce, but returns a list of successively
reduced values from the left"""

slice(from_index, to_index, list_or_string)
    """Returns the elements of the given list or string (or object with a slice
method) from fromIndex (inclusive) to toIndex (exclusive).
Dispatches to the slice method of the third argument, if present"""

sort(comparator, list)
    """Returns a copy of the list, sorted according to the comparator function,
which should accept two values at a time and return a negative number if the
first value is smaller, a positive number if it's larger, and zero if they
are equal. Please note that this is a copy of the list. It does not
modify the original"""

sort_by(comparator, list)
    """Sorts the list according to the supplied function"""

sort_with(comparators, list)
    """Sorts a list according to a list of comparators"""

split(separator, string)
    """Splits a string into an array of strings based on the given
separator"""

split_at(index, list)
    """Splits a given list or string at a given index"""

split_every(length, collection)
    """Splits a collection into slices of the specified length"""

split_when(predicate, list)
    """Takes a list and a predicate and returns a pair of lists with the following properties:
the result of concatenating the two output lists is equivalent to the input list;
none of the elements of the first output list satisfies the predicate; and
if the second output list is non-empty, its first element satisfies the predicate"""

starts_with(values, list)
    """Checks if a list starts with the provided values"""

subtract(x, y)
    """Subtracts its second argument from its first argument"""

sum(xs)
    """Adds together all the elements of a list"""

symmetric_difference(first, second)
    """Finds the set (i.e. no duplicates) of all elements contained in the first or
second list, but not both"""

symmetric_difference_with(predicate, first, second)
    """Finds the set (i.e. no duplicates) of all elements contained in the first or
second list, but not both. Duplication is determined according to the value
returned by applying the supplied predicate to two list elements"""

tail(list)
    """Returns all but the first element of the given list or string (or object
with a tail method).
Dispatches to the slice method of the first argument, if present"""

take(n, list)
    """Returns the first n elements of the given list, string, or
transducer/transformer (or object with a take method).
Dispatches to the take method of the second argument, if present"""

take_last(n, list)
    """Returns a new list containing the last n elements of the given list.
If n > list.length, returns a list of list.length elements"""

take_last_while(predicate, list)
    """Returns a new list containing the last n elements of a given list, passing
each value to the supplied predicate function, and terminating when the
predicate function returns false. Excludes the element that caused the
predicate function to fail. The predicate function is passed one argument:
(value)"""

take_while(predicate, list)
    """Returns a new list containing the first n elements of a given list,
passing each value to the supplied predicate function, and terminating when
the predicate function returns false. Excludes the element that caused the
predicate function to fail. The predicate function is passed one argument:
(value).
Dispatches to the takeWhile method of the second argument, if present.
Acts as a transducer if a transformer is given in list position"""

tap(f, v)
    """Runs the given function with the supplied object, then returns the object.
Acts as a transducer if a transformer is given as second parameter"""

test(pattern, string)
    """Determines whether a given string matches a given regular expression"""

times(n)
    """Calls an input function n times, returning an array containing the results
of those function calls.
fn is passed one argument: The current value of n, which begins at 0
and is gradually incremented to n - 1"""

to_lower(string)
    """The lower case version of a string"""

to_pairs(object)
    """Converts an object into an array of key, value arrays. Only the object's
own properties are used.
Note that the order of the output array is not guaranteed to be consistent
across different JS platforms"""

to_upper(string)
    """The upper case version of a string"""

transpose(list)
    """Transposes the rows and columns of a 2D list.
When passed a list of n lists of length x,
returns a list of x lists of length n"""

trim(x)
    """Removes (strips) whitespace from both ends of the string"""

try_catch(tryer, catcher)
    """tryCatch takes two functions, a tryer and a catcher. The returned
function evaluates the tryer; if it does not throw, it simply returns the
result. If the tryer does throw, the returned function evaluates the
catcher function and returns its result. Note that for effective
composition with this function, both the tryer and catcher functions
must return the same type of results"""

unapply(function)
    """Takes a function fn, which takes a single array argument, and returns a
function which:
takes any number of positional arguments;
passes these arguments to fn as an array; and
returns the result.
In other words, R.unapply derives a variadic function from a function which
takes an array. R.unapply is the inverse of R.apply"""

unary(function)
    """Wraps a function of any arity (including nullary) in a function that accepts
exactly 1 parameter. Any extraneous parameters will not be passed to the
supplied function"""

unfold(iterator, seed)
    """Builds a list from a seed value. Accepts an iterator function, which returns
either false to stop iteration or an array of length 2 containing the value
to add to the resulting list and the seed to be used in the next call to the
iterator function.
The iterator function receives one argument: (seed)"""

union(X, Y)
    """Combines two lists into a set (i.e. no duplicates) composed of the elements
of each list"""

union_with(predicate, X, Y)
    """Combines two lists into a set (i.e. no duplicates) composed of the elements
of each list. Duplication is determined according to the value returned by
applying the supplied predicate to two list elements"""

uniq(xs)
    """Returns a new list containing only one copy of each element in the original
list. R.equals is used to determine equality"""

uniq_by(predicate, list)
    """Returns a new list containing only one copy of each element in the original
list, based upon the value returned by applying the supplied function to
each list element. Prefers the first item if the supplied function produces
the same value on two items. R.equals is used for comparison"""

unless(predicate, function, value)
    """Tests the final argument by passing it to the given predicate function. If
the predicate is not satisfied, the function will return the result of
calling the whenFalseFn function with the same argument. If the predicate
is satisfied, the argument is returned as is"""

unnest(list)
    """Shorthand for R.chain(R.identity), which removes one level of nesting from
any Chain"""

until(predicate, transformation, value)
    """Takes a predicate, a transformation function, and an initial value,
and returns a value of the same type as the initial value.
It does so by applying the transformation until the predicate is satisfied,
at which point it returns the satisfactory value"""

update(i, v, xs)
    """Returns a new copy of the array with the element at the provided index
replaced with the given value"""

use_with(function, transformers)
    """Accepts a function fn and a list of transformer functions and returns a
new curried function. When the new function is invoked, it calls the
function fn with parameters consisting of the result of calling each
supplied handler on successive arguments to the new function.
If more arguments are passed to the returned function than transformer
functions, those arguments are passed directly to fn as additional
parameters. If you expect additional arguments that don't need to be
transformed, although you can ignore them, it's best to pass an identity
function so that the new function reports the correct arity"""

values(dict)
    """Returns a list of all the enumerable own properties of the supplied object.
Note that the order of the output array is not guaranteed across different
JS platforms"""

when(predicate, when_true_fn, value)
    """Tests the final argument by passing it to the given predicate function. If
the predicate is satisfied, the function will return the result of calling
the whenTrueFn function with the same argument. If the predicate is not
satisfied, the argument is returned as is"""

where(spec, object)
    """Takes a spec object and a test object; returns true if the test satisfies
the spec. Each of the spec's own properties must be a predicate function.
Each predicate is applied to the value of the corresponding property of the
test object. where returns true if all the predicates return true, false
otherwise.
where is well suited to declaratively expressing constraints for other
functions such as filter and find"""

where_eq(spec, object)
    """Takes a spec object and a test object; returns true if the test satisfies
the spec, false otherwise. An object satisfies the spec if, for each of the
spec's own properties, accessing that property of the object gives the same
value (in R.equals terms) as accessing that property of the
spec.
whereEq is a specialization of where"""

without(xs1, xs2)
    """Returns a new list without values in the first argument.
R.equals is used to determine equality.
Acts as a transducer if a transformer is given in list position"""

xprod(xs1, xs2)
    """Creates a new list out of the two supplied by creating each possible pair
from the lists"""

zip(first, second)
    """Creates a new list out of the two supplied by pairing up equally-positioned
items from both lists. The returned list is truncated to the length of the
shorter of the two input lists.
Note: zip is equivalent to zipWith(function(a, b) { return [a, b] })"""

zip_obj(key, val)
    """Creates a new object out of a list of keys and a list of values.
Key/value pairing is truncated to the length of the shorter of the two lists.
Note: zipObj is equivalent to pipe(zip, fromPairs)"""

zip_with(f, xs1, xs2)
    """Creates a new list out of the two supplied by applying the function to each
equally-positioned pair in the lists. The returned list is truncated to the
length of the shorter of the two input lists"""

```
