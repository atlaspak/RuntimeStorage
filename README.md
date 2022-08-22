# Runtime Storage

## Storage Algorithm
Storage.py based on two different Python collection data structures; Dictionary and Counter. 

Dictionary is key-value based data structure. 
Access, add, delete time complexity is O(1) which makes it a good candidate where we need to relate two different data and we don't need to recursively iterate them.

Counter is wrapped version of the Dictionary only difference is values are counts of the keys.

This two data structure help this project the keep count of each data which costs us O(N) extra space for value pair.

```Add: O(1) Access: O(1) Delete: O(1) Counting: O(1)```

```Space: O(N) for data + O(N) for counts```

### Alternative Solutions
#### Naive approach: 
Single list for entire data. This approach would use the smallest space possible. No redudancy, single storage for each data. Basic operations would already need to iteration of entire list. 

```Add: O(1) Access: O(N) Delete: O(N) Counting: O(N)```

```Space: O(N)```

#### Optimized Naive approach:
Single Dictionary for entire data. This approach would use the smallest space possibe. Only costly operation for this approach would be the cost of counting values.

```Add: O(1) Access: O(1) Delete: O(1) Counting: O(N)```

```Space: O(N)```


## Transaction

### Transaction Handling
With the current handling mechanism, we are allowing only one transaction to be handled at a time. 

#### Pros
- Help to unset(delete) items from transaction database
- Read from transaction memory
  
#### Cons
- Single transaction storage is allowed
- Counter data storage is not needed (or if it's needed it needs to be defined more clearly)

### Alternative Ideas
- Single dictionary would have been used for the same operations which would make code less readable, hard to test. The design would be little bit complex due to deciding ownership of this data. Currently CommandManager is only functional class.
- Multiple Lists: This is a good idea indeed which allows user to start new transactions recursively, I would also implement this approach if I would have use some more time. But this also comes with some clumsiness. Code would have been much harder to test also more error prone. Design would be more complicated. Transaction memory wouldn't allow us to access to data or delete random items from it.


## Design
Current code mechanism consist of three components Script.py and CommandLiner.py is only there to help you to interact with the actual logic. 

```CommandLiner:``` Functional class which decides which function to be called and send responses to the UI  
```Storage:``` Data class for storing each pair of data and keep track of the occurence of each value


## Usage
Simply run:
```python Script.py```

#### Example
```
$ python Script.py
> SET 5 7
Key Added
> GET 5
7
> NUMEQUALTO 7
1
> UNSET 5
Key Deleted
> GET 5
None
> NUMEQUALTO 7
0
> BEGIN
Transaction Started
> SET 6 4
Transaction Key Added
> ROLLBACK
Transaction Cleared
> COMMIT
Transaction Merged
> GET 6
None
> END
Bye
$
```


## Unit Test
On ```CommandLiner``` and ```Storage``` classes we have almost full coverage with unit tests.
```
$ python -m unittest
....................
----------------------------------------------------------------------
Ran 20 tests in 0.003s

OK
```
