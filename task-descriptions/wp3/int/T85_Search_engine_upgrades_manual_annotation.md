<h1 id="t85-search-engine-upgrades-manual-annotation">T85: search engine upgrades: manual annotation </h1>
<p><strong>IDs in Google Sheets:</strong> T85</p>
<p><strong>Author:</strong> INT/Jesse de Does</p>
<p><strong>What exists:</strong> static corpora and search engines; annotation tools</p>
<p><strong><br />
What must be adapted / extended / created anew:</strong> Create an infrastructure for managing user annotations in corpora. All corpus search applications should support the manual annotation of search results with codes to further refine/classify the search results (cf. the Lancaster BNC interface).</p>
<ul>
<li><blockquote>
<p>Users should be able to add annotations to search results and to share these annotations with other users.</p>
</blockquote></li>
<li><blockquote>
<p>Deposit (manual) annotation results back into an archive (closing the data management life cycle)</p>
</blockquote></li>
<li><blockquote>
<p>Annotations should be searchable in the corpus (depends on design approach)</p>
</blockquote></li>
<li><blockquote>
<p>Should also benefit treebank search</p>
</blockquote></li>
</ul>
<p>There are two basic scenarios: either there is a strong integration with the search engine, which would simplify support of making annotations searchable; or one implements a module that can be combined with any type of search engine.<br />
Example use cases:</p>
<ul>
<li><blockquote>
<p>Annotate word senses</p>
</blockquote></li>
<li><blockquote>
<p>Annotate tagger errors</p>
</blockquote></li>
<li><blockquote>
<p>Add fine-grained syntactic information</p>
</blockquote></li>
</ul>
<p>Cf also:</p>
<ul>
<li><blockquote>
<p>bnc web annotated queries (screenshots below)</p>
</blockquote></li>
<li><blockquote>
<p><a href="https://github.com/emanjavacas/cosycat/wiki/Annotations"><em>https://github.com/emanjavacas/cosycat/wiki/Annotations</em></a></p>
</blockquote></li>
</ul>
<p><strong>Why important for CLARIAH (scientific impact):</strong> Added value to research with corpora.</p>
<p><strong>Targeted/Actual users:</strong> corpus users</p>
<p><strong>Actual use (quantify!):</strong></p>
<p><strong>Social Impact</strong> <strong>(concrete examples):</strong> Facilitate linguistic research; publish data on which research is based; foster collaborative corpus research</p>
<p><strong>Estimate in PMs (try to justify):</strong> 6PM</p>
<p><strong>Lead + PMs:</strong></p>
<p><strong>Participants + PMs: INT</strong></p>
<table>
<thead>
<tr class="header">
<th align="left"><strong>Taak</strong></th>
<th align="left"><strong>Type personeel</strong></th>
<th align="left"><strong>Available</strong></th>
<th align="left"><strong>2019</strong></th>
<th align="left"><strong>2020</strong></th>
<th align="left"><strong>2021</strong></th>
<th align="left"><strong>2022</strong></th>
<th align="left"><strong>2023</strong></th>
<th align="left"><strong>Summed</strong></th>
<th align="left"><strong>Task total</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">T085 Manual Annotation</td>
<td align="left">Software developer(s)</td>
<td align="left">5</td>
<td align="left">1</td>
<td align="left">2</td>
<td align="left">2</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><strong>5</strong></td>
<td align="left"><strong>6</strong></td>
</tr>
<tr class="even">
<td align="left">T085 Manual annotation</td>
<td align="left">(Computational) linguist</td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><strong>1</strong></td>
<td align="left"></td>
</tr>
</tbody>
</table>
<p><strong>Deliverables:</strong></p>
<table>
<thead>
<tr class="header">
<th align="left">Task</th>
<th align="left">ID</th>
<th align="left">D or M</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">T085 Manual Annotation</td>
<td align="left">T085M1</td>
<td align="left">Milestone</td>
<td align="left">Document</td>
<td align="left">Document defining the requirements for the manual annotation of corpus search results, based on input from a set of use cases.</td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left">T085D2</td>
<td align="left">Deliverable</td>
<td align="left">Software</td>
<td align="left">Implementation manual search result annotation, based on BlackLab and the BlackLab corpus frontend</td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left">T005D2</td>
<td align="left">Deliverable</td>
<td align="left">Document</td>
<td align="left">Document describing T085D2 and its application to use cases.</td>
</tr>
</tbody>
</table>
