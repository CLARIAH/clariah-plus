<h1 id="topic-search-engine-upgrades-extension-to-treebanks">Topic: Search engine upgrades: extension to treebanks</h1>
<p><strong>IDs in Google Sheets:</strong> T83</p>
<p><strong>Author:</strong> INT/Jesse de Does</p>
<p><strong>What exists:</strong> Token level annotation search for large corpora; separate treebank query engines</p>
<p><strong>What must be adapted / extended / created anew:</strong> Because of richer and more intuitive searching for syntactic phenomena, it is surprising that treebanks have not superseded token-based corpora as the basic facility for corpus retrieval.</p>
<p>In this task, we develop a scalable integrated treebank search and exploitation infrastructure for large corpora, integrated with the BlackLab search engine.</p>
<p>Requirements</p>
<ul>
<li><blockquote>
<p>Performance. Performance at least for simple queries comparable to CQL (e.g. /node[@cat=&quot;np&quot; and node[@rel=&quot;mod&quot; and @pt=&quot;adj&quot;] and node[@rel=&quot;hd&quot; and @pt=&quot;n&quot; and @lemma=&quot;schaap&quot;]]) should not be much slower than [pos=”adj”][lemma=”schaap”]</p>
</blockquote></li>
<li><blockquote>
<p>Scalable, distributable, federable</p>
</blockquote></li>
<li><blockquote>
<p>Support both dependency and phrase structure</p>
</blockquote></li>
<li><blockquote>
<p>Enable combination of CQL constructions and treebank query (?)</p>
</blockquote></li>
</ul>
<p>Benefits:</p>
<ul>
<li><blockquote>
<p>Leverage efficiency and flexibility of the lucene Span query mechanism and lucene/solr solutions for scalability and distributed processing to achieve goals</p>
</blockquote></li>
<li><blockquote>
<p>One infrastructure to publish corpora instead of different copies of e.g. opensonar in whitelab and gretel3, so management of metadata, distributed deployment, user annotation, statistics and visualization, etc, etc need not be duplicated</p>
</blockquote></li>
</ul>
<p><strong>Why important for CLARIAH (scientific impact): </strong></p>
<p>Current corpus exploitation infrastructure for treebanks and token-based corpora is fragmented and not always scalable; it is difficult to integrate analytics from treebanks and token-based corpora.</p>
<p>On the one hand, analytics, query management, analytics and visualization in treebank applications lag behind the facilities offered by mature token-based corpus exploitation applications like the Sketch Engine, IMS, BlackLab Server, WhiteLab and the Nederlab portal. On the other hand, for many tasks (even very simple ones like finding typical subject or object nouns for a given verb), token-based queries are no more than a poor man’s substitute for phrase structure search. A single, scalable mode of access to modern Dutch data will greatly benefit both linguistic and applied research.</p>
<p><strong>Targeted/Actual users:</strong> linguists; computational linguist; language learners</p>
<p><strong>Actual use (quantify!):</strong> Since the envisaged facility will have all capacities of token-based and treebank query and more, a satisfactory implementation will attract the attention from both user groups</p>
<p><strong>Social Impact</strong> <strong>(concrete examples):</strong> Facilitate linguistic research based on corpus data by creating a single scalable retrieval hub</p>
<p><strong>Estimate in PMs (try to justify):</strong> 8PM. Production-quality implementation of new technology is required; user interface needs to be enhanced; 3PM functional design and testing</p>
<p><strong>Lead + PMs:</strong> INT: 8</p>
<p><strong>Participants + PMs:</strong> INT</p>
<p><strong>Deliverables and milestones:</strong></p>
<table>
<thead>
<tr class="header">
<th align="left">Task</th>
<th align="left"><strong>ID</strong></th>
<th align="left"><strong>Class</strong></th>
<th align="left"><strong>Type</strong></th>
<th align="left"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">T083 Treebanks</td>
<td align="left">T083M1</td>
<td align="left">Milestone</td>
<td align="left">Document</td>
<td align="left">Document defining the requirements for the scalabale treebank search, based on input from a set of use cases.</td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left">T083D1</td>
<td align="left">Deliverable</td>
<td align="left">Software</td>
<td align="left">Scalable treebank search implementation base on BlackLab and GreTeL</td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left">T083D2</td>
<td align="left">Deliverable</td>
<td align="left">Document</td>
<td align="left">Document describing T083D2 and its application to use cases.</td>
</tr>
</tbody>
</table>
<ul>
<li></li>
</ul>
