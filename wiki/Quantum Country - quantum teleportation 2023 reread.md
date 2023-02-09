---
title: Quantum Country - quantum teleportation 2023 reread
author: Issa Rice
created: 2023-02-07
date: 2023-02-08
---

# Background

In a [comment thread](https://www.patreon.com/posts/towards-impact-76438674) on his Patreon, [Andy Matuschak](https://andymatuschak.org/) encouraged me to reread the [quantum teleportation](https://quantum.country/teleportation) essay on Quantum Country. Patreon does not allow formatting or math in its comment threads, and since the topic may be of broader interest, I am publishing reflections on my reread here.

The quantum teleportation essay was published in November 2019 and I believe I read it first within a week after it came out, and haven't read it since (until now), so it's been a little over 3 years since I read this essay. It was my first exposure to the idea of quantum teleportation, and Quantum Country was more generally my first (and so far only) introduction to quantum computing. In the time since then, I have not learned anything else about quantum computing, other than to review the Quantum Country prompts. So I believe my experience provides a "legit" data point as to how well the mnemonic medium works when it is used as the only source of learning and review of a topic (which, to be clear, is not exactly a fair setting in which to judge the mnemonic medium, since hopefully one would be learning things that one naturally encounters/is relevant to one's life).

(Warning for anyone who reads the content below: I expect to be making a fool of myself below.  I do not understand quantum computing, which is why I am so interested in Quantum Country. I expect to be saying things that are totally wrong and hilarious to people who know better!)

# Main thoughts

I remember finding the essay pretty confusing when I first read it, and found it confusing in probably similar ways on my reread.

I think my main confusion is that I'm still not quite sure how quantum teleportation works. In particular, I have three alternative hypotheses about how it might work, and the essay does not seem to me to allow me to figure out which of these is actually the case:

1. Alice and Bob are in a room together. Alice has the state $|\psi\rangle$ and Bob has the state $\frac{|00\rangle + |11\rangle}{\sqrt 2}$. They perform the circuit for quantum teleportation, and then they part ways, with Alice keeping the first two qubits and Bob keeping the third qubit. Later, Alice measures her qubits and posts the values of $x$ and $z$ on the internet, and Bob reads this and applies $Z^z X^x$ to his qubit, obtaining the state $|\psi\rangle$.
2. Alice and Bob are in a room together. Alice has the state $|\psi\rangle$ and Bob has the state $\frac{|00\rangle + |11\rangle}{\sqrt 2}$. Bob gives one of his qubits to Alice. They part ways. Later, Alice performs the circuit for quantum teleportation to her two qubits, measures them, and posts the values of $x$ and $z$ to the internet. Bob reads this and applies $Z^z X^x$ to his qubit, obtaining the state $|\psi\rangle$.
3. Alice and Bob are in a room together. Alice has no qubit, while Bob has the state $\frac{|00\rangle + |11\rangle}{\sqrt 2}$. Bob gives one of his qubits to Alice. They part ways. Later, Alice constructs the state $|\psi\rangle$ and performs the circuit for quantum teleportation to her two qubits, measures them, and posts the values of $x$ and $z$ to the internet. Bob reads this and applies $Z^z X^x$ to his qubit, obtaining the state $|\psi\rangle$.

If quantum teleportation is (1), it does not seem very interesting to me. It would be like Alice encrypting some file, handing it to Bob, and then later posting the password to decrypt the file to the internet, allowing Bob to finally read the file.

If quantum teleportation is (2), this is more interesting. However, Bob was already in the room with Alice when Alice had the state $|\psi\rangle$! So it raises the question of "Well, why didn't Alice just hand the state to Bob?" It also raises the question of how it is possible to perform a quantum circuit over large distances. And questions like, if a quantum circuit can act over large distances on qubits that don't even have a matrix operation on them (as is the case with the third qubit in the teleportation circuit -- nothing acts on the third qubit until Bob applies $Z^z X^x$), then how does it "know" not to act on other random qubits that are "out there"?

If quantum teleportation is (3), this is actually very interesting. But I have similar questions as in the case for (2).

My point is not so much that this particular confusion is so difficult to resolve -- it probably isn't: my guess is that if I googled around for a bit I would probably be able to answer this question myself. My point is more that, even a careful reading of the text does not allow me to answer this question, even though it seems pretty central to understanding how quantum teleportation works, and like, man, this kind of exposition problem is rampant.

My other confusion is something like to what extent quantum teleportation is actually about teleporting information vs about a counterintuitive property of linear algebra. If $M$ is some matrix and $I$ is the identity matrix, and $|\psi\rangle$ and $|\phi\rangle$ are two states, intuitively we would expect $(M\otimes I)(|\psi\rangle \otimes |\phi\rangle) = (M|\psi\rangle)\otimes |\phi\rangle$: the corresponding parts of the circuit apply to the corresponding states. But I think the whole point of quantum teleportation might be that this is not true? Until the matrix $Z^z X^x$ is applied, the third qubit has nothing acting on it, and yet it gets access to the coefficients $\alpha$ and $\beta$ somehow. The only way I can think of for how this could happen is that the above intuitive equality actually doesn't hold all the time. But perhaps I am missing something.

In response to Andy's specific questions:

> Would understanding come rushing back?

I don't think I understood teleportation in the first place, so understanding did not come rushing back.  But I think I was able to hit on the same confusions I experienced the first time I read the essay.

> Would it feel like the first time?

I did have a pretty easy time answering the prompts on this reread (although the Quantum Country site only showed me the prompts that happened to be due, so I likely got a weirdly selected subset of prompts).  A lot of things felt familiar, though also I had completely forgotten some things that aren't in the prompts (e.g. I have no memory at all of reading about Charles Bennett's $1 \text{ ebit} + 2 \text{ cbits} \geq 1 \text{ qubit}$ inequality, even though I found it pretty interesting on this reread, which means I probably also found it pretty interesting the first time I read the essay).

> Would you understand pieces you hadn't understood before?

I think I definitely did clarify where exactly my confusion is, but I think writing this page, and taking notes while I read (see next section), which I did not do the first time around, helped quite a bit more than just the rereading itself.

# Rough notes I took while rereading

- "which enables a quantum state to be transported across long distances, without any need to directly send the quantum state" -- is this really true? i remember it being like, you just copy the thing and then later reveal which state it is, but there's no actual teleportation involved.
- how can alice and bob perform the computation in the quantum circuit, if they are halfway across the globe?
	- "That is, Alice has successfully teleported her state to Bob." -- this only holds if the entire circuit can be completed when alice and bob are in different locations! otherwise it's just copying information! (not even copying, since the measurement destroys alice's copy)
	- "after all, Alice is able to transmit her state $|\psi\rangle$ to Bob, even if he's very distant from her" -- ok, so apparently alice and bob don't need to be near each other? but then how does bob give the symmetric state to alice? they still need to be near each other at *some* point in time.
