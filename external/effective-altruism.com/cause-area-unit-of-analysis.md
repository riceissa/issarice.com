# Why "cause area" as the unit of analysis?

Back in April 2018, I spent some time trying to understand the hierarchy/structure/classification of cause areas. I did this at the suggestion of Vipul Naik, who wanted to (1) categorize cause areas treated on the [Cause Prioritization Wiki](https://causeprioritization.org/) so that there was more structure to it than that of a jumble of 100+ cause areas, and (2) make the analysis of cause areas more systematic.

Some of the outputs of that investigation are:

- A [list of existing classifications of philanthropy](https://causeprioritization.org/List_of_classifications_of_philanthropy)
- A [directed acyclic graph of existing cause areas](https://causeprioritization.org/dagitty-model.svg) (where $A \to B$ means "$A$ has $B$ as a sub-cause" or "if I am claiming that I work on $B$, then I can also claim that I am working on $A$")
- A [list of potential properties with which to classify existing cause areas](https://causeprioritization.org/Cause_area_classification)
- A [table of "form of altruism" vs "beneficiary group"](https://docs.google.com/document/d/1l22FA-QVcER1mANhs2id_fp5Sc-RlQc4etHizMoEtDw/edit) ("form of altruism" and "beneficiary group" are two of the "potential properties" in the previous list, so this table crosses these two properties, resulting in a two-dimensional grid)
- A [generic linkdump and rambling on taxonomies](https://issarice.com/taxonomies)

I came away from the above investigation feeling pretty confused about the nature of cause areas. Given just a description of reality, it didn't seem obvious to me to carve things out into "cause areas" and to take "cause area" as the basic unit of analysis/prioritization.

Some thoughts/intuitions that contribute to this feeling:

- As [explained](http://www.fhi.ox.ac.uk/on-causes/) by Owen Cotton-Barratt back in 2014, there are at least two meanings of "cause area". My impression is that since then, effective altruists have not really distinguished between these different meanings, which suggests to me that some combination of the following things are happening: (1) the distinction isn't too important in practice; (2) people are using "cause area" as a shorthand for something like "the established cause areas in effective altruism, plus some extra hard-to-specify stuff"; (3) people are confused about what a "cause area" even is, but lack the metacognitive abilities to notice this.
- A cause area can try to "seem" big or small by lumping together more and more things in the world (or alternatively excluding more things from itself). Do we compare "animal welfare improvement" against "agent foundations research", or against "technical AI safety work", or against "technical, strategy, or policy work in AI safety", or against "existential risk reduction", or against "applied mathematics related to futuristic technology"?
- More generally, if we take some basic unit of action like "1 person-year of work" then we can form sets of actions and call those sets "cause areas" (these sets don't necessarily form a partition, i.e. there might be actions contained in multiple causes and actions not contained in any cause). But then we can imagine defining some arbitrary "cause area" that just picks out the most high-value actions and declares it "the most important cause".
- I can imagine an argument taking place where the opponent of a cause area picks some ineffective actions within the cause area while a supporter picks effective actions, so they disagree regrading the overall effectiveness of the cause area despite agreeing about the effectiveness of specific actions. Maybe even a motte-and-bailey argument where the supporter draws a tighter boundary around the cause when attacked, and loosens the boundary at other times to be able to call their preferred interventions effective.
- One way looking at cause areas might be useful is from an evaluator's perspective of "what skills/domain expertise do I need to be able to evaluate specific programs/research topics?" If skillsets tend to "unlock" a bunch of potential programs at once, then there might be a natural-seeming boundary around these programs, which might correspond to our intuitive notion of cause area. But this seems to depend on the order in which various skills are acquired. To take an extreme case, if someone had a lot of domain-specific expertise in many domains but lacked some general skill (like generalist research skills, knowledge of statistics, programming experience) then by learning the general skill they suddenly "unlock" a whole bunch of "cause areas" at once.
- There is a loose analogy to other situations where reductionism has been useful.
- In practice, Open Philanthropy Project (which is apparently doing cause prioritization) has fixed a list of cause areas, and is prioritizing among much more specific opportunities within those cause areas.

I am curious to hear people's thoughts on this. I would also appreciate pointers to existing discussions (I feel like I've been paying attention, but it seems plausible to me that I've missed some).


you might think AI safety is super valuable, but if you have more refined opinions about ai safety, then you might think some agendas are useless and some are really useful/worth trying. a naive analysis cannot distinguish effectiveness within a cause area, so puts a uniform score over the whole cause area, whereas a more sophisticated analysis puts precise scores over each action within a cause area.


there is buck's idea that the reason "cause area" is a useful unit is that _within_ this boundary, what matters most is your comparative advantage, but outside this boundary what matters isn't your comparative advantage.
https://eaforum.issarice.com/posts/53JxkvQ7RKAJ4nHc4/some-thoughts-on-deference-and-inside-view-models#QmNp4GfviyfjLwHEA
I'm not sure I agree with this. Even within the boundary of a cause area like AI safety, it seems worth spending a lot of time to carefully choose which technical agenda to work on, for example (one shouldn't just say "i have a comparative advantage at machine learning" and decide to work on ML safety)
Buck makes the point again in https://eaforum.issarice.com/posts/tM8nfmxJshRwxchpz/if-causes-differ-astronomically-in-cost-effectiveness-then#jioBt537xap332wjg

it seems like what actually matters is producing a list of individual tasks ranked by how effective they are. keeping track of cause areas seems mostly useful only to be able to collaborate with others (i.e. others in your same cause area will e.g. be able to give better object level feedback)

another idea: when doing EV calculations, actions in the same cause area divide up the same "pie" whereas actions in different cause areas have different "pies" to divide up.

see paper notebook from 2019-02-23 for my original thinking.

also related: https://worldspiritsockpuppet.com/2021/01/17/group-scale.html
