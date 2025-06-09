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