- "And while I won't prove it here, it turns out to be possible to prove that with only that distribution over states, no information is transferred from Alice to Bob. It's a pity, but that's the way the world seems to work." -- but like, there still is a 1/4 chance that bob will get the right state? what do the other "wrong" states look like, if bob applies the X/Z gates incorrectly? and a 1/4 chance of successfully teleporting a state still seems like a big deal, since it wouldn't even require the classical communication part of the protocol?
- the question about the state $\sqrt{0.8}|01\rangle + \sqrt{0.2}|10\rangle$ and measuring the first qubit. somehow i've never had trouble with this card in reviews, but i completely forgot the discussion about the general rule, and don't think i would've been able to answer if someone asked me what the general rule is (before rereading).
- when i first read this, the stuff like "We apply the CNOT to the first two qubits" did not make sense to me on a mathematical level, even though i could do the steps using the quantum circuit diagram. now (after having read "[quantum mechanics distilled](https://quantum.country/qm)") i know that CNOT is some unitary matrix that takes two vectors, and so you apply $\mathrm{CNOT} \otimes I$ to the whole three-qubit state.
	- this, however, introduces a confusion for me: when the operations are applied to just the first two qubits, it's actually not that; you've got an implicit identity matrix being applied using a tensor product. it's not clear to me that this entire operation, on all three qubits, can be done across the world.
- quantum teleportation seems to actually be a result about tensor products/matrix multiplication. the result is something like: even if you have an identity matrix in one particular slot, the outcome of that part of the circuit can change. in other words, $(A \otimes I)|\psi\rangle |\phi\rangle = (A|\psi\rangle)|\phi\rangle$, while appealing, is actually false.
	- But actually [this other essay](https://quantum.country/qm#fourth-postulate-qm) on quantum country has the equation $(H \otimes I)(|\psi\rangle \otimes |\phi\rangle) = H|\psi\rangle \otimes |\phi\rangle$, so now I am *really* confused. This kind of thing may only work on some matrices but not others, but the Hadamard gate was one of the matrices used in teleportation, so it shouldn't work!
- "Rather, it's about a counter-intuitive way of disassembling an unknown quantum state into classical information, using a fixed shared state and measurement, and then later recovering the original quantum state." -- ok, so this makes me think that the quantum circuit *does* have to be all done in a single location. then alice and bob part ways, and then alice later publishes her measurements and then bob uses the measurements to construct his state. if so, this makes quantum teleportation a lot less interesting to me?