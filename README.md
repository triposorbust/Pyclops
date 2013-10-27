# Closest Pair of Points

Closest Pair of Points algorithm in `O(n lg n)` time. Classic divide-and-conquer algorithm from computational geometry.


### Quickstart

The `main` program expects one argument: filename of a tab-separated file where each row represents a point in XY Cartesian plane.

```
% python main.py <some-filename>
```

Which runs the closest pair of points algorithm on the points in the file.


### Background

Need to find a closest pair of points? Well, it's easy to do it in `O(n^2)`, yes? Simply try all `C(N,2)` combinations and pick the best one.

What about something faster? Divide-and-Conquer works here!

Partition into two roughly equally sized groups. Find the closest pair of points on each set. Then check that no two points _across_ sets are closer! Done!

This runs in `T(n) = 2T(n/2) + O(n)`. Overall: `O(n lg n)`!


### Known Issues

 - Parser is actually just a string processing line. Poorly-formed entries in the input file will break the software.
 - Recursion accumulates stack frames. Large inputs (> 1,250) cause stack overflows.


### Unit Tests

Package includes `unittest` test suite. Tests can be run via the `unittest` module interface:

```
% python -m unittest discover -s spec -p '*spec.py'
test_closest_of_three (pyclops.core_spec.BruteForceClosestPairSpec) ... ok
test_closest_of_two (pyclops.core_spec.BruteForceClosestPairSpec) ... ok
test_a_closest_pair (pyclops.core_spec.ClosestPairSpec) ... ok
test_b_closest_pair (pyclops.core_spec.ClosestPairSpec) ... ok
test_c_closest_pair (pyclops.core_spec.ClosestPairSpec) ... ok
test_1d_distance (pyclops.core_spec.DistanceSpec) ... ok
test_2d_distance (pyclops.core_spec.DistanceSpec) ... ok

----------------------------------------------------------------------
Ran 7 tests in 1.603s

OK
```

For convenience, this command is also wrapped in `test.sh`.


### Dependencies

 - `Python (>= 2.7.3)`
 - `unittest`


### Authors

 - Andy Chiang
 - ...


### License

Copyright &copy; 2013 Andy Chiang.

Distributed under the MIT License.
