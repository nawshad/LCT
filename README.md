# langchain-tutorials
- A set of LangChain Tutorials from my youtube playlist https://www.youtube.com/playlist?list=PL8motc6AQftk1Bs42EW45kwYbyJ4jOdiZ

## Some rough ideas on better Q/A using LLM+KG:
### How to find out the chunks of text which are self contained? 
  - A chunk should represents a discourse
  pretty well. (Current RAG systems create some sort of overlapping chunks, without 
  much idea why it's doing so...). Also, the length of this chunks effect the answer to a 
  query, so, we should have summary of these chunks, instead their full content (incase
  context limit exceeds).
### How to create a relationship among these chunks? 
  - So we can definitely rank the chunks (can be a composite ranking: takes: into account tf+idf, semantic
  similarity, NE distribution etc), provided a given question.
  - Then we can also find the one-hop close members of those chunks, to help answer 
  the question better. (Need to think about this ... )