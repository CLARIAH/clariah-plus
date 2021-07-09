<h1 id="t13-digitization-and-conversion-workflow-joint-work-with-wp6-use-cases-revised-version">T13: Digitization and conversion workflow (joint work with Wp6 use cases; revised version)</h1>
<p><strong>IDs in Google Sheets:</strong> T013</p>
<p><strong>Author:</strong> INT/Jesse de Does</p>
<p><strong>What exists: </strong></p>
<p><em>within CLARIAH:</em></p>
<ul>
<li><blockquote>
<p>PICCL web service workflow for digitization and conversion</p>
</blockquote></li>
<li><blockquote>
<p>various conversion tools (Piereling, OpenConvert; Nederlab conversions; ….)</p>
</blockquote></li>
<li><blockquote>
<p>several CLARIAH partners with expertise on OCR, post-correction and conversion</p>
</blockquote></li>
</ul>
<p><em>in general:</em></p>
<ul>
<li><blockquote>
<p>General purpose OCR systems (Finereader, tesseract)</p>
</blockquote></li>
<li><blockquote>
<p>Web services/applications offering document management and processing (Transkribus, Pero OCR)</p>
</blockquote></li>
<li><blockquote>
<p>A fascinating but confusing array of modern deep learning-based tools for layout analysis and text recognition, image enhancement, ocr evaluation, ocr postcorrection (ticcl, …), ground truth production …</p>
</blockquote></li>
<li><blockquote>
<p>Cf. also <a href="https://www.digitisation.eu/tools-resources/tools-for-text-digitisation/"><em>https://www.digitisation.eu/tools-resources/tools-for-text-digitisation/</em></a></p>
</blockquote></li>
</ul>
<p><strong>What must be adapted / extended / created anew:</strong> Infrastructure for digitization to support humanities researchers wanting to digitize or working with noisy data (eg. OCR’ed material). By infrastructure we mean a combination of tools, services, training material and support.</p>
<p>Researchers should be supported to</p>
<ul>
<li><blockquote>
<p>Choose an optimal combination of tools for their data, which implies</p>
</blockquote>
<ul>
<li><blockquote>
<p>Evaluation platform enabling researchers to quickly assess the potential of tools for their data</p>
</blockquote></li>
<li><blockquote>
<p>Ground truth creation</p>
</blockquote></li>
</ul></li>
<li><blockquote>
<p>Have the possibility to choose from:</p>
</blockquote>
<ul>
<li><blockquote>
<p>A web service based architecture</p>
</blockquote></li>
<li><blockquote>
<p>Offline availability of a wide range of tools for processing large volumes of data</p>
</blockquote></li>
</ul></li>
</ul>
<p>Researchers should be able to acquire information:</p>
<ul>
<li><blockquote>
<p>on how to build their own corpus</p>
</blockquote></li>
<li><blockquote>
<p>on available tools, other than the ones developed by partners</p>
</blockquote></li>
<li><blockquote>
<p>on options for digitisation by service providers</p>
</blockquote></li>
</ul>
<p>INT can rely on work done in projects like IMPACT, SUCCEED and Transcriptorium, and is involved in the IMPACT Centre of Competence in digitisation (founding member and leading the EB). RU: PICCL.</p>
<p>In response to the rapid change of the digitisation landscape and to the requirements from CLARIAH wp6 use cases, we revised the planning.</p>
<p>We observe a very promising but, for users, confusing proliferation of next-generation tools, partly experimental, based on deep learning which outperform the traditional methods by a large margin on difficult documents.</p>
<p>Developing a monolithic workflow system based on the mainstream systems is therefore suboptimal; incorporating all relevant state of the art tools is not feasible, given the different input-output requirements and the continuous evolution of the tools.</p>
<p>We therefore opt for a looser approach, possibly based on/connecting to the similar workflows developed in the OCR-D project (<a href="https://ocr-d.de/en/about"><em>https://ocr-d.de/en/about</em></a>).</p>
<p>Deliverables and planning</p>
<p>Originally envisaged deliverables</p>
<table>
<thead>
<tr class="header">
<th align="left">Taak</th>
<th align="left">ID</th>
<th align="left">D or M</th>
<th align="left">Category</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">T012 Digitisation &amp; Conversion Infra</td>
<td align="left">T012D1</td>
<td align="left">Deliverable</td>
<td align="left">Software</td>
<td align="left"><p>Enhanced version of TICLL (RU)</p>
<p>The planned extensions to PICCL are described in the detailed project plan.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left">T012D2</td>
<td align="left">Deliverable</td>
<td align="left">Software</td>
<td align="left"><p>Enhanced PICCL workflows</p>
<p>The planned extensions to PICCL are describe in the detailed project plan.</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left">T012D3</td>
<td align="left">Deliverable</td>
<td align="left">Software</td>
<td align="left"><p>Enhanced and user-friendly PICCL interface</p>
<p>Create a new web-based front-end for the PICCL workflow system, enabling users to</p>
<p>– Bypass advanced options with the help of a very simple interface (cf. PhilosTEI) that determines more options from the input supplied by the user</p>
<p>– Enable simple evaluation scenarios, with uploaded ground truth or gold standard</p>
<p>– Provide a simple demonstrator platform that allows users to assess easily how tools might work on their material</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left">T012D4</td>
<td align="left">Deliverable</td>
<td align="left">Website</td>
<td align="left">Web site with demonstrator tools and documentation</td>
</tr>
</tbody>
</table>
<p>Revision of deliverables</p>
<table>
<thead>
<tr class="header">
<th align="left">Taak</th>
<th align="left">ID</th>
<th align="left">D or M</th>
<th align="left">Category</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">T012</td>
<td align="left">T012D1</td>
<td align="left">Deliverable</td>
<td align="left">Software</td>
<td align="left">Documented workflows for OCR and conversion of Dutch documents</td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left">T012D2a</td>
<td align="left">Deliverable</td>
<td align="left">Data</td>
<td align="left"><p>Ground truth material for Dutch-language OCR</p>
<ul>
<li><blockquote>
<p>17th century newspaper set</p>
</blockquote></li>
<li><blockquote>
<p>set based on conversion/enhancement to line level of the IMPACT Dutch ground truth</p>
</blockquote></li>
<li><blockquote>
<p>As much as we can grab from other sources</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left">T012D2b</td>
<td align="left">Deliverable</td>
<td align="left">Data</td>
<td align="left">Trained models for OCR of Dutch documents</td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left">T012D2c</td>
<td align="left">Deliverable</td>
<td align="left">Data+software</td>
<td align="left">Evaluation of OCR tools on ground truth data: data, evaluation workflow, document on evaluation</td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left">T012D3</td>
<td align="left">Deliverable</td>
<td align="left">Website</td>
<td align="left">Web site with demonstrator tools and documentation</td>
</tr>
</tbody>
</table>
<p>Original INT workload planning within WP3 (needs revision)</p>
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">T012 Digitisation &amp; Conversion Infra</td>
<td align="left">Linguist</td>
<td align="left">0</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><strong>0</strong></td>
</tr>
<tr class="even">
<td align="left">T012 Digitisation &amp; Conversion Infra</td>
<td align="left">Developer</td>
<td align="left">4</td>
<td align="left"></td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left">2</td>
<td align="left"></td>
<td align="left"><strong>4</strong></td>
</tr>
<tr class="odd">
<td align="left">T012 Digitisation &amp; Conversion Infra</td>
<td align="left">Computational linguist</td>
<td align="left">2</td>
<td align="left"></td>
<td align="left">2</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><strong>2</strong></td>
</tr>
</tbody>
</table>
<p>Partial revision:</p>
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">T012 Digitisation &amp; Conversion Infra</td>
<td align="left">Linguist</td>
<td align="left">0</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><strong>0</strong></td>
</tr>
<tr class="even">
<td align="left">T012 Digitisation &amp; Conversion Infra</td>
<td align="left">Developer</td>
<td align="left">4</td>
<td align="left"></td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">3</td>
<td align="left"></td>
<td align="left"><strong>6</strong></td>
</tr>
<tr class="odd">
<td align="left">T012 Digitisation &amp; Conversion Infra</td>
<td align="left">Computational linguist</td>
<td align="left">0</td>
<td align="left"></td>
<td align="left">0</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><strong>0</strong></td>
</tr>
</tbody>
</table>
<p><em>!The current proposed planning concerns the INT part of the work only; the work of the other partners also needs to be reconsidered.</em></p>
<p>The original project plan states:</p>
<blockquote>
<p>INT and KNAW HuC Meertens Institute and HuC Digital Humanities Lab, Radboud University Nijmegen (RUN, CLST), Tilburg University (TiU). HuC in tandem with RUN will concentrate on backend (TICCL, PICCL, converters, software distribution in a.o. LaMachine) and INT willconcentrate on frontend, converters, information and hosting.</p>
</blockquote>
<p><strong>Targeted/Actual users:</strong> Digital humanities researchers depending on corpus material in an appropriate format for their research<br />
<strong>Actual use (quantify!):</strong> We are currently unable to quantify. Envisaged uses are at least the CLARIAH use cases on historical newspapers and on corpus-based history of ideas.</p>
<p><strong>Social Impact</strong> <strong>(concrete examples):</strong> Researchers will be able to build their own corpora, thus facilitating their research</p>
<p><strong>Estimate in PMs (try to justify): 6</strong></p>
<p><strong>Lead + PMs:</strong></p>
<p><strong>Participants + PMs:</strong> INT: 6</p>
