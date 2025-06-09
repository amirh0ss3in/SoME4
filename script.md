# This weird approximation solves an impossible problem

(intro music)

### Introduction

Let's imagine a situation where a group of people each has to make a simple, binary choice. They could be deciding "yes or no" on some question, or maybe they're choosing between two political candidates.

To make this mathematical, we'll call a "yes" a "+1" and a "no" a "–1".

Let's start with just two people, Alice and Bob. Suppose they both vote "yes", which we'll show with their state as +1.

### Agreement and Disagreement

Now, let's explore the possible outcomes of their choices. We can keep track of Alice's choice, which we'll call *s₁*, and Bob's choice, *s₂*.

There's an interesting mathematical property here. What happens if we multiply their choices together?

If Alice and Bob both choose +1, their product is +1. We can think of this as a state of 'agreement'.

If Alice chooses +1 and Bob chooses –1, their product is –1. This is a state of 'disagreement'.

The same is true if their roles are reversed.

And if they both choose –1, the product is once again +1. They still 'agree', in this case, on "no". So the product *s₁* times *s₂* is a wonderful little measure of whether they agree or disagree.

### Introducing Tension

But in the real world, people aren't isolated. Their decisions are often influenced by their relationship with others. You might say there's a... *tension* between them.

Let's represent this tension with a value, which we'll call *J₁₂*, that lives on the connection between Alice and Bob.

We can think of this tension value as a dial. If *J* is positive, let's say their relationship is 'tense'—they are rivals. If *J* is negative, their relationship is 'cozy' or friendly. And if *J* is zero, they have no influence on each other at all.

### Defining Conflict (The Hamiltonian)

So, how do we combine all these ideas? We have Alice's choice, Bob's choice, and the tension in their relationship.

We can define a single number that captures the state of the whole system. Let's call it the "Conflict", or for those with a physics background, the Hamiltonian, denoted by a capital *H*.

The conflict is simply the product of Alice's choice, the tension, and Bob's choice.

Let's see what this means in practice. Suppose Alice and Bob have a cozy relationship, so *J* is negative one. If they both agree, and choose +1, the total conflict *H* is -1. A low conflict state.

But if Bob disagrees, the conflict becomes +1. This makes sense: in a cozy relationship, disagreement leads to higher conflict.

Now, what happens if we dial up the tension so their relationship is 'tense', with *J* equal to positive one? In this case, with them disagreeing, the conflict is actually low, at -1.

But if they *agree* while in a tense relationship, the conflict becomes high. In this state, they're almost 'expected' to disagree.

### Finding the Ground State

This leads to a fascinating question. If the tension *J* is fixed, what choices will Alice and Bob naturally make to minimize the total conflict?

This lowest-energy, lowest-conflict state has a special name: it's called the **ground state**.

Let's try to find it. In the cozy case, where *J* is -1, we can calculate the conflict for all four possibilities. The lowest value, -1, occurs whenever they agree. This means `[+1, +1]` is a ground state...

...but so is `[–1, –1]`. This system has two ground states.

Now, what if their relationship is tense, with *J* equal to +1? The minimum conflict value is still -1, but this time it occurs when they *disagree*. So the ground states are `[+1, –1]`...

...and `[–1, +1]`.

### Three People

You might wonder... what happens with three people?

Let's introduce a third person, Charlie. Now there isn't just one relationship, but three: between Alice and Bob, Alice and Charlie, and Bob and Charlie. Each of these connections gets its own tension value: *J₁₂, J₁₃,* and *J₂₃*.

The Total Conflict of the system is now just the sum of the conflicts from each individual pair. It’s the conflict between Alice and Bob... plus the conflict between Alice and Charlie... plus the conflict between Bob and Charlie.

### Generalizing to N People

And this pattern continues. If we add a fourth person, Diana, we now have six connections in total. The Total Conflict is the sum of the conflicts over all six of these pairs.

As you can imagine, writing this out gets very long, very quickly. But mathematicians have a beautiful shorthand for this kind of sum.

We can say the Hamiltonian, *H*, is the sum over all pairs of people *i* and *j*, of *sᵢ* times *Jᵢⱼ* times *sⱼ*.

### The Matrix Formulation

This formula has two key components: the state of the spins, *sᵢ*, which for each person is either +1 or -1... and the tensions, *Jᵢⱼ*, which we can think of as the elements of an N-by-N matrix describing the entire network of relationships.

Now, it's fair to assume that in the real world, the tension is mutual. The way Alice feels about Bob is the same as how Bob feels about Alice. In other words, *Jᵢⱼ* is equal to *Jⱼᵢ*. The tension matrix is symmetric.

This symmetry allows us to rewrite the sum in a more general, and often more useful, way. Instead of summing over only the unique pairs where *i* is less than *j*, we can sum over all *i* and all *j*, as long as we multiply the whole thing by one-half to avoid double-counting each relationship.

And for those of you familiar with linear algebra, you might recognize this structure. This entire expression is simply one-half times the vector of spins **s** transposed, times the matrix of tensions **J**, times the vector **s**.

