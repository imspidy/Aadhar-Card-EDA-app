mkdir -p ~/.streamlit/

echo"\
[server]\n\
port = $PORT\n\
enableCORS = flase\n\
\n\
"> ~/.streamlit/config.toml