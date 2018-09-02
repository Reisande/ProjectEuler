This is a compilation of all project Euler solutions I have written. I like to jump around a bit to see what I can do. 

I try to format my problems in accordance with pep 8, but my earlier solutions may not exactly fit the standar. This is largely due to being unaware of pep8.

I'll write notes into this readme for all Project Euler Solutions to explain the solutions I originally came up with, and what I did to optimize them. Usually I come up with a working solution in about 10 minutes, however, that solution is almost never optimized properly. My fastest Solution so far has been Number 20, largely due to python's built in functions, which was 7 min after I solved 16.

I will add these explanations in the order I come up with them.

Any new solutions will be posted Sunday.

--Project Euler 1--

--Project Euler 2--

--Project Euler 3--

--Project Euler 4--

--Project Euler 5--

--Project Euler 6--

--Project Euler 7--

--Project Euler 8--

--Project Euler 10--

--Project Euler 12--

--Project Euler 13--

--Project Euler 14--

--Project Euler 16--

--Project Euler 20--

--Project Euler 9--
Probably the most complex problem I have solved so far. Once again, figuring out A solution wasn't particuarly hard, but I wanted to make a solution which would easily work for any input. I know that this can be slimmed down a bit by merging the two functions which generate original triples into one, and then in all instances where I use another function(like the populate list function) with the output of either one of the original generating function as the argument. Also, this would take out the need of a populate list function, but I feel as though the seperation of the two algorithms for generating triples is useful for readability. However, I don't see this saving me too many LOC. Also, I could just have a function which checks the output of the triples generators if their outputs(or their multiples) would equal the user inpput(in the case of project Euler question 9, 1000). This was my original plan, but proved to be very difficult to check. However, a list was very easy to check, so it was simpler for me to just use a list. If the input was larger, I can see the necessity of these changes, but with the required input, my solution works in under a second.
