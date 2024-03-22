Dependencies: A minimal list of Obsidian backlinks to upstream concepts. \[\[Note 1]], \[\[Note 2]]

Learning Resources:  A bulleted list of links to external learning resources, with descriptions. These resources should be helpful in understanding the core concept.
- \[Description of external resource 1\](link to external resource 1)
- \[Description of external resource 2\](link to external resource 2)

Historical Resources: A bulleted list of links to historical resources, with descriptions. These resources should help the reader track the origin of these ideas, though they may not be the best resources for learning.
- \[Description of external resource 1\](link to external resource 1)
- \[Description of external resource 2\](link to external resource 2)
# Summary
**Written by the presenter prior to the presentation.** Give a high-level overview of the topics discussed in this note, including:
- A brief description of the context behind this note
- A bulleted list outlining the main topics discussed in the note and defining relevant terms
- A discussion of key takeaways, including an explanation of why we care, and some example areas of application of these ideas
# Introduction
**Written by the scribe during (and perhaps after) the presentation.** Introduce the topic being discussed to an audience that hasn't encountered this topic before.
- Ensure that each piece of the topic is properly motivated. To keep this section brief, don't over-explain the motivation for any piece of the topic. (For example, if you're introducing MLPs, and they include nonlinearities, why are the nonlinearities there? State that nonlinearities prevent a collapse to linear functions, but save the full argument that infinite-width ReLU networks are universal function approximators for the [[#Exposition|exposition]] section.) 
- Avoid getting into the weeds! If you make a statement that requires a mathematical proof, put that in the [[New Note Template#Analysis|analysis]] section. If there's more than a couple lines of math, but it in the [[New Note Template#Exposition|exposition]] section. Use intra-note links to connect your propositions (in the introduction and exposition) to their proofs (in the analysis).
- Separate content using level-4 headers (e.g. "\#\#\#\# Title of section") in ways that make sense conceptually.
# Exposition
**Written by the presenter prior to the presentation, refined by scribe after presentation.** Dive into details that are too verbose to include in the [[#Introduction|introduction]] section, but still necessary for full understanding.
- Mathematical derivations of propositions presented in the [[#Introduction|introduction]], where the derivation is *necessary to fully understand why* the proposition is true (e.g. Bayes' Rule has a simple derivation arising directly from definitions in conditional probability, and such a derivation would go here; so would derivations for statements that intuitively follow from Bayes Rule).
- Diagrams displaying ideas or systems that are conceptually central to the topic (e.g. for research where the main contribution is a new neural architecture, like ResNets, the system architecture diagram goes here).
- Expositions that explain and provide context for the content of the [[#Introduction|introduction]] section.
# Analysis
**Written by the presenter prior to the presentation, refined by scribe after presentation. Depth is very optional, this section will mainly be useful for the presenter while learning about the details of their topic.** Present any mathematical derivations, technical details, or documentation that is too verbose to be worth including in the [[#Introduction|introduction]]/[[#Exposition|exposition]] sections. Use this section to keep the note technically complete without overcomplicating the [[#Introduction|introduction]]/[[#Exposition|exposition]]. Examples of content that would go in the analysis section:
- Mathematical derivations of propositions presented in the [[#Introduction|introduction]], where the derivation *doesn't shed any light* on the meaning or use cases of the proposition
- Diagrams showing details of system architecture that are important for a working solution, but not conceptually central
- Paragraphs that relate the content of the [[#Introduction|introduction]] to more advanced concepts, which are only fully explored in other notes
- Additional information about the concept which are relevant in downstream concepts