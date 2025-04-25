import re

def analyze_query(user_query):
    query = user_query.lower()
    if any(x in query for x in ['latest', 'news', 'recent']):
        query_type = 'news'
    elif any(x in query for x in ['how', 'why', 'what']):
        query_type = 'exploratory'
    else:
        query_type = 'factual'

    keywords = re.findall(r'\b\w+\b', user_query)
    return {
        'original': user_query,
        'query_type': query_type,
        'keywords': keywords
    }