This is what that compact formula actually represents: a neat, clean way to capture all the pairwise interactions in the entire system.

### The Complexity of Finding the Ground State

So, we return to our central question: how do you find the ground state of a system like this? The most direct, brute-force approach would be to check the conflict value for every single possible configuration of spins.

But just how many configurations are there?

Well, the first person has two choices. For *each* of those choices, the second person has two choices. And so on, for all N people in the system. The total number of configurations is 2, multiplied by itself N times... or simply, 2 to the power of N.

What does that number actually look like as N grows? For a small number of people, it seems manageable. At N=5, there are 32 configurations to check.

But as we increase N, this curve bends upwards with terrifying speed. This is the nature of exponential growth.

By the time we get to N=10, we have over a thousand states. By N=30, the number of possibilities has exploded to over a billion. And the problem gets unimaginably big, incredibly fast.

To put this in perspective, for a system of just 300 people, the number of possible configurations—2 to the 300—is a number so vast that it's greater than the estimated number of atoms in the entire known universe.

So, simply checking every possibility is not just slow; for any reasonably sized problem, it's physically impossible. This is what makes finding the ground state of these systems such a profoundly difficult, and deeply interesting, problem in physics, computer science, and mathematics.





### The Universal Puzzle

So, we've established that finding the ground state is an impossibly hard problem, at least by checking every single possibility. The number of states grows so fast that it's beyond the reach of any computer.

But you might be wondering... so what? Is this just a niche problem for physicists studying magnets? Or is there something deeper going on here?

It turns out, this "Ising Problem" is a kind of universal puzzle. It secretly describes a huge number of other difficult problems that seem completely unrelated at first glance.

To see how, let's take a look at one of those other problems. It's a simple puzzle that you could try to solve yourself, called the **Number Partitioning Problem**.

The rules are simple. Given a set of numbers, can you divide them into two groups that have the exact same sum?

For a small set, like {8, 7, 6, 5}, you might be able to find a solution with a bit of trial and error. In this case, if we put 8 and 5 in one group, their sum is 13. And the remaining numbers, 7 and 6, also sum to 13. So, yes, we found a perfect partition.

But what if the set had a hundred numbers, all with many digits? You can feel how, just like our spin problem, the difficulty would start to grow exponentially.

Now, here comes the magic trick. How on earth does this connect to our spins?

Let's try to reframe the problem. Instead of thinking about putting numbers into bins, let's think about assigning a spin to each number. Let's say that if a number goes into the first group, we'll assign it a spin of +1. And if it goes into the second group, we'll assign it a spin of –1.

Now, what happens if we calculate something interesting: the sum of each number multiplied by its assigned spin?

In our example, that would be (+1) times 8, plus (–1) times 7, plus (–1) times 6, plus (+1) times 5.

If you work that out, you get 8 minus 7 minus 6 plus 5... which equals zero.

This isn't a coincidence. Think about what this sum actually represents. It's the sum of the first group minus the sum of the second group. So, saying that the two groups have an equal sum is *exactly the same* as saying that this special spin-weighted sum is zero.

Our goal has been transformed: can we find a set of spins `sᵢ` that makes the total sum `Σ sᵢaᵢ` equal to zero?

But hold on. You should be a little skeptical here. Our original Ising Hamiltonian had pairs of spins, `sᵢ` times `sⱼ`, and those `J` tension values. This new formula only has single spins. How can these possibly be the same problem?

Well, here's the final piece of the puzzle. Consider what happens if we take that entire sum... and square it.

If our goal is to make a number equal to zero, that's the same thing as trying to make its *square* as small as possible, right? The minimum possible value of a squared number is, after all, zero.

Now, if we expand this squared term—and you can pause and try this yourself if you'd like—something amazing happens. The expression splits into two distinct parts.

The first part is just the sum of the squares of all our original numbers. But think about that for a moment. Our original numbers are fixed. They're given to us. So this part of the expression is just a constant value. It doesn't depend on our choices of spin at all. When we're looking for a minimum, we can completely ignore it.

And the second part... look closely at what's left. It's a sum over all pairs of spins, `i` and `j`, of `sᵢ` times `sⱼ`... times some other values.

This structure should look very familiar. It's exactly the form of our Ising Hamiltonian. If we simply define the "tension" `Jᵢⱼ` between any two spins to be the product of their corresponding numbers, `aᵢ` times `aⱼ`... then minimizing this expression is mathematically identical to finding the ground state of that specific Ising system.

And this isn't just a special relationship. The Ising model is like a master key.

Many of the most notoriously difficult problems in computer science and operations research can be translated, or 'mapped', into the language of finding an Ising ground state. Problems like **Max-Cut**, which is about splitting a network... the famous **Traveling Salesman Problem**... even problems from other fields, like the **k-satisfiability problem** from logic.

All of these problems, which look so different on the surface, share the same computational skeleton. They are all, in essence, about finding the one configuration out of an astronomical number of possibilities that minimizes some global 'conflict' or 'energy'.

