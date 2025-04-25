import streamlit as st
from agents.query_analyzer import analyze_query
from agents.web_search import search_web
from agents.web_scraper import extract_content
from agents.content_analyzer import summarize_content_groq

st.title("Web Research Agent")

query = st.text_input("Enter your research query:")

if query:
    with st.spinner("Analyzing query..."):
        # Step 1: Analyze the user's query to identify relevant keywords and intent
        analysis = analyze_query(query)

    with st.spinner("Searching the web..."):
        # Step 2: Perform a web search based on the analyzed keywords
        results = search_web(analysis['keywords'])

    summaries = []
    for r in results:
        st.markdown(f"### [{r['title']}]({r['link']})")
        st.write(r['snippet'])  # Display the snippet for context

        with st.spinner(f"Summarizing content from: {r['link']}"):
            # Step 3: Extract the relevant content from the URL
            content = extract_content(r['link'])

            # Step 4: Use Groq to summarize the extracted content
            summary = summarize_content_groq(content, query)

            # Step 5: Store and display the summary
            summaries.append((r['link'], summary))
            st.success("Summary:")
            st.write(summary)

    st.markdown("---")
    st.header("📄 Full Summary Report")
    for link, summary in summaries:
        st.markdown(f"**Source:** {link}")
        st.write(summary)
        st.markdown("---")
