#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This code has a runtime of O(n). The while loop makes it appear as though the code will run n^3 times, however, the code inside the loop increases a by n^2, which makes this code O(n^-2). Multiplying the runtime of the code inside the loop by the runtime of the loop itself, we get O(n^3) \* O(n^-2), which results in O(n). Testing the code with several numbers verifies this. When n = 2, the loop runs twice. When n = 5, the loop runs five times.

b) This code has a runtime of (n^2). The inner loop is O(n) and the outer loop is O(n), so multiplying them together, results in a total runtimes of O(n^2)

c) This function has a runtime of O(n). Because the function contains one recursion of n - 1, the function will recurse n times. The rest of the code is pretty simple, so the overall result is O(n).

## Exercise II

Find the middle floor halfway between the ground and the nth floor
While we have not yet found f, drop an egg on this middle floor
If the egg is not broken, move up to the floor halfway between the current floor and n
If the egg is broken, move down to the floor halfway between the ground and the current floor
F is the lowest floor that results in a broken egg

The runtime of this algorithm would be O(log(n)), because we're reducing n each time we run our loop
