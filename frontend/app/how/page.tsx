export default function How(){

return(

<div style={{padding:40,fontFamily:"Arial"}}>

<h1>How the AI News Trend Agent Works</h1>

<p>
This system continuously monitors multiple technology news feeds
and identifies emerging trends using lightweight signal analysis.
</p>

<h3>Pipeline</h3>

<p>
RSS Feeds → Headline Extraction → Topic Similarity Folding →
Topic Memory → Trend Scoring → Spike Detection → Dashboard
</p>

<h3>Topic Similarity Folding</h3>

<p>
News headlines are clustered using lexical similarity and anchor entities
(e.g. Apple, Tesla, ChatGPT). This prevents duplicate topics from appearing
separately.
</p>

<h3>Trend Scoring</h3>

<p>
Each topic is scored using multiple signals:
</p>

<ul>
<li>Frequency – how often the topic appears</li>
<li>Spread – number of sources reporting it</li>
<li>Growth – change in frequency over time</li>
<li>Persistence – how long the topic remains active</li>
</ul>

<h3>Spike Detection</h3>

<p>
Sudden jumps in topic frequency trigger spike alerts,
highlighting rapidly emerging news events.
</p>

<h3>Adaptive Learning</h3>

<p>
The agent continuously adjusts its scoring weights based on
observed patterns in news propagation across sources.
</p>
</div>

)

}
