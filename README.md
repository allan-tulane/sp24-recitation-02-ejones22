# CMPS 2200  Recitation 02

**Name (Team Member 1):**___Emma Jones______  
**Name (Team Member 2):**____Nicolas Labarca__

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

For f(n)=1, W(n) increases linearly with n. Each increase in n results in a proportional increase in W(n). For f(n) = log n , increases logarithmically with n. As n grows W(n) increases, but at a decreasing rate. For f(n) = n, W(n) increases quadratically with n. Asn grows, W(n) increases at an accelerating rate.


- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

When f(n) = n^c  the behavior of W(n) in relation to a, b, and c depends on the relative growth rates of these factors. If c < logb a, the function f(n) grows slower than the recurrence relation, resulting in W(n) increasing at a rate primarily determined by the branching factor a and the splitting factor b. When c > logb a, f(n) grows faster than the recurrence relation, causing W(n) to increase a rate dominated by f(n) as n grows. When c = logb a, the growth rate of W(n) balances between the effects of a, b, and f(n), with the overall growth determined by the interplay between a and f(n). These observations illustrate how the relationship between a, b, and c influences the asymptotic behaviour of W(n) in cases where f(n) = n^c.

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

For the given recursive algorithms with different work functions f(n), the span of the algorithm represents the maximum time it takes for any processor to execute its portion of the work. When f(n)=1, indicating constant work per node, the span S(n) is determined by the maximum depth of the recursion tree, resulting in a span of logb n,  where n is the input size. Similarly, for f(n) = logn, where the work per node increases logarithmically, the span remains f(n) = logb n. Even when f(n)=n, signifying linear work per node, the span retains its logarithmic nature with respect to n. These observations reveal that the span of the recursive algorithms remains logarithmic irrespective of the specific work function used, as it is dictated solely by the maximum depth of the recursion tree, which scales logarithmically with the input size.