This is the real reason scientists, engineers, and mathematicians are so obsessed with this problem. If you can build a machine or an algorithm that is good at finding the ground state of an Ising model, you haven't just solved one niche puzzle. You've created a powerful tool for tackling thousands of others.

### The Edge of Solvability

So this brings us back to our central question. If checking every state is impossible, how can we ever hope to find this ground state?

The short, and perhaps surprising, answer is... for a general, complex system... you don't. At least, not perfectly.

There is no known algorithm that can efficiently find the exact ground state for *any* arbitrary set of tensions `Jᵢⱼ`. It belongs to a class of problems believed to be fundamentally hard for classical computers.

However, for a few, very special cases where the network of connections is highly structured, mathematicians and physicists *have* found clever ways to solve it exactly. The most famous example is the **2D planar graph**—any graph that can be drawn flat without its edges crossing. In a landmark 1944 paper, Lars Onsager found a stunning analytical solution for these systems. But this is only possible because of the grid's rigid, two-dimensional structure. The moment you allow connections in 3D, an exact solution is once again out of reach.

Things get even stranger for **spin glasses**, where the tensions are completely random. Finding the ground state for any *one* specific spin glass is still incredibly hard. However, thanks to the monumental work of physicists like Giorgio Parisi, we now have a profound mathematical understanding of their *statistical* nature—what the energy landscape looks like on average. Parisi's Nobel-winning work revealed the incredibly complex structure of the low-energy states, even if it doesn't give us a simple recipe to find the single ground state for any given instance.

But these are the exceptions—beautiful, clean, mathematical worlds. What about the messy, real-world problems we saw earlier?

For those, we need a different approach. If you can't *calculate* the answer, maybe you can *build* a physical system that naturally *finds* the answer for you.

This is precisely the goal of machines like this one: a **quantum annealer**. It's not a general-purpose computer. It's a highly specialized piece of hardware designed to do one thing, and one thing only: find the lowest energy state of a physical system that is programmed to behave just like our Ising model.

It tackles the problem not by crunching numbers, but by using the laws of quantum mechanics to "feel out" the entire landscape of possibilities at once and settle into the valley of lowest energy—the ground state.


### A New Kind of Order

So, how do you make progress on a problem that seems fundamentally impossible? Sometimes, the answer is to step back and change the question entirely.

The Ising model is defined by its matrix of tensions, the `Jᵢⱼ` values. For decades, the most studied cases were those where these tensions were either uniform and repeating, or completely random.

But a young physics student began to wonder about the nature of that `J` matrix itself. What other kinds of structures could it have?

He imagined a system where the components weren't all identical, but had an intrinsic rank or identity. A hierarchy. And he posed a simple, creative question: "What if the interaction between any two spins was a direct function of their rank?"

He started with the simplest rule he could think of: the tension between any two spins is just the sum of their ranks, `Jᵢⱼ` equals `i` plus `j`. He had defined a new mathematical world. But what were its laws? What did its most stable state—its ground state—look like?

With a small computer, he could begin to explore. He set the number of spins to 10 and had the machine search through all 1,024 possible configurations to find the one with the lowest energy. The result was surprisingly simple. A clean split. Two blocks of spins, all aligned together.

Curious, he tried it again for 11 spins. The same pattern. For 12, 13, 14, and 15 spins, the same beautiful, simple structure emerged from the complexity every single time. This was the moment of discovery. The feeling that this wasn't a coincidence, but a fundamental property of the world he had created.

He pushed the idea further, discovering this was just one example of a whole family of rules, governed by a single parameter, `d`. And for each of them, as he moved a dial for `d` to positive or negative values, the same elegant, two-cluster pattern held true. The size of the clusters would change, but the fundamental structure was always the same.

He had found a vast new class of systems—each complex and fully connected—that all shared the same simple, predictable ground state pattern.

But as he stared at these patterns, he noticed something even stranger. It wasn't just that the ground state was always two clusters. He looked at the size of the first cluster, which we can call `M`, and he compared it to the total number of spins, `N`.

He saw that for a given rule, say `d=1`, this ratio, `q = M/N`, seemed to be settling down, converging to a specific constant value as `N` grew larger.

He could track this convergence perfectly up to around N equals 30, using brute force to be absolutely sure he had the true ground state. But beyond that, the calculation became impossible. He hit the `2^N` complexity wall. He was stuck.

And here, he took a crucial leap of faith. He made a bold assumption. "What if," he thought, "the two-cluster pattern isn't just a coincidence for small N? What if it's a fundamental law of this system, true for *any* N?"

This assumption changes everything. The problem is no longer about searching through an ocean of `2^N` states. It's now a simple search through just `N` possible cluster splits. A problem that was impossible for a supercomputer becomes trivial for a laptop.

With this new power, he could see the convergence clearly. And he could test other rules. For `d=4`, the ratio `q` converges to a different value. For `d=-0.5`, yet another. Each rule, each `d`, had its own unique, constant ratio that the system was trying to reach. The pattern was real. The leap of faith was justified.

The next question was... why? What deeper principle was forcing the system to behave this way?