# Source code size vs learned model size in ML and in humans?

To [build intuition](https://www.lesswrong.com/posts/bDwQddhqaTiMhbpPF/what-are-some-exercises-for-building-generating-intuitions) about content vs architecture in AI (which comes up a lot in discussions about AI takeoff that involve Robin Hanson), I've been wondering about content vs architecture _size_ (where size is measured in number of bits).

Here's how I'm operationalizing content and architecture size for ML systems:

- content size: The number of bits required to store the learned model of the ML system (e.g. all the floating point numbers in a neural network).
- architecture size: The number of bits of source code. I'm not sure if it makes sense to include the source code of supporting software (e.g. standard machine learning libraries).

I tried looking at the [AlphaGo paper](http://augmentingcognition.com/assets/Silver2016a.pdf) to see if I could find this kind of information, but after trying for about 30 minutes was unable to find what I wanted. I can't tell if this is because I'm not acquainted enough with the ML field to locate this information or if that information just isn't in the paper.

Is this information easily available for various ML systems? What is the fastest way to gather this information?

I'm also wondering about this same content vs architecture size split in humans. For humans one way I'm thinking of it is as "amount of information encoded in inheritance mechanisms" vs "amount of information encoded in a typical adult human brain". I know that Eliezer Yudkowsky has cited [750 megabytes](https://docs.google.com/document/pub?id=17yLL7B7yRrhV3J9NuiVuac3hNmjeKTVHnqiEa6UQpJk) as the amount of information in the human DNA, and also emphasizes that most of this information is junk. This was in 2011 and I don't know if there's a new consensus or how to factor in epigenetic information. There is also [content stored in genes](https://en.wikipedia.org/wiki/The_Adapted_Mind), and I'm not sure how to separate out the content and architecture in genes.

I'm pretty uncertain about whether this is even a good way to think about this topic, so I would also appreciate any feedback on this question itself. For example, if this isn't an interesting question to ask, I would like to know why.
