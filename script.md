## **Hello, and welcome!**

Today, we’re diving into a beautifully simple idea from physics — one that shows up in surprising places.

It helps explain how **magnets** work.
It models how **opinions spread** through a social network.
It even helps us **solve tough optimization problems** in machine learning and beyond.

This idea is called the **Ising model**.

At its core, the Ising model is about **binary choices** — simple yes-or-no decisions — and how those decisions **influence one another**.

---

### **A simple thought experiment**

Imagine a group of people, each deciding **yes or no** on some question. It doesn’t matter what the question is. We’ll call “yes” **+1** and “no” **–1**.

But here’s the twist:
People don’t decide in isolation.
They **care about what their neighbors think**.

---

### **Let’s start small: Just two people. Alice and Bob.**

Each of them chooses +1 or –1.

Let’s call their choices:

* $s_1$ for Alice
* $s_2$ for Bob

Now, let’s introduce a number, $J_{12}$, to represent how their relationship works — specifically, how much **tension** or **comfort** exists when they agree or disagree.

You can think of $J_{12}$ as a kind of **social tension dial**:

* If $J_{12} > 0$, they **prefer to disagree**. Agreement feels tense.
* If $J_{12} < 0$, they **prefer to agree**. Disagreement feels awkward.
* If $J_{12} = 0$, they don’t influence each other at all.

Let’s see how this plays out.

Here are all 4 possible combinations of their choices, and the corresponding “energy” of each — a number that tells us how comfortable or uncomfortable the system feels:

| $s_1$ | $s_2$ |  $s_1$ $s_2$ | Energy if $J_{12} = +1$ |
| -------- | -------- | -------------- | -------------------------- |
| +1       | +1       | +1             |    +1                      |
| +1       | –1       | –1             |    –1                      |
| –1       | +1       | –1             |    –1                      |
| –1       | –1       | +1             |    +1                      |

Lower energy = better.
So in this case, the system **prefers disagreement**.

Now flip the sign: set $J_{12} = -1$. That means Alice and Bob **like being aligned**. The energies flip:

* Agreement becomes **energy –1** → preferred.
* Disagreement becomes **energy +1** → not so cozy.

You can think of it like this:
When $J$ is negative, it’s like two cold people huddling for warmth. They find **comfort in alignment**.

---

### **Let’s add one more person: Charlie.**

Now we have three people:

* Alice ($s_1$)
* Bob ($s_2$)
* Charlie ($s_3$)

And three relationships:

* $J_{12}$ between Alice and Bob
* $J_{13}$ between Alice and Charlie
* $J_{23}$ between Bob and Charlie

Suppose they all prefer to agree. So we set:

$$
J_{12} = J_{13} = J_{23} = -1
$$

Now let’s look at all **8 possible configurations** of their opinions and compute the energy:

| $s_1$ | $s_2$ | $s_3$ | $s_1 s_2$ | $s_1 s_3$ | $s_2 s_3$ | Total Energy |
| -------- | -------- | -------- | ------------- | ------------- | ------------- | ------------ |
| +1       | +1       | +1       |  +1           |  +1           |  +1           | –3           |
| +1       | +1       | –1       |  +1           |  –1           |  –1           | –1           |
| +1       | –1       | +1       |  –1           |  +1           |  –1           | –1           |
| +1       | –1       | –1       |  –1           |  –1           |  +1           | –1           |
| –1       | +1       | +1       |  –1           |  –1           |  +1           | –1           |
| –1       | +1       | –1       |  –1           |  +1           |  –1           | –1           |
| –1       | –1       | +1       |  +1           |  –1           |  –1           | –1           |
| –1       | –1       | –1       |  +1           |  +1           |  +1           | –3           |

Just like before, the configurations with **everyone aligned** have the lowest energy.
The system is happiest — most stable — when everyone agrees.

---

### **The big picture: the Hamiltonian**

All of this can be captured in a single formula, called the **Hamiltonian**:

$$
H = \sum_{i<j} J_{ij} s_i s_j
$$

This sums over all the relationships, multiplying each pair's alignment by the strength of their connection.

You can think of it as a kind of **global discomfort score**.
The lower it is, the more “at peace” the whole system feels.

And the configuration that gives the lowest possible energy — the **ground state** — is what the system naturally tends toward.




## **Part 2 — Complexity Creeps In**

In the last part, we saw how the Ising model gives us a way to score different configurations — based on how much agreement or disagreement exists between interacting "spins".

But here’s the kicker:

To *actually find* the best configuration — the one with the **lowest energy** — you’d have to check **every possible arrangement** of spins.

And if you have $N$ people (or spins), each of whom can be either +1 or –1, then there are:

$$
2^N
$$

possible configurations.

Just 10 spins? 1,024 possibilities.
20 spins? Over a million.
50 spins? You’re looking at more than a **quadrillion**.

And this number just keeps exploding.

Now imagine trying to solve this for a system with **hundreds or thousands** of interacting parts.

---

### **Why Does This Matter?**

Because this isn’t just about magnets anymore.

This kind of problem — minimizing the Ising Hamiltonian — shows up in **many real-world tasks** that are known to be **NP-hard**.

That means: there’s *no known efficient algorithm* that can always find the best solution quickly. You’d have to try every possible configuration... which is hopelessly slow as the problem grows.

---

### **A Real Example: The Number Partition Problem**

Let’s look at a concrete example.

Suppose I give you a list of numbers:

**[7, 3, 5, 9, 1]**

Your task: **divide them into two groups** so that the **sums of each group are as equal as possible**.

That’s the **Number Partition Problem**, and it’s **NP-hard**.

But here’s the fun part:

We can *translate* this into an Ising model.

Assign a spin $s_i = +1$ if number $i$ goes into group A, and $s_i = -1$ if it goes into group B.
Then define the Hamiltonian so that it punishes imbalanced group sums.

Minimizing the energy of this spin system is **exactly** the same as solving the number partition problem.

So the Ising model isn't just a physics toy — it’s a **universal language for hard problems**.

---

### **Other NP-Hard Problems**

And it’s not alone.

Many famous NP-hard problems can be **converted** into Ising form:

* **Traveling Salesman Problem**
* **Graph Coloring**
* **Max-Cut**
* **3-SAT**
* **Subset Sum**

All of these — and many more — can be *reduced* to each other.

(We won’t dive into how reductions work here, but just know: they’re like mathematical “translations” from one problem to another.)

---

### **Why Does That Matter?**

Because it means:

> **If you can solve the Ising model efficiently, you can solve all these problems.**

And that’s a big deal — for computer science, optimization, AI, logistics, cryptography... you name it.

