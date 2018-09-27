This is a compilation of all project Euler solutions I have written. I like to jump around a bit to see what I can do. 

I try to format my problems in accordance with pep 8, but my earlier solutions may not exactly fit the standard. This is largely due to being unaware of PEP8.

I'll write notes into this readme for all Project Euler Solutions to explain the solutions I originally came up with, and what I did to optimize them. Usually I come up with a working solution in about 10 minutes, however, that solution is almost never optimized properly. My fastest Solution so far has been Number 20, largely due to python's built in functions, which was 7 min after I solved 16.

I will add these explanations in the order I come up with them, not in the order listed on the Project Euler website

--Project Euler 1--

Not a very complex solution. I satred out with just a for loop and a list, but I changed my solution to use a list comprehension, and print the sum of the list.

--Project Euler 2--

This is kind of a funny problem to me. I misunderstood the wording originally; I thought that the question was asking for the sum of the first 2 million terms of the Fibonacci Sequence, and became frustrated with the length of my computation rather quickly. I worked on the problem for 4 hours wondering how I could optimize the solution, but I realized when I started to work on the problem a day later that is was asking for terms whose value were less than 2 million, not the first 2 million terms.

--Project Euler 3--

This was not a very glamorous solution or problem. Two for loops, I optimized my solution a little by limiting the range of the second for loop to go from 1 to the square root of the input value, instead of the entire number. The is_prime function was slightly modified to print out a pair of numbers- the number checking for primality, and the original input divided by the prime.

--Project Euler 4--

Once again, not a very complex solution. I turned the number into a list to generate the backwards version of itself by slicing the list in reverse order, then checked if the new number was larger than the last palindrome number.

--Project Euler 5--



--Project Euler 6--



--Project Euler 7--

See "Sieve of Eratosthenes"

--Project Euler 8--



--Project Euler 10--



--Project Euler 12--



--Project Euler 13--



--Project Euler 14--



--Project Euler 16--



--Project Euler 20--



--Project Euler 9--

Probably the most complex solution I have made so far. Once again, figuring out A solution wasn't particuarly hard, but I wanted to make a solution which would easily work for any input. I know that this program can be slimmed a bit by merging the two functions which generate original triples into one, single, triple generating function, and then in all instances where I use another function(like the populate list function) I could use the single triple creator. Also, this would take out the need of a populate list function, but I feel as though the seperation of the two algorithms for generating triples is useful for readability. Also, I don't see this saving me too many LOC. Also, I could just have a function which checks the output of the triples generators if their outputs(or their multiples) would equal the user inpput(in the case of project Euler question 9, 1000). This was my original plan, but proved to be very difficult to check. However, a list was very easy to check for functionality of the Stifel and Onazam algorithms, so it was simpler for me to just use a list. If the input was larger, I can see the necessity of these changes, but with the required input, my solution works in under a second.

--Project Euler 21--

This was a pretty simple solution. I was somewhat confused in my first attempt, but I realized that the question didn't consider perfect numbers to be amicable. I used two functions, one for amicability and to check for divisbility. This was mainly to aid in readability of the program, but two functions had the added benefit of making debugging easier. My reasoning for the loop was if a number was perfect, you could go through the function to sum the divisors twice in order to find the original number. I could increase efficiency by just adding the second half of couple to the amicable number list, instead of making the loop iterate through every number in the necessary range. However, I felt as though this would make no practical difference to computation time as my current solution takes less than a second to run. 

--Project Euler 15--

Not a very complex solution. I wrote out a few lattice paths to figure out if there was any pattern to how the sum of possibilities for lattice paths formed, and realized I could it was a basic combinatoric equation. Originally I didn't even program the solution, I just looked on WolframAlpha 40 Choose 20. I decided to write out a solution afterwords simply for the practice.

--Project Euler 18--

Again, not a very complex solution. The algorithm I used worked by finding the larger of the two child nodes for each parent row in the range (0, n-1), in a triangle with number of rows n. For the larger child node, the parent node was replaced by the parent node + the child node, and this process was completed until the largest node remained in the 0th column. The time complexity for this algorithm is 0(nlogn)

--ELSE-------------

Sieve of Eratosthenes

Not a very complex piece of code, but one which was enjoyable for me to write. I looked on a Project Euler forum, and it was suggested to look up the Sieve as it was immensely useful to find primality. This was not wrong whatsoever. Funnily enough, I came up wth something very similar when I was in math class when I was in middle school. Whenever I was bored in class I liked write out sequences of numbers, one of these sequences was primes.. I generated these by hand, and my method was almost identical to the sieve, except I didn't think to check all potential factors up until the square root of the number I was checking for primality. Normally I just checked for the smaller potential factors(2, 3, ... 17). My Answer for Number seven isn't present in the repository because I just modified my sieve to solve 7
