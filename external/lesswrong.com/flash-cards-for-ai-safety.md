I've made around 250 Anki cards about AI safety. I haven't prioritized sharing my cards because I think finding a specific card useful requires someone to have read the source material generating the card (e.g. if I made the card based on a blog post, one would need to read that exact blog post to get value out of reviewing the card; see [learn before you memorize](http://super-memory.com/articles/20rules.htm)). Since there are many AI safety blog posts and I don't have the sense that lots of Anki users read any particular blog post, it seems to me that the value generated from sharing a set of cards about a blog post isn't high enough to overcome the annoyance cost of polishing, packaging, and uploading the cards.

More generally, from a consumer perspective, I think people tend to be pretty bad at making good Anki cards (I'm often embarrassed at the cards I've created several months ago!), which makes it unexciting for me to spend a lot of effort trying to collaborate with others on making cards (because I expect to receive poorly-made cards in return for the cards I provide). I think collaborative card-making *can* be done though, e.g. [Michael Nielsen and Andy Matuschak's quantum computing guide](https://quantum.country/) comes with pre-made cards that I think are pretty good.

Different people also have different goals/interests so even given a single source material, the specifics one wants to Ankify can be different. For example, someone who wants to understand the technical details of logical induction will want to Ankify the common objects used (market, pricing, trader, valuation feature, etc.), the theorems and proof techniques, and so forth, whereas someone who just wants a high-level overview and the "so what" of logical induction can get away with Ankifying much less detail.

Something I've noticed is that many AI safety posts aren't very good at explaining things (not enough concrete examples, not enough emphasis on common misconceptions and edge cases, not enough effort to answer what I think of as "obvious" questions); this fact is often revealed by the comments people make in response to a post. This makes it hard to make Anki cards because one doesn't really understand the content of the post, at least not well enough to confidently generate Anki cards (one of the benefits of being an Anki user is having a greater sensitivity to when one does not understand something; see "illusion of explanatory depth" and related terms). There are other problems like conflicting usage of terminology (e.g. multiple definitions of "benign", "aligned", "corrigible") and the fact that some of the debates are ongoing/some of the knowledge is still being worked out.

For "What would be a good strategy for generating useful flashcards?": I try to read a post or a series of posts and once I feel that I understand the basic idea, I will usually reread it to add cards about the basic terms and ask myself simple questions. Some examples cards for iterated amplification:

- what kind of training does the Distill step use?
- in the pseudocode, what step gets repeated/iterated?
- how do we get A[0]?
- write A[1] in terms of H and A[0]
- when Paul says IDA is going to be competitive with traditional RL agents in terms of time and resource costs, what exactly does he mean?
- advantages of A[0] over H
- symbolic expression for the overseer
- why should the amplified system (of human + multiple copies of the AI) be expected to perform better than the human alone?
